import os
import json
from modelos.advogadoModelo import AdvogadoModelo


class CacheLogin:

    def __init__(self):
        self.pathLoginTxt = os.path.join(os.getcwd(), 'cache', '.login.txt')
        self.pathLoginTempTxt = os.path.join(os.getcwd(), 'cache', '.login.temp.txt')
        self.pathCache = os.path.join(os.getcwd(), 'cache')

    def salvarCache(self, advogado: AdvogadoModelo) -> bool:
        jsonAdv = json.dumps(advogado.toDict())

        try:
            with open(self.pathLoginTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonAdv)
            return True
        except Exception:
            print('Deu Bosta')

    def carregarCache(self) -> AdvogadoModelo:
        if '.login.txt' in os.listdir(self.pathCache):
            with open(self.pathLoginTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return AdvogadoModelo().fromDict(advJson)

        else:
            return AdvogadoModelo()

    def carregarCacheTemporario(self) -> AdvogadoModelo:
        if '.login.temp.txt' in os.listdir(self.pathCache):
            with open(self.pathLoginTempTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)
                return AdvogadoModelo().fromDict(advJson)

        else:
            return AdvogadoModelo()

    def limpaTemporarios(self):
        for temp in os.listdir(self.pathCache):
            if temp.endswith('temp.txt'):
                os.remove(os.path.join(self.pathCache, temp))

    def salvarCacheTemporario(self, advogado: AdvogadoModelo) -> bool:
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
