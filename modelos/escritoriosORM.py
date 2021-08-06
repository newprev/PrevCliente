from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade

from datetime import datetime
from peewee import AutoField, IntegerField, CharField, DateTimeField


class Escritorios(BaseModel, Model):
    escritorioId = AutoField(column_name='escritorioId', null=True)
    bairro = CharField(null=True)
    cep = CharField(null=True)
    cidade = CharField(null=True)
    cnpj = CharField(null=True)
    complemento = CharField(null=True)
    cpf = CharField(null=True)
    email = CharField(null=True)
    endereco = CharField(null=True)
    estado = CharField(default='SP')
    inscEstadual = CharField(column_name='inscEstadual', null=True)
    nomeEscritorio = CharField(column_name='nomeEscritorio')
    nomeFantasia = CharField(column_name='nomeFantasia')
    numero = IntegerField(null=True)
    telefone = CharField(null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'escritorios'

    def toDict(self):
        dictUsuario = {
            'escritorioId': self.escritorioId,
            'nomeEscritorio': self.nomeEscritorio,
            'nomeFantasia': self.nomeFantasia,
            'cnpj': self.cnpj,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'email': self.email,
            'inscEstadual': self.inscEstadual,
            'endereco': self.endereco,
            'numero': self.numero,
            'cep': self.cep,
            'complemento': self.complemento,
            'cidade': self.cidade,
            'estado': self.estado,
            'bairro': self.bairro,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt

        }
        return dictUsuario

    def fromDict(self, dictEscritorio: dict):

        if dictEscritorio['escritorioId'] is list or dictEscritorio['escritorioId'] is tuple:
            self.escritorioId = dictEscritorio['escritorioId'][0]
        else:
            self.escritorioId = dictEscritorio['escritorioId']

        if isinstance(dictEscritorio['email'], list):
            self.email = dictEscritorio['email'][0]
        else:
            self.email = dictEscritorio['email']

        if isinstance(dictEscritorio['telefone'], list):
            self.telefone = dictEscritorio['telefone'][0]
        else:
            self.telefone = dictEscritorio['telefone']

        self.nomeEscritorio = dictEscritorio['nomeEscritorio']
        self.nomeFantasia = dictEscritorio['nomeFantasia']
        self.cnpj = dictEscritorio['cnpj']
        self.cpf = dictEscritorio['cpf']
        self.inscEstadual = dictEscritorio['inscEstadual']
        self.endereco = dictEscritorio['endereco']
        self.numero = dictEscritorio['numero']
        self.estado = dictEscritorio['estado']
        self.cidade = dictEscritorio['cidade']
        self.bairro = dictEscritorio['bairro']
        self.cep = dictEscritorio['cep']
        self.complemento = dictEscritorio['complemento']
        self.dataCadastro = dictEscritorio['dataCadastro']
        self.dataUltAlt = dictEscritorio['dataUltAlt']

        return self

    def __repr__(self):
        return f"""
        Escritorio(
            escritorioId: {self.escritorioId},
            nomeEscritorio: {self.nomeEscritorio},
            nomeFantasia: {self.nomeFantasia},
            cnpj: {self.cnpj},
            cpf: {self.cpf},
            email: {self.email},
            inscEstadual: {self.inscEstadual},
            endereco: {self.endereco},
            numero: {self.numero},
            estado: {self.estado},
            cidade: {self.cidade},
            bairro: {self.bairro},
            cep: {self.cep},
            complemento: {self.complemento},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )         
    """

    def __bool__(self):
        return self.escritorioId is not None


@post_save(sender=Escritorios)
def inserindoEscritorios(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoEscritorios>___________________{Escritorios.Meta.table_name}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoEscritorios>___________________ |Erro| {Escritorios.Meta.table_name}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=Escritorios)
def deletandoEscritorios(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoEscritorios>___________________{Escritorios.Meta.table_name}', TipoEdicao.delete, Prioridade.saidaImportante)
