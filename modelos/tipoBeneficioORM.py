from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete
from systemLog.logs import logPrioridade
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import CharField, BooleanField, DateTimeField, AutoField
from datetime import datetime

TABLENAME = 'tipoBeneficio'


class TipoBeneficio(BaseModel, Model):
    tipoId = AutoField(column_name='tipoId', null=True, unique=True)
    nome = CharField(max_length=20, null=False)
    descricao = CharField(max_length=600, null=False)
    ativo = BooleanField(default=True)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())

    class Meta:
        table_name = 'tipoBeneficio'

    def toDict(self):
        dictSalario = {
            'tipoId': self.tipoId,
            'nome': self.nome,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'dataUltAlt': self.dataUltAlt,
            'dataCadastro': self.dataCadastro
        }
        return dictSalario

    def fromDict(self, dictSalario):
        self.tipoId = dictSalario['indicadorId']
        self.descricao = dictSalario['descricao']
        self.ativo = dictSalario['ativo']
        self.dataUltAlt = dictSalario['dataUltAlt']
        self.dataCadastro = dictSalario['dataCadastro']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        IndicadorModelo(
            tipoId: {self.tipoId},
            descricao: {self.descricao},
            ativo: {self.ativo},
            dataUltAlt: {self.dataUltAlt}
            dataCadastro: {self.dataCadastro}
        )""")


@post_save(sender=TipoBeneficio)
def inserindoTipoBeneficio(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoTipoBeneficio>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComum)
    else:
        logPrioridade(f'UPDATE<inserindoTipoBeneficio>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComum)


@pre_delete(sender=TipoBeneficio)
def deletandoTipoBeneficio(*args, **kwargs):
    logPrioridade(f'DELETE<inserindoTipoBeneficio>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)