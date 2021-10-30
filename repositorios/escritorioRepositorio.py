import requests as http
from requests.exceptions import *

from Configs.systemConfig import buscaSystemConfigs
from logs import logPrioridade
from util.enums.newPrevEnums import *
from util.enums.logEnums import TipoLog
from modelos.escritoriosORM import Escritorios


class EscritorioRepositorio:

    def __init__(self):
        configs: dict = buscaSystemConfigs()

        if configs['tipoConexao'] == 'dev':
            # url para desenvolvimento
            self.baseUrl = 'http://localhost:8000/api/'
        else:
            # url para produção
            self.baseUrl = 'http://newprev.dev.br/api/'

    def buscaEscritorio(self, escritorioId) -> Escritorios:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/'

        try:
            response = http.get(url)

            if 199 < response.status_code < 400:

                escritorioModelo = Escritorios().fromDict(response.json())
                logPrioridade(f"API____________________GET<escritorio/<int:id>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComun)
                return escritorioModelo
            else:
                logPrioridade(f"API____________________GET<escritorio/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                return Escritorios()
        except ConnectionError as err:
            print(f'buscaEscritorio ({type(err)}): {err}')
            return ErroConexao.ConnectionError
