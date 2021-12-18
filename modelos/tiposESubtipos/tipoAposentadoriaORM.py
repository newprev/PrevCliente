from modelos.baseModelORM import BaseModel
from playhouse.signals import Model

from peewee import CharField, DateTimeField
from datetime import datetime

TABLENAME = 'tipoAposentadoria'


class TipoAposentadoria(BaseModel, Model):
    tipoAposentadoriaId = CharField(column_name='tipoAposentadoriaId')
    descricao = CharField(column_name='descricao')
    baseLegal = CharField(column_name='baseLegal', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'tipoAposentadoria'

    def toDict(self):
        dictUsuario = {
            'tipoAposentadoriaId': self.tipoAposentadoriaId,
            'descricao': self.descricao,
            'baseLegal': self.baseLegal,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictBeneficios):
        self.tipoAposentadoriaId = dictBeneficios['tipoAposentadoriaId']
        self.descricao = dictBeneficios['descricao']
        self.baseLegal = dictBeneficios['baseLegal']
        self.dataCadastro = dictBeneficios['dataCadastro']
        self.dataUltAlt = dictBeneficios['dataUltAlt']

    def prettyPrint(self):
        print(f"""
        TipoAposentadoria(
            tipoAposentadoriaId: {self.tipoAposentadoriaId},
            descricao: {self.descricao},
            baseLegal: {self.baseLegal},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")
