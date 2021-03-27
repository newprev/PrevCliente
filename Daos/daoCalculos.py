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
        SELECT contribuicoesId, seq, competencia, salContribuicao, 'Contribuição', indicadores FROM {self.config.tblCnisContribuicoes} con
            WHERE clienteId = {clienteId}
        UNION ALL
        SELECT remuneracoesId, seq, competencia, remuneracao, 'Remuneração', indicadores FROM {self.config.tblCnisRemuneracoes} rem
            WHERE clienteId = {clienteId}
        ORDER BY competencia;"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getRemECon({self.config.tblCnisRemuneracoes}, {self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def contaContribuicoes(self, clienteId: int):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT COUNT(*) FROM {self.config.tblCnisContribuicoes} WHERE clienteId = {clienteId}"""

        try:
            cursor.execute(strComando)
            return cursor.fetchone()
        except:
            raise Warning(f'Erro SQL - contaContribuicoes({self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def contaRemuneracoes(self, clienteId: int):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT COUNT(*) FROM {self.config.tblCnisRemuneracoes} WHERE clienteId = {clienteId}"""

        try:
            cursor.execute(strComando)
            return cursor.fetchone()
        except:
            raise Warning(f'Erro SQL - contaRemuneracoes({self.config.tblCnisRemuneracoes}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()