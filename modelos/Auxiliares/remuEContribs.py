from util.helpers import dataUSAtoBR


class RemuEContribs:
    itemContribuicaoId: int
    seq: int
    competencia: str
    salContribuicao: float
    natureza: str
    indicadores: str
    sinal: str
    convMonId: int
    nomeMoeda: str
    tetosPrevId: int
    valor: float

    def __init__(self, info: list):
        self.carregaDados(info)

    def carregaDados(self, listaInfo: list):
        self.itemContribuicaoId = listaInfo[0]
        self.seq = listaInfo[1]
        self.competencia = dataUSAtoBR(listaInfo[2])
        self.salContribuicao = listaInfo[3]
        self.natureza = listaInfo[4]
        self.indicadores = listaInfo[5]
        self.sinal = listaInfo[6]
        self.convMonId = listaInfo[7]
        self.nomeMoeda = listaInfo[8]
        self.tetosPrevId = listaInfo[9]
        self.valor = listaInfo[10]

