import os
import json
from modelos.advogadoModelo import AdvogadoModelo


class CacheLogin:

    def __init__(self):
        self.pathLoginTxt = os.path.join(os.getcwd(), 'cache', '.login.txt')
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
