from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from modelos.escritoriosORM import Escritorios
from util.dateHelper import strToDate
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, ForeignKeyField, DeferredForeignKey, DateField, IntegerField, DateTimeField, BooleanField
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
    telefoneId = DeferredForeignKey('Telefones', column_name='telefoneId', field='telefoneId', backref='telefones', null=True)
    nomeCliente = CharField(column_name='nomeCliente')
    sobrenomeCliente = CharField(column_name='sobrenomeCliente')
    agenciaBanco = CharField(column_name='agenciaBanco', null=True)
    bairro = CharField(null=True)
    cep = CharField(null=True)
    cidade = CharField(null=True)
    complemento = CharField(null=True)
    cpfCliente = CharField(column_name='cpfCliente', unique=True)
    dataNascimento = DateField(column_name='dataNascimento', default=datetime.now, formats=DATEFORMATS)
    email = CharField(null=True)
    endereco = CharField(null=True)
    estado = CharField(null=True)
    estadoCivil = CharField(column_name='estadoCivil', default='Solteiro(A)', null=True)
    genero = CharField(default='M')
    grauEscolaridade = CharField(column_name='grauEscolaridade', null=True)
    idade = IntegerField()
    nit = CharField()
    nomeBanco = CharField(column_name='nomeBanco', null=True)
    nomeMae = CharField(column_name='nomeMae')
    numCarteiraProf = CharField(column_name='numCarteiraProf', null=True)
    numero = IntegerField(null=True)
    numCartProf = CharField(column_name='numCartProf', null=True)
    numeroConta = CharField(column_name='numeroConta', null=True)
    pixCliente = CharField(column_name='pixCliente', null=True)
    profissao = CharField(null=True)
    professor = BooleanField(default=False)
    quaCarteiraProf = CharField(column_name='quaCarteiraProf', null=True)
    rgCliente = CharField(column_name='rgCliente', null=True)
    senhaINSS = CharField(column_name='senhaINSS', null=True)
    serieCarteiraProf = CharField(column_name='serieCarteiraProf', null=True)
    pathCnis = CharField(column_name='pathCnis', null=True)
    observacoes = CharField(column_name='observacoes', max_length=4000, null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

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
            'professor': self.professor,
            'numCartProf': self.numCartProf,
            'nit': self.nit,
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
        self.nomeBanco = dictCliente['nomeBanco']
        self.agenciaBanco = dictCliente['agenciaBanco']
        self.numeroConta = dictCliente['numeroConta']
        self.pixCliente = dictCliente['pixCliente']
        self.grauEscolaridade = dictCliente['grauEscolaridade']
        self.senhaINSS = dictCliente['senhaINSS']
        self.professor = dictCliente['professor']
        self.numCartProf = dictCliente['numCartProf']
        self.nit = dictCliente['nit']
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
        return self.nit != '' and self.nit is not None

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
            nomeBanco: {self.nomeBanco},
            agenciaBanco: {self.agenciaBanco},
            numeroConta: {self.numeroConta},
            pixCliente: {self.pixCliente},
            grauEscolaridade: {self.grauEscolaridade},
            senhaINSS: {self.senhaINSS},
            professor: {self.professor},
            nit: {self.nit},
            nomeMae: {self.nomeMae},
            estadoCivil: {self.estadoCivil},
            numCartProf: {self.numCartProf},
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
        logPrioridade(f'INSERT<inserindoCabecalho>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'UPDATE<inserindoCabecalho>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComun)


@pre_delete(sender=Cliente)
def deletandoCliente(*args, **kwargs):
    logPrioridade(f'DELETE<inserindoCabecalho>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)