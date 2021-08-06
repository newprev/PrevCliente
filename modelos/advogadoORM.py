from modelos.baseModelORM import BaseModel
from modelos.escritoriosORM import Escritorios
from logs import *

from peewee import AutoField, ForeignKeyField, BooleanField, CharField, DateTimeField
from playhouse.signals import Model, post_save, pre_save, pre_init, pre_delete
from datetime import datetime


class Advogados(BaseModel, Model):
    advogadoId = AutoField(column_name='advogadoId', null=True)
    escritorioId = ForeignKeyField(column_name='escritorioId', field='escritorioId', model=Escritorios, backref='escritorios')
    admin = BooleanField(default=False)
    ativo = BooleanField(default=False)
    confirmado = BooleanField()
    email = CharField()
    estadoCivil = CharField(column_name='estadoCivil')
    login = CharField()
    nacionalidade = CharField()
    nomeUsuario = CharField(column_name='nomeUsuario')
    numeroOAB = CharField(column_name='numeroOAB')
    senha = CharField(null=False)
    sobrenomeUsuario = CharField(column_name='sobrenomeUsuario', null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'advogados'

    def toDict(self):
        dictUsuario = {
            'advogadoId': self.advogadoId,
            'escritorioId': self.escritorioId.escritorioId,
            'nomeUsuario': self.nomeUsuario,
            'login': self.login,
            'senha': self.senha,
            'email': self.email,
            'sobrenomeUsuario': self.sobrenomeUsuario,
            'nacionalidade': self.nacionalidade,
            'estadoCivil': self.estadoCivil,
            'numeroOAB': self.numeroOAB,
            'admin': self.admin,
            'confirmado': self.confirmado,
            'ativo': self.ativo,
            'dataCadastro': datetimeToSql(self.dataCadastro),
            'dataUltAlt': datetimeToSql(self.dataUltAlt)
        }
        return dictUsuario


@post_save(sender=Advogados)
def inserindoAdvogados(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoAdvogados>___________________{Advogados.Meta.table_name}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoAdvogados>___________________ |Erro| {Advogados.Meta.table_name}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_init(sender=Advogados)
def criandoTabela(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    logPrioridade(f'CREATE<criandoTabela>___________________ advogados', TipoEdicao.createTable, Prioridade.saidaComun)


@pre_delete(sender=Advogados)
def deletandoAdvogados(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    logPrioridade(f'CREATE<deletandoAdvogados>___________________{Advogados.Meta.table_name}', TipoEdicao.delete, Prioridade.saidaImportante)

