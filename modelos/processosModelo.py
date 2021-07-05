import datetime


class ProcessosModelo:

    def __init__(self):
        self.processoId: int = None
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
        self.pontuacao: int = 0
        self.dib: datetime = None
        self.der: datetime = None
        self.mediaSalarial: float = 0.0
        self.dataInicio: datetime = None
        self.dataFim: datetime = None
        self.valorCausa: float = 0
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictUsuario = {
            'processoId': self.processoId,
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
            'pontuacao': self.pontuacao,
            'dib': self.dib,
            'der': self.der,
            'mediaSalarial': self.mediaSalarial,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'valorCausa': self.valorCausa,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictProcessos):
        self.processoId = dictProcessos['processoId']
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
        self.pontuacao = dictProcessos['pontuacao']
        self.dib = dictProcessos['dib']
        self.der = dictProcessos['der']
        self.mediaSalarial = dictProcessos['mediaSalarial']
        self.dataInicio = dictProcessos['dataInicio']
        self.dataFim = dictProcessos['dataFim']
        self.valorCausa = dictProcessos['valorCausa']
        self.dataCadastro = dictProcessos['dataCadastro']
        self.dataUltAlt = dictProcessos['dataUltAlt']

        return self

    def fromList(self, listProcessos: list, retornaInst: bool = True):

        self.processoId = listProcessos[0]
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
        self.pontuacao = listProcessos[12]
        self.dib = listProcessos[13]
        self.der = listProcessos[14]
        self.mediaSalarial = listProcessos[15]
        self.dataInicio = listProcessos[16]
        self.dataFim = listProcessos[17]
        self.valorCausa = listProcessos[18]
        self.dataCadastro = listProcessos[19]
        self.dataUltAlt = listProcessos[20]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""Processos(
            processoId: {self.processoId},
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
            pontuacao: {self.pontuacao},
            dib: {self.dib},
            der: {self.der},
            mediaSalarial: {self.mediaSalarial},
            dataInicio: {self.dataInicio},
            dataFim: {self.dataFim},
            valorCausa: {self.valorCausa},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
