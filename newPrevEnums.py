from enum import Enum

class TelaPosicao(Enum):
    Cliente = 0
    Calculos = 1
    Configuracoes = 2
    Ferramentas = 3
    Entrevista = 4

class TiposConexoes(Enum):
    local = 1
    nuvem = 2
    sqlite = 3

class TamanhoData(Enum):
    p = 1
    m = 2
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
    erro = 7

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
    AposDeficiencia = 1
    AposRural = 2
    AposEspecial = 3
    AuxDoenca = 4
    AuxReclusao = 5
    BeneIdoso = 6
    BeneDeficiencia = 7
    PensaoMorte = 8
    SalMaternidade = 9

class TipoWidget(Enum):
    label = 0
    icone = 1

class EtapaEntrevista(Enum):
    infoPessoais = 0
    infoProcessual = 1
    detalhamento = 2
    documentacao = 3