import datetime


class IndiceAtuMonetarioModelo:

    def __init__(self):
        self.indiceId: str = None
        self.dataReferente: str = None
        self.dib: str = None
        self.fator: str = None
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictIndiceAtuMonetario = {
            'indiceId': self.indiceId,
            'dataReferente': self.dataReferente,
            'dib': self.dib,
            'fator': self.fator,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictIndiceAtuMonetario

    def fromDict(self, dictIndiceAtuMonetario):
        self.indiceId = dictIndiceAtuMonetario['indiceId']
        self.dataReferente = dictIndiceAtuMonetario['dataReferente']
        self.dib = dictIndiceAtuMonetario['dib']
        self.fator = dictIndiceAtuMonetario['fator']
        self.dataCadastro = dictIndiceAtuMonetario['dataCadastro']
        self.dataUltAlt = dictIndiceAtuMonetario['dataUltAlt']
        return self

    def fromList(self, listIndiceAtuMonetario: list, retornaInst: bool = True):
        self.indiceId = listIndiceAtuMonetario[0]
        self.dataReferente = listIndiceAtuMonetario[1]
        self.dib = listIndiceAtuMonetario[2]
        self.fator = listIndiceAtuMonetario[3]
        self.dataCadastro = listIndiceAtuMonetario[22]
        self.dataUltAlt = listIndiceAtuMonetario[23]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""IndiceAtuMonetarioModelo(
            indiceId: {self.indiceId},
            dataReferente: {self.dataReferente},
            dib: {self.dib},
            fator: {self.fator},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )"""
