import datetime

from helpers import strToDatetime
from newPrevEnums import TamanhoData


class ContribuicoesModelo:

    def __init__(self):
        self.contribuicoesId: int = None
        self.clienteId: int = None
        self.seq: int = None
        self.competencia: datetime = None
        self.dataPagamento: datetime = None
        self.contribuicao: float = None
        self.salContribuicao: float = None
        self.indicadores: str = None
        self.dadoOrigem: str = None
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None


    def toDict(self):
        dictUsuario = {
            'contribuicoesId': self.contribuicoesId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'competencia': self.competencia,
            'dataPagamento': self.dataPagamento,
            'contribuicao': self.contribuicao,
            'salContribuicao': self.salContribuicao,
            'indicadores': self.indicadores,
            'dadoOrigem': self.dadoOrigem,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictContribuicoes):
        self.contribuicoesId = dictContribuicoes['contribuicoesId'],
        self.clienteId = dictContribuicoes['clienteId'],
        self.seq = dictContribuicoes['seq'],
        self.competencia = dictContribuicoes['competencia'],
        self.dataPagamento = dictContribuicoes['dataPagamento'],
        self.contribuicao = dictContribuicoes['contribuicao'],
        self.salContribuicao = dictContribuicoes['salContribuicao'],
        self.indicadores = dictContribuicoes['indicadores'],
        self.dadoOrigem = dictContribuicoes['dadoOrigem'],
        self.dataCadastro = dictContribuicoes['dataCadastro'],
        self.dataUltAlt = dictContribuicoes['dataUltAlt'],

    def fromList(self, listContribuicoes: list, retornaInst: bool = True):
        self.contribuicoesId = listContribuicoes[0]
        self.clienteId = listContribuicoes[1]
        self.seq = listContribuicoes[2]
        self.competencia = strToDatetime(listContribuicoes[3], TamanhoData.gg)
        self.dataPagamento = strToDatetime(listContribuicoes[4], TamanhoData.gg)
        self.contribuicao = listContribuicoes[5]
        self.salContribuicao = listContribuicoes[6]
        self.indicadores = listContribuicoes[7]
        self.dadoOrigem = listContribuicoes[8]
        self.dataCadastro = listContribuicoes[9]
        self.dataUltAlt = listContribuicoes[10]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""Contribuicoes(
            contribuicoesId: {self.contribuicoesId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            competencia: {self.competencia},
            dataPagamento: {self.dataPagamento},
            contribuicao: {self.contribuicao},
            salContribuicao: {self.salContribuicao},
            indicadores: {self.indicadores},
            dadoOrigem: {self.dadoOrigem},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
