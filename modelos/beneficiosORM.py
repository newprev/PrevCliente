from modelos.baseModelORM import BaseModel, DATEFORMATS
from logs import logPrioridade
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete

from peewee import AutoField, CharField, ForeignKeyField, DateTimeField, IntegerField, FloatField, BigIntegerField
from datetime import datetime

from util.enums.newPrevEnums import TipoEdicao, Prioridade

TABLENAME = 'cnisBeneficios'


class CnisBeneficios(BaseModel, Model):
    beneficiosId = AutoField(column_name='beneficiosId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    seq = IntegerField()
    nb = BigIntegerField(column_name='nb', null=True)
    dadoOrigem = CharField(column_name='dadoOrigem', default='CNIS')
    competencia = DateTimeField(column_name='competencia', default=datetime.min, formats=DATEFORMATS)
    remuneracao = FloatField(column_name='remuneracao')
    indicadores = CharField(default=None)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'cnisBeneficios'

    def toDict(self):
        dictUsuario = {
            'beneficiosId': self.beneficiosId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'nb': self.nb,
            'dadoOrigem': self.dadoOrigem,
            'competencia': self.competencia,
            'remuneracao': self.remuneracao,
            'indicadores': self.indicadores,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictBeneficios):
        self.beneficiosId = dictBeneficios['beneficiosId']
        self.clienteId = dictBeneficios['clienteId']
        self.seq = dictBeneficios['seq']
        self.nb = dictBeneficios['nb']
        self.dadoOrigem = dictBeneficios['dadoOrigem']
        self.competencia = dictBeneficios['competencia']
        self.remuneracao = dictBeneficios['remuneracao']
        self.indicadores = dictBeneficios['indicadores']
        self.dataCadastro = dictBeneficios['dataCadastro']
        self.dataUltAlt = dictBeneficios['dataUltAlt']

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        Beneficios(
            beneficiosId: {self.beneficiosId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            nb: {self.nb},
            competencia: {self.competencia},
            remuneracao: {self.remuneracao},
            indicadores: {self.indicadores},
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

