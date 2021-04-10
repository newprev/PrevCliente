import sqlite3

from connections import ConfigConnection
from Daos.tabelas import TabelasConfig
from helpers import dinheiroToFloat, datetimeToSql
from modelos.convMonModelo import ConvMonModelo
from modelos.tetosPrevModelo import TetosPrevModelo
from logs import *
from datetime import datetime


class DaoInfoImportante:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()
        self.tabelas = TabelasConfig()

    def insereListaTetos(self, tetosDict: dict, deletarTabela: bool = False):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.tabelas.tblTetosPrev}
            (
                dataValidade, valor, dataCAdastro, dataUltAlt
            )
            VALUES """

        for index in range(0, len(tetosDict['valor'])):
            if index == 0:
                strComando += f"""
            (
                '{tetosDict['data'][index]}', {tetosDict['valor'][index]}"""
            else:
                strComando += f""",
            (
                '{tetosDict['data'][index]}', {tetosDict['valor'][index]}"""

            if isinstance(self.db, sqlite3.Connection):
                strComando += f""", '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}' 
            )"""
            else:
                strComando += f""", NOW(), NOW()
            )"""

        try:
            if deletarTabela:
                self.deletarTabela(commitar=False)

            cursor.execute(strComando)
            tetosPrevId = cursor.lastrowid
            logPrioridade(f'INSERT<insereListaTetos>___________________{self.tabelas.tblTetosPrev} ({tetosPrevId})', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - atualizaTetos({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereTeto(self, tetoDict: dict):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.tabelas.tblTetosPrev}
            (
                dataValidade, valor
            )
            VALUES 
            (
                '{tetoDict['data']}', {tetoDict['valor']}
            )"""

        try:
            cursor.execute(strComando)
            tetoPrevId = cursor.lastrowid
            logPrioridade(f'INSERT<insereTeto>___________________{self.tabelas.tblTetosPrev} ({tetoPrevId})', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - atualizaTetos({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereConvMon(self, convMon: ConvMonModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.tabelas.tblConvMon}
            (
                nomeMoeda, fator, dataInicial, 
                dataFinal, conversao, moedaCorrente, 
                dataUltAlt, dataCadastro
            )
            VALUES 
            (
                '{convMon.nomeMoeda}', {convMon.fator}, '{convMon.dataInicial}',
                '{convMon.dataFinal}', '{convMon.conversao}', {convMon.moedaCorrente}"""

        if isinstance(self.db, sqlite3.Connection):
            strComando += f""", '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
            )"""
        else:
            strComando += f""",
                NOW(), NOW()
            )"""

        try:

            cursor.execute(strComando)
            convMonId = cursor.lastrowid
            logPrioridade(f'INSERT<insereConvMon>___________________{self.tabelas.tblConvMon} ({convMonId})', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - insereConvMon({self.config.banco}) <INSERT {self.tabelas.tblConvMon}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def atualizaTeto(self, tetoModel: TetosPrevModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            UPDATE {self.tabelas.tblTetosPrev} SET
                dataValidade = '{tetoModel.data}',
                valor = {dinheiroToFloat(tetoModel.valor)},
                dataUltAlt = NOW()
            WHERE 
                tetosPrevId = {tetoModel.tetosPrevId}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'UPDATE<atualizaTeto>___________________{self.tabelas.tblTetosPrev} ({tetoModel.tetosPrevId})', TipoEdicao.update, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - atualizaTeto({self.config.banco}) <UPDATE {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def deletaTetoById(self, tetoPrevId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            DELETE FROM {self.tabelas.tblTetosPrev}
            WHERE
                tetosPrevId = {tetoPrevId}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'UPDATE<deletaTetoById>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.update, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - atualizaTeto({self.config.banco}) <UPDATE {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def deletarTabela(self, commitar: bool = True):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"DELETE FROM {self.tabelas.tblTetosPrev};"

        try:
            cursor.execute(strComando)
            logPrioridade(f'DELETE<deletarTabela>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.delete, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - deletarTabela({self.config.banco}) <DELETE {self.tabelas.tblTetosPrev}>')
        finally:
            if commitar:
                self.db.commit()
                self.disconectBD(cursor)
            else:
                self.db.commit()
                cursor.close()

    def getAllTetos(self):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT tetosPrevId, dataValidade, valor FROM {self.tabelas.tblTetosPrev} ORDER BY dataValidade DESC"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getAllTetos>___________________{self.tabelas.tblTetosPrev};', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getAllTetos({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.disconectBD(cursor)

    def getConvMonByNomeMoeda(self, nomeMoeda: str):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()

        cursor = self.db.cursor()

        strComando = f"""
            SELECT 
                convMonId, nomeMoeda, fator, 
                dataInicial, dataFinal, conversao, 
                moedaCorrente, dataUltAlt, dataCadastro 
            FROM {self.tabelas.tblConvMon}
            WHERE
                nomeMoeda = '{nomeMoeda}'"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getConvMonByNomeMoeda>___________________{self.tabelas.tblConvMon}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchone()
        except:
            raise Warning(f'Erro SQL - getConvMonByNomeMoeda({self.config.banco}) <INSERT {self.tabelas.tblConvMon}>')
        finally:
            self.disconectBD(cursor)

    def getAllMoedas(self):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT convMonId, nomeMoeda, fator, dataInicial, dataFinal, conversao, moedaCorrente 
                FROM {self.tabelas.tblConvMon} ORDER BY dataFinal DESC"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getAllMoedas>___________________{self.tabelas.tblConvMon}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getAllTetos({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()