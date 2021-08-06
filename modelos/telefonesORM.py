from modelos.baseModelORM import BaseModel
from modelos.clientesORM import Cliente

from peewee import CharField, DateTimeField, AutoField, ForeignKeyField, BooleanField
from datetime import datetime


class Telefones(BaseModel):
    telefoneId = AutoField(column_name='telefoneId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    ativo = BooleanField(default=True)
    numero = CharField(null=False)
    pessoalRecado = CharField(column_name='pessoalRecado')
    tipoTelefone = CharField(column_name='tipoTelefone')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'telefones'