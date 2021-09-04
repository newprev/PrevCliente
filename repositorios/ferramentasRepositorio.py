import requests
import aiohttp
from util.enums.ferramentasEInfoEnums import FerramentasEInfo
from logs import logPrioridade, TipoEdicao, Prioridade


class ApiFerramentas:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    async def getAllFerramentas(self, tipo: FerramentasEInfo):
        if tipo == FerramentasEInfo.atuMonetaria:
            endpoint = 'indiceAtuMonetaria/'
        elif tipo == FerramentasEInfo.tetos:
            endpoint = 'tetosPrev/'
        elif tipo == FerramentasEInfo.convMon:
            endpoint = 'convMon/'

        async with aiohttp.ClientSession() as http:
            url = self.baseUrl + endpoint

            async with http.get(url) as response:
                statusCode = response.status
                if 199 < statusCode < 400:
                    logPrioridade(f"API(Sync)<getAllFerramentas>____________________GET<{endpoint}>::::{url}", TipoEdicao.api, Prioridade.sync)
                    return await response.json()
                else:
                    logPrioridade(f"API(Sync)<getAllFerramentas>____________________GET<{endpoint}ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
                    return []

    #
    # async def getAllTetosPrevidenciarios(self) -> list:
    #     url = self.baseUrl + 'tetosPrev/'
    #     async with aiohttp.ClientSession() as http:
    #         async with http.get(url) as response:
    #             statusCode = response.status
    #             if 199 < statusCode < 400:
    #                 logPrioridade(f"API(Sync)____________________GET<tetosPrev/>::::{url}", TipoEdicao.api, Prioridade.sync)
    #                 return await response.json()
    #             else:
    #                 logPrioridade(f"API(Sync)____________________GET<tetosPrev/ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
    #                 return []
    #
    # async def getAllConvMon(self) -> list:
    #     url = self.baseUrl + 'convMon/'
    #     async with aiohttp.ClientSession() as http:
    #         async with http.get(url) as response:
    #             statusCode = response.status
    #             if 199 < statusCode < 400:
    #                 logPrioridade(f"API(Sync)____________________GET<convMon/>::::{url}", TipoEdicao.api, Prioridade.sync)
    #                 return await response.json()
    #             else:
    #                 logPrioridade(f"API(Sync)____________________GET<convMon/ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
    #                 return []
    #
    # async def getAllIndicesAtuMonetarias(self) -> list:
    #     url = self.baseUrl + 'indiceAtuMonetaria/'
    #     async with aiohttp.ClientSession() as http:
    #         async with http.get(url) as response:
    #             statusCode = response.status
    #             if 199 < statusCode < 400:
    #                 logPrioridade(f"API(Sync)____________________GET<indiceAtuMonetaria/>::::{url}", TipoEdicao.api, Prioridade.sync)
    #                 return await response.json()
    #             else:
    #                 logPrioridade(f"API(Sync)____________________GET<indiceAtuMonetaria/ERRO>::::{url}", TipoEdicao.api, Prioridade.saidaImportante)
    #                 return []

    def conexaoOnline(self) -> bool:
        try:
            response = requests.get(self.baseUrl)
            if 199 < response.status_code < 400:
                return True
        except:
            return False
