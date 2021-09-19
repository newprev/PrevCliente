from peewee import SqliteDatabase, Model

database = SqliteDatabase('Daos/producao.db')

DATEFORMATS = ['%d/%m/%Y', '%m/%Y']


class BaseModel(Model):
    class Meta:
        database = database
