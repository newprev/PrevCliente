from modelos.baseModelORM import BaseModel
from modelos.clientesORM import Cliente

from peewee import DateField, DateTimeField, IntegerField, ForeignKeyField, CharField
from datetime import datetime


class Ppp(BaseModel):
    pppId = IntegerField(column_name='pppId', null=True, primary_key=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    caEpi = CharField(column_name='caEpi', null=True)
    cnae = CharField(null=True)
    cnpj = CharField(null=True)
    ctps = CharField(null=True)
    dataAdminssao = DateField(column_name='dataAdminssao', null=True)
    dataNascimento = DateField(column_name='dataNascimento')
    dataRegistro = DateField(column_name='dataRegistro', null=True)
    eficEpc = CharField(column_name='eficEpc', null=True)
    eficEpi = CharField(column_name='eficEpi', null=True)
    exposicaoDataFim = DateField(column_name='exposicaoDataFim', null=True)
    exposicaoDataInicio = DateField(column_name='exposicaoDataInicio', null=True)
    exposicaoFator = CharField(column_name='exposicaoFator', null=True)
    exposicaoIntensidade = CharField(column_name='exposicaoIntensidade', null=True)
    exposicaoTecnicaUtilizada = CharField(column_name='exposicaoTecnicaUtilizada', null=True)
    exposicaoTipo = CharField(column_name='exposicaoTipo', null=True)
    genero = CharField()
    nit = CharField()
    nomeEmpresa = CharField(column_name='nomeEmpresa', null=True)
    numCAT = CharField(column_name='numCAT', null=True)
    profissiografiaData = DateField(column_name='profissiografiaData', null=True)
    profissiografiaDesc = CharField(column_name='profissiografiaDesc', null=True)
    sitEmpregado = CharField(column_name='sitEmpregado', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'ppp'