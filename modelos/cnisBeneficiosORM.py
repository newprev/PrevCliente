from modelos.baseModelORM import BaseModel
from modelos.clientesORM import Cliente

from peewee import AutoField, CharField, ForeignKeyField, DateTimeField, BigIntegerField, DateField, IntegerField
from datetime import datetime


class CnisBeneficios(BaseModel):
    beneficiosId = AutoField(column_name='beneficiosId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    dado_origem = CharField(column_name='dadoOrigem', default='CNIS')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_fim = DateField(column_name='dataFim')
    data_inicio = DateField(column_name='dataInicio')
    dataUltAlt = DateTimeField(column_name='dataUltAlt')
    especie = CharField()
    nb = BigIntegerField()
    seq = IntegerField()
    situacao = CharField()

    class Meta:
        table_name = 'cnisBeneficios'