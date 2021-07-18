import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import List

from Daos.tabelas import TabelasConfig
from pymysql import connections
import pandas as pd

from modelos.expSobrevidaModelo import ExpectativaSobrevidaModelo
from newPrevEnums import TipoContribuicao

from helpers import datetimeToSql

from logs import logPrioridade, TipoEdicao, Prioridade

from modelos.beneficiosModelo import BeneficiosModelo
from modelos.contribuicoesModelo import ContribuicoesModelo
from modelos.remuneracaoModelo import RemuneracoesModelo
from modelos.cnisCabecalhoModelo import CabecalhoModelo


class DaoCalculos:

    def __init__(self, db: connections=None):
        self.db = db
        self.config = TabelasConfig()
        # self.cacheLogin = CacheLogin()
        # self.cacheEscritorio = CacheEscritorio()
        # self.advogado: AdvogadoModelo = self.cacheLogin.carregarCache()
        # self.escritorio: EscritorioModelo = self.cacheEscritorio.carregarCache()
        # if not self.advogado:
        #     self.advogado = self.cacheLogin.carregarCacheTemporario()
        # if not self.escritorio:
        #     self.escritorio = self.cacheEscritorio.carregarCacheTemporario()

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
            return ContribuicoesModelo().fromList(cursor.fetchone())
        except Exception as erro:
            print(f'buscaContribuicaoPorId ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaContribuicaoPorId {self.config.tblCnisContribuicoes}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaContribuicaoPorId {self.config.tblCnisContribuicoes} <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaTodasContribuicoes(self, clienteId: int):
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
                clienteId = {clienteId}
        """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaTodasContribuicoes>___________________{self.config.tblCnisContribuicoes}', TipoEdicao.select, Prioridade.saidaComun)
            return (ContribuicoesModelo().fromList(contribuicao) for contribuicao in cursor.fetchall())
        except Exception as erro:
            print(f'buscaTodasContribuicoes ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaTodasContribuicoes {self.config.tblCnisContribuicoes}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaTodasContribuicoes {self.config.tblCnisContribuicoes} <SELECT>')
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
            return RemuneracoesModelo().fromList(cursor.fetchone())
        except Exception as erro:
            print(f'buscaRemuneracaoPorId ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaRemuneracaoPorId {self.config.tblCnisRemuneracoes}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaRemuneracaoPorId {self.config.tblCnisRemuneracoes} <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaTodasRemuneracoes(self, clienteId: int):

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
                clienteId = {clienteId}
        """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaTodasRemuneracoes>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.select, Prioridade.saidaComun)
            return (RemuneracoesModelo().fromList(remuneracao) for remuneracao in cursor.fetchall())
        except Exception as erro:
            print(f'buscaTodasRemuneracoes ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaTodasRemuneracoes {self.config.tblCnisRemuneracoes}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaTodasRemuneracoes {self.config.tblCnisRemuneracoes} <SELECT>')
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
            return BeneficiosModelo().fromList(cursor.fetchone())
        except Exception as erro:
            print(f'buscaBeneficioPorId ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaBeneficioPorId {self.config.tblCnisBeneficios}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaBeneficioPorId {self.config.tblCnisBeneficios} <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaExpSobrevidaPorData(self, data: datetime, idadeCliente: int) -> ExpectativaSobrevidaModelo:
        dataReferente: str = datetimeToSql(data)

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""                
            SELECT 
                infoId, dataReferente, idade,
                expectativaSobrevida, dataCadastro, dataUltAlt
            FROM 
                {self.config.tblExpSobrevida} 
            WHERE 
                dataReferente > '{dataReferente}'
            AND 
                idade = {idadeCliente};
        """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaExpSobrevidaPorData>___________________{self.config.tblExpSobrevida}', TipoEdicao.select, Prioridade.saidaComun)
            if cursor.fetchone() is None:
                return self.buscaExpSobrevidaPorData(data - relativedelta(years=1), idadeCliente)
            else:
                cursor.execute(strComando)
                return ExpectativaSobrevidaModelo().fromList(cursor.fetchone())
        except Exception as erro:
            print(f'buscaExpSobrevidaPorData ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaExpSobrevidaPorData {self.config.tblExpSobrevida}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaExpSobrevidaPorData {self.config.tblExpSobrevida} <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaRemContPorData(self, clienteId: int,  dataInicio: str, dataFim: str = '') -> pd.DataFrame:

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT clienteId, contribuicoesId, competencia, salContribuicao, indicadores, 'CONTRIBUICAO'
            FROM {self.config.tblCnisContribuicoes}
            WHERE clienteId = {clienteId}
            AND competencia > '{dataInicio}'"""

        if dataFim != '':
            strComando += f"""
            AND competencia < '{dataFim}'"""

        strComando += f"""
        
            UNION
                
            SELECT clienteId, remuneracoesId, competencia, remuneracao, indicadores, 'REMUNERACAO'
            FROM {self.config.tblCnisRemuneracoes}
            WHERE clienteId = {clienteId}
            AND competencia > '{dataInicio}'"""

        if dataFim != '':
            strComando += f"""
            AND competencia < '{dataFim}'"""

        try:
            cursor.execute(strComando)
            colunas: list = ['clienteId', 'infoId', 'competencia', 'salContribuicao', 'indicadores', 'tipoInfo']
            dfContribuicoes = pd.DataFrame(cursor.fetchall(), columns=colunas)
            logPrioridade(f'SELECT<buscaRemContPorData>___________________{self.config.tblCnisBeneficios}', TipoEdicao.select, Prioridade.saidaComun)
            return dfContribuicoes
        except Exception as erro:
            print(f'buscaRemContPorData ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaRemContPorData {self.config.tblCnisBeneficios}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaRemContPorData {self.config.tblCnisBeneficios} <SELECT>')
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
                
                UNION
                    
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

    def buscaCabecalhosClienteId(self, clienteId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                cabecalhosId, clienteId, seq, 
                nit, nb, cdEmp,
                nomeEmp, dataInicio, dataFim,
                tipoVinculo, orgVinculo, especie,
                indicadores, ultRem, dadoOrigem,
                situacao, dataCadastro, dataUltAlt
            FROM
                {self.config.tblCnisCabecalhos}
            WHERE
                clienteId = {clienteId}               
        """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaCabecalhosClienteId>___________________{self.config.tblCnisCabecalhos}', TipoEdicao.select, Prioridade.saidaComun)
            listaCabecalhos = (CabecalhoModelo().fromList(cabecalho) for cabecalho in cursor.fetchall())
            return listaCabecalhos
        except Exception as erro:
            print(f'buscaCabecalhosClienteId ({type(erro)}) - {erro}')
            logPrioridade(f'Erro SQL - buscaCabecalhosClienteId {self.config.tblCnisCabecalhos}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaCabecalhosClienteId {self.config.tblCnisCabecalhos} <SELECT>')
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

    def insereListaContribuicoes(self, contribuicoes: List[ContribuicoesModelo]):
        primeiroValor: bool = True
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
            VALUES """

        for contrib in contribuicoes:
            if primeiroValor:
                strComando += f"""
            (
                {contrib.clienteId}, {contrib.seq}, '{contrib.competencia}',
                '{contrib.dataPagamento}', '{contrib.contribuicao}', '{contrib.salContribuicao}',
                '{contrib.indicadores}', '{contrib.dadoOrigem}', '{datetimeToSql(datetime.now())}', 
                '{datetimeToSql(datetime.now())}'
            )"""
                primeiroValor = False
            else:
                strComando += f""",
            (
                {contrib.clienteId}, {contrib.seq}, '{contrib.competencia}',
                '{contrib.dataPagamento}', '{contrib.contribuicao}', '{contrib.salContribuicao}',
                '{contrib.indicadores}', '{contrib.dadoOrigem}', '{datetimeToSql(datetime.now())}', 
                '{datetimeToSql(datetime.now())}'
            )"""

            # if isinstance(self.db, sqlite3.Connection):
            #     strComando += f""", '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
            # )"""
            # else:
            #     strComando += f""", NOW(), NOW()
            # )"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'INSERT<insereListaContribuicoes>___________________{self.config.tblCnisContribuicoes}', TipoEdicao.insert, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - insereListaContribuicoes({self.config.tipoBanco}) <INSERT {self.config.tblCnisContribuicoes}>')
        finally:
            self.disconectBD(cursor)
            self.db.commit()

    def delete(self, tipo: TipoContribuicao, contribuicaoId: int):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()
        # self.db.connect()
        cursor = self.db.cursor()

        if tipo == TipoContribuicao.contribuicao:
            tabela: str = self.config.tblCnisContribuicoes
            where: str = f"contribuicoesId = {contribuicaoId}"
        elif tipo == TipoContribuicao.remuneracao:
            tabela: str = self.config.tblCnisRemuneracoes
            where: str = f"remuneracoesId = {contribuicaoId}"
        else:
            tabela: str = self.config.tblCnisBeneficios
            where: str = f"beneficiosId = {contribuicaoId}"

        strComando = f"""
            DELETE FROM {tabela}
            WHERE {where};"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'DELETE<delete>___________________{tabela}', TipoEdicao.delete, Prioridade.saidaComun)
        except:
            logPrioridade(f'DELETE<delete>___________________ERRO {tabela}', TipoEdicao.delete, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - delete({tabela}) <DELETE>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()