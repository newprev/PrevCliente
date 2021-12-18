from enum import Enum


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

class SituacaoProcesso(Enum):
    aDarEntrada = 0
    emAndamento = 1
    arquivado = 2
    cancelado = 3
    finalizado = 4
