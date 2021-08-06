from modelos.baseModelORM import BaseModel

from datetime import datetime
from peewee import AutoField, IntegerField, CharField, DateTimeField

class Escritorios(BaseModel):
    escritorioId = AutoField(column_name='escritorioId', null=True)
    bairro = CharField(null=True)
    cep = CharField(null=True)
    cidade = CharField(null=True)
    cnpj = CharField(null=True)
    complemento = CharField(null=True)
    cpf = CharField(null=True)
    email = CharField(null=True)
    endereco = CharField(null=True)
    estado = CharField(default='SP')
    inscEstadual = CharField(column_name='inscEstadual', null=True)
    nomeEscritorio = CharField(column_name='nomeEscritorio')
    nomeFantasia = CharField(column_name='nomeFantasia')
    numero = IntegerField(null=True)
    telefone = CharField(null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'escritorios'

    def __bool__(self):
        return self.escritorioId is not None
