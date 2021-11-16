from enum import Enum

class TiposConexoes(Enum):
    local = 1
    nuvem = 2
    sqlite = 3

class TamanhoData(Enum):
    p = 1
    m = 2
    mm = 5
    g = 3
    gg = 4

class Prioridade(Enum):
    saidaComun = 200
    saidaImportante = 300
    sync = 400

class TipoEdicao(Enum):
    select = 0
    insert = 1
    delete = 2
    update = 3
    dropTable = 4
    createTable = 5
    api = 6
    cache = 7
    erro = 8

class TelaLogin(Enum):
    inicio = 1
    buscaEscritorio = 0
    cadastro = 2

class ErroConexao(Enum):
    ConnectionError = 0

class MomentoEntrevista(Enum):
    cadastro = 0
    naturezaProcesso = 1
    tipoProcesso = 2
    tipoBeneficio = 3
    tipoAtividade = 4
    telaGeraDocs = 5

class NaturezaProcesso(Enum):
    administrativo = 0
    judicial = 1

class TipoProcesso(Enum):
    Concessao = 0
    Revisao = 1
    RecOrdinario = 2
    RecEspecial = 3

class TipoBeneficio(Enum):
    Aposentadoria = 0
    AuxDoenca = 1
    AuxAcidente = 2
    AuxReclusao = 3
    BeneIdoso = 4
    BeneDeficiencia = 5
    PensaoMorte = 6
    SalMaternidade = 7

class SubTipoAposentadoria(Enum):
    Idade = 0
    Rural = 1
    Deficiencia = 2
    Especial = 3
    TempoContrib = 4
    Invalidez = 5

class EtapaEntrevista(Enum):
    infoPessoais = 0
    infoProcessual = 1
    detalhamento = 2
    documentacao = 3

class TipoWidget(Enum):
    label = 0
    icone = 1

class TipoContribuicao(Enum):
    contribuicao = 0
    remuneracao = 1
    beneficio = 2

class AtivApos(Enum):
    laborInsalubre = 0
    laborDeficiente = 1
    tempoMilitar = 2
    regimeProprio = 3
    tempoRural = 4
    professor = 5
    contribMenorSalMin = 6
    contribBaixaRenda = 7
    onzePorCento = 8
    indicativoCnis = 9
    editarCnis = 10
    editarCnisB = 11
    faltaLaborCnis = 12
    acaoTrabalhista = 13
    aprendiz = 14
    seminarista = 15

class DireitoAdquirido(Enum):
    lei821391 = 0
    lei987699 = 1
    ec1032019 = 2

class RegraTransicao(Enum):
    todas = 0
    pontos = 1
    reducaoIdadeMinima = 2
    pedagio50 = 3
    reducaoTempoContribuicao = 4
    pedagio100 = 5

class RegraGeralAR(Enum):
    fator85_95 = 0
    idade = 1
    tempoContribuicao = 2

class GeneroCliente(Enum):
    masculino = 'M'
    feminino = 'F'

class ComparaData(Enum):
    anterior = 0
    posterior = 1
    igual = 2

class TipoIcone(Enum):
    beneficio = 0
    remuneracao = 1

class TipoItemContribuicao(Enum):
    beneficio = 'B'
    contribuicao = 'C'
    remuneracao = 'R'

class ItemOrigem(Enum):
    CNIS = 'C'
    NEWPREV = 'N'
    SIMULACAO = 'S'
