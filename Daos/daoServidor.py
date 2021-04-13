import sqlite3

from Daos.daoInfoImportante import DaoInfoImportante
from connections import ConfigConnection
from Daos.tabelas import TabelasConfig
from helpers import dinheiroToFloat, datetimeToSql
from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.convMonModelo import ConvMonModelo
from modelos.tetosPrevModelo import TetosPrevModelo
from datetime import datetime

from newPrevEnums import TiposConexoes


class DaoServidor:

    def __init__(self, db=None):
        self.dbConnection = ConfigConnection(instanciaBanco=TiposConexoes.nuvem)
        self.dbServidor = self.dbConnection.getDatabase()
        self.dbLocal = db
        self.daoInfoImportante = DaoInfoImportante(db=db)

        self.tabelas = TabelasConfig()

    def syncConvMon(self):
        self.dbServidor.ping()
        cursor = self.dbServidor.cursor()

        if isinstance(type(self.dbServidor), type(self.dbLocal)):
            return True

        strComando = f"""
            SELECT 
                convMonId, nomeMoeda, fator, 
                dataInicial, dataFinal, conversao,
                moedaCorrente, sinal, dataUltAlt, 
                dataCadastro
            FROM
                {self.tabelas.tblConvMon}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<syncConvMon>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.select, Prioridade.sync)
            listaConvMonServidor = cursor.fetchall()
            qtdMoedasLocal: int = self.daoInfoImportante.contaQtdMoedas()

            if qtdMoedasLocal == 0:
                for item in listaConvMonServidor:
                    convMon = ConvMonModelo().fromList(item, retornaInst=True)
                    self.daoInfoImportante.insereConvMon(convMon)
            else:
                for item in listaConvMonServidor:
                    convMon = ConvMonModelo().fromList(item, retornaInst=True)
                    self.daoInfoImportante.atualizaConvMon(convMon)
        except:
            raise Warning(f'Erro SQL - atualizaTetos({self.dbConnection.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.dbLocal.commit()
            self.disconectBD(cursor)

    def syncTetosPrev(self):
        self.dbServidor.ping()
        cursor = self.dbServidor.cursor()

        if isinstance(type(self.dbServidor), type(self.dbLocal)):
            return True

        strComando = f"""
                    SELECT 
                        tetosPrevId, dataValidade, valor,
                        dataUltAlt, dataCadastro
                    FROM
                        {self.tabelas.tblTetosPrev}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<syncTetosPrev>___________________{self.tabelas.tblTetosPrev}', TipoEdicao.select, Prioridade.sync)
            listaTetosPrevServidor = cursor.fetchall()
            qtdTetosLocal: int = self.daoInfoImportante.contaQtdTetos()

            if qtdTetosLocal == 0:
                listaTetosAInserir = [TetosPrevModelo().fromList(item, retornaInst=True) for item in listaTetosPrevServidor]
                self.daoInfoImportante.insereListaTetosModel(listaTetosAInserir)
            else:
                for item in listaTetosPrevServidor:
                    tetoPrev = TetosPrevModelo().fromList(item, retornaInst=True)
                    self.daoInfoImportante.atualizaTeto(tetoPrev)
        except:
            raise Warning(f'Erro SQL - syncTetosPrev({self.dbConnection.banco}) <INSERT {self.tabelas.tblTetosPrev}>')
        finally:
            self.dbLocal.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.dbServidor.close()
