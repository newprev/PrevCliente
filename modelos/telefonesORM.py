from logging import info

from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import IntegerField, CharField, DateTimeField, AutoField, ForeignKeyField, BooleanField
from datetime import datetime

TABLENAME = 'telefones'


class Telefones(BaseModel, Model):
    telefoneId = AutoField(column_name='telefoneId', null=True)
    clienteId = IntegerField(column_name='clienteId')
    ativo = BooleanField(default=True)
    principal = BooleanField(default=True)
    numero = CharField(null=False)
    pessoalRecado = CharField(column_name='pessoalRecado')
    tipoTelefone = CharField(column_name='tipoTelefone')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'telefones'
        
    def toDict(self):
        dictUsuario = {
            'telefoneId': self.telefoneId,
            'clienteId': self.clienteId,
            'numero': self.numero,
            'tipoTelefone': self.tipoTelefone,
            'pessoalRecado': self.pessoalRecado,
            'ativo': self.ativo,
            'principal': self.principal,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictTelefone):
        self.telefoneId = dictTelefone['telefoneId'],
        self.clienteId = dictTelefone['clienteId'],
        self.numero = dictTelefone['numero'],
        self.tipoTelefone = dictTelefone['tipoTelefone'],
        self.pessoalRecado = dictTelefone['pessoalRecado'],
        self.ativo = dictTelefone['ativo'],
        self.principal = dictTelefone['principal'],
        self.dataCadastro = dictTelefone['dataCadastro'],
        self.dataUltAlt = dictTelefone['dataUltAlt'],

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        Telefone(
            telefoneId: {self.telefoneId},
            clienteId: {self.clienteId},
            numero: {self.numero},
            tipoTelefone: {self.tipoTelefone},
            pessoalRecado: {self.pessoalRecado},
            ativo: {self.ativo},
            principal: {self.principal},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")
    
    
@post_save(sender=Telefones)
def inserindoTelefones(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::inserindoTelefones___________________{TABLENAME}')


@pre_delete(sender=Telefones)
def deletandoTelefones(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::deletandoTelefones___________________{TABLENAME}')
