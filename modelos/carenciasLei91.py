from logging import info

from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, DateField, DateTimeField, BigIntegerField
from datetime import datetime

TABLENAME = 'carenciaLei91'


class CarenciaLei91(BaseModel, Model):
    carenciaId = AutoField(column_name='indiceId', null=True)
    dataImplemento = DateField(column_name='dataReferente', formats=DATEFORMATS)
    tempoContribuicao = BigIntegerField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'carenciaLei91'

    def toDict(self):
        dictIndiceAtuMonetario = {
            'carenciaId': self.indiceId,
            'dataImplemento': self.dataImplemento,
            'tempoContribuicao': self.tempoContribuicao,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictIndiceAtuMonetario

    def fromDict(self, dictCarenciaLei91):
        self.carenciaId = dictCarenciaLei91['carenciaId']
        self.dataImplemento = dictCarenciaLei91['dataImplemento']
        self.tempoContribuicao = dictCarenciaLei91['tempoContribuicao']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        CarenciaLei91(
           carenciaId: {self.carenciaId},
           dataImplemento: {self.dataImplemento},
           tempoContribuicao: {self.tempoContribuicao},
           fator: {self.fator},
           dataCadastro: {self.dataCadastro},
           dataUltAlt: {self.dataUltAlt}
       )""")


@post_save(sender=CarenciaLei91)
def inserindoCarenciaLei91(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::inserindoCarenciaLei91___________________{TABLENAME}')

@pre_delete(sender=CarenciaLei91)
def deletandoCarenciaLei91(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::inserindoCarenciaLei91___________________{TABLENAME}')