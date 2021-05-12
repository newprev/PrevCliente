import json

import requests as http
from logs import logPrioridade
from newPrevEnums import *
from modelos.escritorioModelo import EscritorioModelo


class EscritorioRepositorio:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    def buscaEscritorio(self, escritorioId) -> EscritorioModelo:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/'

        response = http.get(url)

        if 199 < response.status_code < 400:

            escritorioModelo = EscritorioModelo().fromDict(response.json())
            logPrioridade(f"API____________________GET<escritorio/<int:id>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
            return escritorioModelo
        else:
            logPrioridade(f"API____________________GET<escritorio/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return EscritorioModelo()
