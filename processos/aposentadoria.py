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

    def __init__(self, processo: Processos, cliente: Cliente, db=None):
        self.processo = processo
        self.cliente = cliente
        self.daoCalculos = DaoCalculos(db)

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
            RegraGeralAR.tempoContribuicao
        ]

        self.regrasAposentadoria = {
            RegraTransicao.pontos: None,
            RegraTransicao.reducaoIdadeMinima: None,
            RegraTransicao.pedagio50: None,
            RegraTransicao.reducaoTempoContribuicao: None,
            RegraTransicao.pedagio100: None,
            RegraGeralAR.fator85_95: None,
            RegraGeralAR.idade: None,
            RegraGeralAR.tempoContribuicao: None
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

        # print('\n\n------------------------------------ calculaFatorPrevidenciario')
        # print(f"tempCont: {tempCont}")
        # print(f"aliq: {aliq}")
        # print(f"idade: {idade}")
        # print(f"expSobrevida: {expSobrevida}")
        # print(f"fatorPrev: {fatorPrev}")
        # print(f"Possível dib: {expSobrevidaModelo.dataReferente}")
        # print('------------------------------------ calculaFatorPrevidenciario\n\n')
        return fatorPrev

    def calculaValorBeneficios(self):
        self.valorBeneficios[RegraTransicao.pedagio50] = self.rmiPedagio50()
        self.valorBeneficios[RegraTransicao.pontos] = self.rmiPontos()
        self.valorBeneficios[RegraTransicao.pedagio100] = self.rmiPedagio100()
        self.valorBeneficios[RegraTransicao.reducaoTempoContribuicao] = self.rmiRedTmpContribuicao()
        self.valorBeneficios[RegraTransicao.reducaoIdadeMinima] = self.rmiRedIdadeMinima()
        self.valorBeneficios[RegraGeralAR.idade] = self.rmiIdadeAR()
        self.valorBeneficios[RegraGeralAR.tempoContribuicao] = self.rmiTmpContribuicaoAR()

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

        self.qtdContrib[RegraGeralAR.idade] = qtdContribuicoes
        self.tmpContribPorRegra[RegraGeralAR.idade] = tempoContribuicao

    def setPedagio50(self, qtdContribuicoes, tempoContribuicao, dataMinima: bool = False):
        if dataMinima:
            self.dibs[RegraTransicao.pedagio50] = datetime.date.min

        self.qtdContrib[RegraTransicao.pedagio50] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.pedagio50] = tempoContribuicao

    def setPedagio100(self, competenciaAtual: datetime.date, qtdContribuicoes: int, tempoContribuicao: relativedelta, naoAtingiu: bool = False):
        if naoAtingiu:
            self.dibs[RegraTransicao.pedagio100] = datetime.date.min
            self.qtdContrib[RegraTransicao.pedagio100] = qtdContribuicoes
            self.tmpContribPorRegra[RegraTransicao.pedagio100] = datetime.date.min
            return True

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
        self.dibs[RegraTransicao.pontos] = competenciaAtual
        self.qtdContrib[RegraTransicao.pontos] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.pontos] = tempoContribuicao

    def setReducaoIdadeMinima(self, competenciaAtual, qtdContribuicoes, tempoContribuicao):
        self.dibs[RegraTransicao.reducaoIdadeMinima] = competenciaAtual
        self.qtdContrib[RegraTransicao.reducaoIdadeMinima] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.reducaoIdadeMinima] = tempoContribuicao

    def setRedTmpContribuicao(self, competenciaAtual, qtdContribuicoes, tempoContribuicao):
        self.dibs[RegraTransicao.reducaoTempoContribuicao] = competenciaAtual
        self.qtdContrib[RegraTransicao.reducaoTempoContribuicao] = qtdContribuicoes
        self.tmpContribPorRegra[RegraTransicao.reducaoTempoContribuicao] = tempoContribuicao

    def setTmpContribuicaoAR(self, competenciaAtual, qtdContribuicoes, tempoContribuicao, dataMinima: bool = False):
        if dataMinima:
            self.dibs[RegraGeralAR.tempoContribuicao] = datetime.date.min

        self.dibs[RegraGeralAR.tempoContribuicao] = competenciaAtual
        self.qtdContrib[RegraGeralAR.tempoContribuicao] = qtdContribuicoes
        self.tmpContribPorRegra[RegraGeralAR.tempoContribuicao] = tempoContribuicao

    def calculaMediaSalarial(self, dibReferente: datetime.date) -> float:
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

    #
    # def calculaDireitoAdquirido(self, lei: DireitoAdquirido, subTipo: SubTipoAposentadoria = None):
    #     listTimedeltas: list = []
    #     totalDias: int = 0
    #     anosContribuicao: int = 0
    #     antesReforma: bool = True
    #     listaBanco: List[CnisCabecalhos] = []
    #
    #     if lei == DireitoAdquirido.lei821391:
    #         if subTipo == SubTipoAposentadoria.Idade:
    #             # TODO: Implementar regra para verificar direito adquirido
    #             return False
    #         elif subTipo == SubTipoAposentadoria.TempoContrib:
    #             # TODO: Implementar regra para verificar direito adquirido
    #             return False
    #     elif lei == DireitoAdquirido.lei987699:
    #         # TODO: Implementar o acréscimo da profissão. Caso professor, por exemplo, adicionar 5 anos de contribuição
    #         acrescimoIdade: int = 0
    #         acrescimoProfissao: int = 0
    #
    #         if self.cliente.genero == 'F':
    #             acrescimoIdade = 5
    #
    #         if subTipo == SubTipoAposentadoria.Idade:
    #             listaCarencias: List[CarenciaLei91] = CarenciaLei91.select()
    #
    #             for carencia in listaCarencias:
    #                 listaAux: Generator[CnisCabecalhos] = self.retornaCabecalhosDesde(self.listaCabecalhos, carencia.dataImplemento)
    #                 idadeReferente: relativedelta = self.idadeCalculada
    #                 tempoContribuicao: List[int] = self.calculaTempoContribuicao(listaAux)
    #                 # Idade: M - 65 / F - 60
    #                 # Tempo Contribuição: 15 anos ou tabela
    #
    #                 if idadeReferente.years + acrescimoIdade > 65 and idadeReferente.year + acrescimoProfissao >= carencia.tempoContribuicao:
    #                     return True
    #
    #             return False
    #
    #         elif subTipo == SubTipoAposentadoria.TempoContrib:
    #             listaBanco: List[CnisCabecalhos] = self.listaCabecalhos
    #             tempoContribuicao: List[int] = self.calculaTempoContribuicao(listaBanco)
    #
    #             if self.cliente.genero == 'M':
    #                 return 35 - tempoContribuicao[2] >= 0
    #
    #             elif self.cliente.genero == 'F':
    #                 return 30 - tempoContribuicao[2] >= 0
    #             else:
    #                 raise ValueError('Cliente não possui o campo "genero" preenchido.')
    #
    #         else:
    #             raise ValueError('Nenhum subtipo foi informado para o cáclulo da aposentadoria.')
    #     else:
    #         listaBanco = self.listaCabecalhos
    #
    #         for cabecalho in listaBanco:
    #             if cabecalho.dataFim is None or cabecalho.dataFim == '':
    #                 cabecalho.dadoFaltante = True
    #                 cabecalho.save()
    #                 continue
    #
    #             if comparaMesAno(cabecalho.dataInicio, self.dataReforma2019, ComparaData.posterior):
    #                 antesReforma = False
    #
    #             if antesReforma:
    #                 if cabecalho.nb is not None:
    #                     if cabecalho.situacao != 'INDEFERIDO':
    #                         listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))
    #                     else:
    #                         listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))
    #                 else:
    #                     listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))
    #
    #         for delta in listTimedeltas:
    #             totalDias += delta.days
    #
    #         anosContribuicao = calculaDiaMesAno(totalDias)[2]
    #
    #         if self.cliente.genero == 'M':
    #             return anosContribuicao >= 35
    #         else:
    #             return anosContribuicao >= 30
    #
    #
    #
    # def calculaTempoContribuicao(self, cabecalhos: Union[list, Generator] = None, dataLimitante: datetime = None) -> List[int]:
    #     listTimedeltas: list = []
    #     totalDias: int = 0
    #
    #     indicadoresImpeditivos = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']
    #
    #     if cabecalhos is None:
    #         listaBanco: List[CnisCabecalhos] = self.listaCabecalhos
    #     else:
    #         listaBanco: List[CnisCabecalhos] = cabecalhos
    #
    #     # Criando dicionários de remunerações e contribuições por Id ----------------
    #     dictCabecalhos: dict = {cabecalho.seq: cabecalho for cabecalho in listaBanco}
    #
    #     remPorSeq: defaultdict = defaultdict(list)
    #     for remuneracao in self.listaRemuneracoes:
    #         listaAtual: List[CnisRemuneracoes] = remPorSeq[remuneracao.seq]
    #         listaAtual.append(remuneracao)
    #
    #     contPorSeq: defaultdict = defaultdict(list)
    #     for contribuicao in self.listaContribuicoes:
    #         listaAtual: List[CnisRemuneracoes] = contPorSeq[contribuicao.seq]
    #         listaAtual.append(contribuicao)
    #
    #     for seq, cabecalho in dictCabecalhos.items():
    #         dataReferente: datetime = cabecalho.dataFim
    #
    #         if dataReferente is None or dataReferente == datetime.datetime.min:
    #             continue
    #
    #         if cabecalho.indicadores in indicadoresImpeditivos:
    #             continue
    #
    #         if cabecalho.dataFim is None or cabecalho.dataFim == '':
    #             continue
    #
    #         if comparaMesAno(dataReferente, self.dataReforma2019, ComparaData.posterior):
    #             listTimedeltas.append(self.calculaTimedeltaDr(remPorSeq[seq], listaBanco, dataLimitante=dataLimitante))
    #             listTimedeltas.append(self.calculaTimedeltaDr(contPorSeq[seq], listaBanco, dataLimitante=dataLimitante))
    #         else:
    #             listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))
    #
    #     i = 1
    #     for delta in listTimedeltas:
    #         totalDias += delta.days
    #         i += 1
    #
    #     return calculaDiaMesAno(totalDias)

    # def calculaTimedeltaAr(self, cabecalho: CnisCabecalhos) -> datetime.timedelta:
    #     """
    #     Para o tempo de serviço antes da reforma previdenciária, 13/11/2019, o tempo de contribuição é calculado dia a dia.
    #
    #     :return - timedalta com a diferença de dias de trabalho
    #     """
    #
    #     indicadoresImpeditivos = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']
    #
    #     if cabecalho.indicadores in indicadoresImpeditivos:
    #         return datetime.timedelta(days=0)
    #
    #     if cabecalho.dataInicio is None or cabecalho.dataInicio == datetime.datetime.min:
    #         return datetime.timedelta(days=0)
    #
    #     if cabecalho.dataFim is None or cabecalho.dataFim == datetime.datetime.min:
    #         if cabecalho.ultRem is None or cabecalho.ultRem == datetime.datetime.min:
    #             return datetime.timedelta(days=0)
    #         else:
    #             return strToDate(cabecalho.ultRem) - strToDate(cabecalho.dataInicio)
    #     else:
    #         return strToDate(cabecalho.dataFim) - strToDate(cabecalho.dataInicio)

    # def calculaTimedeltaDr(self, listContOuRem: list, listCabecalhos: List[CnisCabecalhos], dataLimitante: datetime = None) -> datetime.timedelta:
    #     """
    #     Após a reforma previdenciária, 13/11/2019, o tempo de contribuição é calculado mês a mês, descontando os casos que ocorrem o indicador 'PREC-MENOR-MIN'
    #
    #     :return - timedalta com a diferença de dias de trabalho
    #     """
    #     if len(listContOuRem) == 0:
    #         return datetime.timedelta(0)
    #
    #     dataLimite: datetime = dataLimitante
    #     if dataLimite is None:
    #         dataLimite = self.dibAtual
    #
    #     if not isinstance(listContOuRem[0], CnisContribuicoes) and not isinstance(listContOuRem[0], CnisRemuneracoes):
    #         raise Exception()
    #
    #     indiceDR: int = next(index for index, contrib in enumerate(listContOuRem) if comparaMesAno(contrib.competencia, self.dataReforma2019, ComparaData.posterior))
    #     cabecalho: CnisCabecalhos = next(cabecalho for cabecalho in listCabecalhos if cabecalho.seq == listContOuRem[indiceDR].seq)
    #     contaMeses: int = 0
    #     indicadoresImpeditivos = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']
    #
    #     timedetlaAR: datetime.timedelta = self.dataReforma2019 - strToDatetime(cabecalho.dataInicio).date()
    #     if timedetlaAR.days < 0:
    #         timedetlaAR = datetime.timedelta(0)
    #
    #     for i in range(indiceDR, len(listContOuRem)):
    #         if listContOuRem[i].indicadores not in indicadoresImpeditivos:
    #             if comparaMesAno(listContOuRem[i].competencia, dataLimite, ComparaData.anterior):
    #                 contaMeses += 1
    #
    #     return timedetlaAR + datetime.timedelta(days=30*contaMeses)

    # def regraTransPontos(self) -> bool:
    #     pontuacaoAtingida: bool = False
    #     tempoMinimoContrib: bool = False
    #
    #     if self.cliente.genero == GeneroCliente.masculino.value:
    #         pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.masculino)
    #         tempoMinimoContrib = self.tempoContribCalculado[2] >= 35
    #     else:
    #         pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.feminino)
    #         tempoMinimoContrib = self.tempoContribCalculado[2] >= 30
    #
    #     return pontuacaoAtingida and tempoMinimoContrib

    # def regraRedIdadeMinima(self) -> bool:
    #
    #     idadeCliente: relativedelta = self.idadeCalculada
    #
    #     acrescimoAnual: int = self.dibAtual.year - self.dataReforma2019.year
    #     totalAcrescimo = acrescimoAnual * 0.5
    #
    #     if self.cliente.genero == 'M':
    #         if totalAcrescimo > 4:
    #             totalAcrescimo = 4
    #
    #         return self.tempoContribCalculado[2] >= 35 and idadeCliente.years + idadeCliente.months/12 >= 61 + totalAcrescimo
    #     else:
    #         if totalAcrescimo > 6:
    #             totalAcrescimo = 6
    #
    #         return self.tempoContribCalculado[2] >= 30 and idadeCliente.years + idadeCliente.months/12 >= 56 + totalAcrescimo
    #
    # def regraPedagio50(self) -> bool:
    #     listaCabecalhosPedagio = []
    #     tempoContribAntesReforma: int = 0
    #
    #     for cabecalho in self.listaCabecalhos:
    #         if cabecalho.dataFim is None or cabecalho.dataFim == '':
    #             cabecalho.dadoFaltante = True
    #             cabecalho.save()
    #             continue
    #
    #         if cabecalho.nb is not None:
    #             continue
    #
    #         # TODO: HÁ UM PROBLEMA AQUI QUE É VERIFICAR A DATA FINAL E NÃO A DATA INICIAL
    #         if strToDate(cabecalho.dataInicio) <= self.dataReforma2019:
    #             listaCabecalhosPedagio.append(cabecalho)
    #
    #     tempoContribAntesReforma: list = self.calculaTempoContribuicao(listaCabecalhosPedagio, dataLimitante=self.dibAtual)
    #
    #     anosAR = tempoContribAntesReforma[2]
    #
    #     if self.cliente.genero == 'M':
    #         return 35 - anosAR <= 2
    #     else:
    #         return 30 - anosAR <= 2
    #
    # def regraRedTempoContrib(self) -> bool:
    #     """
    #     Para as mulheres, a idade mínima para conquistar o benefício é acrescida de 6 meses a cada ano à partir de 2020.
    #     Em 2023, esse acréscimo é interrompido, permanecendo com o máximo de 62 anos.
    #     :return: bool
    #     """
    #
    #     if self.cliente.genero == 'M':
    #         return self.tempoContribCalculado[2] >= 15 and self.cliente.idade >= 65
    #     else:
    #         mesAtual: int = self.dibAtual.month
    #         mesNascCliente: int = strToDatetime(self.cliente.dataNascimento).month
    #
    #         if self.dibAtual.year >= 2023:
    #             acrescimoTotal: float = 2
    #         else:
    #             acrescimoTotal: float = 0.5 * (self.dibAtual.year - 2019)
    #
    #         # Ginática matemática para caclular a qtd de meses até o aniversário do(a) cliente
    #         if mesAtual - mesNascCliente > 0:
    #             if mesAtual - mesNascCliente < 6:
    #                 idadeMesesCliente = 0
    #             else:
    #                 idadeMesesCliente = 0.5
    #         else:
    #             if 12 + (mesAtual - mesNascCliente) < 6:
    #                 idadeMesesCliente = 0
    #             else:
    #                 idadeMesesCliente = 0.5
    #
    #         return self.tempoContribCalculado[2] >= 15 and self.cliente.idade + idadeMesesCliente >= 60 + acrescimoTotal
    #
    # def calculaPontosRegraPontos(self, generoCliente: GeneroCliente) -> bool:
    #     """
    #     Avalia a pontuação mínima e o tempo mínimo de contribuição (20 anos Homens / 15 anos Mulheres)
    #     :return bool
    #     """
    #     acrescimoAnual = self.dibAtual.year - 2019
    #     tempoContribuicao = self.calculaTempoContribuicao(dataLimitante=self.dibAtual)
    #     if generoCliente == GeneroCliente.masculino:
    #         if acrescimoAnual >= 9:
    #             acrescimoAnual = 9
    #
    #         # print(f"***self.pontuacao: {self.pontuacao}")
    #         # print(f"***tempoContribuicao: {tempoContribuicao[2]}\n\n")
    #         return self.pontuacao >= 96 + acrescimoAnual and tempoContribuicao[2] >= 20
    #     else:
    #         if acrescimoAnual >= 14:
    #             acrescimoAnual = 14
    #
    #         return self.pontuacao >= 86 + acrescimoAnual and tempoContribuicao[2] >= 15
    #
    # def calculaBeneficios(self):
    #
    #     if self.cliente.genero == 'M':
    #         tempoMinimo = 20
    #     else:
    #         tempoMinimo = 15
    #
    #     if self.regrasTransicao[RegraTransicao.pontos]:
    #         self.valorBeneficios[RegraTransicao.pontos] = self.mediaSalarial * (0.6 + 2*(self.tempoContribCalculado[2] - tempoMinimo)/100)
    #
    #     if self.regrasTransicao[RegraTransicao.reducaoIdadeMinima]:
    #         self.valorBeneficios[RegraTransicao.reducaoIdadeMinima] = self.mediaSalarial * (0.6 + 2 * (self.tempoContribCalculado[2] - tempoMinimo) / 100)
    #
    #     if self.regrasTransicao[RegraTransicao.pedagio50]:
    #         self.fatorPrevidenciario = self.calculaFatorPrevidenciario()
    #         self.valorBeneficios[RegraTransicao.pedagio50] = self.mediaSalarial * self.fatorPrevidenciario
    #
    #     if self.regrasTransicao[RegraTransicao.reducaoTempoContribuicao]:
    #         self.valorBeneficios[RegraTransicao.reducaoTempoContribuicao] = self.mediaSalarial * (0.6 + 2 * (self.tempoContribCalculado[2] - tempoMinimo) / 100)
    #
    # def retornaCabecalhosDesde(self, listaCabecalhos: List[CnisCabecalhos], dataInicio: datetime.date) -> List[CnisCabecalhos]:
    #     return [cabecalho for cabecalho in listaCabecalhos if cabecalho.dataInicio <= dataInicio]
