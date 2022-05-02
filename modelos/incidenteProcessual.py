from logging import debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete

from modelos.processosORM import Processos
from util.enums.logEnums import TipoLog

from peewee import AutoField, CharField, DateTimeField, ForeignKeyField, IntegerField, DateField
from datetime import datetime

TABLENAME = 'incidenteProcessual'


class IncidenteProcessual(BaseModel, Model):
    incidenteId = AutoField(column_name='incidenteId', null=True)
    processoId = ForeignKeyField(column_name='processoId', field='processoId', model=Processos, backref='Processos')
    seq = IntegerField(column_name='seq')
    dataIncidente = DateField(column_name='dataIncidente', null=False, formats=DATEFORMATS)
    andamento = IntegerField(column_name='andamento', default=0)
    descricao = CharField(column_name='descricao', max_length=3000)
    codAndamento = IntegerField(column_name='codAndamento', default=None)    
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'IncidenteProcessual'

    def toDict(self):
        dictUsuario = {
            'incidenteId': self.incidenteId,
            'processoId': self.processoId,
            'seq': self.seq,
            'andamento': self.andamento,
            'descricao': self.descricao,
            'codAndamento': self.codAndamento,
        }
        return dictUsuario

    def fromDict(self, dictCliente):
        self.incidenteId = dictCliente['incidenteId']
        self.processoId = dictCliente['processoId']
        self.seq = dictCliente['seq']
        self.andamento = dictCliente['andamento']
        self.descricao = dictCliente['descricao']
        self.codAndamento = dictCliente['codAndamento']

    def __bool__(self):
        return self.descricao != '' and self.descricao is not None

    def prettyPrint(self):

        print("IncidenteProcessual:")
        objeto: dict = self.toDict()

        for chave, valor in objeto.items():
            print(f"{chave}: {valor}")


@post_save(sender=IncidenteProcessual)
def inserindoIncidenteProcessual(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoIncidenteProcessual ___________________{TABLENAME}')


@pre_delete(sender=IncidenteProcessual)
def deletandoIncidenteProcessual(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoIncidenteProcessual ___________________{TABLENAME}')
