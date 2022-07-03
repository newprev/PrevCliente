from logging import info, debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.helpers.dateHelper import strToDate
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from datetime import datetime
from peewee import AutoField, DateField, IntegerField, DateTimeField, CharField

TABLENAME = 'expSobrevida'


class ExpSobrevida(BaseModel, Model):
    infoId = AutoField(column_name='infoId', null=True, primary_key=True)
    dataReferente = DateField(column_name='dataReferente', formats=DATEFORMATS)
    expectativaSobrevida = IntegerField(column_name='expectativaSobrevida')
    idade = IntegerField(null=False)
    genero = CharField(null=False, max_length=1)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

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
        self.dataReferente = strToDate(dictExpectativaSobrevida['dataReferente'])
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
    debug(f'{TipoLog.DataBase.value}::inserindoExpSobrevida___________________{TABLENAME}')


@pre_delete(sender=ExpSobrevida)
def deletandoExpSobrevida(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoExpSobrevida___________________{TABLENAME}')
