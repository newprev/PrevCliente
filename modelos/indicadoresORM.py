from logging import info, debug

from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import CharField, DateTimeField
from datetime import datetime

TABLENAME = 'indicadores'


class Indicadores(BaseModel, Model):
    indicadorId = CharField(column_name='indicadorId', null=True, primary_key=True)
    descricao = CharField()
    fonte = CharField()
    resumo = CharField()
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'indicadores'

    def toDict(self):
        dictIndicador = {
            'indicadorId': self.indicadorId,
            'resumo': self.resumo,
            'descricao': self.descricao,
            'fonte': self.fonte,
            'dataUltAlt': self.dataUltAlt
        }
        return dictIndicador

    def fromDict(self, dictIndicador):
        self.indicadorId = dictIndicador['indicadorId']
        self.resumo = dictIndicador['resumo']
        self.descricao = dictIndicador['descricao']
        self.fonte = dictIndicador['fonte']
        self.dataUltAlt = dictIndicador['dataUltAlt']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        IndicadorModelo(
            indicadorId: {self.indicadorId},
            sigla: {self.resumo},
            descricao: {self.descricao},
            fonte: {self.fonte},
            dataUltAlt: {self.dataUltAlt}
        )""")


@post_save(sender=Indicadores)
def inserindoIndicadores(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoIndicadores___________________{TABLENAME}')

@pre_delete(sender=Indicadores)
def deletandoIndicadores(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoIndicadores___________________{TABLENAME}')