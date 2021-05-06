import requests

from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.tetosPrevModelo import TetosPrevModelo


class ApiFerramentas:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/explorer-api/'

    def getAllTetosPrevidenciarios(self, id: int = None) -> list:
        url = self.baseUrl + 'tetosPrev/'
        response = requests.get(url)

        if 199 < response.status_code < 400:
            listaTetos = [TetosPrevModelo().fromDict(teto) for teto in response.json()]
            logPrioridade("API____________________GET<tetosPrev/>", TipoEdicao.api, Prioridade.sync)
            return listaTetos
        else:
            logPrioridade("API____________________GET<ERRO>", TipoEdicao.api, Prioridade.saidaImportante)
            return []