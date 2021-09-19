import sqlite3
from datetime import datetime
from logs import logPrioridade
from util.enums.newPrevEnums import *

from Daos.tabelas import TabelasConfig
from pymysql import connections
from modelos.advogadoModelo import AdvogadoModelo


class DaoAdvogado:

    def __init__(self, db: connections = None):
        self.db = db
        self.tabelas = TabelasConfig()
        # self.escritorio: EscritorioModelo = EscritorioModelo()

    def insereAdvogado(self, advogado: AdvogadoModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.tabelas.tblAdvogados}
            (
                advogadoId, escritorioId, nomeUsuario, 
                sobrenomeUsuario, login, senha, 
                email, numeroOAB, nacionalidade, 
                estadoCivil, admin, ativo, 
                confirmado, dataCadastro, dataUltAlt
            )
            VALUES
            (
                {advogado.advogadoId}, {advogado.escritorioId}, '{advogado.nomeUsuario}', 
                '{advogado.sobrenomeUsuario}', '{advogado.login}', '{advogado.senha}', 
                '{advogado.email[0]}', '{advogado.numeroOAB}', '{advogado.nacionalidade}', 
                '{advogado.estadoCivil}', {advogado.admin}, {advogado.ativo}, 
                {advogado.confirmado}, '{datetime.now()}', '{datetime.now()}'                
            )"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereAdvogado>___________________{self.tabelas.tblAdvogados}', TipoEdicao.insert, Prioridade.saidaComun)
        except Exception as erro:
            print(f"insereAdvogado({type(erro)}) - {erro}")
            raise Warning(f'Erro SQL - insereAdvogado <INSERT {self.tabelas.tblAdvogados}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def buscaAdvogadoById(self, advogadoId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                advogadoId, escritorioId, nomeUsuario, 
                sobrenomeUsuario, login, senha, 
                email, numeroOAB, nacionalidade, 
                estadoCivil, admin, ativo, 
                confirmado, dataCadastro, dataUltAlt
            FROM 
                '{self.tabelas.tblAdvogados}'
            WHERE
                advogadoId = {advogadoId}
            """

        try:
            cursor.execute(strComando)
            advogado = cursor.fetchone()
            logPrioridade(f'SELECT<buscaAdvogadoById>___________________{self.tabelas.tblAdvogados}', TipoEdicao.select, Prioridade.saidaComun)
            return AdvogadoModelo().fromList(advogado)
        except Exception as erro:
            logPrioridade(f'SELECT<buscaAdvogadoById>___________________ERRO {self.tabelas.tblAdvogados}', TipoEdicao.erro, Prioridade.saidaImportante)
            print(f"buscaAdvogadoById({type(erro)}) - {erro}")
            raise Warning(f'Erro SQL - buscaAdvogadoById <SELECT {self.tabelas.tblAdvogados}>')
        finally:
            self.disconectBD(cursor)

    def atualizaAdvogado(self, advogado: AdvogadoModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        if isinstance(advogado.email, list):
            advogado.email = advogado.email[0]

        strComando = f"""
            UPDATE {self.tabelas.tblAdvogados}
                SET
                    nomeUsuario = '{advogado.nomeUsuario}', 
                    sobrenomeUsuario = '{advogado.sobrenomeUsuario}',
                    login = '{advogado.login}', 
                    senha = '{advogado.senha}',
                    email = '{advogado.email[0]}',
                    numeroOAB = '{advogado.numeroOAB}',
                    nacionalidade = '{advogado.nacionalidade}',
                    estadoCivil = '{advogado.estadoCivil}',
                    admin = {advogado.admin},
                    ativo = {advogado.ativo}, 
                    confirmado = {advogado.confirmado},
                    dataUltAlt = '{datetime.now()}'                
            )"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'UPDATE<atualizaAdvogado>___________________{self.tabelas.tblAdvogados}', TipoEdicao.update, Prioridade.saidaComun)
        except Exception as erro:
            print(f"atualizaAdvogado({type(erro)}) - {erro}")
            raise Warning(f'Erro SQL - atualizaAdvogado <UPDATE {self.tabelas.tblAdvogados}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
