from helpers import strToDatetime
from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade, TamanhoData

from datetime import datetime
from peewee import AutoField, DateField, IntegerField, DateTimeField

TABLENAME = 'expSobrevida'


class ExpSobrevida(BaseModel, Model):
    infoId = AutoField(column_name='infoId', null=True)
    dataReferente = DateField(column_name='dataReferente')
    expectativaSobrevida = IntegerField(column_name='expectativaSobrevida')
    idade = IntegerField(null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'expSobrevida'

    def toDict(self):
        dictUsuario = {
            'infoId': self.infoId,
            'dataReferente': self.dataReferente,
            'idade': self.idade,
            'expectativaSobrevida': self.expectativaSobrevida,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictExpectativaSobrevida: dict):

        self.infoId = dictExpectativaSobrevida['infoId']
        self.dataReferente = strToDatetime(dictExpectativaSobrevida['dataReferente'], TamanhoData.mm)
        self.idade = dictExpectativaSobrevida['idade']
        self.expectativaSobrevida = dictExpectativaSobrevida['expectativaSobrevida']

        if 'dataCadastro' in dictExpectativaSobrevida.keys():
            self.dataCadastro = dictExpectativaSobrevida['dataCadastro']

        if 'dataUltAlt' in dictExpectativaSobrevida.keys():
            self.dataUltAlt = dictExpectativaSobrevida['dataUltAlt']

        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        ExpectativaSobrevida(
            infoId: {self.infoId},
            dataReferente: {self.dataReferente},
            idade: {self.idade},
            expectativaSobrevida: {self.expectativaSobrevida},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")


@post_save(sender=ExpSobrevida)
def inserindoExpSobrevida(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoExpSobrevida>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoExpSobrevida>___________________ |Erro| {TABLENAME}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=ExpSobrevida)
def deletandoExpSobrevida(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoExpSobrevida>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)
