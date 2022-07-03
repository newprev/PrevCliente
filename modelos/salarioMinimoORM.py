from logging import info, debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete
from util.enums.logEnums import TipoLog

from peewee import CharField, DateField, DateTimeField, FloatField, AutoField
from datetime import datetime

TABLENAME = 'salarioMinimo'


class SalarioMinimo(BaseModel, Model):
    salarioId = AutoField(column_name='salarioId', null=True, primary_key=True)
    vigencia = DateField(null=False, formats=DATEFORMATS)
    baseLegal = CharField(null=False)
    valor = FloatField(null=False)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())

    class Meta:
        table_name = 'salarioMinimo'

    def toDict(self):
        dictSalario = {
            'salarioId': self.indicadorId,
            'vigencia': self.vigencia,
            'baseLegal': self.baseLegal,
            'valor': self.valor,
            'dataUltAlt': self.dataUltAlt,
            'dataCadastro': self.dataCadastro
        }
        return dictSalario

    def fromDict(self, dictSalario):
        self.salarioId = dictSalario['indicadorId']
        self.vigencia = dictSalario['vigencia']
        self.baseLegal = dictSalario['baseLegal']
        self.valor = dictSalario['valor']
        self.dataUltAlt = dictSalario['dataUltAlt']
        self.dataCadastro = dictSalario['dataCadastro']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        IndicadorModelo(
            salarioId: {self.salarioId},
            vigencia: {self.vigencia},
            baseLegal: {self.baseLegal},
            valor: {self.valor},
            dataUltAlt: {self.dataUltAlt}
            dataCadastro: {self.dataCadastro}
        )""")


@post_save(sender=SalarioMinimo)
def inserindoSalarioMinimo(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoSalarioMinimo___________________{TABLENAME}')


@pre_delete(sender=SalarioMinimo)
def deletandoSalarioMinimo(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoSalarioMinimo___________________{TABLENAME}')
