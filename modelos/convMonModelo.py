import datetime

from helpers import strToDatetime
from newPrevEnums import TamanhoData


class ConvMonModelo:

    def __init__(self):
        self.convMonId: int = None
        self.nomeMoeda: str = None
        self.fator: float = 1
        self.dataInicial: datetime = None
        self.dataFinal: datetime = None
        self.conversao: str = 'Valorizou'
        self.moedaCorrente: bool = True
        self.dataUltAlt: datetime = None
        self.dataCadastro: datetime = None


    def toDict(self):
        dictConvMon = {
            'convMonId': self.convMonId,
            'nomeMoeda': self.nomeMoeda,
            'fator': self.fator,
            'dataInicial': self.dataInicial,
            'dataFinal': self.dataFinal,
            'conversao': self.conversao,
            'moedaCorrente': self.moedaCorrente,
            'dataUltAlt': self.dataUltAlt,
            'dataCadastro': self.dataCadastro
        }
        return dictConvMon

    def fromDict(self, dictConvMon):
        self.convMonId = dictConvMon['convMonId']
        self.nomeMoeda = dictConvMon['nomeMoeda']
        self.fator = dictConvMon['fator']
        self.dataInicial = dictConvMon['dataInicial']
        self.dataFinal = dictConvMon['dataFinal']
        self.conversao = dictConvMon['conversao']
        self.moedaCorrente = dictConvMon['moedaCorrente']
        self.dataUltAlt = dictConvMon['dataUltAlt']
        self.dataCadastro = dictConvMon['dataCadastro']

    def fromList(self, listConvMon: list, retornaInst: bool = False):
        self.convMonId = listConvMon[0]
        self.nomeMoeda = listConvMon[1]
        self.fator = listConvMon[2]
        self.dataInicial = strToDatetime(listConvMon[3], tamanho=TamanhoData.g)
        self.dataFinal = strToDatetime(listConvMon[4], tamanho=TamanhoData.g)
        self.conversao = listConvMon[5]
        self.moedaCorrente = listConvMon[6]
        self.dataUltAlt = listConvMon[7]
        self.dataCadastro = listConvMon[8]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""ConvMonModelo(
            convMonId: {self.convMonId},
            nomeMoeda: {self.nomeMoeda},
            fator: {self.fator}
            dataInicial: {self.dataInicial}
            dataFinal: {self.dataFinal}
            conversao: {self.conversao}
            moedaCorrente: {self.moedaCorrente}
            dataUltAlt: {self.dataUltAlt}
            dataCadastro: {self.dataCadastro}
        )"""
