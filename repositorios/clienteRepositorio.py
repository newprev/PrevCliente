import json
import requests as http
from os import getenv

from typing import List, Tuple
from playhouse.shortcuts import dict_to_model
from logging import info, warning, error, debug
from util.enums.logEnums import TipoLog

from modelos.advogadoORM import Advogados
from modelos.escritoriosORM import Escritorios
from modelos.Auth.AdvAuthModelo import AdvAuthModelo


class UsuarioRepository:
    header: dict

    def __init__(self):
        self.header = {"Content-Type": "application/json"}
        self.baseUrl = getenv('BASE_URL', 'http://localhost:8000/api/')

    def confirmaAlteraSenha(self, senha: str, advogadoId: int) -> bool:
        url: str = self.baseUrl + 'advogados/'
        testeJson = json.dumps({
            "senhaEnviada": senha,
            "advogadoId": advogadoId
        })

        info(f"{TipoLog.Rest.value}::confirmaAlteraSenha ____________________ PATCH<{url}>")

        response = http.patch(url, data=testeJson, headers=self.header)

        if 199 < response.status_code < 400:
            debug(f"{TipoLog.Rest.value}[{response.status_code}]::confirmaAlteraSenha ____________________ PATCH<{url}>")
            return True
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::confirmaAlteraSenha ____________________ PATCH<{url}>")
            return False

    def desconfirmaAdvogado(self, advogadoId: int) -> bool:
        url: str = self.baseUrl + f'advogados/{advogadoId}/confirmacao/'
        body: dict = {'confirmado': False}

        info(f"{TipoLog.Rest.value}::desconfirmaAdvogado ____________________ PATCH<{url}>")

        response = http.patch(url, data=body)
        if 199 < response.status_code < 400:
            debug(f"{TipoLog.Rest.value}[{response.status_code}]::desconfirmaAdvogado ____________________ PATCH<{url}>")
            return True
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::desconfirmaAdvogado ____________________ PATCH<{url}>")
            return False

    def buscaCpfEmailPrimeiroAcesso(self, cpfEmail: str, esqueceuSenha: bool = False) -> int:
        url: str = self.baseUrl + 'advogados/auth/trocaSenha/'

        body: dict = {
            'info': cpfEmail,
            'esqueceuSenha': esqueceuSenha
        }

        info(f"{TipoLog.Rest.value}::buscaEscritorioPrimeiroAcesso ____________________ GET<{url}>")
        response = http.post(url, data=body)

        if 199 < response.status_code < 400:
            debug(f"{TipoLog.Rest.value}[{response.status_code}]::buscaCpfEmailPrimeiroAcesso ____________________ POST<{url}>")
            clienteId: int = response.json()['advogadoId']
            return clienteId
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaCpfEmailPrimeiroAcesso ____________________ POST<{url}>")
            return -1

    def verificaCodAcesso(self, codAcesso: int) -> bool:
        url: str = self.baseUrl + 'advogados/auth/autenticaCodAcesso/'

        body: dict = {
            'codigo': codAcesso
        }

        info(f"{TipoLog.Rest.value}::verificaCodAcesso ____________________ PATCH<{url}>")
        response = http.patch(url, data=body)

        if 199 < response.status_code < 400:
            debug(f"{TipoLog.Rest.value}[{response.status_code}]::verificaCodAcesso ____________________ PATCH<{url}>")
            return True
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::verificaCodAcesso ____________________ PATCH<{url}>")
            return False

    def buscaEscritorioById(self, escritorioId: int) -> Escritorios:
        # TODO: Criar função que faz um GET buscando o escritório pelo Id
        pass

    def buscaAdvNaoCadastrados(self, escritorioId) -> list:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/advogado?confirmado=false&ativo=true&ordering=login'
        info(f"{TipoLog.Rest.value}::buscaAdvNaoCadastrados ____________________ GET<{url}>")

        response = http.get(url)

        if 199 < response.status_code < 400:
            listaAdvogadosJson: list = response.json()
            listaObjAdv: List[Advogados] = [dict_to_model(Advogados, adv, ignore_unknown=True) for adv in listaAdvogadosJson]

            debug(f"{TipoLog.Rest.value}[{response.status_code}]::buscaAdvNaoCadastrados ____________________ GET<{url}>")
            return listaObjAdv
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaAdvNaoCadastrados ____________________ GET<{url}>")
            return []

    def buscaSenhaProvisoria(self, usuarioId: int) -> dict:
        url: str = self.baseUrl + f'advogados/{usuarioId}/confirmacao/'
        info(f"{TipoLog.Rest.value}::buscaSenhaProvisoria ____________________ GET<{url}>")

        response = http.get(url)

        if 199 < response.status_code < 400:
            advogadoSenha: dict = response.json()

            debug(f"{TipoLog.Rest.value}[{response.status_code}]::buscaSenhaProvisoria ____________________ GET<{url}>")
            return advogadoSenha
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaSenhaProvisoria ____________________ GET<{url}>", extra={"erro": response.json()})
            return {"erro": response.json()}

    def buscaSenhaDefinitiva(self, usuarioId: int) -> dict:
        url: str = self.baseUrl + f'advogados/{usuarioId}/confirmacao/'
        info(f"{TipoLog.Rest.value}::buscaSenhaDefinitiva ____________________ GET<{url}>")

        response = http.get(url)

        if 199 < response.status_code < 400:
            advogadoSenha: dict = response.json()

            if advogadoSenha['confirmado']:
                debug(f"{TipoLog.Rest.value}[{response.status_code}]::buscaSenhaDefinitiva ____________________ GET<{url}>")
                return advogadoSenha
            else:
                warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaSenhaDefinitiva ____________________ GET<{url}>", extra={"erro": response.json()})
                return {"erro": response.json()}
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaSenhaDefinitiva ____________________ GET<{url}>", extra={"erro": response.json()})
            return {"erro": response.json()}

    def atualizaSenha(self, advogadoId: int, senha: str) -> dict:
        url: str = self.baseUrl + f'advogados/{advogadoId}/confirmacao/'
        info(f"{TipoLog.Rest.value}::atualizaSenha ____________________ PATCH<{url}>")

        obj: dict = {
            "senha": senha,
            "confirmado": True
        }
        response = http.patch(url, data=obj)

        if 199 < response.status_code < 400:
            senha = response.json()

            debug(f"{TipoLog.Rest.value}[{response.status_code}]::atualizaSenha ____________________ PATCH<{url}>")
            return senha
        else:
            warning(f"{TipoLog.Rest.value}[{response.status_code}]::atualizaSenha ____________________ PATCH<{url}>")
            return {"statusCode": response.status_code}

    def buscaAdvPor(self, advogadoId: int = None, senhaInserida: str = None) -> Tuple[Advogados, int]:
        """
        Por necessidade do framework peewee, essa função devolve o escritorioId e a instância do
        advogado.
        """

        url: str = self.baseUrl + f'advogados/{advogadoId}/'
        info(f"{TipoLog.Rest.value}::buscaAdvPor ____________________ PATCH<{url}>")

        response = http.get(url)

        try:
            if 199 < response.status_code < 400:
                debug(f"{TipoLog.Rest.value}[{response.status_code}]::buscaAdvPor ____________________ GET<{url}>")
                advogado = Advogados().fromDict(response.json())

                if senhaInserida is not None:
                    advogado.senha = senhaInserida
                else:
                    advogado.senha = 'senhaProvisoria'

                escritorioId = response.json()['escritorioId']

                if not advogado:
                    warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaAdvPor ____________________ GET<{url}>")
                    return Advogados(), 0
                else:
                    debug(f"{TipoLog.Rest.value}[{response.status_code}]::buscaAdvPor ____________________ GET<{url}>")
                    return advogado, escritorioId
            else:
                warning(f"{TipoLog.Rest.value}[{response.status_code}]::buscaAdvPor ____________________ GET<{url}>")
                return Advogados(), 0

        except Exception as err:
            error(f'{TipoLog.Rest.value}::buscaAdvPor', extra={"err": err})

    def loginAuth(self, senha, OabCpf: str = None, email: str = None) -> AdvAuthModelo:
        url: str = self.baseUrl + f'advogados/auth/login/'
        info(f"{TipoLog.Rest.value}::loginAuth ____________________ PATCH<{url}>")

        authAdvogado: AdvAuthModelo = AdvAuthModelo()
        authAdvogado.senha = senha
        authAdvogado.ativo = True
        authAdvogado.confirmado = True

        if OabCpf is not None:
            if len(OabCpf) == 9:
                authAdvogado.cpf = OabCpf
            else:
                authAdvogado.numeroOAB = OabCpf
        else:
            authAdvogado.email = email

        try:
            response = http.patch(url, data=authAdvogado.toDict())

            if 199 < response.status_code < 400:
                advAuth = AdvAuthModelo().fromDict(response.json())

                if not advAuth:
                    warning(f"{TipoLog.Rest.value}[{response.status_code}]::loginAuth ____________________ PATCH<{url}>")
                    return None
                else:
                    debug(f"{TipoLog.Rest.value}[{response.status_code}]::loginAuth ____________________ PATCH<{url}>")
                    return advAuth
            else:
                warning(f"{TipoLog.Rest.value}[{response.status_code}]::loginAuth ____________________ PATCH<{url}>", extra={"err": response.json()})
                return None

        except AttributeError as err:
            error(f'{TipoLog.Rest.value}::buscaAdvPor', extra={"err": err})
            return None
        except Exception as err:
            error(f'{TipoLog.Rest.value}::buscaAdvPor', extra={"err": err})
            return None

    def loginAuthFromCache(self, advogado: Advogados) -> bool:
        url: str = self.baseUrl + f'advogados/auth/{advogado.numeroOAB}'
        info(f"{TipoLog.Rest.value}::loginAuthFromCache ____________________ GET<{url}>")

        try:
            response = http.get(url)

            if 199 < response.status_code < 400:
                auth: AdvAuthModelo = AdvAuthModelo().fromDict(response.json())

                if auth is not None and auth == advogado:
                    debug(f"{TipoLog.Rest.value}[{response.status_code}]::loginAuthFromCache ____________________ GET<{url}>")
                    return True
                else:
                    warning(f"{TipoLog.Rest.value}[{response.status_code}]::loginAuthFromCache ____________________ GET<{url}>")
                    return False

        except KeyError as err:
            # Acontece quando buscamos uma chave que não existe em um dicionário
            error(f'{TipoLog.Rest.value}::loginAuthFromCache', extra={"err": err})
            return False
        except Exception as err:
            error(f'{TipoLog.Rest.value}::loginAuthFromCache', extra={"err": err})
            return False






