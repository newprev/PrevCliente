import sqlite3
from datetime import datetime
from logs import logPrioridade
from newPrevEnums import *

from Daos.tabelas import TabelasConfig
from pymysql import connections
from modelos.advogadoModelo import AdvogadoModelo
from modelos.escritorioModelo import EscritorioModelo

class DaoAdvogado:

    def __init__(self, db: connections=None):
        self.db = db
        self.tabelas = TabelasConfig()
        self.escritorio: EscritorioModelo = EscritorioModelo()

    def insereAdvogado(self, advogado: AdvogadoModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()
        response = True

        strComando = f"""
            INSERT INTO {self.tabelas.tblAdvogados}
            (
                escritorioId, nomeEscritorio, nomeFantasia,
                cnpj, cpf, inscEstadual,
                numero, cep, complemento, 
                profissao, endereco, estado, 
                cidade, bairro, cep, 
                qtdChaves, dataCadastro, dataUltAlt, 
                ativo
            )
            VALUES
            (
                
            )"""

        try:
            cursor.execute()
            logPrioridade(f'CREATE<criaTabela>___________________{self.tabelas.tblAdvogados}', TipoEdicao.createTable, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - criaTabela({self.config.banco}) <CREATE {scriptCreate}>')
        finally:
            self.disconectBD(cursor)
            return response
