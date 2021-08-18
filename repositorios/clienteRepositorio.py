import requests as http
from logs import logPrioridade
from typing import List
from playhouse.shortcuts import dict_to_model, model_to_dict

from newPrevEnums import *

from modelos.advogadoORM import Advogados
from modelos.escritoriosORM import Escritorios
from modelos.Auth.ClientAuthModelo import ClientAuthModelo
from repositorios.escritorioRepositorio import EscritorioRepositorio


class UsuarioRepository:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/api/'

    def buscaEscritorioPrimeiroAcesso(self, nomeEscritorio) -> Escritorios:
        url: str = self.baseUrl + 'escritorio/'
        busca: str = f"?search={nomeEscritorio}"

        response = http.get(url+busca)

        if 199 < response.status_code < 400:
            escritorioJson = response.json()
            if len(escritorioJson) == 1:
                escritorioAux = dict_to_model(Escritorios, escritorioJson[0], ignore_unknown=True)
                escritorio, created = Escritorios.get_or_create(**model_to_dict(escritorioAux, recurse=False))

                logPrioridade(f"API => buscaEscritorioPrimeiroAcesso ____________________GET<escritorio/>:::{url+busca}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
                return escritorio
            else:
                logPrioridade(f"API => buscaEscritorioPrimeiroAcesso ____________________GET<escritorio/Erro>:::{url+busca}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                return None

    def buscaEscritorioById(self, escritorioId: int) -> Escritorios:
        # TODO: Criar função que faz um GET buscando o escritório pelo Id
        pass

    def buscaAdvNaoCadastrados(self, escritorioId) -> list:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/advogado?confirmado=false&ativo=true&ordering=login'

        response = http.get(url)

        if 199 < response.status_code < 400:
            listaAdvogadosJson: list = response.json()
            listaObjAdv: List[Advogados] = [dict_to_model(Advogados, adv, ignore_unknown=True) for adv in listaAdvogadosJson]

            logPrioridade(f"API => buscaAdvNaoCadastrados ____________________GET<escritorio/<escritorioId>/advogado:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
            return listaObjAdv
        else:
            logPrioridade(f"API => buscaAdvNaoCadastrados ____________________GET<escritorio/<escritorioId>/advogado/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return []

    def buscaSenhaProvisoria(self, usuarioId: int) -> dict:
        url: str = self.baseUrl + f'advogados/{usuarioId}/confirmacao/'

        response = http.get(url)

        if 199 < response.status_code < 400:
            advogadoSenha: dict = response.json()

            logPrioridade(f"API => buscaSenhaProvisoria ____________________GET<advogado/<int:id>/confirmacao>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
            return advogadoSenha
        else:
            logPrioridade(f"API => buscaSenhaProvisoria GET<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return {"erro": response.json()}

    def buscaSenhaDefinitiva(self, usuarioId: int) -> dict:
        url: str = self.baseUrl + f'advogados/{usuarioId}/confirmacao/'

        response = http.get(url)

        if 199 < response.status_code < 400:
            advogadoSenha: dict = response.json()

            if advogadoSenha['confirmado']:
                logPrioridade(f"API => buscaSenhaDefinitiva ____________________GET<advogado/<int:id>/confirmacao>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
                return advogadoSenha
            else:
                logPrioridade(f"API => buscaSenhaDefinitiva GET<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                return {"erro": response.json()}
        else:
            logPrioridade(f"API => buscaSenhaDefinitiva GET<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return {"erro": response.json()}

    def atualizaSenha(self, advogadoId: int, senha: str) -> dict:
        url: str = self.baseUrl + f'advogados/{advogadoId}/confirmacao/'

        obj: dict = {
            "senha": senha,
            "confirmado": True
        }
        response = http.patch(url, data=obj)

        if 199 < response.status_code < 400:
            senha = response.json()

            logPrioridade(f"API => atualizaSenha ____________________PATCH<advogado/<int:id>/confirmacao>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
            return senha
        else:
            logPrioridade(f"API => atualizaSenha ____________________PATCH<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return {"statusCode": response.status_code}

    def buscaAdvPor(self, advogadoId: int = None, senhaInserida: str = None) -> Advogados:
        url: str = self.baseUrl + f'advogados/{advogadoId}/'
        advogado: Advogados = Advogados()

        response = http.get(url)

        try:
            if 199 < response.status_code < 400:
                escritorioId = response.json()['escritorioId']
                advogado = Advogados().fromDict(response.json())
                advogado.escritorioId = Escritorios.select().where(Escritorios.escritorioId == escritorioId)

                if senhaInserida is not None:
                    advogado.senha = senhaInserida

                Advogados.insert(advogado.toDict()).on_conflict_replace().execute()

                if not advogado:
                    logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                    return False
                else:
                    logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
                    return advogado
            else:
                logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                return False
        except Escritorios.DoesNotExist:
            escritorio: Escritorios = EscritorioRepositorio().buscaEscritorio(escritorioId)
            Escritorios.insert(escritorio.toDict()).on_conflict_replace().execute()
            return self.buscaAdvPor(advogadoId, senhaInserida=senhaInserida)

        except Exception as erro:
            print(f'buscaAdvPor - Erro: {type(erro)}')
            logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)

    def loginAuth(self, senha, numeroOAB: str = None, email: str = None) -> Advogados:
        url: str = self.baseUrl + f'advogados/auth/'
        if numeroOAB is not None:
            url += numeroOAB
        else:
            url += email
        try:
            response = http.get(url)

            if 199 < response.status_code < 400:
                advAuth = ClientAuthModelo().fromDict(response.json())
                advAuth.ativo = True

                if not advAuth:
                    logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                    return None
                else:

                    try:
                        advogadoALogar = Advogados.get_by_id(advAuth.advogadoId)
                    except Advogados.DoesNotExist:
                        logPrioridade(f"API => buscaAdvPor ____________________GET<Advogados.DoesNotExist>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                        advogadoALogar = self.buscaAdvPor(advAuth.advogadoId, senhaInserida=advAuth.senha)

                    advogadoALogar.senha = senha
                    if advAuth == advogadoALogar:
                        logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
                        return advogadoALogar
                    else:
                        logPrioridade(f"API => buscaAdvPor ____________________GET<Autenticação não confere com o advogado em questão>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                        return None
            else:
                logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                return None
        except AttributeError as erro:
            print(f'loginAuth - AttributeError: {erro}')
            logPrioridade(f"API => buscaAdvPor (AttributeError)____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return None
        except Exception as erro:
            print(f'loginAuth - Exception: {type(erro)}')
            logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return None

    def loginAuthFromCache(self, advogado: Advogados) -> bool:
        url: str = self.baseUrl + f'advogados/auth/{advogado.numeroOAB}'

        try:
            response = http.get(url)

            if 199 < response.status_code < 400:
                auth: ClientAuthModelo = ClientAuthModelo().fromDict(response.json())

                if auth is not None and auth == advogado:
                    logPrioridade(f"API => loginAuthFromCache ____________________GET</advogados/auth/<str:numeroOAB>>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaComun)
                    return True
                else:
                    logPrioridade(f"API => loginAuthFromCache ____________________GET</advogados/auth/<str:numeroOAB>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
                    return False
        except KeyError:
            # Acontece quando buscamos uma chave que não existe em um dicionário
            logPrioridade(f"API => buscaAdvPor ____________________PATCH</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return False
        except Exception as erro:
            print(f'loginAuthFromCache - Exception: {type(erro)}')
            logPrioridade(f"API => buscaAdvPor ____________________PATCH</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, priodiade=Prioridade.saidaImportante)
            return False






