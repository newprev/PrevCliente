from modelos.baseModelORM import BaseModel
from modelos.escritoriosORM import Escritorios
from systemLog.logs import *

from peewee import AutoField, ForeignKeyField, BooleanField, CharField, DateTimeField
from playhouse.signals import Model, post_save, pre_delete
from datetime import datetime

TABLENAME = 'advogados'


class Advogados(BaseModel, Model):
    advogadoId = AutoField(column_name='advogadoId', null=True)
    escritorioId = ForeignKeyField(column_name='escritorioId', field='escritorioId', model=Escritorios, backref='escritorios')
    admin = BooleanField(default=False)
    ativo = BooleanField(default=False)
    confirmado = BooleanField(default=False)
    email = CharField()
    estadoCivil = CharField(column_name='estadoCivil')
    login = CharField()
    nacionalidade = CharField()
    nomeAdvogado = CharField(column_name='nomeAdvogado')
    numeroOAB = CharField(column_name='numeroOAB')
    senha = CharField(null=False)
    sobrenomeAdvogado = CharField(column_name='sobrenomeAdvogado', null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = TABLENAME

    def toDict(self):
        if self.email is not None and (isinstance(self.email, tuple) or isinstance(self.email, list)):
            email = self.email[0]
        else:
            email = self.email

        dictUsuario = {
            'advogadoId': self.advogadoId,
            'escritorioId': self.escritorioId.escritorioId,
            'nomeAdvogado': self.nomeAdvogado,
            'login': self.login,
            'senha': self.senha,
            'email': email,
            'sobrenomeAdvogado': self.sobrenomeAdvogado,
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

    def fromDict(self, dictUsuario: dict, retornaInst: bool = True):

        if dictUsuario['advogadoId'] is list or dictUsuario['advogadoId'] is tuple:
            self.advogadoId = dictUsuario['advogadoId'][0]
        else:
            self.advogadoId = dictUsuario['advogadoId']

        if 'senha' in dictUsuario.keys():
            self.senha = dictUsuario['senha']

        if 'dataCadastro' in dictUsuario.keys():
            self.dataCadastro = dictUsuario['dataCadastro']

        if 'dataUltAlt' in dictUsuario.keys():
            self.dataUltAlt = dictUsuario['dataUltAlt']

        if isinstance(dictUsuario['escritorioId'], dict):
            escritorio = Escritorios().fromDict(dictUsuario['escritorioId'])
        else:
            escritorio = dictUsuario['escritorioId']

        self.escritorioId = escritorio
        self.nomeAdvogado = dictUsuario['nomeAdvogado']
        self.login = dictUsuario['login']
        # self.telefone = dictUsuario['telefone'],
        self.email = dictUsuario['email'],
        self.sobrenomeAdvogado = dictUsuario['sobrenomeAdvogado']
        self.nacionalidade = dictUsuario['nacionalidade']
        self.numeroOAB = dictUsuario['numeroOAB']
        self.estadoCivil = dictUsuario['estadoCivil']
        self.admin = dictUsuario['admin']
        self.confirmado = dictUsuario['confirmado']
        self.ativo = dictUsuario['ativo']

        if retornaInst:
            return self

    def __eq__(self, other):
        instVariavel: bool = isinstance(self, type(other))
        if not instVariavel:
            return False

        senhaAuth: bool = self.senha == other.senha
        loginAuth: bool = self.login == other.login

        return senhaAuth and loginAuth

    def __bool__(self):
        return self.advogadoId is not None and self.nomeAdvogado is not None

    def prettyPrint(self, backRef: bool = False):

        if backRef:
            print('--- backRef', end='')
            self.escritorioId.prettyPrint()
            print('backRef ---')

        print(f"""
        Usuario(
            escritorioId: {self.escritorioId},
            advogadoId: {self.advogadoId},
            nomeAdvogado: {self.nomeAdvogado},
            login: {self.login},
            senha: {self.senha},
            sobrenomeAdvogado: {self.sobrenomeAdvogado},
            nacionalidade: {self.nacionalidade},
            email: {self.email},
            numeroOAB: {self.numeroOAB},
            estadoCivil: {self.estadoCivil},
            admin: {self.admin},
            confirmado: {self.confirmado},
            ativo: {self.ativo}
        )""")


@post_save(sender=Advogados)
def inserindoAdvogados(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoAdvogados>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComum)
    else:
        logPrioridade(f'UPDATE<inserindoAdvogados>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComum)


@pre_delete(sender=Advogados)
def deletandoAdvogados(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoAdvogados>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)

