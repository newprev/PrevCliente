from modelos.baseModelORM import BaseModel
from modelos.clientesORM import Cliente

from peewee import AutoField, CharField, ForeignKeyField, DateTimeField, FloatField, DateField, IntegerField
from datetime import datetime


class CnisRemuneracoes(BaseModel):
    remuneracoesId = AutoField(column_name='remuneracoesId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, null=True)
    seq = IntegerField(null=False)
    competencia = DateField(null=False)
    dadoOrigem = CharField(column_name='dadoOrigem')
    remuneracao = FloatField()
    indicadores = CharField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'cnisRemuneracoes'
