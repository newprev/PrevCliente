import datetime
import os
import json

from logs import logPrioridade
from playhouse.shortcuts import model_to_dict

from modelos.escritoriosORM import Escritorios
from newPrevEnums import *
from modelos.escritorioModelo import EscritorioModelo


class CacheEscritorio:

    def __init__(self):
        self.pathEscritorioTxt = os.path.join(os.getcwd(), 'cache', '.escritorio.txt')
        self.pathEscritorioTempTxt = os.path.join(os.getcwd(), 'cache', '.escritorio.temp.txt')
        self.pathCache = os.path.join(os.getcwd(), 'cache')

    def salvarCache(self, escritorio: Escritorios) -> bool:
        jsonEscritorio = json.dumps(pyToDefault(model_to_dict(escritorio, recurse=False)))
        # jsonAdv = json.dumps(escritorio.toDict())

        try:
            with open(self.pathEscritorioTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonEscritorio)
            logPrioridade(f'salvarCache<CacheEscritorio>___________________', TipoEdicao.insert, Prioridade.saidaComun)
            return True
        except Exception as erro:
            print(f'salvarCache({type(erro)}) - {erro}')
            logPrioridade(f'salvarCache<CacheEscritorio> ({type(erro)})___________________', TipoEdicao.erro, Prioridade.saidaImportante)

    def carregarCache(self) -> Escritorios:
        if '.escritorio.txt' in os.listdir(self.pathCache):
            with open(self.pathEscritorioTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)

            logPrioridade(f'carregarCache<CacheEscritorio>___________________', TipoEdicao.select, Prioridade.saidaComun)
            return Escritorios().fromDict(advJson)

        else:
            return Escritorios()

    def carregarCacheTemporario(self) -> EscritorioModelo:
        if '.escritorio.temp.txt' in os.listdir(self.pathCache):
            with open(self.pathEscritorioTempTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return EscritorioModelo().fromDict(advJson)

        else:
            return EscritorioModelo()

    def limpaTemporarios(self):
        for temp in os.listdir(self.pathCache):
            if temp.endswith('escritorio.temp.txt'):
                os.remove(os.path.join(self.pathCache, temp))

    def salvarCacheTemporario(self, escritorio: EscritorioModelo) -> bool:
        jsonAdv = json.dumps(escritorio.toDict())

        try:
            with open(self.pathEscritorioTempTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonAdv)
            return True
        except Exception as erro:
            print(f'salvarCacheTemporario({type(erro)} - {erro})')

    def limpaCache(self):
        self.limpaTemporarios()
        for f in os.listdir(self.pathCache):
            if f.endswith('escritorio.txt'):
                os.remove(os.path.join(self.pathCache, f))


# Essa função está aqui para evitar importação circular. Ela é uma cópia da função que está no arquivo "PrevCliente/helpers.py"
def pyToDefault(dicionario: dict) -> dict:
    dictReturn: dict = dict()
    for chave, valor in dicionario.items():
        if isinstance(valor, datetime.datetime):
            dictReturn[chave] = valor.strftime('%Y-%m-%d')
        elif isinstance(valor, datetime.date):
            dictReturn[chave] = valor.strftime('%Y-%m-%d')
        else:
            dictReturn[chave] = valor

    return dictReturn