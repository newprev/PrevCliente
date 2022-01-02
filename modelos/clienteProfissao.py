from modelos.baseModelORM import BaseModel
from playhouse.signals import Model, post_save, pre_delete

from util.enums.newPrevEnums import TipoEdicao, Prioridade
from systemLog.logs import logPrioridade

from peewee import AutoField, CharField, IntegerField, DateTimeField, BooleanField, FloatField
from datetime import datetime

TABLENAME = 'clienteProfissao'


class ClienteProfissao(BaseModel, Model):
    infoId = AutoField(column_name='infoId')
    clienteId = IntegerField(column_name='clienteId')
    nomeProfissao = CharField(column_name='nomeProfissao', null=True)
    numCaretiraTrabalho = CharField(column_name='numCaretiraTrabalho', null=True)
    nit = CharField(column_name='nit')
    professor = BooleanField(column_name='professor', default=False)
    insalubridade = BooleanField(column_name='insalubridade', default=False)
    nlvInsalubre = FloatField(column_name='nlvInsalubre', null=True, default=None)
    jovemAprendiz = BooleanField(column_name='jovemAprendiz', default=False)
    servicoMilitar = BooleanField(column_name='servicoMilitar', default=False)
    observacoes = CharField(column_name='observacoes', max_length=4000, null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'ClienteProfissao'

    def toDict(self):
        dictUsuario = {
            'infoId': self.infoId,
            'clienteId': self.clienteId,
            'nomeProfissao': self.nomeProfissao,
            'numCaretiraTrabalho': self.numCaretiraTrabalho,
            'nit': self.nit,
            'professor': self.professor,
            'insalubridade': self.insalubridade,
            'nlvInsalubre': self.nlvInsalubre,
            'jovemAprendiz': self.jovemAprendiz,
            'servicoMilitar': self.servicoMilitar,
            'observacoes': self.observacoes
        }
        return dictUsuario

    def fromDict(self, dictCliente):
        self.infoId = dictCliente['infoId']
        self.clienteId = dictCliente['clienteId']
        self.nomeProfissao = dictCliente['nomeProfissao']
        self.numCaretiraTrabalho = dictCliente['numCaretiraTrabalho']
        self.nit = dictCliente['nit']
        self.professor = dictCliente['professor']
        self.insalubridade = dictCliente['insalubridade']
        self.nlvInsalubre = dictCliente['nlvInsalubre']
        self.jovemAprendiz = dictCliente['jovemAprendiz']
        self.servicoMilitar = dictCliente['servicoMilitar']
        self.observacoes = dictCliente['observacoes']

    def __bool__(self):
        return self.nit != '' and self.nit is not None

    def prettyPrint(self, backRef: bool = False):

        if backRef:
            print('--- backRef', end='')
            self.infoId.prettyPrint()
            self.telefoneId.prettyPrint()
            print('backRef ---')

        print("ClienteProfissao:")
        objeto: dict = self.toDict()

        for chave, valor in objeto.items():
            print(f"{chave}: {valor}")


@post_save(sender=ClienteProfissao)
def inserindoCliente(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoCabecalho>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComum)
    else:
        logPrioridade(f'UPDATE<inserindoCabecalho>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComum)


@pre_delete(sender=ClienteProfissao)
def deletandoCliente(*args, **kwargs):
    logPrioridade(f'DELETE<inserindoCabecalho>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)