import os
import json

from util.helpers import pyToDefault
from modelos.advogadoORM import Advogados
from playhouse.shortcuts import model_to_dict


class CacheLogin:

    def __init__(self):
        self.pathLoginTxt = os.path.join(os.getcwd(), 'cache', '.login.txt')
        self.pathLoginTempTxt = os.path.join(os.getcwd(), 'cache', '.login.temp.txt')
        self.pathCache = os.path.join(os.getcwd(), 'cache')

    def salvarCache(self, advogado: Advogados) -> bool:
        # pyToDefault transforma os objetos datetime em str para serem inseridos no json
        jsonAdv = json.dumps(pyToDefault(model_to_dict(advogado, recurse=False)))

        try:
            with open(self.pathLoginTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonAdv)
            return True
        except Exception:
            print('Deu Bosta')

    def carregarCache(self) -> Advogados:
        if '.login.txt' in os.listdir(self.pathCache):
            with open(self.pathLoginTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return Advogados().fromDict(advJson)

        else:
            return Advogados()

    def carregarCacheTemporario(self) -> Advogados:
        if '.login.temp.txt' in os.listdir(self.pathCache):
            with open(self.pathLoginTempTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return Advogados().fromDict(advJson)

        else:
            return Advogados()

    def limpaTemporarios(self):
        for temp in os.listdir(self.pathCache):
            if temp.endswith('temp.txt'):
                os.remove(os.path.join(self.pathCache, temp))

    def salvarCacheTemporario(self, advogado: Advogados) -> bool:
        jsonAdv = json.dumps(advogado.toDict())

        try:
            with open(self.pathLoginTempTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonAdv)
            return True
        except Exception as erro:
            print(f'salvarCacheTemporario({type(erro)} - {erro})')

    def limpaCache(self):
        self.limpaTemporarios()
        for temp in os.listdir(self.pathCache):
            if temp.endswith('login.txt'):
                os.remove(os.path.join(self.pathCache, temp))
