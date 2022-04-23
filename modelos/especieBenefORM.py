from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from logging import info, warning, error

from peewee import AutoField, CharField, BooleanField

TABLENAME = 'especieBene'


class EspecieBene(BaseModel, Model):
    especieId = AutoField(column_name='especieId', null=True)
    descricao = CharField()
    ativo = BooleanField(default=True)

    class Meta:
        table_name = 'especieBene'

    def toDict(self):
        dictEspecieBene = {
            'especieId': self.especieId,
            'descricao': self.descricao,
            'ativo': self.ativo
        }
        return dictEspecieBene

    def fromDict(self, dictEscritorio: dict):
        self.especieId = dictEscritorio['especieId']
        self.descricao = dictEscritorio['descricao']
        self.ativo = dictEscritorio['ativo']

        return self


@post_save(sender=EspecieBene)
def inserindoEspecieBenef(*args, **kwargs):
    if kwargs['created']:
        info(f'{TipoLog.DataBase.value}::inserindoEspecieBene___________________{TABLENAME}')
    else:
        info(f'{TipoLog.DataBase.value}::inserindoEspecieBene___________________ {TABLENAME}')


@pre_delete(sender=EspecieBene)
def deletandoEspecieBenef(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::deletandoEspecieBene___________________{TABLENAME}')
