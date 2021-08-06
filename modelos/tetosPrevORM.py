from modelos.baseModelORM import BaseModel

from peewee import DateField, DateTimeField, AutoField, FloatField
from datetime import datetime


class TetosPrev(BaseModel):
    tetosPrevId = AutoField(column_name='tetosPrevId', null=True)
    dataValidade = DateField(column_name='dataValidade')
    valor = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'tetosPrev'