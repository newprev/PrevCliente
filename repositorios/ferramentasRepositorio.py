import requests
import aiohttp
from logging import info, debug, warning

from Configs.systemConfig import buscaSystemConfigs
from util.enums.ferramentasEInfoEnums import FerramentasEInfo
from util.enums.configEnums import TipoConexao
from util.enums.logEnums import TipoLog


class ApiFerramentas:
    header: dict

    def __init__(self):
        configs: dict = buscaSystemConfigs()
        self.header = {"Content-Type": "application/json"}

        if TipoConexao.desenvolvimento.name == configs['tipoConexao']:
            # url para desenvolvimento
            self.baseUrl = 'http://localhost:8000/api/'
        else:
            # url para produção
            self.baseUrl = 'http://3.139.65.128:8080/api/'

    async def getAllFerramentas(self, tipo: FerramentasEInfo):
        if tipo == FerramentasEInfo.atuMonetaria:
            endpoint = 'indiceAtuMonetaria/'
        elif tipo == FerramentasEInfo.tetos:
            endpoint = 'tetosPrev/'
        elif tipo == FerramentasEInfo.convMon:
            endpoint = 'convMon/'

        async with aiohttp.ClientSession() as http:
            url = self.baseUrl + endpoint
            info(f"{TipoLog.Rest.value}::getAllFerramentas ____________________ GET<{url}>")

            async with http.get(url) as response:
                statusCode = response.status
                if 199 < statusCode < 400:
                    debug(f"{TipoLog.Rest.value}[{statusCode}]::getAllFerramentas ____________________ GET<{url}>")
                    return await response.json()
                else:
                    warning(f"{TipoLog.Rest.value}[{statusCode}]::buscaEscritorio ____________________ GET<{url}>", extra={"json": response.json()})
                    return []

    def conexaoOnline(self) -> bool:
        try:
            response = requests.get(self.baseUrl)
            if 199 < response.status_code < 400:
                return True
        except:
            return False
