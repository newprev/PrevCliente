from enum import Enum


class EtapaEntrevista(Enum):
    naturezaProcesso = 0
    tipoBeneficio = 1
    tipoProcesso = 2
    quizEntrevista = 3


class CategoriaQuiz(Enum):
    insalubridade = 0
    deficiencia = 1
    servicoMilitar = 2
    trabalhoRural = 3
    alteracaoManual = 4
    outros = 5
