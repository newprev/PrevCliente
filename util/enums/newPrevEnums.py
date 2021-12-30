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
    saidaComum = 200
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


class ErroConexao(Enum):
    ConnectionError = 0

class MomentoEntrevista(Enum):
    cadastro = 0
    naturezaProcesso = 1
    tipoProcesso = 2
    tipoBeneficio = 3
    tipoAtividade = 4
    telaGeraDocs = 5

class EtapaEntrevista(Enum):
    infoPessoais = 0
    infoProcessual = 1
    detalhamento = 2
    documentacao = 3

class TipoWidget(Enum):
    label = 0
    icone = 1

class TipoContribuicao(Enum):
    contribuicao = 'C'
    remuneracao = 'R'
    beneficio = 'B'

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

class TipoFiltro(Enum):
    indicador = 0
    data = 1
