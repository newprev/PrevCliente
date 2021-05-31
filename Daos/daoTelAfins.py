import sqlite3
from datetime import datetime

from Daos.tabelas import TabelasConfig
from connections import ConfigConnection
from logs import logPrioridade
from modelos.telefoneModelo import TelefoneModelo
from newPrevEnums import TipoEdicao, Prioridade


class DaoTelAfins:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()
        self.tabelas = TabelasConfig()

    def inserirAtualizaTelefone(self, telefone: TelefoneModelo):

        if not isinstance(self.db, sqlite3.Connection):
            self.db.ping()

        cursor = self.db.cursor()

        strComando = f"""
            SELECT MIN(telefoneId) FROM {self.tabelas.tblTelefones}
	            WHERE clienteId = 3;
            """
        try:
            cursor.execute(strComando)
            fetch = cursor.fetchone()[0]
            if fetch is None:
                print(f"len(cursor.fetchall()) == 0")
                print(telefone)
                strComando = f"""
                            INSERT INTO {self.tabelas.tblTelefones}
                            (
                                clienteId, numero, tipoTelefone,
                                pessoalRecado, ativo, dataCadastro,
                                dataUltAlt
                            )
                            VALUES 
                            (
                                {telefone.clienteId}, '{telefone.numero}', '{telefone.tipoTelefone}',
                                '{telefone.pessoalRecado}', {telefone.ativo}, '{datetime.now()}',
                                '{datetime.now()}'
                            )"""

                cursor.execute(strComando)
                telefoneId = cursor.lastrowid
                logPrioridade(f'INSERT<inserirTelefone>___________________{self.tabelas.tblTelefones} ({telefoneId})', TipoEdicao.insert, Prioridade.saidaComun)
            else:
                print(f"len(cursor.fetchall()) != 0")
                strComando = f"""
                    UPDATE {self.tabelas.tblTelefones} SET
                        numero = '{telefone.numero}',
                        tipoTelefone = '{telefone.tipoTelefone}',
                        pessoalRecado = '{telefone.ativo}',
                        dataUltAlt = '{datetime.now()}'
                    WHERE telefoneId = {telefone.telefoneId}
                    """
                print(strComando)
                cursor.execute(strComando)
                logPrioridade(f'UPDATE<inserirTelefone>___________________{self.tabelas.tblTelefones}', TipoEdicao.update, Prioridade.saidaComun)
        except Exception as err:
            print(f"inserirAtualizaTelefone: {err}({type(err)})")
            logPrioridade(f'INSERT/UPDATE<inserirAtualizaTelefone>___________________Erro{self.tabelas.tblTelefones}', TipoEdicao.erro, Prioridade.saidaImportante)
            raise Warning(f'Erro SQL - inserirAtualizaTelefone({self.config.banco}) <INSERT/UPDATE {self.tabelas.tblTelefones}>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()
