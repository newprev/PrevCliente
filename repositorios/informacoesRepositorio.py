import requests
import aiohttp


from Configs.systemConfig import buscaSystemConfigs
from systemLog.logs import logPrioridade, TipoEdicao, Prioridade
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
            self.baseUrl = 'http://newprev.dev.br/api/'

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
