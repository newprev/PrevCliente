import sqlite3
from datetime import datetime

from Daos.tabelas import TabelasConfig
from pymysql import connections

from newPrevEnums import TipoContribuicao

from helpers import datetimeToSql
from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.beneficiosModelo import BeneficiosModelo
from modelos.contribuicoesModelo import ContribuicoesModelo
from modelos.remuneracaoModelo import RemuneracoesModelo


class DaoCalculos:

    def __init__(self, db: connections=None):
        self.db = db
        self.config = TabelasConfig()

    def buscaContribuicaoPorId(self, contribuicaoId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                contribuicoesId, clienteId, seq,
                competencia, dataPagamento, contribuicao,
                salContribuicao, indicadores, dadoOrigem,
                dataCadastro, dataUltAlt
            FROM
                {self.config.tblCnisContribuicoes}
            WHERE
                contribuicoesId = {contribuicaoId}
        """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaContribuicaoPorId>___________________{self.config.tblCnisContribuicoes}', TipoEdicao.select, Prioridade.saidaComun)
            return ContribuicoesModelo().fromList(cursor.fetchall())
        except Exception as erro:
            print(f'buscaContribuicaoPorId ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaContribuicaoPorId {self.config.tblCnisContribuicoes}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaContribuicaoPorId {self.config.tblCnisContribuicoes} <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaRemuneracaoPorId(self, remuneracaoId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                remuneracoesId, clienteId, seq,
                competencia, remuneracao, indicadores,
                dadoOrigem, dataCadastro, dataUltAlt
            FROM
                {self.config.tblCnisRemuneracoes}
            WHERE
                remuneracoesId = {remuneracaoId}
        """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaRemuneracaoPorId>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.select, Prioridade.saidaComun)
            return RemuneracoesModelo().fromList(cursor.fetchall())
        except Exception as erro:
            print(f'buscaRemuneracaoPorId ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaRemuneracaoPorId {self.config.tblCnisRemuneracoes}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaRemuneracaoPorId {self.config.tblCnisRemuneracoes} <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaBeneficioPorId(self, beneficioId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                beneficiosId, clienteId, seq,
                nb, especie, dataInicio,
                dataFim, situacao, dadoOrigem,
                dataCadastro, dataUltAlt
            FROM
                {self.config.tblCnisBeneficios}
            WHERE
                beneficiosId = {beneficioId}
        """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaBeneficioPorId>___________________{self.config.tblCnisBeneficios}', TipoEdicao.select, Prioridade.saidaComun)
            return BeneficiosModelo().fromList(cursor.fetchall())
        except Exception as erro:
            print(f'buscaBeneficioPorId ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaBeneficioPorId {self.config.tblCnisBeneficios}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaBeneficioPorId {self.config.tblCnisBeneficios} <SELECT>')
        finally:
            self.disconectBD(cursor)

    def getRemECon(self, clienteId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
                    SELECT
                        --Contribuições
                        con.contribuicoesId, con.seq, con.competencia, 
                        con.salContribuicao, 'Contribuição' AS natureza, con.indicadores,
                        
                        --Conversão monetária
                        cm.sinal, cm.convMonId, cm.nomeMoeda,
                        
                        --Tetos previdenciários
                        tp.tetosPrevId, tp.valor
                    FROM {self.config.tblCnisContribuicoes} con
                        JOIN {self.config.tblConvMon} cm 
                            ON con.competencia >= cm.dataInicial
                                AND con.competencia <= cm.dataFinal
                        JOIN {self.config.tblTetosPrev} tp
                            ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', con.competencia)
                    WHERE clienteId = {clienteId}
                
                UNION ALL
                    
                    SELECT 
                        --Remunerações
                        rem.remuneracoesId, rem.seq, rem.competencia, 
                        rem.remuneracao, 'Remuneração' AS natureza, rem.indicadores,
                        
                        --Conversão monetária
                        cm.sinal, cm.convMonId, cm.nomeMoeda,
                        
                        --Tetos previdenciários
                        tp.tetosPrevId, tp.valor
                    FROM {self.config.tblCnisRemuneracoes} rem
                        JOIN {self.config.tblConvMon} cm 
                            ON rem.competencia >= cm.dataInicial
                                AND rem.competencia <= cm.dataFinal
                        JOIN {self.config.tblTetosPrev} tp
                            ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', rem.competencia) 
                        WHERE clienteId = {clienteId}
                    ORDER BY competencia DESC  """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getRemECon>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchall()
        except:
            logPrioridade(f'Erro SQL - getRemECon({self.config.tblCnisRemuneracoes}, {self.config.tblCnisContribuicoes})', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - getRemECon({self.config.tblCnisRemuneracoes}, {self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def getBeneficiosPor(self, clienteId: int) -> list:

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT 
                beneficiosId, clienteId, seq,
                nb, especie, dataInicio,
                dataFim, situacao, dadoOrigem,
                dataCadastro, dataUltAlt
            FROM {self.config.tblCnisBeneficios} 
            WHERE clienteId = {clienteId}"""

        try:
            cursor.execute(strComando)
            beneficiosLista: list = cursor.fetchall()
            beneficiosModels: list = []

            for beneficio in beneficiosLista:
                beneficiosModels.append(BeneficiosModelo().fromList(beneficio))

            logPrioridade(f'SELECT<getBeneficiosPor>___________________{self.config.tblCnisBeneficios}', TipoEdicao.select, Prioridade.saidaComun)
            return beneficiosModels

        except Exception as erro:
            print(f'getBeneficiosPor({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - getBeneficiosPor({self.config.tblCnisBeneficios})', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - getBeneficiosPor({self.config.tblCnisBeneficios}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def getCount(self, clienteId: int, listaTabelas: list = []):
        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        # Se a lista estiver vazia, traz todos as contribuições no CNIS
        if len(listaTabelas) == 0:
            strComando = f"""
                SELECT COUNT(*) FROM 
                (
                    SELECT con.clienteId, con.competencia, con.seq FROM cnisContribuicoes con
                    WHERE con.clienteId = {clienteId}
                        UNION
                    SELECT ben.clienteId, ben.dataInicio, ben.seq FROM cnisBeneficios ben
                    WHERE ben.clienteId = {clienteId}
                        UNION
                    SELECT rem.clienteId, rem.competencia , rem.seq FROM cnisRemuneracoes rem
                    WHERE rem.clienteId = {clienteId}
    
                ) total;"""
        else:
            if TipoContribuicao.contribuicao in listaTabelas:
                strContribuicoes = f"""
                    SELECT con.clienteId, con.competencia, con.seq FROM cnisContribuicoes con
                    WHERE con.clienteId = {clienteId}"""

                # Adiciona o UNION
                if TipoContribuicao.beneficio in listaTabelas or TipoContribuicao.remuneracao in listaTabelas:
                    strContribuicoes += f"""\nUNION\n"""
            else:
                strContribuicoes = ''

            if TipoContribuicao.beneficio in listaTabelas:
                strBeneficios = f"""
                    SELECT ben.clienteId, ben.dataInicio, ben.seq FROM cnisBeneficios ben
                    WHERE ben.clienteId = {clienteId}"""

                # Adiciona o UNION
                if TipoContribuicao.remuneracao in listaTabelas:
                    strBeneficios += f"""\nUNION\n"""

            else:
                strBeneficios = ''

            if TipoContribuicao.remuneracao in listaTabelas:
                strRemuneracoes = f"""
                    SELECT rem.clienteId, rem.competencia , rem.seq FROM cnisRemuneracoes rem
                    WHERE rem.clienteId = {clienteId}"""

            else:
                strRemuneracoes = ''

            strComando = f"""
                SELECT COUNT(*) FROM 
                (
                    '{strContribuicoes}'
                    '{strBeneficios}'
                    '{strRemuneracoes}'
                ) total;"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getCount>___________________{listaTabelas}', TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchone()[0]
        except:
            logPrioridade(f'Erro SQL - getCount({listaTabelas})', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - getCount({listaTabelas}, {self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
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
                    '{contribuicao.dataPagamento}', '{contribuicao.contribuicao}', '{contribuicao.salContribuicao}',
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