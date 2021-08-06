from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField


class EspecieBenef(BaseModel, Model):
    especieId = AutoField(column_name='especieId', null=True)
    descricao = CharField()

    class Meta:
        table_name = 'especieBenef'

    def toDict(self):
        dictEspecieBenef = {
            'especieId': self.especieId,
            'descricao': self.descricao
        }
        return dictEspecieBenef

    def fromDict(self, dictEscritorio: dict):
        self.especieId = dictEscritorio['especieId']
        self.descricao = dictEscritorio['descricao']

        return self


@post_save(sender=EspecieBenef)
def inserindoEspecieBenef(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoEspecieBenef>___________________{EspecieBenef.Meta.table_name}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoEspecieBenef>___________________ |Erro| {EspecieBenef.Meta.table_name}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=EspecieBenef)
def deletandoEspecieBenef(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoEspecieBenef>___________________{EspecieBenef.Meta.table_name}', TipoEdicao.delete, Prioridade.saidaImportante)