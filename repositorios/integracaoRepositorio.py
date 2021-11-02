import requests as http

from systemLog.logs import logPrioridade
from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import *


class IntegracaoRepository:

    def __init__(self):
        self.urlBase = 'https://'

    def getCep(self, numCep):
        url = self.urlBase + f'viacep.com.br/ws/{numCep}/json/'
        try:
            logPrioridade(f"API(CEP)<getCep>____________________GET<viacep.com.br/ws/<numCep>/json/>::::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.sync, tipoLog=TipoLog.Rest)
            response: http.Response = http.get(url)

            if response.status_code == 200:
                if response.text != "" and 'erro' not in response.json().keys():
                    return response.json()
                else:
                    return dict()
            else:
                return dict()
        except http.exceptions.ConnectionError:
            mensagem = {'erro': 'Falta de conexão com a internet.'}
            return mensagem
