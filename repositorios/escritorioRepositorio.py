import requests as http
from requests.exceptions import *
from logs import logPrioridade
from util.enums.newPrevEnums import *
from modelos.escritoriosORM import Escritorios


class EscritorioRepositorio:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    def buscaEscritorio(self, escritorioId) -> Escritorios:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/'

        try:
            response = http.get(url)

            if 199 < response.status_code < 400:

                escritorioModelo = Escritorios().fromDict(response.json())
                logPrioridade(f"API____________________GET<escritorio/<int:id>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
                return escritorioModelo
            else:
                logPrioridade(f"API____________________GET<escritorio/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                return Escritorios()
        except ConnectionError:
            return ErroConexao.ConnectionError
