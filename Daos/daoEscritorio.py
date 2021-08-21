import sqlite3
from datetime import datetime

from Daos.tabelas import TabelasConfig
from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.escritorioModelo import EscritorioModelo
from cache.cacheEscritorio import CacheEscritorio
from pymysql import connections


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

    def buscaEscritorioById(self, escritorioId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                escritorioId, nomeEscritorio, nomeFantasia, 
                cnpj, cpf, telefone, 
                email, inscEstadual, endereco, 
                numero, cep, complemento, 
                cidade, estado, bairro, 
                dataCadastro, dataUltAlt
            FROM 
                '{self.tabelas.tblEscritorios}'
            WHERE
                escritorioId = {escritorioId}
            """

        try:
            cursor.execute(strComando)
            escritorio = cursor.fetchone()
            logPrioridade(f'SELECT<buscaEscritorioById>___________________{self.tabelas.tblEscritorios}', TipoEdicao.select, Prioridade.saidaComun)
            return EscritorioModelo().fromList(escritorio)
        except Exception as erro:
            logPrioridade(f'SELECT<buscaEscritorioById>___________________ERRO {self.tabelas.tblEscritorios}', TipoEdicao.erro, Prioridade.saidaImportante)
            print(f"buscaEscritorioById({type(erro)}) - {erro}")
            raise Warning(f'Erro SQL - buscaEscritorioById <SELECT {self.tabelas.tblEscritorios}>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()