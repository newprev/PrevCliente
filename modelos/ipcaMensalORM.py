from logging import info, debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, DateField, DateTimeField, FloatField
from datetime import datetime

TABLENAME = 'ipcaMensal'


class IpcaMensal(BaseModel, Model):
    ipcaId = AutoField(column_name='ipcaId', null=True)
    dataReferente = DateField(column_name='dataReferente', formats=DATEFORMATS)
    valor = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'ipcaMensal'

    def toDict(self):
        dictIndiceAtuMonetario = {
            'ipcaId': self.ipcaId,
            'dataReferente': self.dataReferente,
            'valor': self.valor,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictIndiceAtuMonetario

    def fromDict(self, dictIpcaMensal):
        self.ipcaId = dictIpcaMensal['ipcaId']
        self.dataReferente = dictIpcaMensal['dataReferente']
        self.valor = dictIpcaMensal['valor']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        IpcaMensal(
           ipcaId: {self.ipcaId},
           dataReferente: {self.dataReferente},
           valor: {self.valor},
           dataCadastro: {self.dataCadastro},
           dataUltAlt: {self.dataUltAlt}
       )""")


@post_save(sender=IpcaMensal)
def inserindoIpcaMensal(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoIpcaMensal___________________{TABLENAME}')


@pre_delete(sender=IpcaMensal)
def deletandoIpcaMensal(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoIpcaMensal___________________{TABLENAME}')
