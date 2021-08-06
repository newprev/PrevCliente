from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, DateField, DateTimeField, BigIntegerField, FloatField
from datetime import datetime


class IndiceAtuMonetaria(BaseModel, Model):
    indiceId = AutoField(column_name='indiceId', null=True)
    dataReferente = DateField(column_name='dataReferente')
    dib = BigIntegerField()
    fator = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

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

    def prettyPrint(self):
        return f"""
        IndiceAtuMonetarioModelo(
               indiceId: {self.indiceId},
               dataReferente: {self.dataReferente},
               dib: {self.dib},
               fator: {self.fator},
               dataCadastro: {self.dataCadastro},
               dataUltAlt: {self.dataUltAlt}
           )"""
        
        
@post_save(sender=IndiceAtuMonetaria)
def inserindoIndiceAtuMonetaria(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoIndiceAtuMonetaria>___________________{IndiceAtuMonetaria.Meta.table_name}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoIndiceAtuMonetaria>___________________ |Erro| {IndiceAtuMonetaria.Meta.table_name}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=IndiceAtuMonetaria)
def deletandoIndiceAtuMonetaria(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoIndiceAtuMonetaria>___________________{IndiceAtuMonetaria.Meta.table_name}', TipoEdicao.delete, Prioridade.saidaImportante)