import sqlite3

from connections import ConfigConnection
from Daos.tabelas import TabelasConfig
from helpers import datetimeToSql
from logs import TipoEdicao, Prioridade, logPrioridade
from modelos.convMonModelo import ConvMonModelo
from modelos.tetosPrevModelo import TetosPrevModelo
from datetime import datetime


class DaoFerramentas:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()
        self.tabelas = TabelasConfig()

    def insereDictListaTetos(self, tetosDict: dict, deletarTabela: bool = False):

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
            logPrioridade(f'INSERT<insereDictListaTetos>___________________{self.tabelas.tblTetosPrev} ({tetosPrevId})', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - atualizaTetos({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereListaTetos(self, tetos: list, deletarTabela: bool = False):

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

        for teto in tetos:
            if teto == tetos[0]:
                strComando += f"""
            (
                '{teto.dataValidade}', {teto.valor}"""
            else:
                strComando += f""",
            (
                '{teto.dataValidade}', {teto.valor}"""

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
            logPrioridade(f'INSERT<insereListaTetos>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - atualizaTetos({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereListaTetosModel(self, tetosModel: list):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.tabelas.tblTetosPrev}
            (
                dataValidade, valor, dataCAdastro, 
                dataUltAlt
            )
            VALUES """

        for index in range(0, len(tetosModel)):
            if index == 0:
                strComando += f"""
            (
                '{tetosModel[index].dataValidade}', {tetosModel[index].valor}, '{datetime.now()}', 
                '{datetime.now()}'
            )"""
            else:
                strComando += f""",
            (
                '{tetosModel[index].dataValidade}', {tetosModel[index].valor}, '{datetime.now()}', 
                '{datetime.now()}'
            )"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereListaTetosModel>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - insereListaTetosModel({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereListaConvMonModel(self, convMons: list):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.tabelas.tblConvMon}
            (
                nomeMoeda, fator, dataInicial, 
                dataFinal, conversao, moedaCorrente, 
                sinal, dataUltAlt, dataCadastro
            )
            VALUES  """

        for convMon in convMons:
            if convMon == convMons[0]:
                strComando += f"""
            (
                '{convMon.nomeMoeda}', {convMon.fator}, '{convMon.dataInicial}',
                '{convMon.dataFinal}', '{convMon.conversao}', {convMon.moedaCorrente}, 
                '{convMon.sinal}', '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
            )"""
            else:
                strComando += f""",
            (
                '{convMon.nomeMoeda}', {convMon.fator}, '{convMon.dataInicial}',
                '{convMon.dataFinal}', '{convMon.conversao}', {convMon.moedaCorrente}, 
                '{convMon.sinal}', '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
            )"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereListaConvMonModel>___________________{self.tabelas.tblConvMon}', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            logPrioridade(f'INSERT<insereListaConvMonModel>___________________{self.tabelas.tblConvMon}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - insereListaTetosModel({self.config.banco}) <INSERT {self.tabelas.tblConvMon}>')
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
                dataValidade, valor, dataUltAlt,
                dataCadastro
            )
            VALUES 
            (
                '{tetoDict['dataValidade']}', {tetoDict['valor']}, '{datetime.now()}',
                '{datetime.now()}'
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
                sinal, dataUltAlt, dataCadastro
            )
            VALUES 
            (
                '{convMon.nomeMoeda}', {convMon.fator}, '{convMon.dataInicial}',
                '{convMon.dataFinal}', '{convMon.conversao}', {convMon.moedaCorrente}, 
                '{convMon.sinal}', '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
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
                dataValidade = '{tetoModel.dataValidade}',
                valor = {tetoModel.valor},
                dataUltAlt = '{datetime.now()}'
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
            logPrioridade(f'DELETE<deletaTetoById>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.update, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - deletaTetoById({self.config.banco}) <DELETE {self.tabelas.tblTetosPrev}>')
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

        strComando = f"""
            SELECT 
                tetosPrevId, dataValidade, valor                
                FROM {self.tabelas.tblTetosPrev} 
            ORDER BY dataValidade DESC"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getAllTetos>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchall()
        except:
            logPrioridade(f'Erro SQL - getAllTetos({self.config.banco}) <INSERT {self.tabelas.tblTetosPrev}>', TipoEdicao.erro, Prioridade.saidaImportante)
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
                moedaCorrente, sinal, dataUltAlt, dataCadastro 
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

    def atualizaConvMon(self, convMon: ConvMonModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            UPDATE {self.tabelas.tblConvMon} 
                SET
                    nomeMoeda = '{convMon.nomeMoeda}',
                    fator = {convMon.fator},
                    dataInicial = '{convMon.dataInicial}',
                    dataFinal = '{convMon.dataFinal}',
                    conversao = '{convMon.conversao}',
                    moedaCorrente = {convMon.moedaCorrente},
                    sinal = '{convMon.sinal}',
                    dataUltAlt = '{datetimeToSql(datetime.now())}'
            WHERE
                convMonId = {convMon.convMonId}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'UPDATE<atualizaConvMon>___________________{self.tabelas.tblConvMon}', TipoEdicao.update, Prioridade.saidaComun)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - atualizaConvMon({self.config.banco}) <UPDATE {self.tabelas.tblConvMon}>')
        finally:
            self.disconectBD(cursor)

    def contaQtdMoedas(self) -> int:

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT COUNT(*) FROM {self.tabelas.tblConvMon}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<contaQtdMoedas>___________________{self.tabelas.tblConvMon}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchone()[0]
        except:
            raise Warning(f'Erro SQL - contaQtdMoedas({self.config.banco}) <SELECT {self.tabelas.tblConvMon}>')
        finally:
            self.disconectBD(cursor)

    def contaQtdTetos(self) -> int:

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
               SELECT COUNT(*) FROM {self.tabelas.tblTetosPrev}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<contaQtdTetos>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchone()[0]
        except:
            raise Warning(f'Erro SQL - contaQtdTetos({self.config.banco}) <SELECT {self.tabelas.tblTetosPrev}>')
        finally:
            self.disconectBD(cursor)

    def deletarConvMon(self):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
               DELETE FROM {self.tabelas.tblConvMon}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'DELETE<deletarConvMon>___________________{self.tabelas.tblConvMon}', TipoEdicao.delete, Prioridade.saidaComun)
        except:
            logPrioridade(f'Erro SQL - deletarConvMon({self.config.banco}) <DELETE {self.tabelas.tblTetosPrev}>', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - deletarConvMon({self.config.banco}) <DELETE {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def deletarTetosPrev(self):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
               DELETE FROM {self.tabelas.tblTetosPrev}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'DELETE<deletarTetosPrev>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.delete, Prioridade.saidaComun)
        except:
            logPrioridade(f'Erro SQL - deletarTetosPrev({self.config.banco}) <DELETE {self.tabelas.tblTetosPrev}>', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - deletarTetosPrev({self.config.banco}) <DELETE {self.tabelas.tblTetosPrev}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()