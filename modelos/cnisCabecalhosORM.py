from modelos.baseModelORM import BaseModel
from modelos.clientesORM import Cliente

from peewee import AutoField, CharField, ForeignKeyField, BooleanField, BigIntegerField, DateField, IntegerField, DateTimeField
from datetime import datetime

class CnisCabecalhos(BaseModel):
    cabecalhosId = AutoField(column_name='cabecalhosId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente)
    seq = IntegerField(null=False)
    cdEmp = CharField(column_name='cdEmp', null=True)
    dadoFaltante = BooleanField(column_name='dadoFaltante', default=False)
    dadoOrigem = CharField(column_name='dadoOrigem', default='CNIS')
    dataFim = DateField(column_name='dataFim', null=True)
    dataInicio = DateField(column_name='dataInicio')
    especie = CharField(null=True)
    indicadores = CharField(null=True)
    nb = BigIntegerField(null=True)
    nit = CharField(null=False)
    nomeEmp = CharField(column_name='nomeEmp', null=True)
    orgVinculo = CharField(column_name='orgVinculo', null=True)
    situacao = CharField(null=True)
    tipoVinculo = CharField(column_name='tipoVinculo', null=True)
    ultRem = DateField(column_name='ultRem', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'cnisCabecalhos'
