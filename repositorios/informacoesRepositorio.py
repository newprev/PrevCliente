import requests
import aiohttp

from logs import logPrioridade, TipoEdicao, Prioridade
from util.enums.ferramentasEInfoEnums import FerramentasEInfo
from util.enums.logEnums import TipoLog


class ApiInformacoes:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    async def getAllInformacoes(self, tipo: FerramentasEInfo):

        if tipo == FerramentasEInfo.indicadores:
            endpoint = 'indicadores/'
        elif tipo == FerramentasEInfo.expSobrevida:
            endpoint = 'expSobrevida/'
        elif tipo == FerramentasEInfo.carenciasLei91:
            endpoint = 'carenciasLei91/'
        elif tipo == FerramentasEInfo.atuMonetaria:
            endpoint = 'indiceAtuMonetaria/'
        elif tipo == FerramentasEInfo.salarioMinimo:
            endpoint = 'salarioMinimo/'

        async with aiohttp.ClientSession() as http:
            url = self.baseUrl + endpoint

            async with http.get(url) as response:
                statusCode = response.status
                if 199 < statusCode < 400:
                    logPrioridade(f"API(Sync)<getAllInformacoes>____________________GET<{endpoint}>::::{url}", tipoLog=TipoLog.Rest, tipoEdicao=TipoEdicao.api, priodiade=Prioridade.sync)
                    return await response.json()
                else:
                    logPrioridade(f"API(Sync)<getAllInformacoes>____________________GET<{endpoint}ERRO>::::{url}", tipoLog=TipoLog.Rest, tipoEdicao=TipoEdicao.api, priodiade=Prioridade.sync)
                    return []

    def conexaoOnline(self) -> bool:
        try:
            response = requests.get(self.baseUrl)
            if 199 < response.status_code < 400:
                return True
        except:
            return False
