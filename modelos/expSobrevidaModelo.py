import datetime

from helpers import strToDatetime
from newPrevEnums import TamanhoData


class ExpectativaSobrevidaModelo:

    def __init__(self):
        self.infoId: int = None
        self.dataReferente: int = None
        self.idade: int = None
        self.expectativaSobrevida: int = None
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictUsuario = {
            'infoId': self.infoId,
            'dataReferente': self.dataReferente,
            'idade': self.idade,
            'expectativaSobrevida': self.expectativaSobrevida,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictExpectativaSobrevida: dict):

        self.infoId = dictExpectativaSobrevida['infoId']
        self.dataReferente = strToDatetime(dictExpectativaSobrevida['dataReferente'], TamanhoData.mm)
        self.idade = dictExpectativaSobrevida['idade']
        self.expectativaSobrevida = dictExpectativaSobrevida['expectativaSobrevida']

        if 'dataCadastro' in dictExpectativaSobrevida.keys():
            self.dataCadastro = dictExpectativaSobrevida['dataCadastro']

        if 'dataUltAlt' in dictExpectativaSobrevida.keys():
            self.dataUltAlt = dictExpectativaSobrevida['dataUltAlt']

        return self

    def fromList(self, listExpectativaSobrevida: list, retornaInst: bool = True):
        print(listExpectativaSobrevida)
        self.infoId = listExpectativaSobrevida[0]
        self.dataReferente = strToDatetime(listExpectativaSobrevida[1], TamanhoData.gg)
        self.idade = listExpectativaSobrevida[2]
        self.expectativaSobrevida = listExpectativaSobrevida[3]
        self.dataCadastro = strToDatetime(listExpectativaSobrevida[4], TamanhoData.gg)
        self.dataUltAlt = strToDatetime(listExpectativaSobrevida[5], TamanhoData.gg)

        if retornaInst:
            return self

    def __repr__(self):
        return f"""ExpectativaSobrevida(
            infoId: {self.infoId},
            dataReferente: {self.dataReferente},
            idade: {self.idade},
            expectativaSobrevida: {self.expectativaSobrevida},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
