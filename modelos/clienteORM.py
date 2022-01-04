from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete

from modelos.telefonesORM import Telefones
from modelos.clienteProfissao import ClienteProfissao
from modelos.clienteInfoBanco import ClienteInfoBanco
from systemLog.logs import logPrioridade
from modelos.escritoriosORM import Escritorios
from util.dateHelper import strToDate
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, ForeignKeyField, DateField, IntegerField, DateTimeField
from datetime import datetime

TABLENAME = 'cliente'


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
    telefoneId = ForeignKeyField(column_name='telefoneId', field='telefoneId', model=Telefones, backref='telefones', null=True)
    nomeCliente = CharField(column_name='nomeCliente')
    sobrenomeCliente = CharField(column_name='sobrenomeCliente')
    bairro = CharField(null=True)
    cep = CharField(null=True)
    cidade = CharField(null=True)
    complemento = CharField(null=True)
    cpfCliente = CharField(column_name='cpfCliente', unique=True)
    dataNascimento = DateField(column_name='dataNascimento', default=datetime.now(), formats=DATEFORMATS)
    email = CharField(null=True)
    endereco = CharField(null=True)
    estado = CharField(null=True)
    estadoCivil = CharField(column_name='estadoCivil', default='Solteiro(A)', null=True)
    genero = CharField(default='M')
    grauEscolaridade = CharField(column_name='grauEscolaridade', null=True)
    idade = IntegerField()
    nomeMae = CharField(column_name='nomeMae')
    numero = IntegerField(null=True)
    dadosBancarios = ForeignKeyField(column_name='dadosBancarios', field='infoId', model=ClienteInfoBanco, backref='clienteInfoBanco', null=True)
    dadosProfissionais = ForeignKeyField(column_name='dadosProfissionais', field='infoId', model=ClienteProfissao, backref='clienteProfissao', null=True)
    rgCliente = CharField(column_name='rgCliente', null=True)
    senhaINSS = CharField(column_name='senhaINSS', null=True)
    pathCnis = CharField(column_name='pathCnis', null=True)
    observacoes = CharField(column_name='observacoes', max_length=4000, null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

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
            'grauEscolaridade': self.grauEscolaridade,
            'senhaINSS': self.senhaINSS,
            'nomeMae': self.nomeMae,
            'estadoCivil': self.estadoCivil,
            'endereco': self.endereco,
            'estado': self.estado,
            'cidade': self.cidade,
            'bairro': self.bairro,
            'cep': self.cep,
            'telefoneId': self.telefoneId,
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
        self.dataNascimento = strToDate(dictCliente['dataNascimento'])
        self.email = dictCliente['email']
        self.rgCliente = dictCliente['rgCliente']
        self.cpfCliente = dictCliente['cpfCliente']
        self.grauEscolaridade = dictCliente['grauEscolaridade']
        self.senhaINSS = dictCliente['senhaINSS']
        self.nomeMae = dictCliente['nomeMae']
        self.estadoCivil = dictCliente['estadoCivil']
        self.endereco = dictCliente['endereco']
        self.numero = dictCliente['numero']
        self.estado = dictCliente['estado']
        self.cidade = dictCliente['cidade']
        self.bairro = dictCliente['bairro']
        self.cep = dictCliente['cep']
        self.telefoneId = dictCliente['telefoneId']
        self.complemento = dictCliente['complemento']
        self.pathCnis = dictCliente['pathCnis']

    def __bool__(self):
        return self.nomeCliente != '' and self.nomeCliente is not None

    def prettyPrint(self, backRef: bool = False):

        if backRef:
            print('--- backRef', end='')
            self.escritorioId.prettyPrint()
            self.telefoneId.prettyPrint()
            print('backRef ---')

        print(f"""
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
            grauEscolaridade: {self.grauEscolaridade},
            senhaINSS: {self.senhaINSS},
            nomeMae: {self.nomeMae},
            estadoCivil: {self.estadoCivil},
            endereco: {self.endereco},
            numero: {self.numero},
            estado: {self.estado},
            cidade: {self.cidade},
            bairro: {self.bairro},
            cep: {self.cep},
            telefoneId: {self.telefoneId},
            complemento: {self.complemento},
            pathCnis: {self.pathCnis}
        )""")


@post_save(sender=Cliente)
def inserindoCliente(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoCabecalho>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComum)
    else:
        logPrioridade(f'UPDATE<inserindoCabecalho>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComum)


@pre_delete(sender=Cliente)
def deletandoCliente(*args, **kwargs):
    logPrioridade(f'DELETE<inserindoCabecalho>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)