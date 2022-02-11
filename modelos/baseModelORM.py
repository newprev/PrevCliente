from peewee import SqliteDatabase, Model
from util.enums.databaseEnums import DatabaseEnum

database = SqliteDatabase(DatabaseEnum.producao.value)

DATEFORMATS = ['%d/%m/%Y', '%m/%Y']


class BaseModel(Model):
    class Meta:
        database = database
