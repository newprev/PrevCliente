import datetime

from helpers import mascaraDataPequena


class TetosPrevModelo:

    def __init__(self):
        self.tetosPrevId: int = None
        self.data: str = None
        self.valor: int = None


    def toDict(self):
        dictTetosPrev = {
            'tetosPrevId': self.tetosPrevId,
            'data': self.data,
            'valor': self.valor
        }
        return dictTetosPrev

    def fromDict(self, dictCliente):
        self.tetosPrevId = dictCliente['tetosPrevId']
        self.data = dictCliente['data']
        self.valor = dictCliente['valor']

    def fromList(self, listCliente: list, retornaInst: bool = False):
        self.tetosPrevId = listCliente[0]
        self.data = mascaraDataPequena(listCliente[1])
        self.valor = listCliente[2]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""TetosPrevModelo(
            tetosPrevId: {self.tetosPrevId},
            data: {self.data},
            valor: {self.valor}
        )"""
