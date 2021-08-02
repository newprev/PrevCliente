from datetime import datetime

from peewee import *

database = SqliteDatabase('Daos/producao.db')

class BaseModel(Model):
    class Meta:
        database = database

class Escritorios(BaseModel):
    escritorio_id = AutoField(column_name='escritorioId', null=True)
    bairro = CharField(null=True)
    cep = CharField(null=True)
    cidade = CharField(null=True)
    cnpj = CharField(null=True)
    complemento = CharField()
    cpf = CharField()
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    email = CharField()
    endereco = CharField(null=True)
    estado = CharField()
    insc_estadual = CharField(column_name='inscEstadual', null=True)
    nome_escritorio = CharField(column_name='nomeEscritorio')
    nome_fantasia = CharField(column_name='nomeFantasia')
    numero = IntegerField()
    telefone = CharField(null=True)

    class Meta:
        table_name = 'escritorios'

class Advogados(BaseModel):
    advogado_id = AutoField(column_name='advogadoId', null=True)
    escritorio = ForeignKeyField(column_name='escritorioId', field='escritorio_id', model=Escritorios, null=True)
    admin = BooleanField()
    ativo = BooleanField()
    confirmado = BooleanField()
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    email = CharField()
    estado_civil = CharField(column_name='estadoCivil')
    login = CharField()
    nacionalidade = CharField()
    nome_usuario = CharField(column_name='nomeUsuario')
    numero_oab = CharField(column_name='numeroOAB')
    senha = CharField()
    sobrenome_usuario = CharField(column_name='sobrenomeUsuario')

    class Meta:
        table_name = 'advogados'

class Cliente(BaseModel):
    cliente_id = AutoField(column_name='clienteId', null=True)
    escritorio = ForeignKeyField(column_name='escritorioId', field='escritorio', model=Escritorios, null=True)
    agencia_banco = CharField(column_name='agenciaBanco', null=True)
    bairro = CharField(null=True)
    cep = CharField()
    cidade = CharField()
    complemento = CharField(null=True)
    cpf_cliente = CharField(column_name='cpfCliente', null=True)
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_nascimento = DateField(column_name='dataNascimento', default=datetime.now)
    data_ult_alt = DateTimeField(column_name='dataUltAlt')
    email = CharField()
    endereco = CharField()
    estado = CharField()
    estado_civil = CharField(column_name='estadoCivil', constraints=[SQL("DEFAULT 'SOLTEIRO(A)'")], null=True)
    genero = CharField(constraints=[SQL("DEFAULT 'M'")])
    grau_escolaridade = CharField(column_name='grauEscolaridade', null=True)
    idade = IntegerField()
    nit = CharField()
    nome_banco = CharField(column_name='nomeBanco', null=True)
    nome_cliente = CharField(column_name='nomeCliente')
    nome_mae = CharField(column_name='nomeMae')
    num_carteira_prof = CharField(column_name='numCarteiraProf', null=True)
    numero = IntegerField()
    numero_conta = CharField(column_name='numeroConta', null=True)
    pix_cliente = CharField(column_name='pixCliente', null=True)
    profissao = CharField()
    qua_carteira_prof = CharField(column_name='quaCarteiraProf', null=True)
    rg_cliente = CharField(column_name='rgCliente')
    senha_inss = CharField(column_name='senhaINSS', null=True)
    serie_carteira_prof = CharField(column_name='serieCarteiraProf', null=True)
    sobrenome_cliente = CharField(column_name='sobrenomeCliente')
    telefone = CharField(null=True)

    class Meta:
        table_name = 'cliente'

