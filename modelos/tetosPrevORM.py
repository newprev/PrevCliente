from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade

from peewee import DateField, DateTimeField, AutoField, FloatField
from datetime import datetime


class TetosPrev(BaseModel, Model):
    tetosPrevId = AutoField(column_name='tetosPrevId', null=True)
    dataValidade = DateField(column_name='dataValidade')
    valor = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'tetosPrev'
        
    def toDict(self):
        dictTetosPrev = {
            'tetosPrevId': self.tetosPrevId,
            'dataValidade': self.dataValidade,
            'valor': self.valor
        }
        return dictTetosPrev

    def fromDict(self, dictTeto):
        self.tetosPrevId = dictTeto['tetosPrevId']
        self.dataValidade = dictTeto['dataValidade']
        self.valor = dictTeto['valor']
        self.dataUltAlt = datetime.now()
        self.dataCadastro = datetime.now()
        return self

    def prettyPrint(self):
        return f"""TetosPrevModelo(
            tetosPrevId: {self.tetosPrevId},
            dataValidade: {self.dataValidade},
            valor: {self.valor}
        )"""
    
    
@post_save(sender=TetosPrev)
def inserindoTetosPrev(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoTetosPrev>___________________{TetosPrev.Meta.table_name}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoTetosPrev>___________________ |Erro| {TetosPrev.Meta.table_name}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=TetosPrev)
def deletandoTetosPrev(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoTetosPrev>___________________{TetosPrev.Meta.table_name}', TipoEdicao.delete, Prioridade.saidaImportante)
