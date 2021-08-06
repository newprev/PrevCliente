from modelos.baseModelORM import BaseModel

from peewee import CharField, DateTimeField
from datetime import datetime


class Indicadores(BaseModel):
    indicadorId = CharField(column_name='indicadorId', null=True, primary_key=True)
    descricao = CharField()
    fonte = CharField()
    resumo = CharField()
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'indicadores'