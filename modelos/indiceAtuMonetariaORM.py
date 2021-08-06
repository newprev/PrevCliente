from modelos.baseModelORM import BaseModel

from peewee import AutoField, DateField, DateTimeField, BigIntegerField, FloatField
from datetime import datetime


class IndiceAtuMonetaria(BaseModel):
    indiceId = AutoField(column_name='indiceId', null=True)
    dataReferente = DateField(column_name='dataReferente')
    dib = BigIntegerField()
    fator = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'indiceAtuMonetaria'