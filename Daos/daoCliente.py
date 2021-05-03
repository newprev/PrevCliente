import sqlite3
from datetime import datetime

from Daos.tabelas import TabelasConfig
from helpers import datetimeToSql, mascaraDataSql
from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.clienteModelo import ClienteModelo
from pymysql import connections, cursors


class DaoCliente:

    def __init__(self, db: connections = None):
        self.db = db
        self.config = TabelasConfig()

    def atualizaCliente(self, cliente: ClienteModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            UPDATE {self.config.tblCliente} SET
                    nomeCliente = '{cliente.nomeCliente}',
                    sobrenomeCliente = '{cliente.sobrenomeCliente}',
                    idade = {cliente.idade},
                    dataNascimento = '{mascaraDataSql(cliente.dataNascimento)}',
                    telefone = '{cliente.telefone}',
                    email = '{cliente.email}',
                    rgCliente = '{cliente.rgCliente}',
                    cpfCliente = '{cliente.cpfCliente}',
                    numCarteiraProf = '{cliente.numCartProf}',
                    nit = '{cliente.nit}',
                    nomeMae = '{cliente.nomeMae}',
                    estadoCivil = '{cliente.estadoCivil}',
                    profissao = '{cliente.profissao}',
                    numero = {cliente.numero},
                    endereco = '{cliente.endereco}',
                    estado = '{cliente.estado}',
                    cidade = '{cliente.cidade}',
                    bairro = '{cliente.bairro}',
                    cep = '{cliente.cep}',
                    complemento = '{cliente.complemento}',
                    dataUltAlt = '{datetimeToSql(datetime.now())}'
                WHERE
                    clienteId = {cliente.clienteId}
                """
        try:
            cursor.execute(strComando)
            logPrioridade(f'UPDATE<atualizaCliente>___________________{self.config.tblCliente}', TipoEdicao.update, Prioridade.saidaComun)
        except:
            raise Warning(f'Erro SQL - atualizaCliente({self.config.tblCliente}) <UPDATE>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def cadastroClienteComCnis(self, cliente: ClienteModelo, dictAllInfo: dict) -> int:

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor: cursors = self.db.cursor()
        clienteId = 0

        strComando = f"""
            INSERT INTO {self.config.tblCliente} 
            (
                nomeCliente, sobrenomeCliente, idade, 
                dataNascimento, telefone, email, 
                rgCliente, cpfCliente, numCarteiraProf, 
                nit, nomeMae, estadoCivil, 
                profissao, endereco, numero, 
                estado, cidade, bairro, 
                cep, complemento, dataCadastro, 
                dataUltAlt
            )
            VALUES
            (
                '{cliente.nomeCliente}', '{cliente.sobrenomeCliente}', {cliente.idade}, 
                '{cliente.dataNascimento}', '{cliente.telefone}', '{cliente.email}', 
                '{cliente.rgCliente}', '{cliente.cpfCliente}', '{cliente.numCartProf}', 
                '{cliente.nit}', '{cliente.nomeMae}', '{cliente.estadoCivil}', 
                '{cliente.profissao}', '{cliente.endereco}', {cliente.numero}, 
                '{cliente.estado}', '{cliente.cidade}', '{cliente.bairro}', 
                '{cliente.cep}', '{cliente.complemento}', '{datetime.now()}', 
                '{datetime.now()}'
            );"""

        try:
            cursor.execute(strComando)
            clienteId = cursor.lastrowid
            logPrioridade(f'INSERT<cadastroClienteComCnis>___________________{self.config.tblCliente} ({clienteId})', TipoEdicao.insert, Prioridade.saidaComun)

            # Verifica se há benefícios para inserir no banco
            strComando = self.insertSqlBenecifio(dictAllInfo['cabecalhoBeneficio'], clienteId)
            if strComando != '':
                try:
                    cursor.execute(strComando)
                    logPrioridade(f'INSERT<cadastroClienteComCnis>___________________{self.config.tblCnisBeneficios}', TipoEdicao.insert, Prioridade.saidaComun)
                except:
                    raise Warning(f'Erro SQL - cadastroClienteComCnis({self.config.tblCnisBeneficios}) <INSERT>')

            # Verifica se há contribuições para inserir no banco
            strComando = self.insertSqlContribuicoes(dictAllInfo['contribuicoes'], clienteId)
            if strComando != '':
                try:
                    cursor.execute(strComando)
                    logPrioridade(f'INSERT<cadastroClienteComCnis>___________________{self.config.tblCnisContribuicoes}', TipoEdicao.insert, Prioridade.saidaComun)
                except:
                    raise Warning(
                        f'Erro SQL - cadastroClienteComCnis({self.config.tblCnisContribuicoes}) <INSERT>')

            # Verifica se há cabeçalhos para inserir no banco
            strComando = self.insertSqlCabecalhos(dictAllInfo['cabecalho'], clienteId)
            if strComando != '':
                try:
                    cursor.execute(strComando)
                    logPrioridade(f'INSERT<cadastroClienteComCnis>___________________{self.config.tblCnisCabecalhos}', TipoEdicao.insert, Prioridade.saidaComun)
                except:
                    raise Warning(f'Erro SQL - cadastroClienteComCnis({self.config.tblCnisCabecalhos}) <INSERT>')

            # Verifica se há remunerações para inserir no banco
            strComando = self.insertSqlRemuneracoes(dictAllInfo['remuneracoes'], clienteId)
            if strComando != '':
                try:
                    cursor.execute(strComando)
                    logPrioridade(f'INSERT<cadastroClienteComCnis>___________________{self.config.tblCnisRemuneracoes}', TipoEdicao.insert, Prioridade.saidaComun)
                except:
                    raise Warning(
                        f'Erro SQL - cadastroClienteComCnis({self.config.tblCnisCabecalhos}) <INSERT>')

            self.db.commit()
            logPrioridade(f'INSERT<cadastroClienteComCnis>___________________{self.config.tblCliente}', TipoEdicao.insert, Prioridade.saidaImportante)
        except:
            raise Warning(f'Erro SQL - cadastroClienteComCnis({self.config.tblCliente}) <INSERT>')
        finally:
            self.disconectBD(cursor)
            return clienteId

    def insertSqlBenecifio(self, beneficio: dict, clienteId: int) -> str:
        strComando = ''
        if len(beneficio['Seq']) > 0 and clienteId != None and clienteId != 0:
            strComando = f"""
                INSERT INTO {self.config.tblCnisBeneficios}
                    (
                        clienteId, seq, nb,
                        especie, dataInicio, dataFim,
                        situacao, dadoOrigem, dataCadastro, 
                        dataUltAlt
                    )
                VALUES """

            for i in range(0, len(beneficio['Seq'])):
                if i != 0:
                    strComando += ', '
                strComando += f""" 
                    (
                        {clienteId}, {beneficio['Seq'][i]}, {beneficio['NB'][i]},
                        '{beneficio['especie'][i]}', '{mascaraDataSql(beneficio['dataInicio'][i])}', '{mascaraDataSql(beneficio['dataFim'][i])}',
                        '{beneficio['situacao'][i]}', 'CNIS', '{datetime.now()}',
                        '{datetime.now()}'
                    )"""

            return strComando
        else:
            return ''

    def insertSqlContribuicoes(self, contribuicoes: dict, clienteId: int):
        strComando = ''
        if len(contribuicoes['Seq']) > 0 and clienteId != None and clienteId != 0:
            strComando = f"""
                        INSERT INTO {self.config.tblCnisContribuicoes}
                            (
                                clienteId, seq, competencia,
                                dataPagamento, contribuicao, salContribuicao,
                                indicadores, dadoOrigem, dataCadastro, 
                                dataUltAlt
                            )
                        VALUES """

            for i in range(0, len(contribuicoes['Seq'])):
                if i != 0:
                    strComando += ', '
                strComando += f""" 
                            (
                                {clienteId}, {contribuicoes['Seq'][i]}, '{mascaraDataSql(contribuicoes['competencia'][i], short=True)}',
                                '{mascaraDataSql(contribuicoes['dataPagamento'][i])}', {contribuicoes['contribuicao'][i]}, {contribuicoes['salContribuicao'][i]},
                                '{contribuicoes['indicadores'][i]}', 'CNIS', '{datetimeToSql(datetime.now())}', 
                                '{datetimeToSql(datetime.now())}'
                            )"""

            return strComando
        else:
            return ''

    def insertSqlCabecalhos(self, cabecalhos: dict, clienteId: int):
        strComando = ''
        if len(cabecalhos['Seq']) > 0 and clienteId != None and clienteId != 0:
            strComando = f"""
                        INSERT INTO {self.config.tblCnisCabecalhos}
                            (
                                clienteId, seq, nit,
                                cdEmp, nomeEmp, dataInicio,
                                dataFim, tipoVinculo, indicadores, 
                                ultRem, dadoOrigem, dataCadastro, 
                                dataUltAlt
                            )
                        VALUES """

            for i in range(0, len(cabecalhos['Seq'])):
                if i != 0:
                    strComando += ', '
                strComando += f""" 
                            (
                                {clienteId}, {cabecalhos['Seq'][i]}, '{cabecalhos['nit'][i]}',
                                '{cabecalhos['cdEmp'][i]}', '{cabecalhos['nomeEmp'][i]}', '{mascaraDataSql(cabecalhos['dataInicio'][i])}',
                                '{mascaraDataSql(cabecalhos['dataFim'][i])}', '{cabecalhos['tipoVinculo'][i]}', '{cabecalhos['indicadores'][i]}',
                                '{mascaraDataSql(cabecalhos['ultRem'][i], short=True)}', 'CNIS', '{datetimeToSql(datetime.now())}', 
                                '{datetimeToSql(datetime.now())}'
                            )"""

            return strComando
        else:
            return ''

    def insertSqlRemuneracoes(self, remuneracoes: dict, clienteId: int):
        strComando = ''
        if len(remuneracoes['Seq']) > 0 and clienteId != None and clienteId != 0:
            strComando = f"""
                        INSERT INTO {self.config.tblCnisRemuneracoes}
                            (
                                clienteId, seq, competencia,
                                remuneracao, indicadores, dadoOrigem,
                                dataCadastro, dataUltAlt
                            )
                        VALUES """

            for i in range(0, len(remuneracoes['Seq'])):
                if i != 0:
                    strComando += ', '
                strComando += f""" 
                            (
                                {clienteId}, {remuneracoes['Seq'][i]}, '{mascaraDataSql(remuneracoes['competencia'][i], short=True)}',
                                {remuneracoes['remuneracao'][i]}, '{remuneracoes['indicadores'][i]}', 'CNIS',
                                '{datetimeToSql(datetime.now())}', '{datetimeToSql(datetime.now())}'
                            )"""

            return strComando
        else:
            return ''

    def buscaClienteById(self, clienteId, returnInstance: bool = False):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT 
                clienteId, nomeCliente, sobrenomeCliente,
                idade, dataNascimento, telefone, 
                email, rgCliente, cpfCliente,
                numCarteiraProf, nit, nomeMae, 
                estadoCivil, profissao, endereco,
                estado, cidade, numero, 
                bairro, cep, complemento, 
                dataCadastro, dataUltAlt
            FROM {self.config.tblCliente} 
            WHERE clienteId = {clienteId}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaClienteById>___________________{self.config.tblCliente}', TipoEdicao.select, Prioridade.saidaComun)
            if returnInstance:
                return ClienteModelo().fromList(cursor.fetchone(), retornaInst=True)
            else:
                return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - buscaClienteById({self.config.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaTodos(self, returnModel: bool = False):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT 
                clienteId, nomeCliente, sobrenomeCliente,
                idade, dataNascimento, telefone, 
                email, rgCliente, cpfCliente,
                numCarteiraProf, nit, nomeMae, 
                estadoCivil, profissao, endereco,
                estado, cidade, numero, 
                bairro, cep, complemento, 
                dataCadastro, dataUltAlt
            FROM {self.config.tblCliente}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaTodos>___________________{self.config.tblCliente}', TipoEdicao.select, Prioridade.saidaComun)

            if returnModel:
                clientesModel = []
                for cliente in cursor.fetchall():
                    clientesModel.append(ClienteModelo().fromList(cliente, retornaInst=True))
                return clientesModel
            else:
                return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - buscaTodos({self.config.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()
