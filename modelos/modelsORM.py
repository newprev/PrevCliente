from datetime import datetime

from peewee import *

database = SqliteDatabase('Daos/producao.db')

class BaseModel(Model):
    class Meta:
        database = database

class Escritorios(BaseModel):
    escritorioId = AutoField(column_name='escritorioId', null=True)
    bairro = CharField(null=True)
    cep = CharField(null=True)
    cidade = CharField(null=True)
    cnpj = CharField(null=True)
    complemento = CharField()
    cpf = CharField()
    email = CharField()
    endereco = CharField(null=True)
    estado = CharField(default='SP')
    inscEstadual = CharField(column_name='inscEstadual', null=True)
    nomeEscritorio = CharField(column_name='nomeEscritorio')
    nomeFantasia = CharField(column_name='nomeFantasia')
    numero = IntegerField()
    telefone = CharField(null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'escritorios'

class Advogados(BaseModel):
    advogadoId = AutoField(column_name='advogadoId', null=True)
    escritorio = ForeignKeyField(column_name='escritorioId', field='escritorioId', model=Escritorios, backref='escritorios')
    admin = BooleanField(default=False)
    ativo = BooleanField(default=False)
    confirmado = BooleanField()
    email = CharField()
    estadoCivil = CharField(column_name='estadoCivil')
    login = CharField()
    nacionalidade = CharField()
    nomeUsuario = CharField(column_name='nomeUsuario')
    numeroOAB = CharField(column_name='numeroOAB')
    senha = CharField(null=False)
    sobrenomeUsuario = CharField(column_name='sobrenomeUsuario', null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'advogados'

class Cliente(BaseModel):
    clienteId = AutoField(column_name='clienteId', null=True)
    escritorioId = ForeignKeyField(column_name='escritorioId', field='escritorioId', model=Escritorios, backref='escritorios')
    agenciaBanco = CharField(column_name='agenciaBanco', null=True)
    bairro = CharField(null=True)
    cep = CharField()
    cidade = CharField()
    complemento = CharField(null=True)
    cpfCliente = CharField(column_name='cpfCliente', null=True)
    dataNascimento = DateField(column_name='dataNascimento', default=datetime.now)
    email = CharField()
    endereco = CharField()
    estado = CharField()
    estadoCivil = CharField(column_name='estadoCivil', default='SOLTEIRO(A)', null=True)
    genero = CharField(default='M')
    grauEscolaridade = CharField(column_name='grauEscolaridade', null=True)
    idade = IntegerField()
    nit = CharField()
    nomeBanco = CharField(column_name='nomeBanco', null=True)
    nomeCliente = CharField(column_name='nomeCliente')
    nomeMae = CharField(column_name='nomeMae')
    numCarteiraProf = CharField(column_name='numCarteiraProf', null=True)
    numero = IntegerField()
    numeroConta = CharField(column_name='numeroConta', null=True)
    pixCliente = CharField(column_name='pixCliente', null=True)
    profissao = CharField()
    quaCarteiraProf = CharField(column_name='quaCarteiraProf', null=True)
    rgCliente = CharField(column_name='rgCliente')
    senhaINSS = CharField(column_name='senhaINSS', null=True)
    serieCarteiraProf = CharField(column_name='serieCarteiraProf', null=True)
    sobrenomeCliente = CharField(column_name='sobrenomeCliente')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt')
    # telefone = CharField(null=True)

    class Meta:
        table_name = 'cliente'

class CnisBeneficios(BaseModel):
    beneficiosId = AutoField(column_name='beneficiosId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    dado_origem = CharField(column_name='dadoOrigem', default='CNIS')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_fim = DateField(column_name='dataFim')
    data_inicio = DateField(column_name='dataInicio')
    dataUltAlt = DateTimeField(column_name='dataUltAlt')
    especie = CharField()
    nb = BigIntegerField()
    seq = IntegerField()
    situacao = CharField()

    class Meta:
        table_name = 'cnisBeneficios'

class CnisCabecalhos(BaseModel):
    cabecalhosId = AutoField(column_name='cabecalhosId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente)
    seq = IntegerField(null=False)
    cdEmp = CharField(column_name='cdEmp', null=True)
    dadoFaltante = BooleanField(column_name='dadoFaltante', default=False)
    dadoOrigem = CharField(column_name='dadoOrigem', default='CNIS')
    dataFim = DateField(column_name='dataFim', null=True)
    dataInicio = DateField(column_name='dataInicio')
    especie = CharField(null=True)
    indicadores = CharField(null=True)
    nb = BigIntegerField(null=True)
    nit = CharField(null=False)
    nomeEmp = CharField(column_name='nomeEmp', null=True)
    orgVinculo = CharField(column_name='orgVinculo', null=True)
    situacao = CharField(null=True)
    tipoVinculo = CharField(column_name='tipoVinculo', null=True)
    ultRem = DateField(column_name='ultRem', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'cnisCabecalhos'

class CnisContribuicoes(BaseModel):
    contribuicoesId = AutoField(column_name='contribuicoesId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    seq = IntegerField(null=False)
    competencia = DateField(null=False)
    contribuicao = FloatField(null=False)
    dadoOrigem = CharField(column_name='dadoOrigem')
    dataPagamento = DateField(column_name='dataPagamento')
    indicadores = CharField(default=None)
    salContribuicao = FloatField(column_name='salContribuicao')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'cnisContribuicoes'

class CnisRemuneracoes(BaseModel):
    remuneracoesId = AutoField(column_name='remuneracoesId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, null=True)
    seq = IntegerField(null=False)
    competencia = DateField(null=False)
    dadoOrigem = CharField(column_name='dadoOrigem')
    remuneracao = FloatField()
    indicadores = CharField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'cnisRemuneracoes'

class ConvMon(BaseModel):
    convMonId = AutoField(column_name='convMonId', null=True)
    conversao = CharField(null=False)
    dataFinal = DateField(column_name='dataFinal')
    dataInicial = DateField(column_name='dataInicial', null=False)
    fator = FloatField(null=False)
    moedaCorrente = BooleanField(column_name='moedaCorrente')
    nomeMoeda = CharField(column_name='nomeMoeda')
    sinal = CharField(null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'convMon'

class EspecieBenef(BaseModel):
    especieId = AutoField(column_name='especieId', null=True)
    descricao = CharField()

    class Meta:
        table_name = 'especieBenef'

class ExpSobrevida(BaseModel):
    infoId = AutoField(column_name='infoId', null=True)
    dataReferente = DateField(column_name='dataReferente')
    expectativaSobrevida = IntegerField(column_name='expectativaSobrevida')
    idade = IntegerField(null=False)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'expSobrevida'

class Indicadores(BaseModel):
    indicadorId = CharField(column_name='indicadorId', null=True, primary_key=True)
    descricao = CharField()
    fonte = CharField()
    resumo = CharField()
    dataUltAlt = DateTimeField(column_name='dataUltAlt')

    class Meta:
        table_name = 'indicadores'

class IndiceAtuMonetaria(BaseModel):
    indiceId = AutoField(column_name='indiceId', null=True)
    dataReferente = DateField(column_name='dataReferente')
    dib = BigIntegerField()
    fator = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'indiceAtuMonetaria'

class Ppp(BaseModel):
    pppId = IntegerField(column_name='pppId', null=True, primary_key=True)
    clienteId = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    caEpi = CharField(column_name='caEpi', null=True)
    cnae = CharField(null=True)
    cnpj = CharField(null=True)
    ctps = CharField(null=True)
    dataAdminssao = DateField(column_name='dataAdminssao', null=True)
    dataNascimento = DateField(column_name='dataNascimento')
    dataRegistro = DateField(column_name='dataRegistro', null=True)
    eficEpc = CharField(column_name='eficEpc', null=True)
    eficEpi = CharField(column_name='eficEpi', null=True)
    exposicaoDataFim = DateField(column_name='exposicaoDataFim', null=True)
    exposicaoDataInicio = DateField(column_name='exposicaoDataInicio', null=True)
    exposicaoFator = CharField(column_name='exposicaoFator', null=True)
    exposicaoIntensidade = CharField(column_name='exposicaoIntensidade', null=True)
    exposicaoTecnicaUtilizada = CharField(column_name='exposicaoTecnicaUtilizada', null=True)
    exposicaoTipo = CharField(column_name='exposicaoTipo', null=True)
    genero = CharField()
    nit = CharField()
    nomeEmpresa = CharField(column_name='nomeEmpresa', null=True)
    numCAT = CharField(column_name='numCAT', null=True)
    profissiografiaData = DateField(column_name='profissiografiaData', null=True)
    profissiografiaDesc = CharField(column_name='profissiografiaDesc', null=True)
    sitEmpregado = CharField(column_name='sitEmpregado', null=True)
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'ppp'

class Processos(BaseModel):
    processoId = AutoField(column_name='processoId', null=True)
    advogado = ForeignKeyField(column_name='advogadoId', field='advogadoId', model=Advogados, null=True, backref='advogados')
    cliente = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, null=True, backref='cliente')
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

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

class Telefones(BaseModel):
    telefoneId = AutoField(column_name='telefoneId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='clienteId', model=Cliente, backref='cliente')
    ativo = BooleanField(default=True)
    numero = CharField(null=False)
    pessoalRecado = CharField(column_name='pessoalRecado')
    tipoTelefone = CharField(column_name='tipoTelefone')
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'telefones'

class TetosPrev(BaseModel):
    tetosPrevId = AutoField(column_name='tetosPrevId', null=True)
    dataValidade = DateField(column_name='dataValidade')
    valor = FloatField()
    dataCadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    dataUltAlt = DateTimeField(column_name='dataUltAlt', default=datetime.now)

    class Meta:
        table_name = 'tetosPrev'

