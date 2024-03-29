from logging import info, debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, ForeignKeyField, FloatField, DateTimeField, DateField, IntegerField, BooleanField
from datetime import datetime

from util.helpers.helpers import getTipoItem, getItemOrigem

TABLENAME = 'itemContribuicao'


class ItemContribuicao(BaseModel, Model):
    TIPO = getTipoItem()
    ORIGEM = getItemOrigem()

    itemContribuicaoId = AutoField(column_name='itemContribuicaoId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    seq = IntegerField(null=False)
    tipo = CharField(choices=TIPO, default='C')
    competencia = DateField(null=False, formats=DATEFORMATS)
    contribuicao = FloatField(null=True)
    salContribuicao = FloatField(null=True)
    ativPrimaria = BooleanField(null=False, default=True)
    dadoOrigem = CharField(column_name='dadoOrigem', choices=ORIGEM, default='C')
    geradoAutomaticamente = BooleanField(null=False, default=True)
    indicadores = CharField(default=None, null=True)
    validoTempoContrib = BooleanField(default=True)
    validoSalContrib = BooleanField(default=True)
    fatorInsalubridade = FloatField(null=True)
    grauDeficiencia = IntegerField(null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'itemContribuicao'

    def toDict(self):
        dictUsuario = {
            'itemContribuicaoId': self.itemContribuicaoId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'tipo': self.tipo,
            'competencia': self.competencia,
            'contribuicao': self.contribuicao,
            'ativPrimaria': self.ativPrimaria,
            'dadoOrigem': self.dadoOrigem,
            'indicadores': self.indicadores,
            'validoTempoContrib': self.validoTempoContrib,
            'validoSalContrib': self.validoSalContrib,
            'indiceInsalubridade': self.indiceInsalubridade,
            'indiceDeficiencia': self.indiceDeficiencia,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictContribuicoes):
        self.itemContribuicaoId = dictContribuicoes['itemContribuicaoId']
        self.clienteId = dictContribuicoes['clienteId']
        self.seq = dictContribuicoes['seq']
        self.tipo = dictContribuicoes['tipo']
        self.competencia = dictContribuicoes['competencia']
        self.contribuicao = dictContribuicoes['contribuicao']
        self.ativPrimaria = dictContribuicoes['ativPrimaria']
        self.dadoOrigem = dictContribuicoes['dadoOrigem']
        self.indicadores = dictContribuicoes['indicadores']
        self.validoTempoContrib = dictContribuicoes['validoTempoContrib']
        self.validoSalContrib = dictContribuicoes['validoSalContrib']
        self.indiceInsalubridade = dictContribuicoes['indiceInsalubridade']
        self.indiceDeficiencia = dictContribuicoes['indiceDeficiencia']
        self.dataCadastro = dictContribuicoes['dataCadastro']
        self.dataUltAlt = dictContribuicoes['dataUltAlt']

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        ItemContribuicao(
            itemContribuicaoId: {self.itemContribuicaoId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            tipo: {self.tipo},
            competencia: {self.competencia},
            contribuicao: {self.contribuicao},
            ativPrimaria: {self.ativPrimaria},
            dadoOrigem: {self.dadoOrigem},
            indicadores: {self.indicadores},
            validoTempoContrib: {self.validoTempoContrib},
            validoSalContrib: {self.validoSalContrib},
            indiceInsalubridade: {self.indiceInsalubridade},
            indiceDeficiencia: {self.indiceDeficiencia},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")


@post_save(sender=ItemContribuicao)
def inserindoItemContribuicao(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoItemContribuicao___________________{TABLENAME}')


@pre_delete(sender=ItemContribuicao)
def deletandoItemContribuicao(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoItemContribuicao___________________{TABLENAME}')
