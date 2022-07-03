import requests as http
from requests.exceptions import *
from logging import debug, info, warning, error
from os import getenv

from util.enums.newPrevEnums import *
from util.enums.logEnums import TipoLog
from modelos.escritoriosORM import Escritorios


class EscritorioRepositorio:
    header: dict

    def __init__(self):
        self.header = {"Content-Type": "application/json"}
        self.baseUrl = getenv('BASE_URL', 'http://localhost:8000/api/')

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
