from helpers import strToDatetime
from modelos.baseModelORM import BaseModel
from modelos.escritoriosORM import Escritorios
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade, TamanhoData

from peewee import AutoField, CharField, ForeignKeyField, DeferredForeignKey, DateField, IntegerField, DateTimeField
from datetime import datetime


def buscaEscritorioIdAtual() -> int:
    from cache.cacheEscritorio import CacheEscritorio

    escritorioCache = CacheEscritorio()
    escritorio = escritorioCache.carregarCache()
    if not escritorio:
        escritorio = escritorioCache.carregarCacheTemporario()

    return escritorio.escritorioId


class Cliente(BaseModel, Model):
    clienteId = AutoField(column_name='clienteId', null=True)
    escritorioId = ForeignKeyField(column_name='escritorioId', field='escritorioId', model=Escritorios, backref='escritorios', default=buscaEscritorioIdAtual())
    telefoneId = DeferredForeignKey('Telefones', column_name='telefoneId', field='telefoneId', null=True)
    nomeCliente = CharField(column_name='nomeCliente')
    sobrenomeCliente = CharField(column_name='sobrenomeCliente')
    agenciaBanco = CharField(column_name='agenciaBanco', null=True)
    bairro = CharField(null=True)
    cep = CharField()
    cidade = CharField()
    complemento = CharField(null=True)
    cpfCliente = CharField(column_name='cpfCliente', null=True)
    dataNascimento = DateField(column_name='dataNascimento', default=datetime.now)
    email = CharField()
    endereco = CharField()
    estado = CharField()
    estadoCivil = CharField(column_name='estadoCivil', default='SOLTEIRO(A)', null=True)
    genero = CharField(default='M')
    grauEscolaridade = CharField(column_name='grauEscolaridade', null=True)
    idade = IntegerField()
    nit = CharField()
    nomeBanco = CharField(column_name='nomeBanco', null=True)
    nomeMae = CharField(column_name='nomeMae')
    numCarteiraProf = CharField(column_name='numCarteiraProf', null=True)
    numero = IntegerField()
    numeroConta = CharField(column_name='numeroConta', null=True)
    pixCliente = CharField(column_name='pixCliente', null=True)
    profissao = CharField()
    quaCarteiraProf = CharField(column_name='quaCarteiraProf', null=True)
    rgCliente = CharField(column_name='rgCliente')
    senhaINSS = CharField(column_name='senhaINSS', null=True)
    serieCarteiraProf = CharField(column_name='serieCarteiraProf', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt')

    class Meta:
        table_name = 'cliente'

    def toDict(self):
        dictUsuario = {
            'escritorioId': self.escritorioId,
            'clienteId': self.clienteId,
            'nomeCliente': self.nomeCliente,
            'sobrenomeCliente': self.sobrenomeCliente,
            'genero': self.genero,
            'idade': self.idade,
            'dataNascimento': self.dataNascimento,
            'email': self.email,
            'rgCliente': self.rgCliente,
            'cpfCliente': self.cpfCliente,
            'nomeBanco': self.nomeBanco,
            'agenciaBanco': self.agenciaBanco,
            'numeroConta': self.numeroConta,
            'pixCliente': self.pixCliente,
            'grauEscolaridade': self.grauEscolaridade,
            'senhaINSS': self.senhaINSS,
            'numCartProf': self.numCartProf,
            'nit': self.nit,
            'nomeMae': self.nomeMae,
            'estadoCivil': self.estadoCivil,
            'endereco': self.endereco,
            'estado': self.estado,
            'cidade': self.cidade,
            'bairro': self.bairro,
            'cep': self.cep,
            'telefone': self.telefone,
            'complemento': self.complemento,
            'pathCnis': self.pathCnis
        }
        return dictUsuario

    def fromDict(self, dictCliente):
        self.escritorioId = dictCliente['escritorioId']
        self.clienteId = dictCliente['clienteId']
        self.nomeCliente = dictCliente['nomeCliente']
        self.sobrenomeCliente = dictCliente['sobrenomeCliente']
        self.genero = dictCliente['genero']
        self.idade = dictCliente['idade']
        self.dataNascimento = strToDatetime(dictCliente['dataNascimento'], TamanhoData.gg)
        self.email = dictCliente['email']
        self.rgCliente = dictCliente['rgCliente']
        self.cpfCliente = dictCliente['cpfCliente']
        self.nomeBanco = dictCliente['nomeBanco']
        self.agenciaBanco = dictCliente['agenciaBanco']
        self.numeroConta = dictCliente['numeroConta']
        self.pixCliente = dictCliente['pixCliente']
        self.grauEscolaridade = dictCliente['grauEscolaridade']
        self.senhaINSS = dictCliente['senhaINSS']
        # self.numCartProf = dictCliente['numCartProf']
        self.nit = dictCliente['nit']
        self.nomeMae = dictCliente['nomeMae']
        self.estadoCivil = dictCliente['estadoCivil']
        self.endereco = dictCliente['endereco']
        self.numero = dictCliente['numero']
        self.estado = dictCliente['estado']
        self.cidade = dictCliente['cidade']
        self.bairro = dictCliente['bairro']
        self.cep = dictCliente['cep']
        self.telefoneId = dictCliente['telefone']
        self.complemento = dictCliente['complemento']
        # self.pathCnis = dictCliente['pathCnis']

    def __bool__(self):
        return self.nit != '' and self.nit is not None

    def __repr__(self):
        return f"""
        Cliente(
            escritorioId: {self.escritorioId},
            clienteId: {self.clienteId},
            nomeCliente: {self.nomeCliente},
            sobrenomeCliente: {self.sobrenomeCliente},
            genero: {self.genero},
            idade: {self.idade},
            dataNascimento: {self.dataNascimento},
            email: {self.email},
            rgCliente: {self.rgCliente},
            cpfCliente: {self.cpfCliente},
            nomeBanco: {self.nomeBanco},
            agenciaBanco: {self.agenciaBanco},
            numeroConta: {self.numeroConta},
            pixCliente: {self.pixCliente},
            grauEscolaridade: {self.grauEscolaridade},
            senhaINSS: {self.senhaINSS},
            numCartProf: {self.numCartProf},
            nit: {self.nit},
            nomeMae: {self.nomeMae},
            estadoCivil: {self.estadoCivil},
            endereco: {self.endereco},
            numero: {self.numero},
            estado: {self.estado},
            cidade: {self.cidade},
            bairro: {self.bairro},
            cep: {self.cep},
            telefone: {self.telefone},
            complemento: {self.complemento},
            pathCnis: {self.pathCnis}
        )"""


@post_save(sender=Cliente)
def inserindoCliente(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoCabecalho>___________________{Cliente.Meta.table_name}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoCabecalho>___________________ |Erro| {Cliente.Meta.table_name}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=Cliente)
def deletandoCliente(*args, **kwargs):
    logPrioridade(f'DELETE<inserindoCabecalho>___________________{Cliente.Meta.table_name}', TipoEdicao.delete, Prioridade.saidaImportante)
