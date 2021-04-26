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