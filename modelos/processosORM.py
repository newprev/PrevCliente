from datetime import datetime
from peewee import AutoField, ForeignKeyField, CharField, DateField, IntegerField, FloatField, DateTimeField

from modelos.baseModelORM import BaseModel
from modelos.advogadoORM import Advogados
from modelos.clientesORM import Cliente


class Processos(BaseModel):
    processoId = AutoField(column_name='processoId', null=True)
    advogado = ForeignKeyField(column_name='advogadoId', field='advogadoId', model=Advogados, null=True, backref='advogados')
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, null=True, backref='cliente')
    cidade = CharField()
    dataFim = DateField(column_name='dataFim', null=True)
    dataInicio = DateField(column_name='dataInicio', null=True)
    der = DateField(null=True)
    dib = DateField(null=True)
    estado = CharField(null=True)
    incidenteProcessual = IntegerField(column_name='incidenteProcessual', null=True)
    mediaSalarial = FloatField(column_name='mediaSalarial', null=True)
    natureza = IntegerField()
    numeroProcesso = CharField(column_name='numeroProcesso', null=True)
    pontuacao = IntegerField(null=True)
    situacaoId = IntegerField(column_name='situacaoId', default=1)
    subTipoApos = IntegerField(column_name='subTipoApos')
    tempoContribuicao = IntegerField(column_name='tempoContribuicao', null=True)
    tipoBeneficio = IntegerField(column_name='tipoBeneficio')
    tipoProcesso = IntegerField(column_name='tipoProcesso')
    valor_causa = FloatField(column_name='valorCausa', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'processos'