from modelos.baseModelORM import BaseModel, DATEFORMATS
from modelos.clienteORM import Cliente
from playhouse.signals import Model, post_save, pre_delete
from systemLog.logs import logPrioridade
from util.enums.newPrevEnums import TipoEdicao, Prioridade

from peewee import DateField, DateTimeField, IntegerField, ForeignKeyField, CharField
from datetime import datetime

TABLENAME = 'ppp'


class Ppp(BaseModel, Model):
    pppId = IntegerField(column_name='pppId', null=True, primary_key=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    caEpi = CharField(column_name='caEpi', null=True)
    cnae = CharField(null=True)
    cnpj = CharField(null=True)
    ctps = CharField(null=True)
    dataAdminssao = DateField(column_name='dataAdminssao', null=True, formats=DATEFORMATS)
    dataNascimento = DateField(column_name='dataNascimento', formats=DATEFORMATS)
    dataRegistro = DateField(column_name='dataRegistro', null=True, formats=DATEFORMATS)
    eficEpc = CharField(column_name='eficEpc', null=True)
    eficEpi = CharField(column_name='eficEpi', null=True)
    exposicaoDataFim = DateField(column_name='exposicaoDataFim', null=True, formats=DATEFORMATS)
    exposicaoDataInicio = DateField(column_name='exposicaoDataInicio', null=True, formats=DATEFORMATS)
    exposicaoFator = CharField(column_name='exposicaoFator', null=True)
    exposicaoIntensidade = CharField(column_name='exposicaoIntensidade', null=True)
    exposicaoTecnicaUtilizada = CharField(column_name='exposicaoTecnicaUtilizada', null=True)
    exposicaoTipo = CharField(column_name='exposicaoTipo', null=True)
    genero = CharField()
    nit = CharField()
    nomeEmpresa = CharField(column_name='nomeEmpresa', null=True)
    numCAT = CharField(column_name='numCAT', null=True)
    profissiografiaData = DateField(column_name='profissiografiaData', null=True, formats=DATEFORMATS)
    profissiografiaDesc = CharField(column_name='profissiografiaDesc', null=True)
    sitEmpregado = CharField(column_name='sitEmpregado', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = 'ppp'
        
    def toDict(self):
        dictPpp = {
            'pppId': self.pppId,
            'cnpj': self.cnpj,
            'nomeEmpresa': self.nomeEmpresa,
            'cnae': self.cnae,
            'sitEmpregado': self.sitEmpregado,
            'nit': self.nit,
            'dataNascimento': self.dataNascimento,
            'genero': self.genero,
            'ctps': self.ctps,
            'dataAdminssao': self.dataAdminssao,
            'dataRegistro': self.dataRegistro,
            'numCAT': self.numCAT,
            'profissiografiaData': self.profissiografiaData,
            'profissiografiaDesc': self.profissiografiaDesc,
            'exposicaoDataInicio': self.exposicaoDataInicio,
            'exposicaoDataFim': self.exposicaoDataFim,
            'exposicaoTipo': self.exposicaoTipo,
            'exposicaoFator': self.exposicaoFator,
            'exposicaoIntensidade': self.exposicaoIntensidade,
            'exposicaoTecnicaUtilizada': self.exposicaoTecnicaUtilizada,
            'eficEpc': self.eficEpc,
            'eficEpi': self.eficEpi,
            'caEpi': self.caEpi,
            'dataUltAlt': self.dataUltAlt
        }
        return dictPpp

    def fromDict(self, dictPpp):
        self.pppId = dictPpp['pppId']
        self.cnpj = dictPpp['cnpj']
        self.nomeEmpresa = dictPpp['nomeEmpresa']
        self.cnae = dictPpp['cnae']
        self.sitEmpregado = dictPpp['sitEmpregado']
        self.nit = dictPpp['nit']
        self.dataNascimento = dictPpp['dataNascimento']
        self.genero = dictPpp['genero']
        self.ctps = dictPpp['ctps']
        self.dataAdminssao = dictPpp['dataAdminssao']
        self.dataRegistro = dictPpp['dataRegistro']
        self.numCAT = dictPpp['numCAT']
        self.profissiografiaData = dictPpp['profissiografiaData']
        self.profissiografiaDesc = dictPpp['profissiografiaDesc']
        self.exposicaoDataInicio = dictPpp['exposicaoDataInicio']
        self.exposicaoDataFim = dictPpp['exposicaoDataFim']
        self.exposicaoTipo = dictPpp['exposicaoTipo']
        self.exposicaoFator = dictPpp['exposicaoFator']
        self.exposicaoIntensidade = dictPpp['exposicaoIntensidade']
        self.exposicaoTecnicaUtilizada = dictPpp['exposicaoTecnicaUtilizada']
        self.eficEpc = dictPpp['eficEpc']
        self.eficEpi = dictPpp['eficEpi']
        self.caEpi = dictPpp['caEpi']
        self.dataUltAlt = dictPpp['dataUltAlt']
        return self

    def prettyPrint(self, backRef: bool = False):
        print(f"""
        PppModelo(
            pppId: {self.pppId},
            cnpj: {self.cnpj},
            nomeEmpresa: {self.nomeEmpresa},
            cnae: {self.cnae},
            sitEmpregado: {self.sitEmpregado},
            nit: {self.nit},
            dataNascimento: {self.dataNascimento},
            genero: {self.genero},
            ctps: {self.ctps},
            dataAdminssao: {self.dataAdminssao},
            dataRegistro: {self.dataRegistro},
            numCAT: {self.numCAT},
            profissiografiaData: {self.profissiografiaData},
            profissiografiaDesc: {self.profissiografiaDesc},
            exposicaoDataInicio: {self.exposicaoDataInicio},
            exposicaoDataFim: {self.exposicaoDataFim},
            exposicaoTipo: {self.exposicaoTipo},
            exposicaoFator: {self.exposicaoFator},
            exposicaoIntensidade: {self.exposicaoIntensidade},
            exposicaoTecnicaUtilizada: {self.exposicaoTecnicaUtilizada},
            eficEpc: {self.eficEpc},
            eficEpi: {self.eficEpi},
            caEpi: {self.caEpi},
            dataUltAlt: {self.dataUltAlt}
        )""")
    
    
@post_save(sender=Ppp)
def inserindoPpp(*args, **kwargs):
    if kwargs['created']:
        logPrioridade(f'INSERT<inserindoPpp>___________________{TABLENAME}', TipoEdicao.insert, Prioridade.saidaComum)
    else:
        logPrioridade(f'UPDATE<inserindoPpp>___________________ {TABLENAME}', TipoEdicao.update, Prioridade.saidaComum)


@pre_delete(sender=Ppp)
def deletandoPpp(*args, **kwargs):
    logPrioridade(f'DELETE<deletandoPpp>___________________{TABLENAME}', TipoEdicao.delete, Prioridade.saidaImportante)
    
