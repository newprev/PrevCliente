from logging import info, debug, warning, error

import requests as http

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import *


class IntegracaoRepository:
    header: dict

    def __init__(self):
        self.urlBase = 'https://'
        self.header = {"Content-Type": "application/json"}

    def getCep(self, numCep):
        url = self.urlBase + f'viacep.com.br/ws/{numCep}/json/'
        info(f"{TipoLog.Rest.value}::getCep ____________________ GET<{url}>")

        try:
            response: http.Response = http.get(url)

            if response.status_code == 200:
                debug(f"{TipoLog.Rest.value}[{response.status_code}]::getCep ____________________ GET<{url}>")
                if response.text != "" and 'erro' not in response.json().keys():
                    return response.json()
                else:
                    warning(f"{TipoLog.Rest.value}[{response.status_code}]::getCep ____________________ GET<{url}>", extra={'json': response.json()})
                    return dict()
            else:
                warning(f"{TipoLog.Rest.value}[{response.status_code}]::getCep ____________________ GET<{url}>", extra={'json': response.json()})
                return dict()
        except http.exceptions.ConnectionError as err:
            error(f'{TipoLog.Rest.value}::getCep', extra={"err": err})
            mensagem = {'erro': 'Falta de conexão com a internet.'}
            return mensagem
