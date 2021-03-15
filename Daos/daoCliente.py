from datetime import datetime

from Daos.tabelas import TabelasConfig
from connections import ConfigConnection
from helpers import mascaraDataSql
from modelos.clienteModelo import ClienteModelo
from pymysql import connections, cursors
import pprint


class DaoCliente:

    def __init__(self, db: connections=None):
        self.db = db
        self.config = TabelasConfig()

    def cadastroClienteComCnis(self, cliente: ClienteModelo, dictAllInfo: dict):
        self.db.connect()
        cursor: cursors = self.db.cursor()
        clienteId = 0

        # print('\ncadastroClienteComCnis')
        # print(f'db: {self.db}')
        # print(cliente)
        # for chave, valor in dictAllInfo.items():
        #     print(f"{chave}:")
        #     for key, value in valor.items():
        #         print(f'   {key}:{len(value)}')

        strComando = f"""INSERT INTO {self.config.tblCliente} 
                        (
                            nomeCliente, sobrenomeCliente, telefone,
                            email, rgCliente, cpfCliente,
                            numCarteiraProf, nit, nomeMae,
                            estadoCivil, profissao, endereco,
                            estado, cidade, bairro,
                            cep, complemento, dataCadastro,
                            dataUltAlt
                        )
                        VALUES
                        (
                            '{cliente.nomeCliente}', '{cliente.sobrenomeCliente}', '{cliente.telefone}',
                            '{cliente.email}', '{cliente.rgCliente}', '{cliente.cpfCliente}',
                            '{cliente.numCartProf}', '{cliente.nit}', '{cliente.nomeMae}',
                            '{cliente.estadoCivil}', '{cliente.profissao}', '{cliente.endereco}',
                            '{cliente.estado}', '{cliente.cidade}', '{cliente.bairro}',
                            '{cliente.cep}', '{cliente.complemento}', NOW(), 
                            NOW()
                        )"""

        try:
            cursor.execute(strComando)
            clienteId = cursor.lastrowid

            # Verifica se há benefícios para inserir no banco
            strComando = self.insertSqlBenecifio(dictAllInfo['cabecalhoBeneficio'], clienteId)
            if strComando != '':
                try:
                    cursor.execute(strComando)
                except:
                    raise Warning(f'Erro SQL - cadastroClienteComCnis({self.config.tblCnisBeneficios}) <INSERT>')

            # Verifica se há contribuições para inserir no banco
            strComando = self.insertSqlContribuicoes(dictAllInfo['contribuicoes'], clienteId)
            if strComando != '':
                try:
                    print(strComando)
                    cursor.execute(strComando)
                except:
                    raise Warning(
                        f'Erro SQL - cadastroClienteComCnis({self.config.tblCnisBeneficios}) <INSERT>')


            self.db.commit()
        except:
            raise Warning(f'Erro SQL - cadastroClienteComCnis({self.config.tblCliente}) <INSERT>')
        finally:
            self.disconectBD(cursor)

    def insertSqlBenecifio(self, beneficio: dict, clienteId: int) -> str:
        strComando = ''
        if len(beneficio['Seq']) > 0 and clienteId != None and clienteId != 0:
            strComando = f"""
                INSERT INTO {self.config.tblCnisBeneficios}
                    (
                        clienteId, seq, nb,
                        especie, dataInicio, dataFim,
                        situacao, dataCadastro, dataUltAlt
                    )
                VALUES """

            for i in range(0, len(beneficio['Seq'])):
                if i != 0:
                    strComando += ', '
                strComando += f""" 
                    (
                        {clienteId}, {beneficio['Seq'][i]}, {beneficio['NB'][i]},
                        '{beneficio['especie'][i]}', '{mascaraDataSql(beneficio['dataInicio'][i])}', '{mascaraDataSql(beneficio['dataFim'][i])}',
                        '{beneficio['situacao'][i]}', NOW(), NOW()
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
                                indicadores, dataCadastro, dataUltAlt
                            )
                        VALUES """

            for i in range(0, len(contribuicoes['Seq'])):
                if i != 0:
                    strComando += ', '
                strComando += f""" 
                            (
                                {clienteId}, {contribuicoes['Seq'][i]}, '{mascaraDataSql(contribuicoes['competencia'][i], short=True)}',
                                '{mascaraDataSql(contribuicoes['dataPagamento'][i])}', {contribuicoes['contribuicao'][i]}, {contribuicoes['salContribuicao'][i]},
                                '{contribuicoes['indicadores'][i]}', NOW(), NOW()
                            )"""
            return strComando
        else:
            return ''


    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()