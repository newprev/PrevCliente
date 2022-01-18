from enum import Enum


class Status(Enum):
    naoCadastrado = 0
    semCabecalho = 1
    semContrib = 2
    jaCadastrado = 3
    erro = 4
