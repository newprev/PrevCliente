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

class TelasEntrevista(Enum):
    cadastro = 0
    natureza = 1
    administrativo = 2
    judicial = 3

class TipoWidget(Enum):
    label = 0
    icone = 1

class EtapaEntrevista(Enum):
    infoPessoais = 0
    infoProcessual = 1
    detalhamento = 2
    documentacao = 3