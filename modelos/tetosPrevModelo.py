import datetime


class TetosPrevModelo:

    def __init__(self):
        self.tetosPrevId: int = None
        self.dataValidade: datetime = None
        self.valor: int = None
        self.dataUltAlt: datetime = None
        self.dataCadastro: datetime = None

    def toDict(self):
        dictTetosPrev = {
            'tetosPrevId': self.tetosPrevId,
            'dataValidade': self.dataValidade,
            'valor': self.valor
        }
        return dictTetosPrev

    def fromDict(self, dictTeto):
        self.tetosPrevId = dictTeto['tetosPrevId']
        self.dataValidade = dictTeto['dataValidade']
        self.valor = dictTeto['valor']
        self.dataUltAlt = datetime.datetime.now()
        self.dataCadastro = datetime.datetime.now()
        return self

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
