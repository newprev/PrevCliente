from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete
from systemLog.logs import logPrioridade
from util.enums.newPrevEnums import TipoEdicao, Prioridade

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
        logPrioridade(f'INSERT<inserindoEspecieBene>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComum)
    else:
        logPrioridade(f'UPDATE<inserindoEspecieBene>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComum)


@pre_delete(sender=EspecieBene)
def deletandoEspecieBenef(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoEspecieBene>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)