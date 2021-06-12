import sqlite3
from sqlite3 import OperationalError
from datetime import datetime

from Daos.tabelas import TabelasConfig
from Daos.daoTelAfins import DaoTelAfins
from helpers import datetimeToSql, mascaraDataSql
from logs import logPrioridade, TipoEdicao, Prioridade
from modelos.clienteModelo import ClienteModelo
from modelos.escritorioModelo import EscritorioModelo
from cache.cacheEscritorio import CacheEscritorio
from pymysql import connections, cursors


class DaoCliente:

    def __init__(self, db: connections = None, escritorio: EscritorioModelo = None):
        self.db = db
        self.config = TabelasConfig()
        self.escritorioCache = CacheEscritorio()
        self.daoTelefone = DaoTelAfins(db=db)

        if escritorio is None:
            self.escritorio = self.escritorioCache.carregarCache()
            if not self.escritorio:
                self.escritorio = self.escritorioCache.carregarCacheTemporario()
        else:
            self.escritorio = escritorio

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
                    dataNascimento = '{cliente.dataNascimento}',
                    email = '{cliente.email}',
                    rgCliente = '{cliente.rgCliente}',
                    cpfCliente = '{cliente.cpfCliente}',
                    nomeBanco = '{cliente.nomeBanco}',
                    agenciaBanco = '{cliente.agenciaBanco}',
                    numeroConta = '{cliente.numeroConta}',
                    pixCliente = '{cliente.pixCliente}',
                    grauEscolaridade = '{cliente.grauEscolaridade}',
                    senhaINSS = '{cliente.senhaINSS}',
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
                AND escritorioId = {self.escritorio.escritorioId}
                """
        try:
            cursor.execute(strComando)
            logPrioridade(f'UPDATE<atualizaCliente>___________________{self.config.tblCliente}', TipoEdicao.update, Prioridade.saidaComun)
            self.daoTelefone.inserirAtualizaTelefone(cliente.telefone)
        except:
            logPrioridade(f'UPDATE<atualizaCliente>___________________Erro({self.config.tblCliente})', TipoEdicao.erro, Prioridade.saidaImportante)
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
                escritorioId, nomeCliente, sobrenomeCliente, 
                idade, dataNascimento, email, 
                rgCliente, cpfCliente, nomeBanco, 
                agenciaBanco, numeroConta, grauEscolaridade, 
                senhaINSS, numCarteiraProf, nit, 
                nomeMae, estadoCivil, profissao, 
                endereco, numero, estado, 
                cidade, bairro, cep, 
                complemento, dataCadastro, dataUltAlt
            )
            VALUES
            (
                '{self.escritorio.escritorioId}', '{cliente.nomeCliente}', '{cliente.sobrenomeCliente}',
                {cliente.idade}, '{cliente.dataNascimento}', '{cliente.email}', 
                '{cliente.rgCliente}', '{cliente.cpfCliente}', '{cliente.nomeBanco}', 
                '{cliente.agenciaBanco}', '{cliente.numeroConta}', '{cliente.grauEscolaridade}', 
                '{cliente.senhaINSS}', '{cliente.numCartProf}', '{cliente.nit}', 
                '{cliente.nomeMae}', '{cliente.estadoCivil}', '{cliente.profissao}', 
                '{cliente.endereco}', {cliente.numero}, '{cliente.estado}', 
                '{cliente.cidade}', '{cliente.bairro}', '{cliente.cep}', 
                '{cliente.complemento}', '{datetime.now()}', '{datetime.now()}'
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
                -- Clientes
                c.escritorioId, c.clienteId, c.nomeCliente, 
                c.sobrenomeCliente, c.idade, c.dataNascimento, 
                c.email, c.rgCliente, c.cpfCliente,
                c.nomeBanco, c.agenciaBanco, c.numeroConta, 
                c.pixCliente, c.grauEscolaridade, c.senhaINSS,
                c.numCarteiraProf, c.nit, c.nomeMae, 
                c.estadoCivil, c.profissao, endereco,
                c.estado, c.cidade, c.numero, 
                c.bairro, c.cep, c.complemento,
                c.dataCadastro, c.dataUltAlt,
                
                -- Telefones
                t.telefoneId, t.clienteId, t.numero, 
                t.tipoTelefone, t.pessoalRecado, t.ativo
                
            FROM cliente c
                LEFT JOIN telefones t
                    ON t.telefoneId  = 
                    (
                        SELECT 
                            MIN(t.telefoneId) 
                        FROM telefones t
                        WHERE t.clienteId = c.clienteId
                    )
            WHERE c.escritorioId = {self.escritorio.escritorioId}
            AND c.clienteId = {clienteId}
            """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaClienteById>___________________{self.config.tblCliente}', TipoEdicao.select, Prioridade.saidaComun)
            if returnInstance:
                return ClienteModelo().fromList(cursor.fetchone(), retornaInst=True)
            else:
                return cursor.fetchall()
        except IndexError:
            logPrioridade(f'SELECT<buscaClienteById>(IndexError)___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'IndexError - buscaClienteById({self.config.tblCliente}) <SELECT>')
        except:
            logPrioridade(f'SELECT<buscaClienteById>___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaClienteById({self.config.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaClienteByNit(self, clienteNit: str):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                -- Clientes
                c.escritorioId, c.clienteId, c.nomeCliente, 
                c.sobrenomeCliente, c.idade, c.dataNascimento, 
                c.email, c.rgCliente, c.cpfCliente,
                c.nomeBanco, c.agenciaBanco, c.numeroConta, 
                c.pixCliente, c.grauEscolaridade, c.senhaINSS,
                c.numCarteiraProf, c.nit, c.nomeMae, 
                c.estadoCivil, c.profissao, endereco,
                c.estado, c.cidade, c.numero, 
                c.bairro, c.cep, c.complemento,
                c.dataCadastro, c.dataUltAlt,
                
                -- Telefones
                t.telefoneId, t.clienteId, t.numero, 
                t.tipoTelefone, t.pessoalRecado, t.ativo
                
            FROM cliente c
                LEFT JOIN telefones t 
                    ON t.telefoneId  = 
                        (
                            SELECT 
                                MIN(t.telefoneId) 
                            FROM telefones t
                            WHERE t.clienteId = c.clienteId
                        ) 
            WHERE c.escritorioId = {self.escritorio.escritorioId}
            AND c.nit = {clienteNit}"""

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaClienteByNit>___________________{self.config.tblCliente}', TipoEdicao.select, Prioridade.saidaComun)
            return ClienteModelo().fromList(cursor.fetchone(), retornaInst=True)
        except IndexError:
            logPrioridade(f'SELECT<buscaClienteByNit>(IndexError)___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'IndexError - buscaClienteByNit({self.config.tblCliente}) <SELECT>')
        except:
            logPrioridade(f'SELECT<buscaClienteByNit>___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaClienteByNit({self.config.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaTodos(self, returnModel: bool = False):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                -- Clientes
                c.escritorioId, c.clienteId, c.nomeCliente, 
                c.sobrenomeCliente, c.idade, c.dataNascimento, 
                c.email, c.rgCliente, c.cpfCliente,
                c.nomeBanco, c.agenciaBanco, c.numeroConta, 
                c.pixCliente, c.grauEscolaridade, c.senhaINSS,
                c.numCarteiraProf, c.nit, c.nomeMae, 
                c.estadoCivil, c.profissao, endereco,
                c.estado, c.cidade, c.numero, 
                c.bairro, c.cep, c.complemento,
                c.dataCadastro, c.dataUltAlt,
                
                -- Telefones
                t.telefoneId, t.clienteId, t.numero, 
                t.tipoTelefone, t.pessoalRecado, t.ativo
                
            FROM cliente c
                LEFT JOIN telefones t
                    ON t.telefoneId  = 
                    (
                        SELECT 
                            MIN(t.telefoneId) 
                        FROM telefones t
                        WHERE t.clienteId = c.clienteId
                    )
            WHERE c.escritorioId = {self.escritorio.escritorioId}
            """

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

        except OperationalError:
            logPrioridade(f'SELECT<buscaTodos>(OperationalError)___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaTodos({self.config.tblCliente}) <SELECT>')
        except Exception as erro:
            print(f"{type(erro)} - {erro}")
            logPrioridade(f'SELECT<buscaTodos>({type(erro)})___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaTodos({self.config.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaIndicesByClienteId(self, clienteId: int, indices: list = []):
        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        if len(indices) == 0:
            indices.append('')

        # self.db.connect()
        cursor = self.db.cursor()

        if 0 <= len(indices) <= 1:

            strComando = f"""
            SELECT indicadores FROM cnisCabecalhos
                WHERE clienteId = {clienteId}
                    AND indicadores LIKE '%{indices[0]}%'
            
            UNION ALL
            
            SELECT indicadores FROM cnisContribuicoes
                WHERE clienteId = {clienteId}
                    AND indicadores LIKE '%{indices[0]}%'
            
            UNION ALL
            
            SELECT indicadores FROM cnisRemuneracoes
                WHERE clienteId = {clienteId}
                    AND indicadores LIKE '%{indices[0]}%';"""
        else:
            strOr: str = ''
            for condicao in indices:
                strOr += f"""
                indicadores LIKE '%{condicao}%' OR"""
            strOr = strOr.removesuffix(' OR')

            strComando = f"""
            SELECT indicadores FROM cnisCabecalhos
                WHERE clienteId = {clienteId}
                    AND ({strOr})

            UNION ALL

            SELECT indicadores FROM cnisContribuicoes
                WHERE clienteId = {clienteId}
                    AND ({strOr})

            UNION ALL

            SELECT indicadores FROM cnisRemuneracoes
                WHERE clienteId = {clienteId}
                    AND ({strOr})"""

        try:
            cursor.execute(strComando)
            logPrioridade(
                f'INSERT<getIndicesByClienteId>___________________({self.config.tblCnisCabecalhos}, {self.config.tblCnisContribuicoes}, {self.config.tblCnisRemuneracoes})',
                TipoEdicao.select, Prioridade.saidaComun)
            return cursor.fetchall()
        except:
            logPrioridade(
                f'INSERT<getIndicesByClienteId>___________________({self.config.tblCnisCabecalhos}, {self.config.tblCnisContribuicoes}, {self.config.tblCnisRemuneracoes})',
                TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - getIndicesByClienteId({self.config.tblCnisContribuicoes}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaProxCliente(self, clienteId: int):
        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        # self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            SELECT
                -- Clientes
                c.escritorioId, c.clienteId, c.nomeCliente, 
                c.sobrenomeCliente, c.idade, c.dataNascimento, 
                c.email, c.rgCliente, c.cpfCliente,
                c.nomeBanco, c.agenciaBanco, c.numeroConta, 
                c.pixCliente, c.grauEscolaridade, c.senhaINSS,
                c.numCarteiraProf, c.nit, c.nomeMae, 
                c.estadoCivil, c.profissao, endereco,
                c.estado, c.cidade, c.numero, 
                c.bairro, c.cep, c.complemento,
                c.dataCadastro, c.dataUltAlt,

                -- Telefones
                t.telefoneId, t.clienteId, t.numero, 
                t.tipoTelefone, t.pessoalRecado, t.ativo

            FROM cliente c
                LEFT JOIN telefones t
                    ON t.telefoneId  = 
                    (
                        SELECT 
                            MIN(t.telefoneId) 
                        FROM telefones t
                        WHERE t.clienteId = c.clienteId
                    )
            WHERE c.escritorioId = {self.escritorio.escritorioId}
                AND c.clienteId >= {clienteId}
            LIMIT 1;
            """

        try:
            cursor.execute(strComando)
            logPrioridade(f'SELECT<buscaProxCliente>___________________{self.config.tblCliente}', TipoEdicao.select, Prioridade.saidaComun)

            cliente = cursor.fetchone()
            if cliente is None:
                return self.buscaProxCliente(0)
            else:
                clienteModel = ClienteModelo().fromList(cliente, retornaInst=True)
                return clienteModel

        except OperationalError:
            logPrioridade(f'SELECT<buscaProxCliente>(OperationalError)___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaProxCliente({self.config.tblCliente}) <SELECT>')
        except Exception as erro:
            print(f"{type(erro)} - {erro}")
            logPrioridade(f'SELECT<buscaProxCliente>({type(erro)})___________________{self.config.tblCliente}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - buscaProxCliente({self.config.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()
