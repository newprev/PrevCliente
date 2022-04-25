from logging import info, debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, DateField, DateTimeField, BigIntegerField, FloatField
from datetime import datetime

TABLENAME = 'indiceAtuMonetaria'


class IndiceAtuMonetaria(BaseModel, Model):
    indiceId = AutoField(column_name='indiceId', null=True)
    dataReferente = DateField(column_name='dataReferente', formats=DATEFORMATS)
    dib = DateField(column_name='dib', formats=DATEFORMATS)
    fator = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'indiceAtuMonetaria'

    def toDict(self):
        dictIndiceAtuMonetario = {
            'indiceId': self.indiceId,
            'dataReferente': self.dataReferente,
            'dib': self.dib,
            'fator': self.fator,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictIndiceAtuMonetario

    def fromDict(self, dictIndiceAtuMonetario):
        self.indiceId = dictIndiceAtuMonetario['indiceId']
        self.dataReferente = dictIndiceAtuMonetario['dataReferente']
        self.dib = dictIndiceAtuMonetario['dib']
        self.fator = dictIndiceAtuMonetario['fator']
        self.dataCadastro = dictIndiceAtuMonetario['dataCadastro']
        self.dataUltAlt = dictIndiceAtuMonetario['dataUltAlt']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        IndiceAtuMonetarioModelo(
           indiceId: {self.indiceId},
           dataReferente: {self.dataReferente},
           dib: {self.dib},
           fator: {self.fator},
           dataCadastro: {self.dataCadastro},
           dataUltAlt: {self.dataUltAlt}
       )""")
        
        
@post_save(sender=IndiceAtuMonetaria)
def inserindoIndiceAtuMonetaria(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoIndiceAtuMonetaria___________________{TABLENAME}')


@pre_delete(sender=IndiceAtuMonetaria)
def deletandoIndiceAtuMonetaria(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoIndiceAtuMonetaria___________________{TABLENAME}')
