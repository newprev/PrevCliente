import datetime


class ProcessosModelo:

    def __init__(self):
        self.processosId: int = None
        self.clienteId: int = None
        self.advogadoId: int = None
        self.numeroProcesso: str = None
        self.natureza: int = None
        self.tipoProcesso: int = None
        self.tipoBeneficio: int = None
        self.subTipoApos: int = None
        self.estado: str = None
        self.cidade: str = None
        self.situacaoId: int = 0
        self.tempoContribuicao: int = 0
        self.dib: datetime = None
        self.der: datetime = None
        self.dataInicio: datetime = None
        self.dataFim: datetime = None
        self.valorCausa: float = 0
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictUsuario = {
            'processosId': self.processosId,
            'clienteId': self.clienteId,
            'advogadoId': self.advogadoId,
            'numeroProcesso': self.numeroProcesso,
            'natureza': self.natureza,
            'tipoProcesso': self.tipoProcesso,
            'tipoBeneficio': self.tipoBeneficio,
            'subTipoApos': self.subTipoApos,
            'estado': self.estado,
            'cidade': self.cidade,
            'situacaoId': self.situacaoId,
            'tempoContribuicao': self.tempoContribuicao,
            'dib': self.dib,
            'der': self.der,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'valorCausa': self.valorCausa,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictProcessos):
        self.processosId = dictProcessos['processosId']
        self.clienteId = dictProcessos['clienteId']
        self.advogadoId = dictProcessos['advogadoId']
        self.numeroProcesso = dictProcessos['numeroProcesso']
        self.natureza = dictProcessos['natureza']
        self.tipoProcesso = dictProcessos['tipoProcesso']
        self.tipoBeneficio = dictProcessos['tipoBeneficio']
        self.subTipoApos = dictProcessos['subTipoApos']
        self.estado = dictProcessos['estado']
        self.cidade = dictProcessos['cidade']
        self.situacaoId = dictProcessos['situacaoId']
        self.tempoContribuicao = dictProcessos['tempoContribuicao']
        self.dib = dictProcessos['dib']
        self.der = dictProcessos['der']
        self.dataInicio = dictProcessos['dataInicio']
        self.dataFim = dictProcessos['dataFim']
        self.valorCausa = dictProcessos['valorCausa']
        self.dataCadastro = dictProcessos['dataCadastro']
        self.dataUltAlt = dictProcessos['dataUltAlt']

        return self

    def fromList(self, listProcessos: list, retornaInst: bool = False):

        self.processosId = listProcessos[0]
        self.clienteId = listProcessos[1]
        self.advogadoId = listProcessos[2]
        self.numeroProcesso = listProcessos[3]
        self.natureza = listProcessos[4]
        self.tipoProcesso = listProcessos[5]
        self.tipoBeneficio = listProcessos[6]
        self.subTipoApos = listProcessos[7]
        self.estado = listProcessos[8]
        self.cidade = listProcessos[9]
        self.situacaoId = listProcessos[10]
        self.tempoContribuicao = listProcessos[11]
        self.dib = listProcessos[12]
        self.der = listProcessos[13]
        self.dataInicio = listProcessos[14]
        self.dataFim = listProcessos[15]
        self.valorCausa = listProcessos[16]
        self.dataCadastro = listProcessos[17]
        self.dataUltAlt = listProcessos[18]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""Processos(
            processosId: {self.processosId},
            clienteId: {self.clienteId},
            advogadoId: {self.advogadoId},
            numeroProcesso: {self.numeroProcesso},
            natureza: {self.natureza},
            tipoProcesso: {self.tipoProcesso},
            tipoBeneficio: {self.tipoBeneficio},
            subTipoApos: {self.subTipoApos},
            estado: {self.estado},
            cidade: {self.cidade},
            situacaoId: {self.situacaoId},
            tempoContribuicao: {self.tempoContribuicao},
            dib: {self.dib},
            der: {self.der},
            dataInicio: {self.dataInicio},
            dataFim: {self.dataFim},
            valorCausa: {self.valorCausa},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
