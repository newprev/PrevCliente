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
        self.sinal: str = None
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
            'sinal': self.sinal,
            'dataUltAlt': self.dataUltAlt,
            'dataCadastro': self.dataCadastro
        }
        return dictConvMon

    def fromDict(self, dictConvMon: dict):
        if 'convMonId' in dictConvMon.keys():
            self.convMonId = dictConvMon['convMonId']

        if 'dataUltAlt' in dictConvMon.keys():
            self.dataUltAlt = dictConvMon['dataUltAlt']

        if 'dataCadastro' in dictConvMon.keys():
            self.dataCadastro = dictConvMon['dataCadastro']

        if dictConvMon['dataFinal'] is not None:
            self.dataFinal = dictConvMon['dataFinal']
        else:
            self.dataFinal = dictConvMon['dataInicial']

        self.nomeMoeda = dictConvMon['nomeMoeda']
        self.fator = dictConvMon['fator']
        self.dataInicial = dictConvMon['dataInicial']
        self.conversao = dictConvMon['conversao']
        self.moedaCorrente = dictConvMon['moedaCorrente']
        self.sinal = dictConvMon['sinal']
        return self

    def fromList(self, listConvMon: list, retornaInst: bool = True):

        self.convMonId = listConvMon[0]
        self.nomeMoeda = listConvMon[1]
        self.fator = listConvMon[2]
        self.dataInicial = strToDatetime(listConvMon[3], tamanho=TamanhoData.mm)
        self.dataFinal = strToDatetime(listConvMon[4], tamanho=TamanhoData.mm)
        self.conversao = listConvMon[5]
        self.moedaCorrente = listConvMon[6]
        self.sinal = listConvMon[7]
        self.dataUltAlt = listConvMon[8]
        self.dataCadastro = listConvMon[9]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""ConvMonModelo(
            convMonId: {self.convMonId},
            nomeMoeda: {self.nomeMoeda},
            fator: {self.fator},
            dataInicial: {self.dataInicial},
            dataFinal: {self.dataFinal},
            conversao: {self.conversao},
            moedaCorrente: {self.moedaCorrente},
            sinal: {self.sinal},
            dataUltAlt: {self.dataUltAlt},
            dataCadastro: {self.dataCadastro}
        )"""
