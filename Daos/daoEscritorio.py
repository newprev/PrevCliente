import sqlite3
from sqlite3 import OperationalError
from datetime import datetime

from Daos.tabelas import TabelasConfig
from helpers import datetimeToSql, mascaraDataSql
from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.clienteModelo import ClienteModelo
from modelos.escritorioModelo import EscritorioModelo
from cache.cacheEscritorio import CacheEscritorio
from pymysql import connections, cursors


class DaoEscritorio:

    def __init__(self, db: connections = None):
        self.db = db
        self.tabelas = TabelasConfig()
        self.escritorioCache = CacheEscritorio()
        self.escritorio: EscritorioModelo = self.escritorioCache.carregarCache()

    def insereEscritorio(self, escritorio: EscritorioModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.tabelas.tblEscritorios}
            (
                escritorioId, nomeEscritorio, nomeFantasia, 
                cnpj, cpf, telefone, 
                email, inscEstadual, endereco, 
                numero, cep, complemento, 
                cidade, estado, bairro,
                dataCadastro, dataUltAlt
            )
            VALUES 
            (
                {escritorio.escritorioId}, '{escritorio.nomeEscritorio}', '{escritorio.nomeFantasia}',
                '{escritorio.cnpj}', '{escritorio.cpf}', '{escritorio.telefone[0]}',
                '{escritorio.email[0]}', '{escritorio.inscEstadual}', '{escritorio.endereco}',
                {escritorio.numero}, '{escritorio.cep}', '{escritorio.complemento}', 
                '{escritorio.cidade}', '{escritorio.estado}', '{escritorio.bairro}',
                '{datetime.now()}', '{datetime.now()}'
            )"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereEscritorio>___________________{self.tabelas.tblEscritorios}', TipoEdicao.insert, Prioridade.saidaComun)
        except Exception as erro:
            print(f"insereEscritorio({type(erro)}) - {erro}")
            raise Warning(f'Erro SQL - insereEscritorio <INSERT {self.tabelas.tblEscritorios}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()