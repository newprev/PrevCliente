import requests

from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.convMonModelo import ConvMonModelo
from modelos.tetosPrevORM import TetosPrev


class ApiFerramentas:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    def getAllTetosPrevidenciarios(self, id: int = None) -> list:
        url = self.baseUrl + 'tetosPrev/'
        response = requests.get(url)

        if 199 < response.status_code < 400:
            logPrioridade(f"API(Sync)____________________GET<tetosPrev/>::::{url}", TipoEdicao.api, Prioridade.sync)
            return response.json()
        else:
            logPrioridade(f"API(Sync)____________________GET<tetosPrev/ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
            return []

    def getAllConvMon(self, id: int = None) -> list:
        url = self.baseUrl + 'convMon/'
        response = requests.get(url)

        if 199 < response.status_code < 400:
            logPrioridade(f"API(Sync)____________________GET<convMon/>::::{url}", TipoEdicao.api, Prioridade.sync)
            return response.json()
        else:
            logPrioridade(f"API(Sync)____________________GET<ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
            return []

    def conexaoOnline(self) -> bool:
        try:
            response = requests.get(self.baseUrl)
            if 199 < response.status_code < 400:
                return True
        except:
            return False
