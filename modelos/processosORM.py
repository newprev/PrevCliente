from datetime import datetime
from peewee import AutoField, ForeignKeyField, CharField, DateField, IntegerField, FloatField, DateTimeField, BooleanField
from playhouse.signals import Model, post_save, pre_delete
from systemLog.logs import logPrioridade
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from modelos.baseModelORM import BaseModel, DATEFORMATS
from modelos.advogadoORM import Advogados
from modelos.clienteORM import Cliente
from modelos.tipoBeneficioORM import TipoBeneficioModel

TABLENAME = 'processos'


class Processos(BaseModel, Model):
    processoId = AutoField(primary_key=True, column_name='processoId', null=True)
    advogadoId = ForeignKeyField(column_name='advogadoId', field='advogadoId', model=Advogados, null=True, backref='advogados')
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, null=True, backref='cliente')
    cidade = CharField(default='São Paulo')
    dataFim = DateField(column_name='dataFim', null=True, formats=DATEFORMATS)
    dataInicio = DateField(column_name='dataInicio', null=True, formats=DATEFORMATS)
    der = DateField(null=True, formats=DATEFORMATS)
    dib = DateField(null=True, formats=DATEFORMATS)
    estado = CharField(null=True)
    incidenteProcessual = IntegerField(column_name='incidenteProcessual', null=True)
    mediaSalarial = FloatField(column_name='mediaSalarial', null=True)
    natureza = IntegerField(default=0, null=True)
    numeroProcesso = CharField(column_name='numeroProcesso', null=True)
    pontuacao = IntegerField(null=True)
    situacaoId = IntegerField(column_name='situacaoId', default=0)
    subTipoApos = IntegerField(column_name='subTipoApos', null=True)
    tempoContribuicao = IntegerField(column_name='tempoContribuicao', null=True)
    tipoBeneficio = ForeignKeyField(column_name='tipoBeneficio', field='tipoId', model=TipoBeneficioModel, null=True, backref='TipoBeneficioModel')
    tipoProcesso = IntegerField(column_name='tipoProcesso', null=True)
    valorCausa = FloatField(column_name='valorCausa', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'processos'

    def toDict(self, recursive=False):
        dictUsuario = {
            'processoId': self.processoId,
            'clienteId': self.clienteId,
            'advogadoId': self.advogadoId.advogadoId,
            'numeroProcesso': self.numeroProcesso,
            'natureza': self.natureza,
            'tipoProcesso': self.tipoProcesso,
            'tipoBeneficio': self.tipoBeneficio,
            'subTipoApos': self.subTipoApos,
            'estado': self.estado,
            'cidade': self.cidade,
            'situacaoId': self.situacaoId,
            'tempoContribuicao': self.tempoContribuicao,
            'pontuacao': self.pontuacao,
            'dib': self.dib,
            'der': self.der,
            'mediaSalarial': self.mediaSalarial,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'valorCausa': self.valorCausa,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        if recursive:
            dictUsuario['clienteId'] = dictUsuario['clienteId'].toDict()

        return dictUsuario

    def fromDict(self, dictProcessos):
        self.processoId = dictProcessos['processoId']
        self.clienteId = dictProcessos['clienteId']
        self.advogadoId = dictProcessos['advogadoId']
        self.numeroProcesso = dictProcessos['numeroProcesso']
        self.natureza = dictProcessos['natureza']
        self.tipoProcesso = dictProcessos['tipoProcesso']
        self.tipoBeneficio = dictProcessos['tipoBeneficio']
        self.subTipoApos = dictProcessos['subTipoApos']
        self.estado = dictProcessos['estado']
        self.cidade = dictProcessos['cidade']
        self.situacaoId = dictProcessos['situacaoId']
        self.tempoContribuicao = dictProcessos['tempoContribuicao']
        self.pontuacao = dictProcessos['pontuacao']
        self.dib = dictProcessos['dib']
        self.der = dictProcessos['der']
        self.mediaSalarial = dictProcessos['mediaSalarial']
        self.dataInicio = dictProcessos['dataInicio']
        self.dataFim = dictProcessos['dataFim']
        self.valorCausa = dictProcessos['valorCausa']
        self.dataCadastro = dictProcessos['dataCadastro']
        self.dataUltAlt = dictProcessos['dataUltAlt']

        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        Processos(
            processoId: {self.processoId},
            clienteId: {self.clienteId},
            advogadoId: {self.advogadoId},
            numeroProcesso: {self.numeroProcesso},
            natureza: {self.natureza},
            tipoProcesso: {self.tipoProcesso},
            tipoBeneficio: {self.tipoBeneficio},
            subTipoApos: {self.subTipoApos},
            estado: {self.estado},
            cidade: {self.cidade},
            situacaoId: {self.situacaoId},
            tempoContribuicao: {self.tempoContribuicao},
            pontuacao: {self.pontuacao},
            dib: {self.dib},
            der: {self.der},
            mediaSalarial: {self.mediaSalarial},
            dataInicio: {self.dataInicio},
            dataFim: {self.dataFim},
            valorCausa: {self.valorCausa},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
        )""")
        

@post_save(sender=Processos)
def inserindoProcessos(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoProcessos>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComum)
    else:
        logPrioridade(f'UPDATE<inserindoProcessos>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComum)


@pre_delete(sender=Processos)
def deletandoProcessos(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoProcessos>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)