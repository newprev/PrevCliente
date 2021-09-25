import datetime
from dateutil.relativedelta import relativedelta
from typing import List, Generator, Union
import pandas as pd
from collections import defaultdict
from peewee import fn

from Daos.daoCalculos import DaoCalculos
from util.helpers import comparaMesAno, calculaDiaMesAno, strToDatetime, strToDate, verificaIndicadorProibitivo
from util.dateHelper import calculaIdade
from util.ferramentas.tools import prettyPrintDict

from modelos.cabecalhoORM import CnisCabecalhos
from modelos.remuneracaoORM import CnisRemuneracoes
from modelos.contribuicoesORM import CnisContribuicoes
from modelos.itemContribuicao import ItemContribuicao
from modelos.expSobrevidaORM import ExpSobrevida
from modelos.processosORM import Processos
from modelos.clienteORM import Cliente
from modelos.carenciasLei91 import CarenciaLei91
from util.enums.newPrevEnums import RegraTransicao, GeneroCliente, TamanhoData, ComparaData, DireitoAdquirido, SubTipoAposentadoria, TipoItemContribuicao


# Reforma 13/11/2019
# Ar: Antes da reforma
# Dr: Depois da reforma


class CalculosAposentadoria:
    listaCabecalhos: List[CnisCabecalhos] = []
    listaItensContrib: List[ItemContribuicao] = []
    listaRemuneracoes: List[CnisRemuneracoes] = []
    listaContribuicoes: List[CnisContribuicoes] = []
    mediaSalarial: float
    idadeCalculada: relativedelta
    dataPrimeiroTrabalho: datetime.date

    def __init__(self, processo: Processos, cliente: Cliente, db=None):
        self.processo = processo
        self.cliente = cliente
        self.daoCalculos = DaoCalculos(db)

        # Datas importantes
        self.dataReforma2019: datetime.date = datetime.date(2019, 11, 13)
        self.dataTrocaMoeda = datetime.date = datetime.date(1994, 7, 1)

        self.fatorPrevidenciario: int = 1

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

        self.regrasTransicao = {
            RegraTransicao.pontos: None,
            RegraTransicao.reducaoIdadeMinima: None,
            RegraTransicao.pedagio50: None,
            RegraTransicao.reducaoTempoContribuicao: None
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

        self.calculaRegrasTransicao()

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

    # def defineDIB(self, data: datetime):
    #     self.processo.dib = data

    def calculaRegrasTransicao(self, tipo: RegraTransicao = RegraTransicao.todas):
        if tipo == RegraTransicao.pontos:
            self.calculaRegraDosPontos()
        elif tipo == RegraTransicao.reducaoIdadeMinima:
            pass
        elif tipo == RegraTransicao.pedagio50:
            pass
        elif tipo == RegraTransicao.reducaoTempoContribuicao:
            pass
        elif tipo == RegraTransicao.todas:
            self.calculaRegraDosPontos()

    def calculaRegraDosPontos(self):
        if self.cliente.genero == 'M':
            genero = GeneroCliente.masculino
        else:
            genero = GeneroCliente.feminino

        dib: datetime.date = self.dibRegraDosPontos(genero)

        print(dib)

    def dibRegraDosPontos(self, generoCliente: GeneroCliente) -> datetime.date:
        tempoContribuicao: datetime.timedelta = datetime.timedelta(days=0)
        listaItensContribuicao: List[ItemContribuicao] = ItemContribuicao.select().where(ItemContribuicao.clienteId == self.cliente.clienteId).order_by(ItemContribuicao.seq, ItemContribuicao.competencia)
        ultimoSeq: int = ItemContribuicao.select(fn.Max(ItemContribuicao.seq)).where(ItemContribuicao.clienteId == self.cliente.clienteId).scalar()
        mudouSeq: bool = False
        seqAtual: int = 0

        print(f"\n\nultimoSeq: {ultimoSeq}")
        print(f"len(listaItensContribuicao): {len(listaItensContribuicao)}\n\n")

        for index, item in enumerate(listaItensContribuicao):
            mudouSeq = seqAtual != item.seq and seqAtual != 0

            if index == 0 or mudouSeq:
                seqAtual = item.seq
                print(f"index: {index}")
                print(f"mudouSeq: {mudouSeq}")
                continue

            if strToDate(item.competencia) <= self.dataReforma2019:
                # TODO: Calcula datas diariamente
                tempoContribuicao += strToDate(listaItensContribuicao[index].competencia) - strToDate(listaItensContribuicao[index-1].competencia)
            else:
                # TODO: Calcula datas mensalmente
                pass

            # mudouSeq = seqAtual != item.seq

        print(f"tempoContribuicao: {tempoContribuicao}")

        # for cabecalho in self.listaCabecalhos:
        #     dataFimContrib: datetime.date = datetime.date.min
        #     dataFimRemu: datetime.date = datetime.date.min
        #     # listaContrib: List[CnisContribuicoes] = self.buscaContribPelo(seq=cabecalho.seq)
        #     # listaRemu: List[CnisRemuneracoes] = self.buscaRemuPelo(seq=cabecalho.seq)
        #
        #     # for contrib in listaContrib:
        #     #     tempoContribuicao += datetime.timedelta(days=30)
        #     #     # tempoContribuicao += datetime.timedelta(days=len(listaRemu) * 30)
        #     #
        #     #     dataFimContrib = strToDate(contrib.dataPagamento)
        #     #
        #     #     if dataFimContrib == datetime.date.min and dataFimRemu != datetime.date.min:
        #     #         dibAtual = dataFimRemu
        #     #     elif dataFimContrib != datetime.date.min and dataFimRemu == datetime.date.min:
        #     #         dibAtual = dataFimContrib
        #     #     elif dataFimContrib > dataFimRemu:
        #     #         dibAtual = dataFimContrib
        #     #     else:
        #     #         dibAtual = dataFimRemu
        #     #
        #     #     if self.calculaPontosRegraPontos(generoCliente, dibAtual, calculaDiaMesAno(tempoContribuicao.days)):
        #     #         return dibAtual
        #     #
        #     # for remuneracao in listaRemu:
        #     #     tempoContribuicao += datetime.timedelta(days=30)
        #     #
        #     #     dataFimRemu = strToDate(remuneracao.competencia)
        #     #
        #     #     if dataFimContrib == datetime.date.min and dataFimRemu != datetime.date.min:
        #     #         dibAtual = dataFimRemu
        #     #     elif dataFimContrib != datetime.date.min and dataFimRemu == datetime.date.min:
        #     #         dibAtual = dataFimContrib
        #     #     elif dataFimContrib > dataFimRemu:
        #     #         dibAtual = dataFimContrib
        #     #     else:
        #     #         dibAtual = dataFimRemu
        #     #
        #     #     if self.calculaPontosRegraPontos(generoCliente, dibAtual, calculaDiaMesAno(tempoContribuicao.days)):
        #     #         return dibAtual

    def calculaPontosRegraPontos(self, generoCliente: GeneroCliente, dib: datetime.date, tempoContribuicao: List[int]) -> bool:
        """
        Avalia a pontuação mínima e o tempo mínimo de contribuição (20 anos Homens / 15 anos Mulheres)
        :return bool
        """
        acrescimoAnual = dib.year - 2019
        tmpContribuicao = tempoContribuicao
        pontuacao = sum(tempoContribuicao) + self.cliente.idade

        if dib < self.dataReforma2019:
            return False

        if generoCliente == GeneroCliente.masculino:
            if acrescimoAnual >= 9:
                acrescimoAnual = 9

            return pontuacao >= 96 + acrescimoAnual and tmpContribuicao[2] >= 20
        else:
            if acrescimoAnual >= 14:
                acrescimoAnual = 14

            return pontuacao >= 86 + acrescimoAnual and tmpContribuicao[2] >= 15

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
    # def calculaFatorPrevidenciario(self):
    #     """
    #     Cálculo do fator previdenciário
    #
    #     :var<float>: tempCont - Tempo de contribuição até o momento da aposentadoria
    #     :var<float>: aliq - Alíquota de contribuição
    #     :var<float>: expSobrevida - Expectativa de sobrevida após a data do início do benefício (dib)
    #     :var<float>: idade - Idade do cliente na data do início do benefício
    #
    #     :return<float>: fatorPrev  = ((tempCont * aliq) / expSobrevida) * (1 + (idade + (tempCont * aliq)) / 100)
    #     """
    #     tempCont: float = self.tempoContribCalculado[2] + ((self.tempoContribCalculado[0] / 30) + self.tempoContribCalculado[1] / 12)
    #     aliq: float = 0.31
    #     intIdade: relativedelta = self.idadeCalculada
    #     floatIdade: float = (intIdade.days/30 + intIdade.months)/12 + intIdade.years  # Para a fórmula é importante que a idade seja completa com dias e meses transformados em anos
    #
    #     try:
    #         expSobrevidaModelo: ExpSobrevida = ExpSobrevida.select().where(
    #             ExpSobrevida.dataReferente.year == self.dibAtual.year,
    #             ExpSobrevida.idade == intIdade.years
    #         ).get()
    #     except ExpSobrevida.DoesNotExist:
    #         expSobrevidaModelo: ExpSobrevida = ExpSobrevida.select().where(
    #             ExpSobrevida.dataReferente.year == self.dibAtual.year - 1,
    #             ExpSobrevida.idade == intIdade.years
    #         ).get()
    #
    #     expSobrevida: int = expSobrevidaModelo.expectativaSobrevida
    #
    #     fatorPrev = ((tempCont * aliq) / expSobrevida) * (1 + (floatIdade + (tempCont * aliq)) / 100)
    #
    #     # print('\n\n------------------------------------ calculaFatorPrevidenciario')
    #     # print(f"tempCont: {tempCont}")
    #     # print(f"aliq: {aliq}")
    #     # print(f"idade: {idade}")
    #     # print(f"expSobrevida: {expSobrevida}")
    #     # print(f"fatorPrev: {fatorPrev}")
    #     # print(f"Possível dib: {expSobrevidaModelo.dataReferente}")
    #     # print('------------------------------------ calculaFatorPrevidenciario\n\n')
    #     return fatorPrev
    #
    # def calculaMediaSalarial(self) -> float:
    #     avaliaSalario = lambda df: df['salContribuicao'] if df['salContribuicao'] <= df['teto'] else df['teto']
    #
    #     dfContribuicoes: pd.DataFrame = self.daoCalculos.buscaRemContPorData(self.cliente.clienteId, self.dataTrocaMoeda.strftime('%Y-%m-%d'), self.dibAtual.strftime('%Y-%m-%d'))
    #     dfContribuicoes['salContribuicao1'] = dfContribuicoes.apply(avaliaSalario, axis=1)
    #     salAtualizado = dfContribuicoes['salContribuicao1']*dfContribuicoes['fator']
    #     dfContribuicoes['salAtualizado'] = salAtualizado
    #     return dfContribuicoes['salAtualizado'].mean()
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
