import os
import json
from logs import logPrioridade
from newPrevEnums import *
from modelos.escritorioModelo import EscritorioModelo


class CacheEscritorio:

    def __init__(self):
        self.pathEscritorioTxt = os.path.join(os.getcwd(), 'cache', '.escritorio.txt')
        self.pathEscritorioTempTxt = os.path.join(os.getcwd(), 'cache', '.escritorio.temp.txt')
        self.pathCache = os.path.join(os.getcwd(), 'cache')

    def salvarCache(self, advogado: EscritorioModelo) -> bool:
        jsonAdv = json.dumps(advogado.toDict())

        try:
            with open(self.pathEscritorioTxt, encoding='utf-8', mode='w') as cacheLogin:
                cacheLogin.write(jsonAdv)
            logPrioridade(f'salvarCache<CacheEscritorio>___________________', TipoEdicao.insert, Prioridade.saidaComun)
            return True
        except Exception as erro:
            print(f'salvarCache({type(erro)}) - {erro}')
            logPrioridade(f'salvarCache<CacheEscritorio> ({type(erro)})___________________', TipoEdicao.erro, Prioridade.saidaImportante)

    def carregarCache(self) -> EscritorioModelo:
        if '.login.txt' in os.listdir(self.pathCache):
            with open(self.pathEscritorioTxt, encoding='utf-8', mode='r') as cacheLogin:
                advJson = json.load(cacheLogin)

            logPrioridade(f'carregarCache<CacheEscritorio>___________________', TipoEdicao.select, Prioridade.saidaComun)
            return EscritorioModelo().fromDict(advJson)

        else:
            return EscritorioModelo()