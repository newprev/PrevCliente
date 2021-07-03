import sqlite3

from connections import ConfigConnection
from Daos.tabelas import TabelasConfig
from helpers import datetimeToSql
from logs import TipoEdicao, Prioridade, logPrioridade
from modelos.convMonModelo import ConvMonModelo
from modelos.indicadorModelo import IndicadorModelo
from modelos.tetosPrevModelo import TetosPrevModelo
from datetime import datetime

class DaoInformacoes:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()
        self.tabelas = TabelasConfig()

    def buscaIndicadores(self):
        """:return Generator de modelos de indicadores salvos no banco"""

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT 
                indicadorId, resumo, descricao,
                fonte, dataUltAlt
            FROM
                {self.tabelas.tblIndicadores}
             """
        try:
            cursor.execute(strComando)
            listaIndicadores = (IndicadorModelo().fromList(indicador) for indicador in cursor.fetchall())

            logPrioridade(f'SELECT<buscaIndicadores>___________________{self.tabelas.tblIndicadores}', TipoEdicao.select, Prioridade.saidaComun)
            return listaIndicadores
        except:
            logPrioridade(f'SELECT<buscaIndicadores>___________________ Erro {self.tabelas.tblIndicadores}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaIndicadores({self.config.banco}) <SELECT {self.tabelas.tblIndicadores}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def contaIndicadores(self) -> int:

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
                    SELECT COUNT(*) FROM {self.tabelas.tblIndicadores}
                     """
        try:
            cursor.execute(strComando)

            logPrioridade(f'SELECT<contaIndicadores>___________________{self.tabelas.tblIndicadores}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchone()[0]
        except:
            logPrioridade(f'SELECT<contaIndicadores>___________________ Erro {self.tabelas.tblIndicadores}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - contaIndicadores({self.config.banco}) <SELECT {self.tabelas.tblIndicadores}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereListaIndicadores(self, listaIndicadores: list):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
                    INSERT INTO {self.tabelas.tblIndicadores}
                    (
                        indicadorId, resumo, fonte, 
                        descricao, dataUltAlt
                    )
                    VALUES """

        for index in range(0, len(listaIndicadores)):
            if index == 0:
                strComando += f"""
                    (
                        '{listaIndicadores[index].indicadorId}', '{listaIndicadores[index].resumo}', '{listaIndicadores[index].fonte}', 
                        '{listaIndicadores[index].descricao}', '{listaIndicadores[index].dataUltAlt}'
                    )"""
            else:
                strComando += f""",
                    (
                        '{listaIndicadores[index].indicadorId}', '{listaIndicadores[index].resumo}', '{listaIndicadores[index].fonte}', 
                        '{listaIndicadores[index].descricao}', '{listaIndicadores[index].dataUltAlt}'
                    )"""
        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereListaIndicadores>___________________{self.tabelas.tblIndicadores}', TipoEdicao.insert, Prioridade.saidaComun)
            return listaIndicadores
        except:
            logPrioridade(f'INSERT<insereListaIndicadores>___________________ Erro {self.tabelas.tblIndicadores}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaIndicadores({self.config.banco}) <SELECT {self.tabelas.tblIndicadores}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()