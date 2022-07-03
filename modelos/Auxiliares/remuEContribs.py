from util.helpers.helpers import dataUSAtoBR


class RemuEContribs:
    itemContribuicaoId: int
    seq: int
    competencia: str
    fatorInsalubridade: float
    grauDeficiencia: float
    salContribuicao: float
    indicadores: str
    sinal: str
    convMonId: int
    nomeMoeda: str

    def __init__(self, info: list):
        self.carregaDados(info)

    def carregaDados(self, listaInfo: list):
        self.itemContribuicaoId = listaInfo[0]
        self.competencia = dataUSAtoBR(listaInfo[1])
        self.fatorInsalubridade = listaInfo[2]
        self.grauDeficiencia = listaInfo[3]
        self.salContribuicao = listaInfo[4]
        self.indicadores = listaInfo[5]
        self.sinal = listaInfo[6]
        self.convMonId = listaInfo[7]
        self.nomeMoeda = listaInfo[8]

