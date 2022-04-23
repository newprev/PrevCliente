from logging import info, debug, warning

import requests
import aiohttp


from Configs.systemConfig import buscaSystemConfigs
from util.enums.ferramentasEInfoEnums import FerramentasEInfo
from util.enums.configEnums import TipoConexao
from util.enums.logEnums import TipoLog


class ApiInformacoes:
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
        elif tipo == FerramentasEInfo.ipca:
            endpoint = 'ipcaMensal/'
        elif tipo == FerramentasEInfo.tipoBeneficio:
            endpoint = 'tipoBeneficio/'
        elif tipo == FerramentasEInfo.especieBeneficio:
            endpoint = 'especieBeneficio/'
        else:
            endpoint = ''

        async with aiohttp.ClientSession() as http:
            url = self.baseUrl + endpoint
            info(f"{TipoLog.Rest.value}::getAllInformacoes ____________________ GET<{url}>")

            async with http.get(url) as response:
                statusCode = response.status
                if 199 < statusCode < 400:
                    debug(f"{TipoLog.Rest.value}[{statusCode}]::getAllInformacoes ____________________ GET<{url}>")
                    return await response.json()
                else:
                    warning(f"{TipoLog.Rest.value}[{statusCode}]::getAllInformacoes ____________________ GET<{url}>", extra={'json': response.json()})
                    return []

    def conexaoOnline(self) -> bool:
        try:
            response = requests.get(self.baseUrl)
            if 199 < response.status_code < 400:
                return True
        except:
            return False
