from logging import info

from modelos.baseModelORM import BaseModel
from modelos.clienteORM import Cliente
from modelos.processosORM import Processos
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade
from util.helpers.helpers import getRegrasApos, getContribSimulacao

from peewee import AutoField, CharField, ForeignKeyField, DateField, IntegerField, DateTimeField, FloatField, BooleanField
from datetime import datetime

TABLENAME = 'aposentadoria'


class Aposentadoria(BaseModel, Model):
    REGRAS_APOSENTADORIA = getRegrasApos()
    TIPO_SIMULACAO = getContribSimulacao()
    
    aposentadoriaId = AutoField(column_name='aposentadoriaId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente)
    processoId = ForeignKeyField(column_name='processoId', field='processoId', model=Processos)
    seq = IntegerField(null=False)
    tipo = CharField(choices=REGRAS_APOSENTADORIA)
    contribMeses = IntegerField(default=0)
    contribAnos = IntegerField(default=0)
    valorBeneficio = FloatField(default=0)
    idadeCliente = IntegerField(null=True)
    qtdContribuicoes = IntegerField(default=0)
    dib = DateField(default=datetime.min)
    der = DateField(default=datetime.min)
    contribSimulacao = CharField(choices=TIPO_SIMULACAO, default='ULTI')
    valorSimulacao = FloatField(null=True, default=0.0)
    possuiDireito = BooleanField(column_name='possuiDireito', default=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'aposentadoria'

    def toDict(self):
        dictAposentadoria = {
            'aposentadoriaId': self.aposentadoriaId,
            'clienteId': self.clienteId,
            'processoId': self.processoId,
            'seq': self.seq,
            'tipo': self.tipo,
            'contribMeses': self.contribMeses,
            'contribAnos': self.contribAnos,
            'valorBeneficio': self.valorBeneficio,
            'dib': self.dib,
            'der': self.der,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictAposentadoria

    def fromDict(self, dictAposentadoria):
        self.aposentadoriaId = dictAposentadoria['aposentadoriaId']
        self.clienteId = dictAposentadoria['clienteId']
        self.seq = dictAposentadoria['seq']
        self.tipo = int(dictAposentadoria['tipo'])
        self.contribMeses = dictAposentadoria['contribMeses']
        self.contribAnos = dictAposentadoria['contribAnos']
        self.valorBeneficio = dictAposentadoria['valorBeneficio']
        self.dib = dictAposentadoria['dib']
        self.der = dictAposentadoria['der']
        self.dataCadastro = dictAposentadoria['dataCadastro']
        self.dataUltAlt = dictAposentadoria['dataUltAlt']

    def __eq__(self, other):
        return self.aposentadoriaId == other.aposentadoriaId

    def prettyPrint(self):
        print(f"""
        Aposentadoria(
            aposentadoriaId: {self.aposentadoriaId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            tipo: {self.tipo},
            contribMeses: {self.contribMeses},
            contribAnos: {self.contribAnos},
            valorBeneficio: {self.valorBeneficio},
            dib: {self.dib},
            der: {self.der},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")


@post_save(sender=Aposentadoria)
def inserindoAposentadoria(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::inserindoAposentadoria___________________{TABLENAME}')


@pre_delete(sender=Aposentadoria)
def deletandoAposentadoria(*args, **kwargs):
    info(f'{TipoLog.DataBase.value}::deletandoAposentadoria___________________{TABLENAME}')