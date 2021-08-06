from modelos.baseModelORM import BaseModel
from modelos.escritoriosORM import Escritorios

from peewee import AutoField, CharField, ForeignKeyField, DeferredForeignKey, DateField, IntegerField, DateTimeField
from datetime import datetime

def buscaEscritorioIdAtual() -> int:
    from cache.cacheEscritorio import CacheEscritorio

    escritorioCache = CacheEscritorio()
    escritorio = escritorioCache.carregarCache()
    if not escritorio:
        escritorio = escritorioCache.carregarCacheTemporario()

    return escritorio.escritorioId

class Cliente(BaseModel):
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
