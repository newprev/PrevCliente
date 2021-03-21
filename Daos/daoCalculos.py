from datetime import datetime

from Daos.tabelas import TabelasConfig
from connections import ConfigConnection
from helpers import mascaraDataSql
from modelos.clienteModelo import ClienteModelo
from pymysql import connections, cursors
import pprint


class DaoCalculos:

    def __init__(self, db: connections=None):
        self.db = db
        self.config = TabelasConfig()

    def getRemECon(self, clienteId: int):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
        SELECT contribuicoesId, seq, competencia, salContribuicao, indicadores, 'Contribuição' FROM {self.config.tblCnisContribuicoes} con
            WHERE clienteId = {clienteId}
        UNION ALL
        SELECT remuneracoesId, seq, competencia, remuneracao, indicadores, 'Remuneração' FROM {self.config.tblCnisRemuneracoes} rem
            WHERE clienteId = {clienteId};"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getRemECon({self.config.tblCnisRemuneracoes}, {self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()