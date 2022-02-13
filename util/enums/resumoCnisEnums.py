from enum import Enum


class TelaResumo(Enum):
    resumos = 0
    contribuicoes = 1
    beneficios = 2
    addContrib = 3
    addBeneficio = 4


class TipoBotaoResumo(Enum):
    deletar = ':/opcoes/redDeletar.png'
    editar = ':/opcoes/blueEditar.png'
