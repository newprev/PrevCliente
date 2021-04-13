import datetime

from helpers import mascaraDataPequena


class TetosPrevModelo:

    def __init__(self):
        self.tetosPrevId: int = None
        self.dataValidade: datetime = None
        self.valor: int = None


    def toDict(self):
        dictTetosPrev = {
            'tetosPrevId': self.tetosPrevId,
            'dataValidade': self.dataValidade,
            'valor': self.valor
        }
        return dictTetosPrev

    def fromDict(self, dictCliente):
        self.tetosPrevId = dictCliente['tetosPrevId']
        self.dataValidade = dictCliente['dataValidade']
        self.valor = dictCliente['valor']

    def fromList(self, listCliente: list, retornaInst: bool = False):
        self.tetosPrevId = listCliente[0]
        self.dataValidade = listCliente[1]
        self.valor = listCliente[2]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""TetosPrevModelo(
            tetosPrevId: {self.tetosPrevId},
            dataValidade: {self.dataValidade},
            valor: {self.valor}
        )"""
