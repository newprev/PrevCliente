from connections import ConfigConnection


class DaoConfiguracoes:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()

    def criaTabela(self, scriptCreate: str):

        self.db.connect()
        cursor = self.db.cursor()

        try:
            if cursor.execute(scriptCreate) == 1:
                return True
            else:
                return False
        except:
            raise Warning(f'Erro SQL - criaTabela({self.config.banco}) <SELECT {scriptCreate}>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()