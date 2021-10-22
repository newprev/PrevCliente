from modelos.baseModelORM import BaseModel, DATEFORMATS
from modelos.clienteORM import Cliente
from modelos.processosORM import Processos
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, ForeignKeyField, BooleanField, BigIntegerField, DateField, IntegerField, DateTimeField, FloatField
from datetime import datetime

TABLENAME = 'aposentadoria'


class Aposentadoria(BaseModel, Model):
    TIPOS = (
        ('TCAR', 'TEMPO CONTRIBUICAO AR'),
        ('IDAR', 'IDADE AR'),
        ('RIDM', 'REDUCAO IDADE MINIMA'),
        ('RETC', 'REDUCAO TEMPO CONTRIBUICAO'),
        ('PD50', 'PEDAGIO 50'),
        ('P100', 'PEDAGIO 100'),
        ('POTR', 'TRANSICAO PONTOS'),
        ('8595', 'REGRA 8595')
    )
    
    aposentadoriaId = AutoField(column_name='aposentadoriaId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente)
    processoId = ForeignKeyField(column_name='processoId', field='processoId', model=Processos)
    seq = IntegerField(null=False)
    tipo = CharField(choices=TIPOS)
    contribMeses = IntegerField()
    contribAnos = IntegerField()
    valorBeneficio = FloatField()
    dib = DateField(default=datetime.min)
    der = DateField(default=datetime.min)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

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
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoAposentadoria>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoAposentadoria>___________________ |Erro| {TABLENAME}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=Aposentadoria)
def deletandoAposentadoria(*args, **kwargs):
    logPrioridade(f'DELETE<inserindoAposentadoria>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)