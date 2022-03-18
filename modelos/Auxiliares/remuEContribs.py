from util.helpers import dataUSAtoBR


class RemuEContribs:
    itemContribuicaoId: int
    seq: int
    competencia: str
    salContribuicao: float
    indicadores: str
    sinal: str
    convMonId: int
    nomeMoeda: str

    def __init__(self, info: list):
        self.carregaDados(info)

    def carregaDados(self, listaInfo: list):
        self.itemContribuicaoId = listaInfo[0]
        self.seq = listaInfo[1]
        self.competencia = dataUSAtoBR(listaInfo[2])
        self.salContribuicao = listaInfo[3]
        self.indicadores = listaInfo[4]
        self.sinal = listaInfo[5]
        self.convMonId = listaInfo[6]
        self.nomeMoeda = listaInfo[7]

