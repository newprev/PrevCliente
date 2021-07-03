import datetime


class IndicadorModelo:

    def __init__(self):
        self.indicadorId: str = None
        self.resumo: str = None
        self.descricao: str = None
        self.fonte: str = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictIndicador = {
            'indicadorId': self.indicadorId,
            'resumo': self.resumo,
            'descricao': self.descricao,
            'fonte': self.fonte,
            'dataUltAlt': self.dataUltAlt
        }
        return dictIndicador

    def fromDict(self, dictIndicador):
        self.indicadorId = dictIndicador['indicadorId']
        self.resumo = dictIndicador['resumo']
        self.descricao = dictIndicador['descricao']
        self.fonte = dictIndicador['fonte']
        self.dataUltAlt = dictIndicador['dataUltAlt']
        return self

    def fromList(self, listCliente: list, retornaInst: bool = True):
        self.indicadorId = listCliente[0]
        self.resumo = listCliente[1]
        self.descricao = listCliente[2]
        self.fonte = listCliente[2]
        self.dataUltAlt = listCliente[2]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""IndicadorModelo(
            indicadorId: {self.indicadorId},
            sigla: {self.resumo},
            descricao: {self.descricao},
            fonte: {self.fonte},
            dataUltAlt: {self.dataUltAlt}
        )"""
