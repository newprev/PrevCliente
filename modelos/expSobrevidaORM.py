from modelos.baseModelORM import BaseModel

from datetime import datetime
from peewee import AutoField, DateField, IntegerField, DateTimeField


class ExpSobrevida(BaseModel):
    infoId = AutoField(column_name='infoId', null=True)
    dataReferente = DateField(column_name='dataReferente')
    expectativaSobrevida = IntegerField(column_name='expectativaSobrevida')
    idade = IntegerField(null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'expSobrevida'