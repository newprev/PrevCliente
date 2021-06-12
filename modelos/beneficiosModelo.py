import datetime


class BeneficiosModelo:

    def __init__(self):
        self.beneficiosId: int = None
        self.clienteId: int = None
        self.seq: int = None
        self.nb: int = None
        self.especie: str = None
        self.dataInicio: datetime = None
        self.dataFim: datetime = None
        self.situacao: str = None
        self.dadoOrigem: str = None
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None


    def toDict(self):
        dictUsuario = {
            'beneficiosId': self.beneficiosId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'nb': self.nb,
            'especie': self.especie,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'situacao': self.situacao,
            'dadoOrigem': self.dadoOrigem,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictBeneficios):
        self.beneficiosId = dictBeneficios['beneficiosId']
        self.clienteId = dictBeneficios['clienteId']
        self.seq = dictBeneficios['seq']
        self.nb = dictBeneficios['nb']
        self.especie = dictBeneficios['especie']
        self.dataInicio = dictBeneficios['dataInicio']
        self.dataFim = dictBeneficios['dataFim']
        self.situacao = dictBeneficios['situacao']
        self.dadoOrigem = dictBeneficios['dadoOrigem']
        self.dataCadastro = dictBeneficios['dataCadastro']
        self.dataUltAlt = dictBeneficios['dataUltAlt']

    def fromList(self, listBeneficios: list, retornaInst: bool = True):
        self.beneficiosId = listBeneficios[0]
        self.clienteId = listBeneficios[1]
        self.seq = listBeneficios[2]
        self.nb = listBeneficios[3]
        self.especie = listBeneficios[4]
        self.dataInicio = listBeneficios[5]
        self.dataFim = listBeneficios[6]
        self.situacao = listBeneficios[7]
        self.dadoOrigem = listBeneficios[8]
        self.dataCadastro = listBeneficios[9]
        self.dataUltAlt = listBeneficios[10]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""Beneficios(
            beneficiosId: {self.beneficiosId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            nb: {self.nb},
            especie: {self.especie},
            dataInicio: {self.dataInicio},
            dataFim: {self.dataFim},
            situacao: {self.situacao},
            dadoOrigem: {self.dadoOrigem},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
