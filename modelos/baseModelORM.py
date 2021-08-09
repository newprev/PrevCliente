from peewee import SqliteDatabase, Model

database = SqliteDatabase('Daos/producao.db')

DATEFORMATS = ['%d/%m/%Y', '%d/%Y']


class BaseModel(Model):
    class Meta:
        database = database
