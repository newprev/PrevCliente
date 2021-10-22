import datetime
from dateutil.relativedelta import relativedelta
from typing import List, Union
from calendar import monthrange
import pandas as pd
from peewee import SqliteDatabase
from SQLs.itensContribuicao import selectItensDados
from math import floor

from Daos.daoCalculos import DaoCalculos
from util.dateHelper import calculaIdade, strToDate, dataConflitante

from modelos.cabecalhoORM import CnisCabecalhos
from modelos.remuneracaoORM import CnisRemuneracoes
from modelos.contribuicoesORM import CnisContribuicoes
from modelos.itemContribuicao import ItemContribuicao
from modelos.expSobrevidaORM import ExpSobrevida
from modelos.processosORM import Processos
from modelos.clienteORM import Cliente
from modelos.salarioMinimoORM import SalarioMinimo
from modelos.aposentadoriaORM import Aposentadoria
from util.enums.newPrevEnums import RegraTransicao, GeneroCliente, TamanhoData, ComparaData, DireitoAdquirido, SubTipoAposentadoria, TipoItemContribuicao, RegraGeralAR


# Reforma 13/11/2019
# Ar: Antes da reforma
# Dr: Depois da reforma


class CalculosAposentadoria:
    """
    Legendas:
    - RMI: Renda mensal inicial
    - DIB: Data do início do benefício
    """
    listaCabecalhos: List[CnisCabecalhos] = []
    listaItensContrib: List[ItemContribuicao] = []
    listaRemuneracoes: List[CnisRemuneracoes] = []
    listaContribuicoes: List[CnisContribuicoes] = []
    dfTotalContribuicoes: pd.DataFrame
    mediaSalarial: float
    idadeCalculada: relativedelta
    dataPrimeiroTrabalho: datetime.date
    enumGeneroCliente: GeneroCliente

    def __init__(self, processo: Processos, cliente: Cliente):
        self.processo = processo
        self.cliente = cliente

        # Datas importantes
        self.dataReforma2019: datetime.date = datetime.date(2019, 11, 13)
        self.dataTrocaMoeda: datetime.date = datetime.date(1994, 7, 1)

        self.fatorPrevidenciario: int = 1

        if self.cliente.genero == 'M':
            self.enumGeneroCliente = GeneroCliente.masculino
        else:
            self.enumGeneroCliente = GeneroCliente.feminino

        # if dib is None:
        #     self.dibAtual: datetime = datetime.datetime.today()
        # else:
        #     self.dibAtual: datetime = dib

        # self.dibAtual = datetime.datetime(year=2020, month=6, day=15)

        # self.idadeCalculada = calculaIdade(self.cliente.dataNascimento, self.dibAtual)

        # self.mediaSalarial: float = self.calculaMediaSalarial()
        # self.tempoContribCalculado: list = self.calculaTempoContribuicao()
        # self.pontuacao: int = sum(self.tempoContribCalculado) + self.cliente.idade

        # self.regrasTransicao = {
        #     RegraTransicao.pontos: self.regraTransPontos(),
        #     RegraTransicao.reducaoIdadeMinima: self.regraRedIdadeMinima(),
        #     RegraTransicao.pedagio50: self.regraPedagio50(),
        #     RegraTransicao.reducaoTempoContribuicao: self.regraRedTempoContrib()
        # }

        self.regrasACalcular: List[Union[RegraTransicao, RegraGeralAR]] = [
            RegraTransicao.pontos,
            RegraTransicao.reducaoIdadeMinima,
            RegraTransicao.pedagio50,
            RegraTransicao.reducaoTempoContribuicao,
            RegraTransicao.pedagio100,
            RegraGeralAR.idade,
            RegraGeralAR.tempoContribuicao,
            RegraGeralAR.fator85_95
        ]

        self.regrasAposentadoria = {
            RegraTransicao.pontos: False,
            RegraTransicao.reducaoIdadeMinima: False,
            RegraTransicao.pedagio50: False,
            RegraTransicao.reducaoTempoContribuicao: False,
            RegraTransicao.pedagio100: False,
            RegraGeralAR.fator85_95: False,
            RegraGeralAR.idade: False,
            RegraGeralAR.tempoContribuicao: False
        }

        self.valorBeneficios = {
            RegraTransicao.pontos: 0.0,
            RegraTransicao.reducaoIdadeMinima: 0.0,
            RegraTransicao.pedagio50: 0.0,
            RegraTransicao.pedagio100: 0.0,
            RegraTransicao.reducaoTempoContribuicao: 0.0,
            RegraGeralAR.fator85_95: 0.0,
            RegraGeralAR.idade: 0.0,
            RegraGeralAR.tempoContribuicao: 0.0
        }

        self.dibs = {
            RegraTransicao.pontos: None,
            RegraTransicao.reducaoIdadeMinima: None,
            RegraTransicao.pedagio50: None,
            RegraTransicao.reducaoTempoContribuicao: None,
            RegraTransicao.pedagio100: None,
            RegraGeralAR.fator85_95: None,
            RegraGeralAR.idade: None,
            RegraGeralAR.tempoContribuicao: None
        }

        self.qtdContrib = {
            RegraTransicao.pontos: 0,
            RegraTransicao.pedagio50: 0,
            RegraTransicao.reducaoIdadeMinima: 0,
            RegraTransicao.reducaoTempoContribuicao: 0,
            RegraTransicao.pedagio100: 0,
            RegraGeralAR.fator85_95: 0,
            RegraGeralAR.idade: 0,
            RegraGeralAR.tempoContribuicao: 0
        }

        self.tmpContribPorRegra = {
            RegraTransicao.pontos: None,
            RegraTransicao.pedagio50: None,
            RegraTransicao.reducaoIdadeMinima: None,
            RegraTransicao.reducaoTempoContribuicao: None,
            RegraTransicao.pedagio100: None,
            RegraGeralAR.fator85_95: None,
            RegraGeralAR.idade: None,
            RegraGeralAR.tempoContribuicao: None
        }

        self.calculaDibs()
        self.atualizaDataFrameContribuicoes()
        self.calculaValorBeneficios()

        print('Regra -------------------------------------   DIB    -- QtdContrib -- Valor Beneficio ---------- tmpContribPorRegra')
        for chave, valor in self.dibs.items():
            tamanhoStr: int = len(chave.name) + 14
            tamanhoStr -= 2 if isinstance(chave, RegraGeralAR) else 0
            print(f"{chave}{' '*(42 - tamanhoStr)}{valor}       {self.qtdContrib[chave]}       R$ {self.valorBeneficios[chave]}    {self.tmpContribPorRegra[chave]}")

        # self.direitosAdquiridos = {
        #     DireitoAdquirido.lei821391: {
        #         SubTipoAposentadoria.Idade: self.calculaDireitoAdquirido(DireitoAdquirido.lei821391, subTipo=SubTipoAposentadoria.Idade),
        #         SubTipoAposentadoria.TempoContrib: self.calculaDireitoAdquirido(DireitoAdquirido.lei821391, subTipo=SubTipoAposentadoria.TempoContrib)
        #     },
        #     DireitoAdquirido.lei987699: {
        #         SubTipoAposentadoria.Idade: self.calculaDireitoAdquirido(DireitoAdquirido.lei987699, subTipo=SubTipoAposentadoria.Idade),
        #         SubTipoAposentadoria.TempoContrib: False,
        #     },
        #     DireitoAdquirido.ec1032019: self.calculaDireitoAdquirido(DireitoAdquirido.ec1032019)
        # }

        # self.aposentadorias = {
        #     'direitoAdq': self.direitosAdquiridos,
        #     'regrasTransicao': self.regrasTransicao
        # }

        # self.calculaBeneficios()

        # print('\n\n------------------------------------------------------------------ ')
        # print(f'len(self.listaRemuneracoes): {len(self.listaRemuneracoes)}')
        # print(f'len(self.listaContribuicoes): {len(self.listaContribuicoes)}')
        # print(f'self.processo.tempoContribuicao: {self.processo.tempoContribuicao}')
        # print(f'self.valorBeneficios: {self.valorBeneficios}')
        # # print(f'self.tempoContribCalculado: {self.tempoContribCalculado}')
        # print(f'self.fatorPrevidenciario: {self.fatorPrevidenciario}')
        # # prettyPrintDict(self.aposentadorias)
        # print('------------------------------------------------------------------\n\n')

    def atingiuIdadeAR(self, dib: datetime.date, qtdContribuicoes: int) -> bool:
        """
        Calcula requisitos para aquisição do benefício da aposentadoria por idade ANTES DA REFORMA de 2019
        :param dib: Data do início do benefício, caso as condições sejam satisfeitas
        :param qtdContribuicoes:
        :return:
        """

        if qtdContribuicoes < 180 or dib > self.dataReforma2019:
            return False
        else:
            acrescimoProfessor: int = 0
            if self.cliente.professor:
                acrescimoProfessor = 5

            ultimoDiaMes: int = monthrange(dib.year, dib.month)[1]
            dib = datetime.date(dib.year, dib.month, ultimoDiaMes)
            idadeCliente: relativedelta = calculaIdade(strToDate(self.cliente.dataNascimento), dib)
            if self.enumGeneroCliente == GeneroCliente.masculino:
                return idadeCliente.years + acrescimoProfessor >= 65
            else:
                return idadeCliente.years + acrescimoProfessor >= 60

    def atingiuRegra85_95(self, dib: datetime.date, qtdContribuicoes: int, tempoContribuicao: relativedelta) -> bool:
        """
        Calcula requisitos para aquisição do benefício da aposentadoria pelas regras dos pontos (85/95)
        """

        if qtdContribuicoes < 180 or dib > self.dataReforma2019:
            return False
        else:
            acrescimoPontos: int = 0
            if datetime.date(year=2018, month=12, day=31) < dib < self.dataReforma2019:
                acrescimoPontos = 1

            ultimoDiaMes: int = monthrange(dib.year, dib.month)[1]
            dib = datetime.date(dib.year, dib.month, ultimoDiaMes)
            idadeCliente: relativedelta = calculaIdade(strToDate(self.cliente.dataNascimento), dib)
            pontosCliente: int = (idadeCliente + tempoContribuicao).years

            if self.enumGeneroCliente == GeneroCliente.masculino:
                return tempoContribuicao.years >= 35 and pontosCliente >= 95 + acrescimoPontos
            else:
                return tempoContribuicao.years >= 30 and pontosCliente >= 85 + acrescimoPontos

    def atingiuTmpContribuicaoAR(self, dib: datetime.date, qtdContribuicoes: int, tempoContribuicao: relativedelta) -> bool:
        """
        Calcula requisitos para aquisição do benefício da aposentadoria por idade ANTES DA REFORMA de 2019
        :param dib: Data do início do benefício, caso as condições sejam satisfeitas
        :param tempoContribuicao:
        :return:
        """

        if qtdContribuicoes < 180 or dib > self.dataReforma2019:
            return False
        else:
            if self.enumGeneroCliente == GeneroCliente.masculino:
                return tempoContribuicao.years >= 35
            else:
                return tempoContribuicao.years >= 30

    def atingiuRegraPontos(self, dib: datetime.date, tempoContribuicao: relativedelta) -> bool:
        """
        Avalia a pontuação mínima e o tempo mínimo de contribuição (20 anos Homens / 15 anos Mulheres)
        :return bool
        """
        acrescimoAnual = dib.year - 2019
        tmpContribuicao = tempoContribuicao
        ultimoDiaMes = monthrange(dib.year, dib.month)[1]
        dataRelativa: datetime.date = datetime.date(dib.year, dib.month, ultimoDiaMes)
        idadeAteFinalMes: relativedelta = calculaIdade(self.cliente.dataNascimento, dataRelativa)
        pontuacao = tempoContribuicao + idadeAteFinalMes

        if dib < self.dataReforma2019:
            return False

        descontoProfessor: int = 0
        if self.cliente.professor:
            descontoProfessor = 5

        if self.enumGeneroCliente == GeneroCliente.masculino:
            if acrescimoAnual >= 9:
                acrescimoAnual = 9

            return pontuacao.years >= 96 + acrescimoAnual - descontoProfessor and tmpContribuicao.years >= 35 - descontoProfessor
        else:
            if acrescimoAnual >= 14:
                acrescimoAnual = 14

            return pontuacao.years >= 86 + acrescimoAnual - descontoProfessor and tmpContribuicao.years >= 30 - descontoProfessor

    def atingiuRegraIdadeMinima(self, dib: datetime.date, tempoContribuicao: relativedelta) -> bool:
        """
        Avalia a idade mínima e o tempo mínimo de contribuição
        - Tempo mínimo de contribuição: 35 anos Homens / 30 anos Mulheres
        - Idade mínima em 2019 (data da reforma): 61 anos Homens / 56 anos Mulheres
        - Idade mínima padrão: 65 anos Homens / 62 anos Mulheres
        :return bool
        """
        tmpContribuicao = tempoContribuicao
        ultimoDiaMes = monthrange(dib.year, dib.month)[1]
        finalDoMes = datetime.date(dib.year, dib.month, ultimoDiaMes)
        idadeCliente = calculaIdade(self.cliente.dataNascimento, finalDoMes)

        if dib < self.dataReforma2019:
            return False

        if self.enumGeneroCliente == GeneroCliente.masculino and tmpContribuicao.years >= 35:
            acrescimoIdade: relativedelta = relativedelta(years=61, months=(dib.year - 2019) * 6)

            if acrescimoIdade.years >= 65:
                acrescimoIdade = relativedelta(years=65)

        elif self.enumGeneroCliente == GeneroCliente.feminino and tmpContribuicao.years >= 30:
            acrescimoIdade: relativedelta = relativedelta(years=56, months=(dib.year - 2019) * 6)

            if acrescimoIdade.years >= 62:
                acrescimoIdade = relativedelta(years=62)

        else:
            return False

        if idadeCliente.years > acrescimoIdade.years:
            return True
        elif idadeCliente.years == acrescimoIdade.years and idadeCliente.months >= acrescimoIdade.months:
            return True
        else:
            return False

    def atingiuRegraPedagio50(self, dib: datetime.date, tempoContribuicao: relativedelta) -> dict:
        """
        Avalia se até a data da reforma, o indivíduo tinha, no máximo, 2 anos para requerer a aposentadoria
        - Mínimo 35 anos homens / 30 anos mulheres
        :return bool
        """

        if dib > self.dataReforma2019:
            return {'status': False}

        tmpContribuicao = tempoContribuicao

        acrescimoProfessor = 0
        if self.cliente.professor:
            acrescimoProfessor = 5

        if self.enumGeneroCliente == GeneroCliente.masculino:
            resposta: dict = {
                'status': 33 <= tmpContribuicao.years + acrescimoProfessor,
                'ultrapassou': tmpContribuicao.years + acrescimoProfessor > 35
            }
        else:
            resposta: dict = {
                'status': 28 <= tmpContribuicao.years + acrescimoProfessor,
                'ultrapassou': tmpContribuicao.years + acrescimoProfessor > 30
            }
        
        return resposta

    def atingiuRedTmpContribuicao(self, dib: datetime.date, tempoContribuicao: relativedelta) -> bool:
        """
        Avalia se:
        - Homens -- Tempo de contribuição >= 15 e Idade >= 65
        - Mulheres -- Tempo de contribuição >= 15 e Idade >= 60 (acréscimo de 6 meses por ano)
        :return bool:
        """
        if dib < self.dataReforma2019:
            return False

        anosAposReforma: int = self.dataReforma2019.year - dib.year
        acrescimoMensal = relativedelta(months=6*anosAposReforma).normalized()
        ultimoDiaMes: int = monthrange(dib.year, dib.month)[1]
        finalMes: datetime.date = datetime.date(dib.year, dib.month, ultimoDiaMes)
        idadeClienteAteFinalMes: relativedelta = calculaIdade(self.cliente.dataNascimento, finalMes)

        if tempoContribuicao.years < 15:
            return False
        else:
            if self.enumGeneroCliente == GeneroCliente.masculino:
                return idadeClienteAteFinalMes.years >= 65
            else:
                if idadeClienteAteFinalMes.years == 60 + acrescimoMensal.years:
                    return idadeClienteAteFinalMes.months >= acrescimoMensal.months
                elif idadeClienteAteFinalMes.years >= 60:
                    return True

    def atingiuPedagio100(self, dib: datetime.date) -> bool:
        """
        Na data da reforma o segurado deverá cumprir:
        - idade mínima de 60H/57M
        - Tempo de contribuição 35H/30M
        :param dib:
        :return:
        """

        if dib > self.dataReforma2019:
            return False

        acrescimoProfessor = 0
        if self.cliente.professor:
            acrescimoProfessor = 5

        ultimoDiaMes: int = monthrange(dib.year, dib.month)[1]
        competenciaFinalMes = datetime.date(dib.year, dib.month, ultimoDiaMes)
        idadeFimMes: relativedelta = calculaIdade(strToDate(self.cliente.dataNascimento), competenciaFinalMes)

        if self.enumGeneroCliente == GeneroCliente.masculino:
            return idadeFimMes.years + acrescimoProfessor >= 60
        else:
            return idadeFimMes.years + acrescimoProfessor >= 57
        
    def calculaDibsDireitoAdquirido(self, competenciaAtual: datetime.date, qtdContribuicoes: int, tempoContribuicao: relativedelta):
        if competenciaAtual > self.dataReforma2019:
            if RegraGeralAR.idade in self.regrasACalcular:
                self.setIdadeAR(qtdContribuicoes, tempoContribuicao, dataMinima=True)
                self.regrasACalcular.remove(RegraGeralAR.idade)

            if RegraGeralAR.fator85_95 in self.regrasACalcular:
                self.setRegra85_95(competenciaAtual, qtdContribuicoes, tempoContribuicao)
                self.regrasACalcular.remove(RegraGeralAR.fator85_95)
            return True

        ultimoDiaMes: int = monthrange(competenciaAtual.year, competenciaAtual.month)[1]
        competenciaParaEstaRegra = datetime.date(competenciaAtual.year, competenciaAtual.month, ultimoDiaMes)

        if RegraGeralAR.idade in self.regrasACalcular and self.atingiuIdadeAR(competenciaAtual, qtdContribuicoes):
            self.setIdadeAR(competenciaParaEstaRegra, qtdContribuicoes)
            self.regrasACalcular.remove(RegraGeralAR.idade)
        elif RegraGeralAR.idade in self.regrasACalcular and competenciaAtual >= self.dataReforma2019:
            self.setIdadeAR(competenciaParaEstaRegra, qtdContribuicoes, dataMinima=True)
            self.regrasACalcular.remove(RegraGeralAR.idade)

        if RegraGeralAR.tempoContribuicao in self.regrasACalcular and self.atingiuTmpContribuicaoAR(competenciaAtual, qtdContribuicoes, tempoContribuicao):
            self.setTmpContribuicaoAR(competenciaParaEstaRegra, qtdContribuicoes, tempoContribuicao)
            self.regrasACalcular.remove(RegraGeralAR.tempoContribuicao)
        elif RegraGeralAR.tempoContribuicao in self.regrasACalcular and competenciaAtual >= self.dataReforma2019:
            self.setTmpContribuicaoAR(competenciaParaEstaRegra, qtdContribuicoes, tempoContribuicao, dataMinima=True)
            self.regrasACalcular.remove(RegraGeralAR.tempoContribuicao)

        if RegraGeralAR.fator85_95 in self.regrasACalcular and self.atingiuRegra85_95(competenciaAtual, qtdContribuicoes, tempoContribuicao):
            self.setRegra85_95(competenciaAtual, qtdContribuicoes, tempoContribuicao)
            self.regrasACalcular.remove(RegraGeralAR.fator85_95)
        elif RegraGeralAR.fator85_95 in self.regrasACalcular and competenciaAtual >= self.dataReforma2019:
            self.setRegra85_95(competenciaParaEstaRegra, qtdContribuicoes, tempoContribuicao)
            self.regrasACalcular.remove(RegraGeralAR.fator85_95)

    def calculaDibsRegrasTransicao(self, competenciaAtual: datetime.date, qtdContribuicoes: int, tempoContribuicao: relativedelta):
        ultimoDiaMes: int = monthrange(competenciaAtual.year, competenciaAtual.month)[1]
        competenciaParaEstaRegra = datetime.date(competenciaAtual.year, competenciaAtual.month, ultimoDiaMes)

        if RegraTransicao.reducaoTempoContribuicao in self.regrasACalcular and self.atingiuRedTmpContribuicao(competenciaAtual, tempoContribuicao):
            self.setRedTmpContribuicao(competenciaParaEstaRegra, qtdContribuicoes, tempoContribuicao)
            self.regrasACalcular.remove(RegraTransicao.reducaoTempoContribuicao)

        if RegraTransicao.reducaoIdadeMinima in self.regrasACalcular and self.atingiuRegraIdadeMinima(competenciaAtual, tempoContribuicao):
            self.setReducaoIdadeMinima(competenciaParaEstaRegra, qtdContribuicoes, tempoContribuicao)
            self.regrasACalcular.remove(RegraTransicao.reducaoIdadeMinima)

        if RegraTransicao.pontos in self.regrasACalcular and self.atingiuRegraPontos(competenciaAtual, tempoContribuicao):
            self.setPontos(competenciaParaEstaRegra, qtdContribuicoes, tempoContribuicao)
            self.regrasACalcular.remove(RegraTransicao.pontos)

        if competenciaAtual.year == self.dataReforma2019.year and RegraTransicao.pedagio50 in self.regrasACalcular:
            dataRelReferencia = relativedelta(self.dataReforma2019, competenciaAtual)
            months = dataRelReferencia.months
            days = dataRelReferencia.days

            if months == 0 and 0 <= days < 30:
                self.regrasACalcular.remove(RegraTransicao.pedagio50)

                dictResposta = self.atingiuRegraPedagio50(competenciaAtual, tempoContribuicao)

                if dictResposta['status']:
                    self.efetivaDibPedagio50(competenciaAtual, tempoContribuicao, dictResposta['ultrapassou'])
                    self.setPedagio50(qtdContribuicoes, tempoContribuicao)
                else:
                    self.setPedagio50(qtdContribuicoes, tempoContribuicao, dataMinima=True)
        elif competenciaAtual.year > self.dataReforma2019.year and RegraTransicao.pedagio50 in self.regrasACalcular:
            self.setPedagio50(qtdContribuicoes, tempoContribuicao, dataMinima=True)
            self.regrasACalcular.remove(RegraTransicao.pedagio50)

        if competenciaAtual.year == self.dataReforma2019.year and RegraTransicao.pedagio100 in self.regrasACalcular:
            dataRelReferencia = relativedelta(self.dataReforma2019, competenciaAtual)
            months = dataRelReferencia.months
            days = dataRelReferencia.days

            if months == 0 and 0 <= days < 30:
                self.regrasACalcular.remove(RegraTransicao.pedagio100)

                if self.atingiuPedagio100(competenciaAtual):
                    self.setPedagio100(competenciaAtual, qtdContribuicoes, tempoContribuicao)
                else:
                    self.setPedagio100(competenciaAtual, qtdContribuicoes, tempoContribuicao, naoAtingiu=True)
        elif competenciaAtual.year > self.dataReforma2019.year and RegraTransicao.pedagio100 in self.regrasACalcular:
            self.setPedagio100(competenciaAtual, qtdContribuicoes, tempoContribuicao, naoAtingiu=True)
            self.regrasACalcular.remove(RegraTransicao.pedagio100)

    def calculaDibs(self):
        tempoContribuicao: relativedelta = relativedelta(days=0)
        competenciaAtual: datetime.date = datetime.date.min
        seqAtual: int = 0
        qtdContribuicoes: int = 0
        listaItensContribuicao: List[ItemContribuicao] = ItemContribuicao.select().where(ItemContribuicao.clienteId == self.cliente.clienteId).order_by(
            ItemContribuicao.seq,
            ItemContribuicao.competencia
        )

        for index, item in enumerate(listaItensContribuicao):
            mudouSeq = seqAtual != item.seq and seqAtual != 0

            if index == 0 or mudouSeq:
                seqAtual = item.seq
                continue

            competenciaAnterior = strToDate(listaItensContribuicao[index - 1].competencia)
            competenciaAtual = strToDate(item.competencia)

            # No caso de atividades concomitantes, não calcular duas vezes tempo de contribuiçao
            if not item.ativPrimaria and dataConflitante(competenciaAtual, seqAtual, self.cliente.clienteId):
                continue
            else:
                qtdContribuicoes += 1

                # Um indicador deve estar impedindo a soma dessa competência
                if not item.validoTempoContrib:
                    continue

                if competenciaAtual < self.dataReforma2019:
                    tempoContribuicao += relativedelta(competenciaAtual, competenciaAnterior)
                else:
                    tempoContribuicao += relativedelta(months=1)

            self.calculaDibsRegrasTransicao(competenciaAtual, qtdContribuicoes, tempoContribuicao)
            self.calculaDibsDireitoAdquirido(competenciaAtual, qtdContribuicoes, tempoContribuicao)

        if len(self.regrasACalcular) != 0:
            mesesAMais = 0
            itemARepetir = listaItensContribuicao[-1]
            listaItensAMais = []

            while len(self.regrasACalcular) != 0:
                if competenciaAtual > self.dataReforma2019:
                    self.regrasACalcular = [regra for regra in self.regrasACalcular if not isinstance(regra, RegraGeralAR)]

                qtdContribuicoes += 1
                mesesAMais += 1
                competenciaAtual += relativedelta(months=1)
                tempoContribuicao += relativedelta(months=1)
                listaItensAMais.append({
                    'clienteId': itemARepetir.clienteId,
                    'seq': itemARepetir.seq + 1,
                    'tipo': TipoItemContribuicao.remuneracao.value,
                    'competencia': competenciaAtual,
                    'contribuicao': itemARepetir.contribuicao,
                    'ativPrimaria': True,
                    'dadoOrigem': 'N',
                    'geradoAutomaticamente': True,
                    'validoTempoContrib': True,
                    'validoSalContrib': True
                })

                self.calculaDibsRegrasTransicao(competenciaAtual, qtdContribuicoes, tempoContribuicao)
                self.calculaDibsDireitoAdquirido(competenciaAtual, qtdContribuicoes, tempoContribuicao)

            if mesesAMais > 0:
                self.salvarItensNVezes(listaItensAMais)

            return True

    def calculaFatorPrevidenciario(self, dibAtual: datetime.date, tempoContribCalculado: relativedelta):
        """
        Cálculo do fator previdenciário

        :var<float>: tempCont - Tempo de contribuição até o momento da aposentadoria
        :var<float>: aliq - Alíquota de contribuição
        :var<float>: expSobrevida - Expectativa de sobrevida após a data do início do benefício (dib)
        :var<float>: idade - Idade do cliente na data do início do benefício

        :return<float>: fatorPrev  = ((tempCont * aliq) / expSobrevida) * (1 + (idade + (tempCont * aliq)) / 100)
        """

        tempCont: float = tempoContribCalculado.years + ((tempoContribCalculado.days / 30) + tempoContribCalculado.months / 12)
        aliq: float = 0.31
        intIdade: relativedelta = calculaIdade(strToDate(self.cliente.dataNascimento), dibAtual)
        floatIdade: float = (intIdade.days/30 + intIdade.months)/12 + intIdade.years  # Para a fórmula é importante que a idade seja completa com dias e meses transformados em anos

        try:
            expSobrevidaModelo: ExpSobrevida = ExpSobrevida.select().where(
                ExpSobrevida.dataReferente.year == dibAtual.year,
                ExpSobrevida.idade == intIdade.years
            ).get()
        except ExpSobrevida.DoesNotExist:
            expSobrevidaModelo: ExpSobrevida = ExpSobrevida.select().where(
                # ExpSobrevida.dataReferente.year == dibAtual.year - 1,
                ExpSobrevida.idade == intIdade.years
            ).order_by(ExpSobrevida.dataReferente.desc()).get()

        expSobrevida: int = expSobrevidaModelo.expectativaSobrevida

        fatorPrev = ((tempCont * aliq) / expSobrevida) * (1 + (floatIdade + (tempCont * aliq)) / 100)

        return fatorPrev

    def calculaValorBeneficios(self):
        self.valorBeneficios[RegraTransicao.pedagio50] = self.rmiPedagio50()
        self.valorBeneficios[RegraTransicao.pontos] = self.rmiPontos()
        self.valorBeneficios[RegraTransicao.pedagio100] = self.rmiPedagio100()
        self.valorBeneficios[RegraTransicao.reducaoTempoContribuicao] = self.rmiRedTmpContribuicao()
        self.valorBeneficios[RegraTransicao.reducaoIdadeMinima] = self.rmiRedIdadeMinima()
        self.valorBeneficios[RegraGeralAR.idade] = self.rmiIdadeAR()
        self.valorBeneficios[RegraGeralAR.tempoContribuicao] = self.rmiTmpContribuicaoAR()
        self.valorBeneficios[RegraGeralAR.fator85_95] = self.rmiRegra85_95()

    def rmiPedagio50(self) -> float:
        """
        Calcula Renda Básica Inicial, caso cliente tenha optado pela regra de transição Pedágio 50%
        :return: float
        """
        salarioMinimo: SalarioMinimo
        if self.dibs[RegraTransicao.pedagio50] != datetime.date.min and self.tmpContribPorRegra[RegraTransicao.pedagio50] is not None:
            fatorPrev = self.calculaFatorPrevidenciario(self.dibs[RegraTransicao.pedagio50], self.tmpContribPorRegra[RegraTransicao.pedagio50])
            mediaSalarios = self.calculaMediaSalarial(self.dibs[RegraTransicao.pedagio50])

            try:
                salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraTransicao.pedagio50].year).get()
            except SalarioMinimo.DoesNotExist as err:
                salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()

            valorInicial = round(mediaSalarios * fatorPrev, ndigits=2)
            valorBeneficio = max(valorInicial, salarioMinimo.valor)

            return valorBeneficio
        else:
            return 0.0

    def rmiPedagio100(self) -> float:
        if self.dibs[RegraTransicao.pedagio100] != datetime.date.min:
            try:
                salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraTransicao.pedagio50].year).get()
            except SalarioMinimo.DoesNotExist as err:
                salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()

            valorInicial = round(self.calculaMediaSalarial(self.dibs[RegraTransicao.pedagio100]), ndigits=2)
            valorBeneficio = max(valorInicial, salarioMinimo.valor)

            return valorBeneficio
        else:
            return 0.0

    def rmiPontos(self) -> float:
        """
        Calcula Renda Básica Inicial, caso cliente tenha optado pela regra de pontos
        :return: float
        """
        mediaSalarios: float = self.calculaMediaSalarial(self.dibs[RegraTransicao.pontos])
        tempoContribuicao: relativedelta = self.tmpContribPorRegra[RegraTransicao.pontos]
        try:
            salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraTransicao.pedagio50].year).get()
        except SalarioMinimo.DoesNotExist as err:
            salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()

        if self.enumGeneroCliente == GeneroCliente.masculino:
            desconto = (tempoContribuicao.years - 20) * 2 + 60
        else:
            desconto = (tempoContribuicao.years - 15) * 2 + 60

        valorInicial = round(mediaSalarios * (desconto/100), ndigits=2)
        valorBenefício = max(valorInicial, salarioMinimo.valor)

        return valorBenefício

    def rmiRedIdadeMinima(self) -> float:
        """
        Calcula Renda Básica Inicial, caso cliente tenha optado pela Redução do tempo de contribuição
        :return: float
        """
        mediaSalarios: float = self.calculaMediaSalarial(self.dibs[RegraTransicao.reducaoIdadeMinima])
        tempoContribuicao: relativedelta = self.tmpContribPorRegra[RegraTransicao.reducaoIdadeMinima]
        try:
            salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraTransicao.pedagio50].year).get()
        except SalarioMinimo.DoesNotExist as err:
            salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()

        if self.enumGeneroCliente == GeneroCliente.masculino:
            porcentagemAcrescimo = tempoContribuicao.years - 20
            if porcentagemAcrescimo < 0:
                porcentagemAcrescimo = 0

            desconto = porcentagemAcrescimo * 2 + 60
        else:
            porcentagemAcrescimo: int = tempoContribuicao.years - 15
            desconto = porcentagemAcrescimo * 2 + 60

        valorInicial = round(mediaSalarios * (desconto / 100), ndigits=2)
        valorBeneficio = max(valorInicial, salarioMinimo.valor)

        return valorBeneficio

    def rmiRedTmpContribuicao(self) -> float:
        """
        Calcula Renda Básica Inicial, caso cliente tenha optado pela Redução do tempo de contribuição
        :return: float
        """
        mediaSalarios: float = self.calculaMediaSalarial(self.dibs[RegraTransicao.reducaoTempoContribuicao])
        tempoContribuicao: relativedelta = self.tmpContribPorRegra[RegraTransicao.reducaoTempoContribuicao]
        try:
            salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraTransicao.pedagio50].year).get()
        except SalarioMinimo.DoesNotExist as err:
            salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()

        if self.enumGeneroCliente == GeneroCliente.masculino:
            porcentagemAcrescimo = tempoContribuicao.years - 20
            if porcentagemAcrescimo < 0:
                porcentagemAcrescimo = 0

            desconto = porcentagemAcrescimo * 2 + 60
        else:
            porcentagemAcrescimo: int = tempoContribuicao.years - 15
            desconto = porcentagemAcrescimo * 2 + 60

        valorInicial = round(mediaSalarios * (desconto / 100), ndigits=2)
        valorBeneficio = max(valorInicial, salarioMinimo.valor)

        return valorBeneficio

    def rmiIdadeAR(self) -> float:
        """
        Renda mensal inicial antes da reforma
        :return:
        """
        if self.dibs[RegraGeralAR.idade] == datetime.date.min:
            return 0.0

        mediaSalarios: float = self.calculaMediaSalarial(self.dibs[RegraGeralAR.idade])
        tempoContribuicao: relativedelta = self.tmpContribPorRegra[RegraGeralAR.idade]
        fator: float = self.calculaFatorPrevidenciario(self.dibs[RegraGeralAR.idade], self.tmpContribPorRegra[RegraGeralAR.idade])

        try:
            salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraGeralAR.idade].year).get()
        except SalarioMinimo.DoesNotExist as err:
            salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()

        desconto: float = (70 + tempoContribuicao.years) / 100

        valorInicial = mediaSalarios * desconto
        valorBeneficio = max(valorInicial, valorInicial*fator, salarioMinimo.valor)

        return valorBeneficio

    def rmiRegra85_95(self) -> float:
        """
        Renda mensal inicial pela regra 85/95
        :return:
        """
        if self.dibs[RegraGeralAR.fator85_95] == datetime.date.min or self.dibs[RegraGeralAR.fator85_95] is None:
            return 0.0

        mediaSalarios: float = self.calculaMediaSalarial(self.dibs[RegraGeralAR.fator85_95])

        try:
            salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraGeralAR.fator85_95].year).get()
        except SalarioMinimo.DoesNotExist as err:
            salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()

        return round(max(mediaSalarios, salarioMinimo.valor), ndigits=2)

    def rmiTmpContribuicaoAR(self) -> float:
        """
        Calcular regras para aposentadoria por tempo de contribuição AR
        :return:
        """
        if self.dibs[RegraGeralAR.tempoContribuicao] == datetime.date.min or self.dibs[RegraGeralAR.tempoContribuicao] is None:
            return 0.0

        mediaSalarios: float = self.calculaSomaSalarial(self.dibs[RegraGeralAR.tempoContribuicao])

        fatorPrev: float = self.calculaFatorPrevidenciario(self.dibs[RegraGeralAR.tempoContribuicao], self.tmpContribPorRegra[RegraGeralAR.tempoContribuicao])

        try:
            salarioMinimo = SalarioMinimo.select().where(SalarioMinimo.vigencia.year == self.dibs[RegraGeralAR.tempoContribuicao].year).get()
        except SalarioMinimo.DoesNotExist as err:
            salarioMinimo = SalarioMinimo.select().order_by(SalarioMinimo.vigencia.desc()).get()
        valorBeneficio = max(mediaSalarios*fatorPrev, salarioMinimo.valor)

        return round(valorBeneficio, 2)

    def efetivaDibPedagio50(self, competenciaAtual: datetime.date, tempoContribuicao: relativedelta, ultrapassouMinimo: bool):
        if ultrapassouMinimo:
            self.dibs[RegraTransicao.pedagio50] = competenciaAtual
            return True

        tempContribRelativo: relativedelta = tempoContribuicao
        if self.enumGeneroCliente == GeneroCliente.masculino:
            pedagio50: relativedelta = relativedelta(years=35) - tempContribRelativo
        else:
            pedagio50: relativedelta = relativedelta(years=30) - tempContribRelativo

        if pedagio50.years <= 0 and pedagio50.months <= 0:
            self.dibs[RegraTransicao.pedagio50] = competenciaAtual
        else:
            self.dibs[RegraTransicao.pedagio50] = competenciaAtual + pedagio50

    def salvarItensNVezes(self, itemReferente: List[dict]):
        ItemContribuicao.insert_many(itemReferente).execute()

    def setIdadeAR(self, qtdContribuicoes, tempoContribuicao, dataMinima: bool = False):
        if dataMinima:
            self.dibs[RegraGeralAR.idade] = datetime.date.min
        else:
            self.regrasAposentadoria[RegraGeralAR.idade] = True

        self.qtdContrib[RegraGeralAR.idade] = qtdContribuicoes
        self.tmpContribPorRegra[RegraGeralAR.idade] = tempoContribuicao

    def setPedagio50(self, qtdContribuicoes, tempoContribuicao, dataMinima: bool = False):
        if dataMinima:
            self.dibs[RegraTransicao.pedagio50] = datetime.date.min
        else:
            self.regrasAposentadoria[RegraTransicao.pedagio50] = True

        self.qtdContrib[RegraTransicao.pedagio50] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.pedagio50] = tempoContribuicao

    def setPedagio100(self, competenciaAtual: datetime.date, qtdContribuicoes: int, tempoContribuicao: relativedelta, naoAtingiu: bool = False):
        if naoAtingiu:
            self.dibs[RegraTransicao.pedagio100] = datetime.date.min
            self.qtdContrib[RegraTransicao.pedagio100] = qtdContribuicoes
            self.tmpContribPorRegra[RegraTransicao.pedagio100] = tempoContribuicao
            return True
        else:
            self.regrasAposentadoria[RegraTransicao.pedagio100]

        acrescimoProfessor = 0
        if self.cliente.professor:
            acrescimoProfessor = 5

        if self.enumGeneroCliente == GeneroCliente.masculino:
            tmpMinimoContribuicao: relativedelta = relativedelta(years=35 - acrescimoProfessor)
            tempoRestante = tmpMinimoContribuicao - tempoContribuicao
        else:
            tmpMinimoContribuicao: relativedelta = relativedelta(years=30 - acrescimoProfessor)
            tempoRestante = tmpMinimoContribuicao - tempoContribuicao

        self.dibs[RegraTransicao.pedagio100] = competenciaAtual + tempoRestante + tempoRestante
        self.qtdContrib[RegraTransicao.pedagio100] = qtdContribuicoes + 2 * tempoRestante.months
        self.tmpContribPorRegra[RegraTransicao.pedagio100] = tempoContribuicao + tempoRestante + tempoRestante

    def setPontos(self, competenciaAtual, qtdContribuicoes, tempoContribuicao):
        if competenciaAtual != datetime.date.min:
            self.regrasAposentadoria[RegraTransicao.pontos] = True
            
        self.dibs[RegraTransicao.pontos] = competenciaAtual
        self.qtdContrib[RegraTransicao.pontos] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.pontos] = tempoContribuicao

    def setRegra85_95(self, competenciaAtual, qtdContribuicoes, tempoContribuicao):
        if competenciaAtual <= self.dataReforma2019:
            self.dibs[RegraGeralAR.fator85_95] = competenciaAtual
            self.regrasAposentadoria[RegraGeralAR.fator85_95] = True
        else:
            self.dibs[RegraGeralAR.fator85_95] = datetime.date.min

        self.qtdContrib[RegraGeralAR.fator85_95] = qtdContribuicoes
        self.tmpContribPorRegra[RegraGeralAR.fator85_95] = tempoContribuicao

    def setReducaoIdadeMinima(self, competenciaAtual, qtdContribuicoes, tempoContribuicao):
        if competenciaAtual != datetime.date.min:
            self.regrasAposentadoria[RegraTransicao.reducaoIdadeMinima] = True
        
        self.dibs[RegraTransicao.reducaoIdadeMinima] = competenciaAtual
        self.qtdContrib[RegraTransicao.reducaoIdadeMinima] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.reducaoIdadeMinima] = tempoContribuicao

    def setRedTmpContribuicao(self, competenciaAtual, qtdContribuicoes, tempoContribuicao):
        if competenciaAtual != datetime.date.min:
            self.regrasAposentadoria[RegraTransicao.reducaoTempoContribuicao] = True
        
        self.dibs[RegraTransicao.reducaoTempoContribuicao] = competenciaAtual
        self.qtdContrib[RegraTransicao.reducaoTempoContribuicao] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.reducaoTempoContribuicao] = tempoContribuicao

    def setTmpContribuicaoAR(self, competenciaAtual, qtdContribuicoes, tempoContribuicao, dataMinima: bool = False):
        if dataMinima:
            self.dibs[RegraGeralAR.tempoContribuicao] = datetime.date.min
        else:
            self.regrasAposentadoria[RegraGeralAR.tempoContribuicao] = True

        self.dibs[RegraGeralAR.tempoContribuicao] = competenciaAtual
        self.qtdContrib[RegraGeralAR.tempoContribuicao] = qtdContribuicoes
        self.tmpContribPorRegra[RegraGeralAR.tempoContribuicao] = tempoContribuicao

    def calculaMediaSalarial(self, dibReferente: datetime.date) -> float:
        if not isinstance(dibReferente, datetime.date):
            return 0.0

        selecaoDataInicio: bool = self.dfTotalContribuicoes['competencia'] > self.dataTrocaMoeda.strftime('%Y-%m-%d')
        selecaoDataFim: bool = self.dfTotalContribuicoes['competencia'] <= dibReferente.strftime('%Y-%m-%d')
        dfEmQuestao: pd.DataFrame = self.dfTotalContribuicoes[selecaoDataInicio & selecaoDataFim]
        return dfEmQuestao['salAtualizado'].mean()

    def calculaSomaSalarial(self, dibReferente: datetime.date) -> float:
        if dibReferente is None:
            return 0.0

        selecaoDataInicio: bool = self.dfTotalContribuicoes['competencia'] > self.dataTrocaMoeda.strftime('%Y-%m-%d')
        selecaoDataFim: bool = self.dfTotalContribuicoes['competencia'] <= dibReferente.strftime('%Y-%m-%d')
        dfEmQuestao: pd.DataFrame = self.dfTotalContribuicoes[selecaoDataInicio & selecaoDataFim]
        qtdContribuicoes: int = floor(dfEmQuestao.shape[0]*0.8)
        dfFinal = dfEmQuestao.sort_values(by='salAtualizado', ascending=False, ignore_index=True)
        return dfFinal['salAtualizado'][:qtdContribuicoes].mean()

    def atualizaDataFrameContribuicoes(self):
        lambAvaliaSalario = lambda df: df['salContribuicao'] if df['salContribuicao'] <= df['teto'] else df['teto']
        dbInst: SqliteDatabase = ItemContribuicao._meta.database
        query: str = selectItensDados(self.cliente.clienteId)
        listaContribuicoes = dbInst.execute_sql(query)

        colunas: list = ['competencia', 'salContribuicao', 'fator', 'teto']
        dfContribuicoes = pd.DataFrame(listaContribuicoes.fetchall(), columns=colunas)

        dfContribuicoes['salContribuicaoAux'] = dfContribuicoes.apply(lambAvaliaSalario, axis=1)
        salAtualizado = dfContribuicoes['salContribuicaoAux'] * dfContribuicoes['fator']
        dfContribuicoes['salAtualizado'] = salAtualizado
        self.dfTotalContribuicoes = dfContribuicoes
        
    def salvaAposentadorias(self):
        seq: int = 0
        self.processo.dataUltAlt = datetime.datetime.now()
        self.processo.save()

        for chave, atingiu in self.regrasAposentadoria.items():
            if atingiu:
                seq += 1
                if chave == RegraTransicao.pontos:
                    tipo = "POTR"
                elif chave == RegraTransicao.pedagio50:
                    tipo = "PD50"
                elif chave == RegraGeralAR.tempoContribuicao:
                    tipo = "TCAR"
                elif chave == RegraGeralAR.idade:
                    tipo = "IDAR"
                elif chave == RegraTransicao.reducaoIdadeMinima:
                    tipo = "RIDM"
                elif chave == RegraTransicao.reducaoTempoContribuicao:
                    tipo = "RETC"
                elif chave == RegraTransicao.pedagio100:
                    tipo = "P100"
                else:
                    tipo = ''
                    
                Aposentadoria(
                    clienteId=self.cliente.clienteId,
                    processoId=self.processo.processoId,
                    seq=seq,
                    tipo=tipo,
                    contribMeses=self.tmpContribPorRegra[chave].months,
                    contribAnos=self.tmpContribPorRegra[chave].years,
                    valorBeneficio=self.valorBeneficios[chave],
                    dib=self.dibs[chave],
                    der=datetime.date.min,
                ).save()
        return True