class CnisBeneficios(BaseModel):
    beneficios_id = AutoField(column_name='beneficiosId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='cliente_id', model=Cliente, null=True)
    dado_origem = CharField(column_name='dadoOrigem')
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_fim = DateField(column_name='dataFim')
    data_inicio = DateField(column_name='dataInicio')
    data_ult_alt = DateTimeField(column_name='dataUltAlt')
    especie = CharField()
    nb = BigIntegerField()
    seq = IntegerField()
    situacao = CharField()

    class Meta:
        table_name = 'cnisBeneficios'

class CnisCabecalhos(BaseModel):
    cabecalhos_id = AutoField(column_name='cabecalhosId', null=True)
    cd_emp = CharField(column_name='cdEmp', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='cliente_id', model=Cliente, null=True)
    dado_faltante = BooleanField(column_name='dadoFaltante', constraints=[SQL("DEFAULT FALSE")])
    dado_origem = CharField(column_name='dadoOrigem')
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_fim = DateField(column_name='dataFim', null=True)
    data_inicio = DateField(column_name='dataInicio')
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    especie = CharField(null=True)
    indicadores = CharField(null=True)
    nb = BigIntegerField(null=True)
    nit = CharField()
    nome_emp = CharField(column_name='nomeEmp', null=True)
    org_vinculo = CharField(column_name='orgVinculo', null=True)
    seq = IntegerField()
    situacao = CharField(null=True)
    tipo_vinculo = CharField(column_name='tipoVinculo', null=True)
    ult_rem = DateField(column_name='ultRem', null=True)

    class Meta:
        table_name = 'cnisCabecalhos'

class CnisContribuicoes(BaseModel):
    contribuicoes_id = AutoField(column_name='contribuicoesId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='cliente_id', model=Cliente, null=True)
    competencia = DateField()
    contribuicao = FloatField()
    dado_origem = CharField(column_name='dadoOrigem')
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_pagamento = DateField(column_name='dataPagamento')
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    indicadores = CharField()
    sal_contribuicao = FloatField(column_name='salContribuicao')
    seq = IntegerField()

    class Meta:
        table_name = 'cnisContribuicoes'

class CnisRemuneracoes(BaseModel):
    remuneracoes_id = AutoField(column_name='remuneracoesId', null=True)
    cliente = ForeignKeyField(column_name='clienteId', field='cliente_id', model=Cliente, null=True)
    competencia = DateField()
    dado_origem = CharField(column_name='dadoOrigem')
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    indicadores = CharField()
    remuneracao = FloatField()
    seq = IntegerField()

    class Meta:
        table_name = 'cnisRemuneracoes'

class ConvMon(BaseModel):
    conv_mon_id = AutoField(column_name='convMonId', null=True)
    conversao = CharField()
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_final = DateField(column_name='dataFinal')
    data_inicial = DateField(column_name='dataInicial')
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    fator = FloatField()
    moeda_corrente = BooleanField(column_name='moedaCorrente')
    nome_moeda = CharField(column_name='nomeMoeda')
    sinal = CharField()

    class Meta:
        table_name = 'convMon'

class EspecieBenef(BaseModel):
    especie_id = AutoField(column_name='especieId', null=True)
    descricao = CharField()

    class Meta:
        table_name = 'especieBenef'

class ExpSobrevida(BaseModel):
    info_id = AutoField(column_name='infoId', null=True)
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_referente = DateField(column_name='dataReferente')
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    expectativa_sobrevida = IntegerField(column_name='expectativaSobrevida')
    idade = IntegerField()

    class Meta:
        table_name = 'expSobrevida'

class Indicadores(BaseModel):
    indicador_id = CharField(column_name='indicadorId', null=True, primary_key=True)
    data_ult_alt = DateTimeField(column_name='dataUltAlt')
    descricao = CharField()
    fonte = CharField()
    resumo = CharField()

    class Meta:
        table_name = 'indicadores'

class IndiceAtuMonetaria(BaseModel):
    indice_id = AutoField(column_name='indiceId', null=True)
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_referente = DateField(column_name='dataReferente')
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    dib = BigIntegerField()
    fator = FloatField()

    class Meta:
        table_name = 'indiceAtuMonetaria'

class Ppp(BaseModel):
    ppp_id = IntegerField(column_name='pppId', null=True, primary_key=True)
    ca_epi = CharField(column_name='caEpi', null=True)
    cnae = CharField(null=True)
    cnpj = CharField(null=True)
    ctps = CharField(null=True)
    data_adminssao = DateField(column_name='dataAdminssao', null=True)
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_nascimento = DateField(column_name='dataNascimento')
    data_registro = DateField(column_name='dataRegistro', null=True)
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    efic_epc = CharField(column_name='eficEpc', null=True)
    efic_epi = CharField(column_name='eficEpi', null=True)
    exposicao_data_fim = DateField(column_name='exposicaoDataFim', null=True)
    exposicao_data_inicio = DateField(column_name='exposicaoDataInicio', null=True)
    exposicao_fator = CharField(column_name='exposicaoFator', null=True)
    exposicao_intensidade = CharField(column_name='exposicaoIntensidade', null=True)
    exposicao_tecnica_utilizada = CharField(column_name='exposicaoTecnicaUtilizada', null=True)
    exposicao_tipo = CharField(column_name='exposicaoTipo', null=True)
    genero = CharField()
    nit = CharField()
    nome_empresa = CharField(column_name='nomeEmpresa', null=True)
    num_cat = CharField(column_name='numCAT', null=True)
    profissiografia_data = DateField(column_name='profissiografiaData', null=True)
    profissiografia_desc = CharField(column_name='profissiografiaDesc', null=True)
    sit_empregado = CharField(column_name='sitEmpregado', null=True)

    class Meta:
        table_name = 'ppp'

class Processos(BaseModel):
    processo_id = AutoField(column_name='processoId', null=True)
    advogado = ForeignKeyField(column_name='advogadoId', field='advogado_id', model=Advogados, null=True)
    cidade = CharField()
    cliente = ForeignKeyField(column_name='clienteId', field='cliente_id', model=Cliente, null=True)
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_fim = DateField(column_name='dataFim', null=True)
    data_inicio = DateField(column_name='dataInicio', null=True)
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    der = DateField(null=True)
    dib = DateField(null=True)
    estado = CharField(null=True)
    incidente_processual = IntegerField(column_name='incidenteProcessual', null=True)
    media_salarial = FloatField(column_name='mediaSalarial', null=True)
    natureza = IntegerField()
    numero_processo = CharField(column_name='numeroProcesso', null=True)
    pontuacao = IntegerField(null=True)
    situacao_id = IntegerField(column_name='situacaoId', constraints=[SQL("DEFAULT 1")])
    sub_tipo_apos = IntegerField(column_name='subTipoApos')
    tempo_contribuicao = IntegerField(column_name='tempoContribuicao', null=True)
    tipo_beneficio = IntegerField(column_name='tipoBeneficio')
    tipo_processo = IntegerField(column_name='tipoProcesso')
    valor_causa = FloatField(column_name='valorCausa', null=True)

    class Meta:
        table_name = 'processos'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

class Telefones(BaseModel):
    telefone_id = AutoField(column_name='telefoneId', null=True)
    ativo = BooleanField()
    cliente = ForeignKeyField(column_name='clienteId', field='cliente_id', model=Cliente, null=True)
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    numero = CharField()
    pessoal_recado = CharField(column_name='pessoalRecado')
    tipo_telefone = CharField(column_name='tipoTelefone')

    class Meta:
        table_name = 'telefones'

class TetosPrev(BaseModel):
    tetos_prev_id = AutoField(column_name='tetosPrevId', null=True)
    data_cadastro = DateTimeField(column_name='dataCadastro', default=datetime.now)
    data_ult_alt = DateTimeField(column_name='dataUltAlt', default=datetime.now)
    data_validade = DateField(column_name='dataValidade')
    valor = FloatField()

    class Meta:
        table_name = 'tetosPrev'

