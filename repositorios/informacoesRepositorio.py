import requests
from typing import List

from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.indicadorModelo import IndicadorModelo
from modelos.expSobrevidaModelo import ExpectativaSobrevidaModelo


class ApiInformacoes:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    def getAllIndicadores(self) -> List[dict]:
        url = self.baseUrl + 'indicadores/'
        response = requests.get(url)

        if 199 < response.status_code < 400:
            # listaIndicadores = [IndicadorModelo().fromDict(indicador) for indicador in response.json()]
            logPrioridade(f"API(Sync)____________________GET<indicadores/>::::{url}", TipoEdicao.api, Prioridade.sync)
            return response.json()
        else:
            logPrioridade(f"API(Sync)____________________GET<indicadores/ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
            return []

    def getAllExpSobrevida(self) -> List[dict]:
        url = self.baseUrl + 'expSobrevida/'
        response = requests.get(url)

        if 199 < response.status_code < 400:
            # listaExpSobrevida = [ExpectativaSobrevidaModelo().fromDict(expSobrevida) for expSobrevida in response.json()]
            logPrioridade(f"API(Sync)____________________GET<expSobrevida>::::{url}", TipoEdicao.api, Prioridade.sync)
            return response.json()
        else:
            logPrioridade(f"API(Sync)____________________GET<expSobrevidaERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
            return []

    # def getAllConvMon(self, id: int = None) -> list:
    #     url = self.baseUrl + 'convMon/'
    #     response = requests.get(url)
    #
    #     if 199 < response.status_code < 400:
    #         listaConvMon = [ConvMonModelo().fromDict(convMon) for convMon in response.json()]
    #         logPrioridade(f"API(Sync)____________________GET<convMon/>::::{url}", TipoEdicao.api, Prioridade.sync)
    #         return listaConvMon
    #     else:
    #         logPrioridade(f"API(Sync)____________________GET<ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
    #         return []

    def conexaoOnline(self) -> bool:
        try:
            response = requests.get(self.baseUrl)
            if 199 < response.status_code < 400:
                return True
        except:
            return False
