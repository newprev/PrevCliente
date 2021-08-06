from modelos.baseModelORM import BaseModel

from datetime import datetime
from peewee import AutoField, DateField, BooleanField, CharField, DateTimeField, FloatField


class ConvMon(BaseModel):
    convMonId = AutoField(column_name='convMonId', null=True)
    conversao = CharField(null=False)
    dataFinal = DateField(column_name='dataFinal')
    dataInicial = DateField(column_name='dataInicial', null=False)
    fator = FloatField(null=False)
    moedaCorrente = BooleanField(column_name='moedaCorrente')
    nomeMoeda = CharField(column_name='nomeMoeda')
    sinal = CharField(null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'convMon'