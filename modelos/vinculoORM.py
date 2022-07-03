from logging import info, debug

from modelos.baseModelORM import BaseModel, DATEFORMATS
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete
from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoEdicao, Prioridade


from peewee import AutoField, CharField, ForeignKeyField, BooleanField, BigIntegerField, DateField, IntegerField, DateTimeField
from datetime import datetime

TABLENAME = 'cnisVinculos'


class CnisVinculos(BaseModel, Model):
    vinculoId = AutoField(column_name='vinculoId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente)
    seq = IntegerField(null=False)
    cdEmp = CharField(column_name='cdEmp', null=True)
    dadoFaltante = BooleanField(column_name='dadoFaltante', default=False)
    dadoOrigem = CharField(column_name='dadoOrigem', default='CNIS', max_length=10)
    dataFim = DateField(column_name='dataFim', null=True, formats=DATEFORMATS)
    dataInicio = DateField(column_name='dataInicio', formats=DATEFORMATS)
    especie = CharField(null=True)
    indicadores = CharField(null=True)
    nb = BigIntegerField(column_name='nb', null=True)
    nit = CharField(null=False)
    nomeEmp = CharField(column_name='nomeEmp', null=True)
    orgVinculo = CharField(column_name='orgVinculo', null=True)
    situacao = CharField(null=True)
    tipoVinculo = CharField(column_name='tipoVinculo', null=True)
    contribFaltante = BooleanField(default=False)
    ultRem = DateField(column_name='ultRem', null=True, formats=DATEFORMATS)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'cnisVinculos'

    def atualizaDadoFaltante(self):
        # Se nb não existe, é uma contribuição. Caso contrário, o vínculo é um benefício do INSS
        if self.nb is None:
            self.dadoFaltante = self.dataInicio is None or self.dataFim is None
        else:
            self.dadoFaltante = (self.dataInicio is None or self.dataFim is None) and self.situacao == 'CESSADO'

    def toDict(self):
        dictUsuario = {
            'vinculoId': self.vinculoId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'nit': self.nit,
            'nb': self.nb,
            'cdEmp': self.cdEmp,
            'nomeEmp': self.nomeEmp,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'tipoVinculo': self.tipoVinculo,
            'contribFaltante': self.contribFaltante,
            'orgVinculo': self.orgVinculo,
            'especie': self.especie,
            'indicadores': self.indicadores,
            'ultRem': self.ultRem,
            'dadoOrigem': self.dadoOrigem,
            'situacao': self.situacao,
            'dadoFaltante': self.dadoFaltante,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictCabecalho):
        self.vinculoId = dictCabecalho['vinculoId']
        self.clienteId = dictCabecalho['clienteId']
        self.seq = dictCabecalho['seq']
        self.nit = dictCabecalho['nit']
        self.nb = int(dictCabecalho['nb'])
        self.cdEmp = dictCabecalho['cdEmp']
        self.nomeEmp = dictCabecalho['nomeEmp']
        self.dataInicio = dictCabecalho['dataInicio']
        self.dataFim = dictCabecalho['dataFim']
        self.tipoVinculo = dictCabecalho['tipoVinculo']
        self.contribFaltante = dictCabecalho['contribFaltante']
        self.orgVinculo = dictCabecalho['orgVinculo']
        self.especie = dictCabecalho['especie']
        self.indicadores = dictCabecalho['indicadores']
        self.ultRem = dictCabecalho['ultRem']
        self.dadoOrigem = dictCabecalho['dadoOrigem']
        self.situacao = dictCabecalho['situacao']
        self.dadoFaltante = dictCabecalho['dadoFaltante']
        self.dataCadastro = dictCabecalho['dataCadastro']
        self.dataUltAlt = dictCabecalho['dataUltAlt']

    def __eq__(self, other):
        return self.vinculoId == other.vinculoId

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        Cabecalho(
            vinculoId: {self.vinculoId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            nit: {self.nit},
            nb: {self.nb},
            cdEmp: {self.cdEmp},
            nomeEmp: {self.nomeEmp},
            dataInicio: {self.dataInicio},
            dataFim: {self.dataFim},
            tipoVinculo: {self.tipoVinculo},
            contribFaltante: {self.contribFaltante},
            orgVinculo: {self.orgVinculo},
            especie: {self.especie},
            indicadores: {self.indicadores},
            ultRem: {self.ultRem},
            dadoOrigem: {self.dadoOrigem},
            situacao: {self.situacao},
            dadoFaltante: {self.dadoFaltante},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")


@post_save(sender=CnisVinculos)
def inserindoVinculo(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::inserindoVinculo___________________{TABLENAME}')


@pre_delete(sender=CnisVinculos)
def deletandoVinculo(*args, **kwargs):
    debug(f'{TipoLog.DataBase.value}::deletandoVinculo___________________{TABLENAME}')
