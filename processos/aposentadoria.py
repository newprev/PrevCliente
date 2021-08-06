import datetime
from typing import List
import pandas as pd
from math import floor
from collections import defaultdict

from Daos.daoCalculos import DaoCalculos
from helpers import comparaMesAno, calculaDiaMesAno, mascaraDataSql, strToDatetime, datetimeToSql, dateToSql

from modelos.cabecalhoModelo import CabecalhoModelo
from modelos.remuneracaoModelo import RemuneracoesModelo
from modelos.contribuicoesModelo import ContribuicoesModelo
from modelos.expSobrevidaModelo import ExpectativaSobrevidaModelo
from modelos.processosModelo import ProcessosModelo
from modelos.clienteModelo import ClienteModelo
from newPrevEnums import RegraTransicao, GeneroCliente, TamanhoData, ComparaData, DireitoAdquirido, SubTipoAposentadoria


# Reforma 13/11/2019
# Ar: Antes da reforma
# Dr: Depois da reforma


class CalculosAposentadoria:

    def __init__(self, processo: ProcessosModelo, cliente: ClienteModelo, dib: datetime = None, db=None):
        self.processo = processo
        self.cliente = cliente
        self.daoCalculos = DaoCalculos(db)
        self.cabecalhos: List[CabecalhoModelo] = list(self.daoCalculos.buscaCabecalhosClienteId(self.cliente.clienteId))
        self.listaRemuneracoes = list(self.daoCalculos.buscaTodasRemuneracoes(cliente.clienteId))
        self.listaContribuicoes = list(self.daoCalculos.buscaTodasContribuicoes(cliente.clienteId))

        if dib is None:
            self.dibAtual: datetime = datetime.datetime.today()
        else:
            self.dibAtual: datetime = dib.strftime('%Y-%m')

        self.dibAtual = datetime.datetime(year=2019, month=10, day=1)

        self.mediaSalarial: float = self.calculaMediaSalarial()
        self.dataReforma2019: datetime.date = datetime.date(2019, 11, 13)
        self.fatorPrevidenciario: int = 1
        self.tempoContribCalculado: list = self.calculaTempoContribuicao()
        self.pontuacao: int = sum(self.tempoContribCalculado) + self.cliente.idade

        self.regrasTransicao = {
            RegraTransicao.pontos: self.regraTransPontos(),
            RegraTransicao.reducaoIdadeMinima: self.regraRedIdadeMinima(),
            RegraTransicao.pedagio50: self.regraPedagio50(),
            RegraTransicao.reducaoTempoContribuicao: self.regraRedTempoContrib()
        }

        self.valorBeneficios = {
            RegraTransicao.pontos: 0,
            RegraTransicao.reducaoIdadeMinima: 0,
            # TODO: Para calcular o valor do benefício, preciso saber qual o fator previdenciário
            RegraTransicao.pedagio50: 0
        }

        self.dibs = {
            RegraTransicao.pontos: None,
            RegraTransicao.reducaoIdadeMinima: None,
            RegraTransicao.pedagio50: None,
            RegraTransicao.reducaoTempoContribuicao: None
        }

        self.direitosAdquiridos = {
            DireitoAdquirido.lei821391: {
                SubTipoAposentadoria.Idade: self.calculaDireitoAdquirido(DireitoAdquirido.lei821391, subTipo=SubTipoAposentadoria.Idade),
                SubTipoAposentadoria.TempoContrib: self.calculaDireitoAdquirido(DireitoAdquirido.lei821391, subTipo=SubTipoAposentadoria.TempoContrib)
            },
            DireitoAdquirido.lei987699: self.calculaDireitoAdquirido(DireitoAdquirido.lei987699),
            DireitoAdquirido.ec1032019: self.calculaDireitoAdquirido(DireitoAdquirido.ec1032019)
        }

        self.aposentadorias = {
            'direitoAdq': self.direitosAdquiridos,
            'regrasTransicao': self.regrasTransicao
        }

        self.calculaBeneficios()

        print('\n\n------------------------------------- ')
        print(f'len(self.listaRemuneracoes): {len(self.listaRemuneracoes)}')
        print(f'len(self.listaContribuicoes): {len(self.listaContribuicoes)}')
        print(f'self.processo.tempoContribuicao: {self.processo.tempoContribuicao}')
        print(f'self.regrasTransicao: {self.regrasTransicao}')
        print(f'self.valorBeneficios: {self.valorBeneficios}')
        print(f'self.tempoContribCalculado: {self.tempoContribCalculado}')
        print('-------------------------------------\n\n')

    # def defineDIB(self, data: datetime):
    #     self.processo.dib = data

    def calculaDireitoAdquirido(self, lei: DireitoAdquirido, subTipo: SubTipoAposentadoria = None):
        listTimedeltas: list = []
        totalDias: int = 0
        anosContribuicao: int = 0
        antesReforma: bool = True
        listaBanco: List[CabecalhoModelo] = []

        if lei == DireitoAdquirido.lei821391:
            if subTipo == SubTipoAposentadoria.Idade:
                # TODO: Implementar regra para verificar direito adquirido
                return False
            elif subTipo == SubTipoAposentadoria.TempoContrib:
                # TODO: Implementar regra para verificar direito adquirido
                return False
        elif lei == DireitoAdquirido.lei987699:
            pass

        else:
            listaBanco = self.cabecalhos

            for cabecalho in listaBanco:

                if comparaMesAno(cabecalho.dataInicio, self.dataReforma2019, ComparaData.posterior):
                    antesReforma = False

                if antesReforma:
                    if cabecalho.nb is not None:
                        if cabecalho.situacao != 'INDEFERIDO':
                            listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))
                        else:
                            listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))
                    else:
                        listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))

            for delta in listTimedeltas:
                totalDias += delta.days

            anosContribuicao = calculaDiaMesAno(totalDias)[2]

            if self.cliente.genero == 'M':
                return anosContribuicao >= 35
            else:
                return anosContribuicao >= 30

    def calculaFatorPrevidenciario(self):
        """
        Cálculo do fator previdenciário

        :var<float>: tempCont - Tempo de contribuição até o momento da aposentadoria
        :var<float>: aliq - Alíquota de contribuição
        :var<float>: expSobrevida - Expectativa de sobrevida após a data do início do benefício (dib)
        :var<float>: idade - Idade do cliente na data do início do benefício

        :return<float>: fatorPrev  = ((tempCont * aliq) / expSobrevida) * (1 + (idade + (tempCont * aliq)) / 100)
        """
        tempCont: float = self.tempoContribCalculado[2] + ((self.tempoContribCalculado[0] / 30) + self.tempoContribCalculado[1] / 12)
        aliq: float = 0.31
        idade = self.cliente.idade
        expSobrevidaModelo: ExpectativaSobrevidaModelo = self.daoCalculos.buscaExpSobrevidaPorData(self.dibAtual, idade)
        expSobrevida: int = expSobrevidaModelo.expectativaSobrevida

        fatorPrev = ((tempCont * aliq) / expSobrevida) * (1 + (idade + (tempCont * aliq)) / 100)

        # print('\n\n------------------------------------ calculaFatorPrevidenciario')
        # print(f"tempCont: {tempCont}")
        # print(f"aliq: {aliq}")
        # print(f"idade: {idade}")
        # print(f"expSobrevida: {expSobrevida}")
        # print(f"fatorPrev: {fatorPrev}")
        # print(f"Possível dib: {expSobrevidaModelo.dataReferente}")
        # print('------------------------------------ calculaFatorPrevidenciario\n\n')
        return fatorPrev

    def calculaMediaSalarial(self):
        avaliaSalario = lambda df: df['salContribuicao'] if df['salContribuicao'] <= df['teto'] else df['teto']

        dfContribuicoes: pd.DataFrame = self.daoCalculos.buscaRemContPorData(self.cliente.clienteId, '1994-07-31', self.dibAtual)
        dfContribuicoes['salContribuicao1'] = dfContribuicoes.apply(avaliaSalario, axis=1)
        salAtualizado = dfContribuicoes['salContribuicao1']*dfContribuicoes['fator']
        dfContribuicoes['salAtualizado'] = salAtualizado
        return dfContribuicoes['salAtualizado'].mean()

    def calculaTempoContribuicao(self, cabecalhos: list = None, dataLimitante: datetime = None) -> List[int]:
        listTimedeltas: list = []
        totalDias: int = 0

        indicadoresImpeditivos = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']

        if cabecalhos is None:
            listaBanco: List[CabecalhoModelo] = self.cabecalhos
        else:
            listaBanco: List[CabecalhoModelo] = cabecalhos

        # Criando dicionários de remunerações e contribuições por Id ----------------
        dictCabecalhos: dict = {cabecalho.seq: cabecalho for cabecalho in listaBanco}

        remPorSeq: defaultdict = defaultdict(list)
        for remuneracao in self.listaRemuneracoes:
            listaAtual: List[RemuneracoesModelo] = remPorSeq[remuneracao.seq]
            listaAtual.append(remuneracao)

        contPorSeq: defaultdict = defaultdict(list)
        for contribuicao in self.listaContribuicoes:
            listaAtual: List[RemuneracoesModelo] = contPorSeq[contribuicao.seq]
            listaAtual.append(contribuicao)

        for seq, cabecalho in dictCabecalhos.items():
            dataReferente: datetime = cabecalho.dataFim

            if dataReferente is None or dataReferente == datetime.datetime.min:
                dataReferente = cabecalho.ultRem

            if cabecalho.indicadores in indicadoresImpeditivos:
                continue

            if cabecalho.dataFim is None or cabecalho.dataFim == '':
                continue

            if comparaMesAno(dataReferente, self.dataReforma2019, ComparaData.posterior):
                listTimedeltas.append(self.calculaTimedeltaDr(remPorSeq[seq], listaBanco, dataLimitante=dataLimitante))
                listTimedeltas.append(self.calculaTimedeltaDr(contPorSeq[seq], listaBanco, dataLimitante=dataLimitante))
            else:
                listTimedeltas.append(self.calculaTimedeltaAr(cabecalho))

        # Filtra contribuições após a reforma
        # for contribuicao in self.listaContribuicoes:
        #     if comparaMesAno(contribuicao.competencia, self.dataReforma2019, ComparaData.posterior):
        #         listaContDR.append(contribuicao)
        #
        # for remuneracao in self.listaRemuneracoes:
        #     if comparaMesAno(remuneracao.competencia, self.dataReforma2019, ComparaData.posterior):
        #         listaRemDR.append(remuneracao)
        #
        # # Calcula timedeltas de contribuições anteriores à reforma de 2019

        #
        # for cabecalho in listaBanco:
        #
        #     if comparaMesAno(cabecalho.dataInicio, self.dataReforma2019, ComparaData.posterior) or comparaMesAno(cabecalho.dataFim, self.dataReforma2019, ComparaData.posterior):
        #         break
        #
        #     if cabecalho.nb is not None:
        #         if cabecalho.situacao != 'INDEFERIDO':
        #             listTimedeltas.append(self.calculaTimedeltaAr(cabecalho, listaBanco))
        #         else:
        #             listTimedeltas.append(self.calculaTimedeltaAr(cabecalho, listaBanco, buscaProxJob=False))
        #
        # print('\n\n********************************************************')
        # print(f'len(listaRemDR): {len(listaRemDR)}')
        # print(f'len(listaContDR): {len(listaContDR)}')
        # print(f'listTimedeltas: {listTimedeltas}')
        # print('********************************************************\n\n')
        #
        i = 1
        for delta in listTimedeltas:
            totalDias += delta.days
            i += 1

        return calculaDiaMesAno(totalDias)

    def calculaTimedeltaAr(self, cabecalho: CabecalhoModelo) -> datetime.timedelta:
        """
        Para o tempo de serviço antes da reforma previdenciária, 13/11/2019, o tempo de contribuição é calculado dia a dia.

        :return - timedalta com a diferença de dias de trabalho
        """

        indicadoresImpeditivos = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']

        if cabecalho.indicadores in indicadoresImpeditivos:
            return datetime.timedelta(days=0)

        if cabecalho.dataInicio is None or cabecalho.dataInicio == datetime.datetime.min:
            return datetime.timedelta(days=0)

        if cabecalho.dataFim is None or cabecalho.dataFim == datetime.datetime.min:
            if cabecalho.ultRem is None or cabecalho.ultRem == datetime.datetime.min:
                return datetime.timedelta(days=0)
            else:
                return cabecalho.ultRem - cabecalho.dataInicio
        else:
            return cabecalho.dataFim - cabecalho.dataInicio

    def calculaTimedeltaDr(self, listContOuRem: list, listCabecalhos: List[CabecalhoModelo], dataLimitante: datetime = None) -> datetime.timedelta:
        """
        Após a reforma previdenciária, 13/11/2019, o tempo de contribuição é calculado mês a mês, descontando os casos que ocorrem o indicador 'PREC-MENOR-MIN'

        :return - timedalta com a diferença de dias de trabalho
        """
        if len(listContOuRem) == 0:
            return datetime.timedelta(0)

        dataLimite: datetime = dataLimitante
        if dataLimite is None:
            dataLimite = self.dibAtual

        if not isinstance(listContOuRem[0], ContribuicoesModelo) and not isinstance(listContOuRem[0], RemuneracoesModelo):
            raise Exception()

        indiceDR: int = next(index for index, contrib in enumerate(listContOuRem) if comparaMesAno(contrib.competencia, self.dataReforma2019, ComparaData.posterior))
        cabecalho: CabecalhoModelo = next(cabecalho for cabecalho in listCabecalhos if cabecalho.seq == listContOuRem[indiceDR].seq)
        contaMeses: int = 0
        indicadoresImpeditivos = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']

        timedetlaAR: datetime.timedelta = self.dataReforma2019 - cabecalho.dataInicio.date()
        if timedetlaAR.days < 0:
            timedetlaAR = datetime.timedelta(0)

        for i in range(indiceDR, len(listContOuRem)):
            if listContOuRem[i].indicadores not in indicadoresImpeditivos:
                if comparaMesAno(listContOuRem[i].competencia, dataLimite, ComparaData.anterior):
                    contaMeses += 1

        return timedetlaAR + datetime.timedelta(days=30*contaMeses)

        # somaIndicadores: int = 0
        # indicadoresASubtrair = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']
        # indicadoresImpeditivos = ['PDT-NASC-FIL-INV']
        #
        # if cabecalho.indicadores in indicadoresImpeditivos:
        #     return datetime.timedelta(days=0)
        #
        # if cabecalho.dataInicio is None or cabecalho.dataInicio == datetime.datetime.min:
        #     return datetime.timedelta(days=0)
        #
        # for remuneracao in self.listaRemuneracoes:
        #     if remuneracao.seq == cabecalho.seq and remuneracao.indicadores in indicadoresASubtrair:
        #         somaIndicadores += 1
        #
        # for contribuicao in self.listaContribuicoes:
        #     if contribuicao.seq == cabecalho.seq and contribuicao.indicadores in indicadoresASubtrair:
        #         somaIndicadores += 1
        #
        # if cabecalho.dataFim is None or cabecalho.dataFim == datetime.datetime.min:
        #     if cabecalho.ultRem is None or cabecalho.ultRem == datetime.datetime.min:
        #         return datetime.timedelta(days=0)
        #     else:
        #         diferencaMeses: int = floor((cabecalho.ultRem - cabecalho.dataInicio).days/30) + 1 - somaIndicadores
        #         # if diferencaMeses < 0:
        #         #     print(f'{cabecalho.ultRem=} --- {cabecalho.dataInicio=}')
        #         #     print(f'cabecalho.cabecalhosId: {cabecalho.cabecalhosId}')
        #         #     print(f'somaIndicadores: {somaIndicadores}')
        #         #     print(f'cabecalho.ultRem - cabecalho.dataInicio: {cabecalho.ultRem - cabecalho.dataInicio}')
        #         #     print(f'cabecalho.ultRem - cabecalho.dataInicio: {floor((cabecalho.ultRem - cabecalho.dataInicio).days/30)}')
        #         return datetime.timedelta(days=30 * diferencaMeses)
        # else:
        #     diferencaMeses: int = floor((cabecalho.ultRem - cabecalho.dataInicio).days/30) + 1 - somaIndicadores
        #     # if diferencaMeses < 0:
        #     #     print(f'{cabecalho.ultRem=} --- {cabecalho.dataInicio=}')
        #     #     print(f'cabecalho.cabecalhosId: {cabecalho.cabecalhosId}')
        #     #     print(f'somaIndicadores: {somaIndicadores}')
        #     #     print(f'cabecalho.ultRem - cabecalho.dataInicio: {cabecalho.ultRem - cabecalho.dataInicio}')
        #     #     print(f'cabecalho.ultRem - cabecalho.dataInicio: {floor((cabecalho.ultRem - cabecalho.dataInicio).days/30)}')
        #     return datetime.timedelta(days=30 * diferencaMeses)

    def regraTransPontos(self) -> bool:
        pontuacaoAtingida: bool = False
        tempoMinimoContrib: bool = False

        if self.cliente.genero == GeneroCliente.masculino.value:
            pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.masculino)
            tempoMinimoContrib = self.tempoContribCalculado[2] >= 35
        else:
            pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.feminino)
            tempoMinimoContrib = self.tempoContribCalculado[2] >= 30

        return pontuacaoAtingida and tempoMinimoContrib

    def regraRedIdadeMinima(self) -> bool:
        acrescimoMensal: float = 0
        acrescimoAnual: int = 0
        idadeMesesCliente: float = 0
        mesAtual: int = self.dibAtual.month
        mesNascCliente: int = strToDatetime(self.cliente.dataNascimento, TamanhoData.gg).month

        # Ginática matemática para caclular a qtd de meses até o aniversário do(a) cliente
        if mesAtual - mesNascCliente > 0:
            if mesAtual - mesNascCliente < 6:
                idadeMesesCliente = 0
            else:
                idadeMesesCliente = 0.5
        else:
            if 12 + (mesAtual - mesNascCliente) < 6:
                idadeMesesCliente = 0
            else:
                idadeMesesCliente = 0.5

        if mesAtual < 6:
            acrescimoMensal = 0
        elif 6 <= mesAtual < 12:
            acrescimoMensal = 0.5
        elif mesAtual == 12:
            acrescimoMensal = 1

        acrescimoAnual: int = self.dibAtual.year - self.dataReforma2019.year
        totalAcrescimo = acrescimoAnual * (1 + acrescimoMensal)

        if self.cliente.genero == 'M':
            if totalAcrescimo > 4:
                totalAcrescimo = 4
            return self.tempoContribCalculado[2] >= 35 and self.cliente.idade + idadeMesesCliente >= 61 + totalAcrescimo
        else:
            if totalAcrescimo > 6:
                totalAcrescimo = 6
            return self.tempoContribCalculado[2] >= 30 and self.cliente.idade + idadeMesesCliente >= 56 + totalAcrescimo

    def regraPedagio50(self) -> bool:
        listaCabecalhosPedagio = []
        tempoContribAntesReforma = 0

        for cabecalho in self.cabecalhos:
            if cabecalho.dataFim.date() <= self.dataReforma2019:
                listaCabecalhosPedagio.append(cabecalho)
        tempoContribAntesReforma = self.calculaTempoContribuicao(listaCabecalhosPedagio, dataLimitante=self.dibAtual)[2]

        if self.cliente.genero == 'M':
            return 35 - tempoContribAntesReforma <= 2
        else:
            return 30 - tempoContribAntesReforma <= 2

    def regraRedTempoContrib(self) -> bool:
        """
        Para as mulheres, a idade mínima para conquistar o benefício é acrescida de 6 meses a cada ano à partir de 2020.
        Em 2023, esse acréscimo é interrompido, permanecendo com o máximo de 62 anos.
        :return: bool
        """

        if self.cliente.genero == 'M':
            return self.tempoContribCalculado[2] >= 15 and self.cliente.idade >= 65
        else:
            mesAtual: int = self.dibAtual.month
            mesNascCliente: int = strToDatetime(self.cliente.dataNascimento, TamanhoData.gg).month

            if self.dibAtual.year >= 2023:
                acrescimoTotal: float = 2
            else:
                acrescimoTotal: float = 0.5 * (self.dibAtual.year - 2019)

            # Ginática matemática para caclular a qtd de meses até o aniversário do(a) cliente
            if mesAtual - mesNascCliente > 0:
                if mesAtual - mesNascCliente < 6:
                    idadeMesesCliente = 0
                else:
                    idadeMesesCliente = 0.5
            else:
                if 12 + (mesAtual - mesNascCliente) < 6:
                    idadeMesesCliente = 0
                else:
                    idadeMesesCliente = 0.5

            return self.tempoContribCalculado[2] >= 15 and self.cliente.idade + idadeMesesCliente >= 60 + acrescimoTotal

    def calculaPontosRegraPontos(self, generoCliente: GeneroCliente) -> bool:
        """
        Avalia a pontuação mínima e o tempo mínimo de contribuição (20 anos Homens / 15 anos Mulheres)
        :return bool
        """
        acrescimoAnual = self.dibAtual.year - 2019
        if generoCliente == GeneroCliente.masculino:
            if acrescimoAnual >= 9:
                acrescimoAnual = 9
            return self.pontuacao >= 96 + acrescimoAnual and self.tempoContribCalculado[2] >= 20
        else:
            if acrescimoAnual >= 14:
                acrescimoAnual = 14
            return self.pontuacao >= 86 + acrescimoAnual and self.tempoContribCalculado[2] >= 15

    def calculaBeneficios(self):
        """
        O método buscaRemContPorData retorna um DataFrame com as seguintes colunas: ['clienteId', 'infoId', 'competencia', 'salContribuicao', 'indicadores', 'tipoInfo']
        """
        if self.cliente.genero == 'M':
            tempoMinimo = 20
        else:
            tempoMinimo = 15

        if self.regrasTransicao[RegraTransicao.pontos]:
            self.valorBeneficios[RegraTransicao.pontos] = self.mediaSalarial * (0.6 + 2*(self.tempoContribCalculado[2] - tempoMinimo)/100)

        if self.regrasTransicao[RegraTransicao.reducaoIdadeMinima]:
            self.valorBeneficios[RegraTransicao.reducaoIdadeMinima] = self.mediaSalarial * (0.6 + 2 * (self.tempoContribCalculado[2] - tempoMinimo) / 100)

        if self.regrasTransicao[RegraTransicao.pedagio50]:
            self.fatorPrevidenciario = self.calculaFatorPrevidenciario()
            self.valorBeneficios[RegraTransicao.pedagio50] = 4

        if self.regrasTransicao[RegraTransicao.reducaoTempoContribuicao]:
            self.valorBeneficios[RegraTransicao.reducaoTempoContribuicao] = self.mediaSalarial * (0.6 + 2 * (self.tempoContribCalculado[2] - tempoMinimo) / 100)

