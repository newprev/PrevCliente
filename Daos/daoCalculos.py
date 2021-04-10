import sqlite3
from datetime import datetime

from Daos.tabelas import TabelasConfig
from pymysql import connections

from helpers import datetimeToSql
from logs import *
from modelos.beneficiosModelo import BeneficiosModelo
from modelos.contribuicoesModelo import ContribuicoesModelo
from modelos.remuneracaoModelo import RemuneracoesModelo


class DaoCalculos:

    def __init__(self, db: connections=None):
        self.db = db
        self.config = TabelasConfig()

    def getRemECon(self, clienteId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
        SELECT contribuicoesId, seq, competencia, salContribuicao, 'Contribuição', indicadores FROM {self.config.tblCnisContribuicoes} con
            WHERE clienteId = {clienteId}
        UNION ALL
        SELECT remuneracoesId, seq, competencia, remuneracao, 'Remuneração', indicadores FROM {self.config.tblCnisRemuneracoes} rem
            WHERE clienteId = {clienteId}
        ORDER BY competencia DESC;"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getRemECon>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getRemECon({self.config.tblCnisRemuneracoes}, {self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def contaContribuicoes(self, clienteId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
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

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()
        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT COUNT(*) FROM {self.config.tblCnisRemuneracoes} WHERE clienteId = {clienteId}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<contaRemuneracoes>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchone()
        except:
            raise Warning(f'Erro SQL - contaRemuneracoes({self.config.tblCnisRemuneracoes}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereRemuneracao(self, remuneracao: RemuneracoesModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()
        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.config.tblCnisRemuneracoes}
                (
                    clienteId, seq, competencia,
                    remuneracao, indicadores, dadoOrigem,
                    dataCadastro, dataUltAlt
                )
            VALUES
                (
                    {remuneracao.clienteId}, {remuneracao.seq}, '{remuneracao.competencia}',
                    {remuneracao.remuneracao}, '{remuneracao.indicadores}', '{remuneracao.dadoOrigem}',
                    '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
                );"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereRemuneracao>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - insereRemuneracao({self.config.tblCnisRemuneracoes}) <INSERT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereContribuicao(self, contribuicao: ContribuicoesModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()
        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.config.tblCnisContribuicoes}
                (
                    clienteId, seq, competencia,
                    dataPagamento, contribuicao, salContribuicao,
                    indicadores, dadoOrigem, dataCadastro, 
                    dataUltAlt
                )
            VALUES
                (
                    {contribuicao.clienteId}, {contribuicao.seq}, '{contribuicao.competencia}',
                    {contribuicao.dataPagamento}, '{contribuicao.contribuicao}', '{contribuicao.salContribuicao}',
                    '{contribuicao.indicadores}', '{contribuicao.dadoOrigem}', '{datetimeToSql(datetime.now())}', 
                    '{datetimeToSql(datetime.now())}'
                );"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereContribuicao>___________________{self.config.tblCnisContribuicoes}', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - insereContribuicao({self.config.tblCnisContribuicoes}) <INSERT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def insereBeneficio(self, beneficio: BeneficiosModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()
        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.config.tblCnisBeneficios}
                (
                    clienteId, seq, nb,
                    especie, dataInicio, dataFim,
                    situacao, dadoOrigem, dataCadastro, 
                    dataUltAlt
                )
            VALUES
                (
                    {beneficio.clienteId}, {beneficio.seq}, '{beneficio.nb}',
                    '{beneficio.especie}', '{beneficio.dataInicio}', '{beneficio.dataFim}',
                    '{beneficio.situacao}', '{beneficio.dadoOrigem}', '{datetimeToSql(datetime.now())}', 
                    '{datetimeToSql(datetime.now())}'
                );"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereBeneficio>___________________{self.config.tblCnisBeneficios}', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - insereBeneficio({self.config.tblCnisBeneficios}) <INSERT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()