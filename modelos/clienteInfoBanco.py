from logging import info

from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, DateTimeField, IntegerField
from datetime import datetime

TABLENAME = 'clienteInfoBanco'


class ClienteInfoBanco(BaseModel, Model):
    infoId = AutoField(column_name='infoId', null=True)
    clienteId = IntegerField(column_name='clienteId')
    nomeBanco = CharField(column_name='nomeBanco', null=True)
    numeroAgencia = CharField(column_name='numeroAgencia', null=True)
    numeroConta = CharField(column_name='numeroConta', null=True)
    chavePix = CharField(column_name='chavePix', null=True)
    estado = CharField(null=True)
    observacoes = CharField(column_name='observacoes', max_length=4000, null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'ClienteInfoBanco'

    def toDict(self):
        dictUsuario = {
            'infoId': self.infoId,
            'clienteId': self.clienteId,
            'nomeBanco': self.nomeBanco,
            'numeroAgencia': self.numeroAgencia,
            'numeroConta': self.numeroConta,
            'chavePix': self.chavePix,
            'estado': self.estado,
        }
        return dictUsuario

    def fromDict(self, dictCliente):
        self.infoId = dictCliente['infoId']
        self.clienteId = dictCliente['clienteId']
        self.nomeBanco = dictCliente['nomeBanco']
        self.numeroAgencia = dictCliente['numeroAgencia']
        self.numeroConta = dictCliente['numeroConta']
        self.chavePix = dictCliente['chavePix']
        self.estado = dictCliente['estado']

    def __bool__(self):
        return self.nit != '' and self.nit is not None

    def prettyPrint(self, backRef: bool = False):

        if backRef:
            print('--- backRef', end='')
            self.infoId.prettyPrint()
            self.telefoneId.prettyPrint()
            print('backRef ---')

        print(f"""
        Cliente(
            infoId: {self.infoId},
            clienteId: {self.clienteId},
            nomeBanco: {self.nomeBanco},
            numeroAgencia: {self.numeroAgencia},
            numeroConta: {self.numeroConta},
            chavePix: {self.chavePix},
            estado: {self.estado}
        )""")


@post_save(sender=ClienteInfoBanco)
def inserindoCliente(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::inserindoCliente___________________{TABLENAME}')


@pre_delete(sender=ClienteInfoBanco)
def deletandoCliente(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::deletandoCliente___________________{TABLENAME}')