from logs import logPrioridade
from modelos.baseModelORM import BaseModel
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete

from peewee import AutoField, CharField, ForeignKeyField, DateTimeField, BigIntegerField, DateField, IntegerField
from datetime import datetime

from newPrevEnums import TipoEdicao, Prioridade

TABLENAME = 'cnisBeneficios'

class CnisBeneficios(BaseModel, Model):
    beneficiosId = AutoField(column_name='beneficiosId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    dadoOrigem = CharField(column_name='dadoOrigem', default='CNIS')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataFim = DateField(column_name='dataFim')
    dataInicio = DateField(column_name='dataInicio')
    dataUltAlt = DateTimeField(column_name='dataUltAlt')
    especie = CharField()
    nb = BigIntegerField()
    seq = IntegerField()
    situacao = CharField()

    class Meta:
        table_name = 'cnisBeneficios'

    def toDict(self):
        dictUsuario = {
            'beneficiosId': self.beneficiosId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'nb': self.nb,
            'especie': self.especie,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'situacao': self.situacao,
            'dadoOrigem': self.dadoOrigem,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictBeneficios):
        self.beneficiosId = dictBeneficios['beneficiosId']
        self.clienteId = dictBeneficios['clienteId']
        self.seq = dictBeneficios['seq']
        self.nb = dictBeneficios['nb']
        self.especie = dictBeneficios['especie']
        self.dataInicio = dictBeneficios['dataInicio']
        self.dataFim = dictBeneficios['dataFim']
        self.situacao = dictBeneficios['situacao']
        self.dadoOrigem = dictBeneficios['dadoOrigem']
        self.dataCadastro = dictBeneficios['dataCadastro']
        self.dataUltAlt = dictBeneficios['dataUltAlt']

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        Beneficios(
            beneficiosId: {self.beneficiosId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            nb: {self.nb},
            especie: {self.especie},
            dataInicio: {self.dataInicio},
            dataFim: {self.dataFim},
            situacao: {self.situacao},
            dadoOrigem: {self.dadoOrigem},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")


@post_save(sender=CnisBeneficios)
def inserindoBeneficios(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoBeneficios>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoBeneficios>___________________ |Erro| {TABLENAME}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=CnisBeneficios)
def deletandoBeneficios(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoBeneficios>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)

