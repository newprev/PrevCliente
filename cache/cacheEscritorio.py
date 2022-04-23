import datetime
import os
import json
from logging import info, warning, error

from playhouse.shortcuts import model_to_dict

from util.enums.newPrevEnums import *
from util.enums.logEnums import TipoLog
from modelos.escritoriosORM import Escritorios


class CacheEscritorio:

    def __init__(self):
        self.pathEscritorioTxt = os.path.join(os.getcwd(), 'cache', '.escritorio.json')
        self.pathEscritorioTempTxt = os.path.join(os.getcwd(), 'cache', '.escritorio.temp.json')
        self.pathCache = os.path.join(os.getcwd(), 'cache')

    def salvarCache(self, escritorio: Escritorios) -> bool:
        jsonEscritorio = json.dumps(pyToDefault(model_to_dict(escritorio, recurse=False)))
        info(f'{TipoLog.Cache.value}::salvarCache')

        try:
            with open(self.pathEscritorioTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonEscritorio)
            return True
        except Exception as err:
            print(f'salvarCache({type(err)}) - {err}')
            error(f'{TipoLog.Cache.value}::salvarCache', extra={"err": err})

    def carregarCache(self) -> Escritorios:
        info(f'{TipoLog.Cache.value}::carregarCache')

        if '.escritorio.json' in os.listdir(self.pathCache):
            with open(self.pathEscritorioTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)

            return Escritorios().fromDict(advJson)

        else:
            return Escritorios()

    def carregarCacheTemporario(self) -> Escritorios:
        info(f'{TipoLog.Cache.value}::carregarCache')

        if '.escritorio.temp.json' in os.listdir(self.pathCache):
            with open(self.pathEscritorioTempTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return Escritorios().fromDict(advJson)

        else:
            return Escritorios()

    def limpaTemporarios(self):
        for temp in os.listdir(self.pathCache):
            if temp.endswith('escritorio.temp.json'):
                os.remove(os.path.join(self.pathCache, temp))

    def salvarCacheTemporario(self, escritorio: Escritorios) -> bool:
        info(f'{TipoLog.Cache.value}::salvarCacheTemporario')
        jsonAdv = json.dumps(escritorio.toDict())

        try:
            with open(self.pathEscritorioTempTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonAdv)
            return True
        except Exception as err:
            error(f'{TipoLog.Cache.value}::salvarCacheTemporario', extra={"err": err})

    def limpaCache(self):
        self.limpaTemporarios()
        for f in os.listdir(self.pathCache):
            if f.endswith('escritorio.json'):
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