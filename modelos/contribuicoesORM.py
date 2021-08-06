from modelos.baseModelORM import BaseModel
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, ForeignKeyField, FloatField, DateTimeField, DateField, IntegerField
from datetime import datetime


class CnisContribuicoes(BaseModel, Model):
    contribuicoesId = AutoField(column_name='contribuicoesId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    seq = IntegerField(null=False)
    competencia = DateField(null=False)
    contribuicao = FloatField(null=False)
    dadoOrigem = CharField(column_name='dadoOrigem')
    dataPagamento = DateField(column_name='dataPagamento')
    indicadores = CharField(default=None)
    salContribuicao = FloatField(column_name='salContribuicao')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'cnisContribuicoes'

    def toDict(self):
        dictUsuario = {
            'contribuicoesId': self.contribuicoesId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'competencia': self.competencia,
            'dataPagamento': self.dataPagamento,
            'contribuicao': self.contribuicao,
            'salContribuicao': self.salContribuicao,
            'indicadores': self.indicadores,
            'dadoOrigem': self.dadoOrigem,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictContribuicoes):
        self.contribuicoesId = dictContribuicoes['contribuicoesId']
        self.clienteId = dictContribuicoes['clienteId']
        self.seq = dictContribuicoes['seq']
        self.competencia = dictContribuicoes['competencia']
        self.dataPagamento = dictContribuicoes['dataPagamento']
        self.contribuicao = dictContribuicoes['contribuicao']
        self.salContribuicao = dictContribuicoes['salContribuicao']
        self.indicadores = dictContribuicoes['indicadores']
        self.dadoOrigem = dictContribuicoes['dadoOrigem']
        self.dataCadastro = dictContribuicoes['dataCadastro']
        self.dataUltAlt = dictContribuicoes['dataUltAlt']

    def prettyPrint(self):
        return f"""
        Contribuicoes(
            contribuicoesId: {self.contribuicoesId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            competencia: {self.competencia},
            dataPagamento: {self.dataPagamento},
            contribuicao: {self.contribuicao},
            salContribuicao: {self.salContribuicao},
            indicadores: {self.indicadores},
            dadoOrigem: {self.dadoOrigem},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )
            """


@post_save(sender=CnisContribuicoes)
def inserindoCnisContribuicoes(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoCnisContribuicoes>___________________{CnisContribuicoes.Meta.table_name}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoCnisContribuicoes>___________________ |Erro| {CnisContribuicoes.Meta.table_name}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=CnisContribuicoes)
def deletandoCnisContribuicoes(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoCnisContribuicoes>___________________{CnisContribuicoes.Meta.table_name}', TipoEdicao.delete, Prioridade.saidaImportante)
