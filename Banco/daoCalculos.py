import sqlite3

from Banco.tabelas import TabelasConfig
from pymysql import connections
import pandas as pd

from util.enums.newPrevEnums import TipoContribuicao

from systemLog.logs import logPrioridade, TipoEdicao, Prioridade


class DaoCalculos:

    def __init__(self, db: connections=None):
        self.db = db
        self.config = TabelasConfig()

    def buscaRemContPorData(self, clienteId: int,  dataInicio: str, dib: str, dataFim: str = '') -> pd.DataFrame:

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        caseFator = f"""CASE
        WHEN iam.fator
                    """

        strComando = f"""
            SELECT 
                cont.clienteId, 
                cont.contribuicoesId, 
                cont.competencia, 
                cont.salContribuicao, 
                cont.indicadores,
                IFNULL(iam.fator, 1),
                tp.valor,
                'CONTRIBUICAO'
            FROM {self.config.tblCnisContribuicoes} cont
            LEFT JOIN {self.config.tblIndiceAtuMonetaria} iam
                ON STRFTIME('%Y-%m', iam.dataReferente) = STRFTIME('%Y-%m', cont.competencia)
                    AND STRFTIME('%Y-%m', iam.dib) = STRFTIME('%Y-%m', '{dib}')
            LEFT JOIN {self.config.tblTetosPrev} tp
                ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', cont.competencia)
            WHERE cont.clienteId = {clienteId}
            AND competencia > '{dataInicio}'"""

        if dataFim != '':
            strComando += f"""
            AND competencia < '{dataFim}'"""

        strComando += f"""
        
            UNION
                
            SELECT 
                rem.clienteId, 
                rem.remuneracoesId, 
                rem.competencia, 
                rem.remuneracao, 
                rem.indicadores,	
                IFNULL(iam.fator, 1),
                tp.valor,
                'REMUNERACAO'
            FROM cnisRemuneracoes rem
            LEFT JOIN indiceAtuMonetaria iam
                ON STRFTIME('%Y-%m', iam.dataReferente) = STRFTIME('%Y-%m', rem.competencia)
                    AND STRFTIME('%Y-%m', iam.dib) = STRFTIME('%Y-%m', '{dib}')
            LEFT JOIN {self.config.tblTetosPrev} tp
                ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', rem.competencia)
            WHERE rem.clienteId = {clienteId}
            AND rem.competencia > '{dataInicio}';"""

        if dataFim != '':
            strComando += f"""
            AND competencia < '{dataFim}'"""

        try:
            cursor.execute(strComando)
            colunas: list = ['clienteId', 'infoId', 'competencia', 'salContribuicao', 'indicadores', 'fator', 'teto', 'tipoInfo']
            dfContribuicoes = pd.DataFrame(cursor.fetchall(), columns=colunas)
            logPrioridade(f'SELECT<buscaRemContPorData>___________________{self.config.tblCnisBeneficios}', TipoEdicao.select, Prioridade.saidaComum)
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
                con.itemId, con.seq, con.competencia, 
                IFNULL(con.salContribuicao, 0) AS salContribuicao, 'Contribuição' AS natureza, con.indicadores,
                
                --Conversão monetária
                cm.sinal, cm.convMonId, cm.nomeMoeda,
                
                --Tetos previdenciários
                tp.tetosPrevId, tp.valor
            FROM itemContribuicao con
                JOIN convMon cm 
                    ON con.competencia >= cm.dataInicial
                        AND con.competencia <= cm.dataFinal
                LEFT JOIN tetosPrev tp
                    ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', con.competencia)
            WHERE clienteId = {clienteId}
        """

        # strComando = f"""
        #             SELECT
        #                 --Contribuições
        #                 con.contribuicoesId, con.seq, con.competencia,
        #                 con.salContribuicao, 'Contribuição' AS natureza, con.indicadores,
        #
        #                 --Conversão monetária
        #                 cm.sinal, cm.convMonId, cm.nomeMoeda,
        #
        #                 --Tetos previdenciários
        #                 tp.tetosPrevId, tp.valor
        #             FROM {self.config.tblCnisContribuicoes} con
        #                 JOIN {self.config.tblConvMon} cm
        #                     ON con.competencia >= cm.dataInicial
        #                         AND con.competencia <= cm.dataFinal
        #                 LEFT JOIN {self.config.tblTetosPrev} tp
        #                     ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', con.competencia)
        #             WHERE clienteId = {clienteId}
        #
        #         UNION
        #
        #             SELECT
        #                 --Remunerações
        #                 rem.remuneracoesId, rem.seq, rem.competencia,
        #                 rem.remuneracao, 'Remuneração' AS natureza, rem.indicadores,
        #
        #                 --Conversão monetária
        #                 cm.sinal, cm.convMonId, cm.nomeMoeda,
        #
        #                 --Tetos previdenciários
        #                 tp.tetosPrevId, tp.valor
        #             FROM {self.config.tblCnisRemuneracoes} rem
        #                 JOIN {self.config.tblConvMon} cm
        #                     ON rem.competencia >= cm.dataInicial
        #                         AND rem.competencia <= cm.dataFinal
        #                 LEFT JOIN {self.config.tblTetosPrev} tp
        #                     ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', rem.competencia)
        #                 WHERE clienteId = {clienteId}
        #             ORDER BY competencia DESC  """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<getRemECon>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.select, Prioridade.saidaComum)
            return cursor.fetchall()
        except Exception as err:
            print(f'getRemECon: ({type(err)}) {err}')
            logPrioridade(f'Erro SQL - getRemECon({self.config.tblCnisRemuneracoes}, {self.config.tblCnisContribuicoes})', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - getRemECon({self.config.tblCnisRemuneracoes}, {self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    # def buscaCabecalhosClienteId(self, clienteId: int):
    #
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         SELECT
    #             vinculoId, clienteId, seq,
    #             nit, nb, cdEmp,
    #             nomeEmp, dataInicio, dataFim,
    #             tipoVinculo, orgVinculo, especie,
    #             indicadores, ultRem, dadoOrigem,
    #             situacao, dadoFaltante, dataCadastro,
    #             dataUltAlt
    #         FROM
    #             {self.config.tblcnisVinculos}
    #         WHERE
    #             clienteId = {clienteId}
    #     """
    #
    #     try:
    #         cursor.execute(strComando)
    #         logPrioridade(f'SELECT<buscaCabecalhosClienteId>___________________{self.config.tblcnisVinculos}', TipoEdicao.select, Prioridade.saidaComum)
    #         listaCabecalhos = (CabecalhoModelo().fromList(cabecalho) for cabecalho in cursor.fetchall())
    #         return listaCabecalhos
    #     except Exception as erro:
    #         print(f'buscaCabecalhosClienteId ({type(erro)}) - {erro}')
    #         logPrioridade(f'Erro SQL - buscaCabecalhosClienteId {self.config.tblcnisVinculos}', TipoEdicao.erro, Prioridade.saidaImportante)
    #         raise Warning(f'Erro SQL - buscaCabecalhosClienteId {self.config.tblcnisVinculos} <SELECT>')
    #     finally:
    #         self.disconectBD(cursor)

    # def getBeneficiosPor(self, clienteId: int) -> list:
    #
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         SELECT
    #             beneficiosId, clienteId, seq,
    #             nb, especie, dataInicio,
    #             dataFim, situacao, dadoOrigem,
    #             dataCadastro, dataUltAlt
    #         FROM {self.config.tblCnisBeneficios}
    #         WHERE clienteId = {clienteId}"""
    #
    #     try:
    #         cursor.execute(strComando)
    #         beneficiosLista: list = cursor.fetchall()
    #         beneficiosModels: list = []
    #
    #         for beneficio in beneficiosLista:
    #             beneficiosModels.append(BeneficiosModelo().fromList(beneficio))
    #
    #         logPrioridade(f'SELECT<getBeneficiosPor>___________________{self.config.tblCnisBeneficios}', TipoEdicao.select, Prioridade.saidaComum)
    #         return beneficiosModels
    #
    #     except Exception as erro:
    #         print(f'getBeneficiosPor({type(erro)}) - {erro}')
    #         logPrioridade(f'Erro SQL - getBeneficiosPor({self.config.tblCnisBeneficios})', TipoEdicao.erro, Prioridade.saidaImportante)
    #         raise Warning(f'Erro SQL - getBeneficiosPor({self.config.tblCnisBeneficios}) <SELECT>')
    #     finally:
    #         self.disconectBD(cursor)

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
            logPrioridade(f'SELECT<getCount>___________________{listaTabelas}', TipoEdicao.select, Prioridade.saidaComum)
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
            logPrioridade(f'SELECT<contaRemuneracoes>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.select, Prioridade.saidaComum)
            return cursor.fetchone()
        except:
            raise Warning(f'Erro SQL - contaRemuneracoes({self.config.tblCnisRemuneracoes}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    # def insereRemuneracao(self, remuneracao: RemuneracoesModelo):
    #
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         INSERT INTO {self.config.tblCnisRemuneracoes}
    #             (
    #                 clienteId, seq, competencia,
    #                 remuneracao, indicadores, dadoOrigem,
    #                 dataCadastro, dataUltAlt
    #             )
    #         VALUES
    #             (
    #                 {remuneracao.clienteId}, {remuneracao.seq}, '{remuneracao.competencia}',
    #                 {remuneracao.remuneracao}, '{remuneracao.indicadores}', '{remuneracao.dadoOrigem}',
    #                 '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
    #             );"""
    #
    #     try:
    #         cursor.execute(strComando)
    #         logPrioridade(f'INSERT<insereRemuneracao>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.insert, Prioridade.saidaComum)
    #     except:
    #         raise Warning(f'Erro SQL - insereRemuneracao({self.config.tblCnisRemuneracoes}) <INSERT>')
    #     finally:
    #         self.db.commit()
    #         self.disconectBD(cursor)

    # def insereContribuicao(self, contribuicao: ContribuicoesModelo):
    #
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         INSERT INTO {self.config.tblCnisContribuicoes}
    #             (
    #                 clienteId, seq, competencia,
    #                 dataPagamento, contribuicao, salContribuicao,
    #                 indicadores, dadoOrigem, dataCadastro,
    #                 dataUltAlt
    #             )
    #         VALUES
    #             (
    #                 {contribuicao.clienteId}, {contribuicao.seq}, '{contribuicao.competencia}',
    #                 '{contribuicao.dataPagamento}', '{contribuicao.contribuicao}', '{contribuicao.salContribuicao}',
    #                 '{contribuicao.indicadores}', '{contribuicao.dadoOrigem}', '{datetimeToSql(datetime.now())}',
    #                 '{datetimeToSql(datetime.now())}'
    #             );"""
    #
    #     try:
    #         cursor.execute(strComando)
    #         logPrioridade(f'INSERT<insereContribuicao>___________________{self.config.tblCnisContribuicoes}', TipoEdicao.insert, Prioridade.saidaComum)
    #     except:
    #         raise Warning(f'Erro SQL - insereContribuicao({self.config.tblCnisContribuicoes}) <INSERT>')
    #     finally:
    #         self.db.commit()
    #         self.disconectBD(cursor)

    # def insereBeneficio(self, beneficio: BeneficiosModelo):
    #
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         INSERT INTO {self.config.tblCnisBeneficios}
    #             (
    #                 clienteId, seq, nb,
    #                 especie, dataInicio, dataFim,
    #                 situacao, dadoOrigem, dataCadastro,
    #                 dataUltAlt
    #             )
    #         VALUES
    #             (
    #                 {beneficio.clienteId}, {beneficio.seq}, '{beneficio.nb}',
    #                 '{beneficio.especie}', '{beneficio.dataInicio}', '{beneficio.dataFim}',
    #                 '{beneficio.situacao}', '{beneficio.dadoOrigem}', '{datetimeToSql(datetime.now())}',
    #                 '{datetimeToSql(datetime.now())}'
    #             );"""
    #
    #     try:
    #         cursor.execute(strComando)
    #         logPrioridade(f'INSERT<insereBeneficio>___________________{self.config.tblCnisBeneficios}', TipoEdicao.insert, Prioridade.saidaComum)
    #     except:
    #         raise Warning(f'Erro SQL - insereBeneficio({self.config.tblCnisBeneficios}) <INSERT>')
    #     finally:
    #         self.db.commit()
    #         self.disconectBD(cursor)

    # def insereListaContribuicoes(self, contribuicoes: List[ContribuicoesModelo]):
    #     primeiroValor: bool = True
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         INSERT INTO {self.config.tblCnisContribuicoes}
    #             (
    #                 clienteId, seq, competencia,
    #                 dataPagamento, contribuicao, salContribuicao,
    #                 indicadores, dadoOrigem, dataCadastro,
    #                 dataUltAlt
    #             )
    #         VALUES """
    #
    #     for contrib in contribuicoes:
    #         if primeiroValor:
    #             strComando += f"""
    #         (
    #             {contrib.clienteId}, {contrib.seq}, '{contrib.competencia}',
    #             '{contrib.dataPagamento}', '{contrib.contribuicao}', '{contrib.salContribuicao}',
    #             '{contrib.indicadores}', '{contrib.dadoOrigem}', '{datetimeToSql(datetime.now())}',
    #             '{datetimeToSql(datetime.now())}'
    #         )"""
    #             primeiroValor = False
    #         else:
    #             strComando += f""",
    #         (
    #             {contrib.clienteId}, {contrib.seq}, '{contrib.competencia}',
    #             '{contrib.dataPagamento}', '{contrib.contribuicao}', '{contrib.salContribuicao}',
    #             '{contrib.indicadores}', '{contrib.dadoOrigem}', '{datetimeToSql(datetime.now())}',
    #             '{datetimeToSql(datetime.now())}'
    #         )"""
    #
    #         # if isinstance(self.db, sqlite3.Connection):
    #         #     strComando += f""", '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
    #         # )"""
    #         # else:
    #         #     strComando += f""", NOW(), NOW()
    #         # )"""
    #
    #     try:
    #         cursor.execute(strComando)
    #         logPrioridade(f'INSERT<insereListaContribuicoes>___________________{self.config.tblCnisContribuicoes}', TipoEdicao.insert, Prioridade.saidaComum)
    #     except:
    #         raise Warning(f'Erro SQL - insereListaContribuicoes({self.config.tipoBanco}) <INSERT {self.config.tblCnisContribuicoes}>')
    #     finally:
    #         self.disconectBD(cursor)
    #         self.db.commit()

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
            logPrioridade(f'DELETE<delete>___________________{tabela}', TipoEdicao.delete, Prioridade.saidaComum)
        except:
            logPrioridade(f'DELETE<delete>___________________ERRO {tabela}', TipoEdicao.delete, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - delete({tabela}) <DELETE>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()