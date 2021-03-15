from connections import ConfigConnection


class DaoConfiguracoes:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()

    def criaTabela(self, scriptCreate: str = None):

        self.db.connect()
        cursor = self.db.cursor()
        response = True

        try:
            cursor.execute(scriptCreate)
        except:
            raise Warning(f'Erro SQL - criaTabela({self.config.banco}) <SELECT {scriptCreate}>')
        finally:
            self.disconectBD(cursor)
            return response

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()