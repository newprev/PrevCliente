from connections import ConfigConnection
from Daos.tabelas import TabelasConfig


class DaoInfoImportante:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()

    def atualizaTetos(self):
        self.db.connect()
        cursor = self.db.cursor()
        
        strComando = f""""""

        try:
            cursor.execute(strComando)
        except:
            raise Warning(f'Erro SQL - atualizaTetos({self.config.banco}) <INSERT {TabelasConfig.tblEspecieBenef}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()

