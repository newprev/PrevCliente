import datetime


class ContribuicoesModelo:

    def __init__(self):
        self.contribuicoesId: int = None
        self.clienteId: int = None
        self.seq: int = None
        self.competencia: datetime = None
        self.dataPagamento: datetime = None
        self.contribuicao: float = None
        self.salContribuicao: float = None
        self.indicadores: str = None
        self.dadoOrigem: str = None
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None


    def toDict(self):
        dictUsuario = {
            'contribuicoesId': self.contribuicoesId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'competencia': self.competencia,
            'dataPagamento': self.dataPagamento,
            'contribuicao': self.contribuicao,
            'salContribuicao': self.salContribuicao,
            'indicadores': self.indicadores,
            'dadoOrigem': self.dadoOrigem,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictContribuicoes):
        self.contribuicoesId = dictContribuicoes['contribuicoesId'],
        self.clienteId = dictContribuicoes['clienteId'],
        self.seq = dictContribuicoes['seq'],
        self.competencia = dictContribuicoes['competencia'],
        self.dataPagamento = dictContribuicoes['dataPagamento'],
        self.contribuicao = dictContribuicoes['contribuicao'],
        self.salContribuicao = dictContribuicoes['salContribuicao'],
        self.indicadores = dictContribuicoes['indicadores'],
        self.dadoOrigem = dictContribuicoes['dadoOrigem'],
        self.dataCadastro = dictContribuicoes['dataCadastro'],
        self.dataUltAlt = dictContribuicoes['dataUltAlt'],


    def fromList(self, listContribuicoes: list, retornaInst: bool = False):
        self.contribuicoesId = listContribuicoes[0]
        self.clienteId = listContribuicoes[1]
        self.seq = listContribuicoes[2]
        self.competencia = listContribuicoes[3]
        self.dataPagamento = listContribuicoes[4]
        self.contribuicao = listContribuicoes[4]
        self.salContribuicao = listContribuicoes[4]
        self.indicadores = listContribuicoes[5]
        self.dadoOrigem = listContribuicoes[6]
        self.dataCadastro = listContribuicoes[7]
        self.dataUltAlt = listContribuicoes[8]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""Contribuicoes(
            contribuicoesId: {self.contribuicoesId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            competencia: {self.competencia},
            dataPagamento: {self.dataPagamento},
            contribuicao: {self.contribuicao},
            salContribuicao: {self.salContribuicao},
            indicadores: {self.indicadores},
            dadoOrigem: {self.dadoOrigem},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
