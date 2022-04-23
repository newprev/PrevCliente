import requests as http
from requests.exceptions import *
from logging import debug, info, warning, error

from Configs.systemConfig import buscaSystemConfigs
from util.enums.newPrevEnums import *
from util.enums.logEnums import TipoLog
from util.enums.configEnums import TipoConexao
from modelos.escritoriosORM import Escritorios


class EscritorioRepositorio:
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

    def buscaEscritorio(self, escritorioId) -> Escritorios:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/'
        info(f"{TipoLog.Rest.value}::buscaEscritorio ____________________ GET<{url}>")

        try:
            response = http.get(url)

            if 199 < response.status_code < 400:

                escritorioModelo = Escritorios().fromDict(response.json())
                debug(f"{TipoLog.Rest.value}[{response.status_code}]::buscaEscritorio ____________________ GET<{url}>")
                return escritorioModelo
            else:
                warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaEscritorio ____________________ GET<{url}>", extra={"json": response.json()})
                return Escritorios()
        except ConnectionError as err:
            error(f'{TipoLog.Rest.value}::buscaEscritorio', extra={"err": err})
            return ErroConexao.ConnectionError
