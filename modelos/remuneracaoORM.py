from modelos.baseModelORM import BaseModel
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade

from peewee import AutoField, CharField, ForeignKeyField, DateTimeField, FloatField, DateField, IntegerField
from datetime import datetime

TABLENAME = 'cnisRemuneracoes'


class CnisRemuneracoes(BaseModel, Model):
    remuneracoesId = AutoField(column_name='remuneracoesId', null=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, null=True)
    seq = IntegerField(null=False)
    competencia = DateField(null=False)
    dadoOrigem = CharField(column_name='dadoOrigem')
    remuneracao = FloatField()
    indicadores = CharField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'cnisRemuneracoes'
        
    def toDict(self):
        dictUsuario = {
            'remuneracoesId': self.remuneracoesId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'competencia': self.competencia,
            'remuneracao': self.remuneracao,
            'indicadores': self.indicadores,
            'dadoOrigem': self.dadoOrigem,
            'dataUltAlt': self.dataUltAlt,
            'dataCadastro': self.dataCadastro
        }
        return dictUsuario

    def fromDict(self, dictRemuneracoes):
        self.remuneracoesId = dictRemuneracoes['remuneracoesId']
        self.clienteId = dictRemuneracoes['clienteId']
        self.seq = dictRemuneracoes['seq']
        self.competencia = dictRemuneracoes['competencia']
        self.remuneracao = dictRemuneracoes['remuneracao']
        self.dataCadastro = dictRemuneracoes['dataCadastro']
        self.dadoOrigem = dictRemuneracoes['dadoOrigem']
        self.indicadores = dictRemuneracoes['indicadores']
        self.dataUltAlt = dictRemuneracoes['dataUltAlt']

    def prettyPrint(self):
        return f"""Remuneracoes(
            remuneracoesId: {self.remuneracoesId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            competencia: {self.competencia},
            remuneracao: {self.remuneracao},
            indicadores: {self.indicadores},
            dadoOrigem: {self.dadoOrigem},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
        
        
@post_save(sender=CnisRemuneracoes)
def inserindoCnisRemuneracoes(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoCnisRemuneracoes>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoCnisRemuneracoes>___________________ |Erro| {TABLENAME}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=CnisRemuneracoes)
def deletandoCnisRemuneracoes(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoCnisRemuneracoes>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)
