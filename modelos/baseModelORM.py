from peewee import SqliteDatabase, Model

database = SqliteDatabase('Daos/producao.db')


class BaseModel(Model):
    class Meta:
        database = database
