from modelos.baseModelORM import BaseModel

from peewee import AutoField, CharField

class EspecieBenef(BaseModel):
    especieId = AutoField(column_name='especieId', null=True)
    descricao = CharField()

    class Meta:
        table_name = 'especieBenef'