import requests
import aiohttp

from Configs.systemConfig import buscaSystemConfigs
from util.enums.ferramentasEInfoEnums import FerramentasEInfo
from util.enums.logEnums import TipoLog
from logs import logPrioridade, TipoEdicao, Prioridade


class ApiFerramentas:

    def __init__(self):
        configs: dict = buscaSystemConfigs()

        if configs['tipoConexao'] == 'dev':
            # url para desenvolvimento
            self.baseUrl = 'http://localhost:8000/api/'
        else:
            # url para produção
            self.baseUrl = 'http://newprev.dev.br/api/'

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
                    logPrioridade(f"API(Sync)<getAllFerramentas>____________________GET<{endpoint}>::::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.sync, tipoLog=TipoLog.Rest)
                    return await response.json()
                else:
                    logPrioridade(f"API(Sync)<getAllFerramentas>____________________GET<{endpoint}ERRO>::::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante, tipoLog=TipoLog.Rest)
                    return []

    def conexaoOnline(self) -> bool:
        try:
            response = requests.get(self.baseUrl)
            if 199 < response.status_code < 400:
                return True
        except:
            return False
