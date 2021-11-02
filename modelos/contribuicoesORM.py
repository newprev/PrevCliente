from modelos.baseModelORM import BaseModel, DATEFORMATS
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete
from systemLog.logs import logPrioridade
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, ForeignKeyField, FloatField, DateTimeField, DateField, IntegerField
from datetime import datetime

TABLENAME = 'cnisContribuicoes'


class CnisContribuicoes(BaseModel, Model):
    contribuicoesId = AutoField(column_name='contribuicoesId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    seq = IntegerField(null=False)
    competencia = DateField(null=False, formats=DATEFORMATS)
    contribuicao = FloatField(null=True)
    dadoOrigem = CharField(column_name='dadoOrigem', default='CNIS')
    dataPagamento = DateField(column_name='dataPagamento', formats=DATEFORMATS)
    indicadores = CharField(default=None)
    salContribuicao = FloatField(column_name='salContribuicao')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'cnisContribuicoes'

    def toDict(self):
        dictContribuicao = {
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
        return dictContribuicao

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

    def prettyPrint(self, backRef: bool = False):
        print(f"""
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
        )""")


@post_save(sender=CnisContribuicoes)
def inserindoCnisContribuicoes(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoCnisContribuicoes>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoCnisContribuicoes>___________________ |Erro| {TABLENAME}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=CnisContribuicoes)
def deletandoCnisContribuicoes(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoCnisContribuicoes>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)
