import sqlite3

from connections import ConfigConnection
from Daos.tabelas import TabelasConfig
from logs import logPrioridade
from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio
# from modelos.processosModelo import ProcessosModelo
# from modelos.advogadoModelo import AdvogadoModelo
# from modelos.escritorioModelo import EscritorioModelo
# from modelos.clienteModelo import ClienteModelo
from datetime import datetime

from newPrevEnums import TipoEdicao, Prioridade


class DaoProcessos:

    def __init__(self, db=None):
        self.db = db
        self.config = ConfigConnection()
        self.tabelas = TabelasConfig()
        self.cacheLogin = CacheLogin()
        self.cacheEscritorio = CacheEscritorio()
        # self.advogado: AdvogadoModelo = self.cacheLogin.carregarCache()
        # self.escritorio: EscritorioModelo = self.cacheEscritorio.carregarCache()
        if not self.advogado:
            self.advogado = self.cacheLogin.carregarCacheTemporario()
        if not self.escritorio:
            self.escritorio = self.cacheEscritorio.carregarCacheTemporario()

    # def insereProcesso(self, processo: ProcessosModelo):
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         INSERT INTO {self.tabelas.tblProcessos}
    #         (
    #             clienteId , advogadoId, numeroProcesso,
    #             natureza, tipoProcesso, tipoBeneficio,
    #             subTipoApos, estado, cidade,
    #             situacaoId, tempoContribuicao, pontuacao,
    #             dib, der, mediaSalarial,
    #             dataInicio, dataFim, valorCausa,
    #             dataCadastro, dataUltAlt
    #         )
    #         VALUES
    #         (
    #             {processo.clienteId}, {self.advogado.advogadoId}, '{processo.numeroProcesso}',
    #             {processo.natureza}, {processo.tipoProcesso}, {processo.tipoBeneficio},
    #             {processo.subTipoApos}, '{processo.estado}', '{processo.cidade}',
    #             {processo.situacaoId}, {processo.tempoContribuicao}, {processo.pontuacao},
    #             '{processo.dib}', '{processo.der}', {processo.mediaSalarial},
    #             '{processo.dataInicio}', '{processo.dataFim}', {processo.valorCausa},
    #             '{datetime.now()}', '{datetime.now()}'
    #         )"""
    #
    #     try:
    #         cursor.execute(strComando)
    #         processoId = cursor.lastrowid
    #         logPrioridade(f'INSERT<insereProcesso>___________________{self.tabelas.tblProcessos} ({processoId})', TipoEdicao.insert, Prioridade.saidaComun)
    #         return processoId
    #     except:
    #         raise Warning(f'Erro SQL - insereProcesso({self.config.banco}) <INSERT {self.tabelas.tblProcessos}>')
    #     finally:
    #         self.db.commit()
    #         self.disconectBD(cursor)

    # def atualizaProcesso(self, processo: ProcessosModelo):
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         UPDATE {self.tabelas.tblProcessos}
    #             SET
    #                 clienteId = {processo.clienteId},
    #                 advogadoId = {self.advogado.advogadoId},
    #                 numeroProcesso = {processo.numeroProcesso},
    #                 natureza = {processo.natureza},
    #                 tipoProcesso = {processo.tipoProcesso},
    #                 tipoBeneficio = {processo.tipoBeneficio},
    #                 subTipoApos = {processo.subTipoApos},
    #                 estado = '{processo.estado}',
    #                 cidade = '{processo.cidade}',
    #                 situacaoId = {processo.situacaoId},
    #                 tempoContribuicao = {processo.tempoContribuicao},
    #                 pontuacao = {processo.pontuacao},
    #                 dib = '{processo.dib}',
    #                 der = '{processo.der}',
    #                 dataInicio = {processo.dataInicio},
    #                 dataFim = {processo.dataFim},
    #                 valorCausa = {processo.valorCausa},
    #                 dataUltAlt = {datetime.now()}
    #             WHERE
    #                 processoId = {processo.processoId}
    #                 """
    #
    #     try:
    #         cursor.execute(strComando)
    #         logPrioridade(f'UPDATE<atualizaProcesso>___________________{self.tabelas.tblProcessos}', TipoEdicao.update, Prioridade.saidaComun)
    #     except:
    #         raise Warning(f'Erro SQL - atualizaProcesso({self.config.banco}) <UPDATE {self.tabelas.tblProcessos}>')
    #     finally:
    #         self.db.commit()
    #         self.disconectBD(cursor)

    def buscaProcessoPorId(self):
        pass

    def buscaProcessoPorTipo(self):
        pass

    # def buscaProcessoPorCliente(self, cliente: ClienteModelo, limit: int = 0) -> list:
    #     if not isinstance(self.db, sqlite3.Connection):
    #         self.db.ping()
    #
    #     # self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         SELECT
    #             processoId, clienteId, advogadoId,
    #             numeroProcesso, natureza, tipoProcesso,
    #             tipoBeneficio, subTipoApos, estado,
    #             cidade, situacaoId, tempoContribuicao,
    #             pontuacao, dib, der,
    #             mediaSalarial, dataInicio, dataFim,
    #             valorCausa, dataCadastro, dataUltAlt
    #         FROM {self.tabelas.tblProcessos}
    #         WHERE clienteId = {cliente.clienteId}"""
    #
    #     if limit != 0:
    #         strComando += f"""
    #             LIMIT {limit};"""
    #
    #     try:
    #         cursor.execute(strComando)
    #         processos = cursor.fetchall()
    #         logPrioridade(f'SELECT<buscaProcessoPorCliente>___________________{self.tabelas.tblProcessos}', TipoEdicao.select, Prioridade.saidaComun)
    #
    #         if len(processos) == 1:
    #             return [ProcessosModelo().fromList(processos[0], retornaInst=True)]
    #         elif len(processos) == 0:
    #             return [ProcessosModelo()]
    #         else:
    #             listaProcessos = []
    #             for processo in processos:
    #                 listaProcessos.append(ProcessosModelo().fromList(processo, retornaInst=True))
    #             return listaProcessos
    #     except:
    #         raise Warning(f'Erro SQL - buscaProcessoPorCliente({self.config.banco}) <INSERT {self.tabelas.tblProcessos}>')
    #     finally:
    #         self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        # self.db.close()