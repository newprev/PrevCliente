from connections import ConfigConnection
from helpers import dictIndicadores, dictEspecies
from Daos.tabelas import TabelasConfig
from logs import *


class DaoConfiguracoes:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()
        self.tabelas = TabelasConfig()

    def criaTabela(self, scriptCreate: str = None, nomeTabela: str = None):

        self.db.connect()
        cursor = self.db.cursor()
        response = True

        try:
            cursor.execute(scriptCreate)
            logPrioridade(f'CREATE<criaTabela>___________________{nomeTabela}', TipoEdicao.createTable, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - criaTabela({self.config.banco}) <CREATE {scriptCreate}>')
        finally:
            self.disconectBD(cursor)
            return response

    def verificaTblIndicadores(self):
        self.db.connect()
        cursor = self.db.cursor()
        indicadores = dictIndicadores

        strComando = f"""
            INSERT INTO {self.tabelas.tblIndicadores} 
                (
                    indicadoresId, descricao
                )
            VALUES """

        i = 0
        for sigla, descricao in indicadores.items():
            if i == 0:
                strComando += f"""\n ('{sigla}', '{descricao}')"""
            else:
                strComando += f""", \n('{sigla}', '{descricao}')"""
            i += 1

        try:
            cursor.execute(f"""DELETE FROM {self.tabelas.tblIndicadores}""")
            cursor.execute(strComando)
            logPrioridade(f'INSERT<verificaTblIndicadores>___________________{self.tabelas.tblIndicadores}', TipoEdicao.insert, Prioridade.saidaComun)

        except:
            raise Warning(f'Erro SQL - verificaTblIndicadores({self.config.banco}) <INSERT {self.tabelas.tblIndicadores}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def verificaTblEspecieBenef(self):
        self.db.connect()
        cursor = self.db.cursor()
        especieBenef = dictEspecies

        strComando = f"""
            INSERT INTO {self.tabelas.tblEspecieBenef} 
                (
                    especieId, descricao
                )
            VALUES """

        i = 0
        for sigla, descricao in especieBenef.items():
            if i == 0:
                strComando += f"""\n ('{sigla}', '{descricao}')"""
            else:
                strComando += f""", \n('{sigla}', '{descricao}')"""
            i += 1

        try:
            cursor.execute(f"""DELETE FROM {self.tabelas.tblEspecieBenef}""")
            logPrioridade(f'DELETE<verificaTblEspecieBenef>___________________{self.tabelas.tblEspecieBenef}', TipoEdicao.delete, Prioridade.saidaComun)
            cursor.execute(strComando)
            logPrioridade(f'INSERT<verificaTblEspecieBenef>___________________{self.tabelas.tblEspecieBenef}', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - verificaTblEspecieBenef({self.config.banco}) <INSERT {self.tabelas.tblEspecieBenef}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()