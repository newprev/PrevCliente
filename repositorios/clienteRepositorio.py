import json

import requests as http
from systemLog.logs import logPrioridade
from typing import List
from playhouse.shortcuts import dict_to_model, model_to_dict

from util.enums.newPrevEnums import *
from util.enums.logEnums import TipoLog
from util.enums.configEnums import TipoConexao
from Configs.systemConfig import buscaSystemConfigs

from modelos.advogadoORM import Advogados
from modelos.escritoriosORM import Escritorios
from modelos.Auth.ClientAuthModelo import ClientAuthModelo
from repositorios.escritorioRepositorio import EscritorioRepositorio


class UsuarioRepository:
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

    def confirmaAlteraSenha(self, senha: str, advogadoId: int) -> bool:
        url: str = self.baseUrl + 'advogados/'
        testeJson = json.dumps({
            "senhaEnviada": senha,
            "advogadoId": advogadoId
        })

        response = http.patch(url, data=testeJson, headers=self.header)

        if 199 < response.status_code < 400:
            logPrioridade(
                f"API => confirmaAlteraSenha ____________________PATCH<advogados/>:::{url}",
                tipoEdicao=TipoEdicao.api,
                tipoLog=TipoLog.Rest,
                priodiade=Prioridade.saidaComum,
            )
            return True
        else:
            logPrioridade(
                f"API [{response.status_code}]=> confirmaAlteraSenha ____________________PATCH<advogados/>:::{url}",
                tipoEdicao=TipoEdicao.api,
                tipoLog=TipoLog.Rest,
                priodiade=Prioridade.saidaComum,
            )
            return False

    def buscaCpfEmailPrimeiroAcesso(self, cpfEmail: str, esqueceuSenha: bool = False) -> int:
        url: str = self.baseUrl + 'advogados/auth/trocaSenha/'

        body: dict = {
            'info': cpfEmail,
            'esqueceuSenha': esqueceuSenha
        }

        logPrioridade(f"API => buscaEscritorioPrimeiroAcesso ____________________GET<advogados/auth/primeiroAcesso/>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
        response = http.post(url, data=body)

        if 199 < response.status_code < 400:
            clienteId: int = response.json()['advogadoId']
            return clienteId
        else:
            logPrioridade(f"API [{response.status_code}]=> buscaEscritorioPrimeiroAcesso ____________________GET<advogados/auth/primeiroAcesso/>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest,
                          priodiade=Prioridade.saidaComum)
            return -1

    def verificaCodAcesso(self, codAcesso: int) -> bool:
        url: str = self.baseUrl + 'advogados/auth/autenticaCodAcesso/'

        body: dict = {
            'codigo': codAcesso
        }

        response = http.patch(url, data=body)

        if 199 < response.status_code < 400:
            logPrioridade(
                f"API => buscaEscritorioPrimeiroAcesso ____________________GET<api/advogados/primeirosAcessos/<int:cdAcesso>>:::{url}",
                tipoEdicao=TipoEdicao.api,
                tipoLog=TipoLog.Rest,
                priodiade=Prioridade.saidaComum,
            )
            return True
        else:
            logPrioridade(
                f"API [{response.status_code}]=> buscaEscritorioPrimeiroAcesso ____________________GET<advogados/auth/primeiroAcesso/>:::{url}",
                tipoEdicao=TipoEdicao.api,
                tipoLog=TipoLog.Rest,
                priodiade=Prioridade.saidaComum,
            )

    def buscaEscritorioById(self, escritorioId: int) -> Escritorios:
        # TODO: Criar função que faz um GET buscando o escritório pelo Id
        pass

    def buscaAdvNaoCadastrados(self, escritorioId) -> list:
        url: str = self.baseUrl + f'escritorio/{escritorioId}/advogado?confirmado=false&ativo=true&ordering=login'

        response = http.get(url)

        if 199 < response.status_code < 400:
            listaAdvogadosJson: list = response.json()
            listaObjAdv: List[Advogados] = [dict_to_model(Advogados, adv, ignore_unknown=True) for adv in listaAdvogadosJson]

            logPrioridade(f"API => buscaAdvNaoCadastrados ____________________GET<escritorio/<escritorioId>/advogado:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
            return listaObjAdv
        else:
            logPrioridade(f"API => buscaAdvNaoCadastrados ____________________GET<escritorio/<escritorioId>/advogado/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
            return []

    def buscaSenhaProvisoria(self, usuarioId: int) -> dict:
        url: str = self.baseUrl + f'advogados/{usuarioId}/confirmacao/'

        response = http.get(url)

        if 199 < response.status_code < 400:
            advogadoSenha: dict = response.json()

            logPrioridade(f"API => buscaSenhaProvisoria ____________________GET<advogado/<int:id>/confirmacao>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
            return advogadoSenha
        else:
            logPrioridade(f"API => buscaSenhaProvisoria GET<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
            return {"erro": response.json()}

    def buscaSenhaDefinitiva(self, usuarioId: int) -> dict:
        url: str = self.baseUrl + f'advogados/{usuarioId}/confirmacao/'

        response = http.get(url)

        if 199 < response.status_code < 400:
            advogadoSenha: dict = response.json()

            if advogadoSenha['confirmado']:
                logPrioridade(f"API => buscaSenhaDefinitiva ____________________GET<advogado/<int:id>/confirmacao>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
                return advogadoSenha
            else:
                logPrioridade(f"API => buscaSenhaDefinitiva GET<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                return {"erro": response.json()}
        else:
            logPrioridade(f"API => buscaSenhaDefinitiva GET<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
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

            logPrioridade(f"API => atualizaSenha ____________________PATCH<advogado/<int:id>/confirmacao>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
            return senha
        else:
            logPrioridade(f"API => atualizaSenha ____________________PATCH<advogado/<int:id>/confirmacao/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
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
                else:
                    advogado.senha = 'senhaProvisoria'

                Advogados.insert(advogado.toDict()).on_conflict_replace().execute()

                if not advogado:
                    logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                    return False
                else:
                    logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
                    return advogado
            else:
                logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                return False
        except Escritorios.DoesNotExist:
            escritorio: Escritorios = EscritorioRepositorio().buscaEscritorio(escritorioId)
            Escritorios.insert(escritorio.toDict()).on_conflict_replace().execute()
            return self.buscaAdvPor(advogadoId, senhaInserida=senhaInserida)

        except Exception as erro:
            print(f'buscaAdvPor - Erro: {type(erro)}')
            logPrioridade(f"API => buscaAdvPor ____________________GET<advogados/<int:id>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)

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
                    logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                    return None
                else:

                    try:
                        advogadoALogar = Advogados.get_by_id(advAuth.advogadoId)
                    except Advogados.DoesNotExist:
                        logPrioridade(f"API => buscaAdvPor ____________________GET<Advogados.DoesNotExist>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                        advogadoALogar = self.buscaAdvPor(advAuth.advogadoId, senhaInserida=advAuth.senha)

                    advogadoALogar.senha = senha
                    if advAuth == advogadoALogar:
                        logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
                        return advogadoALogar
                    else:
                        logPrioridade(f"API => buscaAdvPor ____________________GET<Autenticação não confere com o advogado em questão>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                        return None
            else:
                logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                return None
        except AttributeError as erro:
            print(f'loginAuth - AttributeError: {erro}')
            logPrioridade(f"API => buscaAdvPor (AttributeError)____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
            return None
        except Exception as erro:
            print(f'loginAuth - Exception: {type(erro)}')
            logPrioridade(f"API => buscaAdvPor ____________________GET</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
            return None

    def loginAuthFromCache(self, advogado: Advogados) -> bool:
        url: str = self.baseUrl + f'advogados/auth/{advogado.numeroOAB}'

        try:
            response = http.get(url)

            if 199 < response.status_code < 400:
                auth: ClientAuthModelo = ClientAuthModelo().fromDict(response.json())

                if auth is not None and auth == advogado:
                    logPrioridade(f"API => loginAuthFromCache ____________________GET</advogados/auth/<str:numeroOAB>>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaComum)
                    return True
                else:
                    logPrioridade(f"API => loginAuthFromCache ____________________GET</advogados/auth/<str:numeroOAB>/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
                    return False
        except KeyError:
            # Acontece quando buscamos uma chave que não existe em um dicionário
            logPrioridade(f"API => buscaAdvPor ____________________PATCH</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
            return False
        except Exception as erro:
            print(f'loginAuthFromCache - Exception: {type(erro)}')
            logPrioridade(f"API => buscaAdvPor ____________________PATCH</advogados/auth/Erro>:::{url}", tipoEdicao=TipoEdicao.api, tipoLog=TipoLog.Rest, priodiade=Prioridade.saidaImportante)
            return False






