from modelos.baseModelORM import BaseModel
from modelos.clientesORM import Cliente

from peewee import AutoField, CharField, ForeignKeyField, FloatField, DateTimeField, DateField, IntegerField
from datetime import datetime


class CnisContribuicoes(BaseModel):
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