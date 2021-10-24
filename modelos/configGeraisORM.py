from datetime import datetime

from peewee import Model, AutoField, ForeignKeyField, BooleanField, DateTimeField

from modelos.baseModelORM import BaseModel
from modelos.advogadoORM import Advogados

TABLENAME = 'configGerais'


class ConfigGerais(BaseModel, Model):
    configId = AutoField(column_name='configId', null=True)
    advogadoId = ForeignKeyField(column_name='advogadoId', field='advogadoId', model=Advogados, backref='advogados')
    iniciaAuto = BooleanField(default=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now())
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now())

    class Meta:
        table_name = TABLENAME

    def toDict(self):

        dictUsuario = {
            'configId': self.configId,
            'advogadoId': self.advogadoId.advogadoId,
            'iniciaAuto': self.iniciaAuto,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    # def fromDict(self, dictUsuario: dict, retornaInst: bool = True):
    #
    #     self.configId = dictUsuario['configId'][0]
    #     self.dataUltAlt = dictUsuario['dataUltAlt']
    #
    #     if retornaInst:
    #         return self

    def prettyPrint(self, backRef: bool = False):

        if backRef:
            print('--- backRef', end='')
            self.advogadoId.prettyPrint()
            print('backRef ---')

        print(f"""
            ConfigGerais(
                configId: {self.configId},
                escritorioId: {self.advogadoId},
                iniciaAuto: {self.iniciaAuto},
                dataCadastro: {self.dataCadastro},
                dataUltAlt: {self.dataUltAlt}
            )""")
