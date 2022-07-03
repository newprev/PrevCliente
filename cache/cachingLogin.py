import os
import json
from logging import info, warning, error

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade
from util.helpers.helpers import pyToDefault
from modelos.advogadoORM import Advogados
from playhouse.shortcuts import model_to_dict


class CacheLogin:

    def __init__(self):
        self.pathLoginTxt = os.path.join(os.getcwd(), 'cache', '.login.json')
        self.pathLoginTempTxt = os.path.join(os.getcwd(), 'cache', '.login.temp.json')
        self.pathCache = os.path.join(os.getcwd(), 'cache')

    def salvarCache(self, advogado: Advogados) -> bool:
        # pyToDefault transforma os objetos datetime em str para serem inseridos no json
        jsonAdv = json.dumps(pyToDefault(model_to_dict(advogado, recurse=False)))

        try:
            with open(self.pathLoginTxt, encoding='utf-8', mode='w') as cacheLogin:
                info(f'{TipoLog.Cache.value}::salvarCache')
                cacheLogin.write(jsonAdv)
            return True
        except Exception as err:
            error(f'{TipoLog.Cache.value}::salvarCache', extra={"err": err})

    def carregarCache(self) -> Advogados:
        if '.login.json' in os.listdir(self.pathCache):
            with open(self.pathLoginTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return Advogados().fromDict(advJson)

        else:
            return Advogados()

    def carregarCacheTemporario(self) -> Advogados:
        if '.login.temp.json' in os.listdir(self.pathCache):
            with open(self.pathLoginTempTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return Advogados().fromDict(advJson)

        else:
            return Advogados()

    def limpaTemporarios(self):
        for temp in os.listdir(self.pathCache):
            if temp.endswith('temp.json'):
                os.remove(os.path.join(self.pathCache, temp))

    def salvarCacheTemporario(self, advogado: Advogados) -> bool:
        jsonAdv = json.dumps(advogado.toDict())

        try:
            with open(self.pathLoginTempTxt, encoding='utf-8', mode='w') as cacheLogin:
                info(f'{TipoLog.Cache.value}::salvarCacheTemporario')
                cacheLogin.write(jsonAdv)
            return True
        except Exception as err:
            error(f'{TipoLog.Cache.value}salvarCacheTemporario', extra={"err": err})

    def limpaCache(self):
        self.limpaTemporarios()
        for temp in os.listdir(self.pathCache):
            if temp.endswith('login.json'):
                os.remove(os.path.join(self.pathCache, temp))
