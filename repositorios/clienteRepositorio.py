import requests as http

from logs import logPrioridade
from newPrevEnums import *
from modelos.escritorioModelo import EscritorioModelo
from modelos.advogadoModelo import AdvogadoModelo


class UsuarioRepository:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    def buscaEscritorioPrimeiroAcesso(self, nomeEscritorio) -> EscritorioModelo:
        url: str = self.baseUrl + 'escritorio/'
        busca: str = f"?search={nomeEscritorio}"

        response = http.get(url+busca)

        if 199 < response.status_code < 400:
            escritorioJson = response.json()
            if len(escritorioJson) == 1:
                escritorio = EscritorioModelo().fromDict(escritorioJson[0])
                logPrioridade(f"API____________________GET<escritorio/>:::{url+busca}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
                return escritorio
            else:
                logPrioridade(f"API____________________GET<escritorio/Erro>:::{url+busca}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                return None

    def buscaAdvNaoCadastrados(self, escritorioId) -> list:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/advogado?confirmado=false'

        response = http.get(url)

        if 199 < response.status_code < 400:
            listaAdvogadosJson: list = response.json()

            listaObjAdv = [AdvogadoModelo().fromDict(adv) for adv in listaAdvogadosJson]

            logPrioridade(f"API____________________GET<escritorio/<escritorioId>/advogado:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
            return listaObjAdv
        else:
            logPrioridade(f"API____________________GET<escritorio/<escritorioId>/advogado/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return []

