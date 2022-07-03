from logging import info, debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import DateField, DateTimeField, AutoField, FloatField
from datetime import datetime

TABLENAME = 'tetosPrev'


class TetosPrev(BaseModel, Model):
    tetosPrevId = AutoField(column_name='tetosPrevId', null=True)
    dataValidade = DateField(column_name='dataValidade', formats=DATEFORMATS)
    valor = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'tetosPrev'
        
    def toDict(self):
        dictTetosPrev = {
            'tetosPrevId': self.tetosPrevId,
            'dataValidade': self.dataValidade,
            'valor': self.valor
        }
        return dictTetosPrev

    def fromDict(self, dictTeto):
        self.tetosPrevId = dictTeto['tetosPrevId']
        self.dataValidade = dictTeto['dataValidade']
        self.valor = dictTeto['valor']
        self.dataUltAlt = datetime.now()
        self.dataCadastro = datetime.now()
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        TetosPrevModelo(
            tetosPrevId: {self.tetosPrevId},
            dataValidade: {self.dataValidade},
            valor: {self.valor}
        )""")
    
    
@post_save(sender=TetosPrev)
def inserindoTetosPrev(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoTetosPrev___________________{TABLENAME}')


@pre_delete(sender=TetosPrev)
def deletandoTetosPrev(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoTetosPrev___________________{TABLENAME}')
