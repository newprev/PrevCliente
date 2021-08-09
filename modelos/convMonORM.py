from modelos.baseModelORM import BaseModel, DATEFORMATS
from playhouse.signals import Model, post_save, pre_delete
from logs import logPrioridade
from newPrevEnums import TipoEdicao, Prioridade

from datetime import datetime
from peewee import AutoField, DateField, BooleanField, CharField, DateTimeField, FloatField

TABLENAME = 'convMon'


class ConvMon(BaseModel, Model):
    convMonId = AutoField(column_name='convMonId', null=True)
    conversao = CharField(null=False)
    dataFinal = DateField(column_name='dataFinal', formats=DATEFORMATS)
    dataInicial = DateField(column_name='dataInicial', null=False, formats=DATEFORMATS)
    fator = FloatField(null=False)
    moedaCorrente = BooleanField(column_name='moedaCorrente')
    nomeMoeda = CharField(column_name='nomeMoeda')
    sinal = CharField(null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'convMon'

    def toDict(self):
        dictConvMon = {
            'convMonId': self.convMonId,
            'nomeMoeda': self.nomeMoeda,
            'fator': self.fator,
            'dataInicial': self.dataInicial,
            'dataFinal': self.dataFinal,
            'conversao': self.conversao,
            'moedaCorrente': self.moedaCorrente,
            'sinal': self.sinal,
            'dataUltAlt': self.dataUltAlt,
            'dataCadastro': self.dataCadastro
        }
        return dictConvMon

    def fromDict(self, dictConvMon: dict):
        if 'convMonId' in dictConvMon.keys():
            self.convMonId = dictConvMon['convMonId']

        if 'dataUltAlt' in dictConvMon.keys():
            self.dataUltAlt = dictConvMon['dataUltAlt']

        if 'dataCadastro' in dictConvMon.keys():
            self.dataCadastro = dictConvMon['dataCadastro']

        if dictConvMon['dataFinal'] is not None:
            self.dataFinal = dictConvMon['dataFinal']
        else:
            self.dataFinal = dictConvMon['dataInicial']

        self.nomeMoeda = dictConvMon['nomeMoeda']
        self.fator = dictConvMon['fator']
        self.dataInicial = dictConvMon['dataInicial']
        self.conversao = dictConvMon['conversao']
        self.moedaCorrente = dictConvMon['moedaCorrente']
        self.sinal = dictConvMon['sinal']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        ConvMonModelo(
            convMonId: {self.convMonId},
            nomeMoeda: {self.nomeMoeda},
            fator: {self.fator},
            dataInicial: {self.dataInicial},
            dataFinal: {self.dataFinal},
            conversao: {self.conversao},
            moedaCorrente: {self.moedaCorrente},
            sinal: {self.sinal},
            dataUltAlt: {self.dataUltAlt},
            dataCadastro: {self.dataCadastro}
        )""")


@post_save(sender=ConvMon)
def inserindoConvMon(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoConvMon>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComun)
    else:
        logPrioridade(f'INSERT<inserindoConvMon>___________________ |Erro| {TABLENAME}', TipoEdicao.erro, Prioridade.saidaImportante)


@pre_delete(sender=ConvMon)
def deletandoConvMon(*args, **kwargs):
    logPrioridade(f'DELETE<inserindoConvMon>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)
