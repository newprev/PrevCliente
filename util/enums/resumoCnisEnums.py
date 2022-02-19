from enum import Enum


class TelaResumo(Enum):
    resumos = 0
    contribuicoes = 1
    beneficios = 2
    addVinculo = 3
    addContriBene = 4


class TipoVinculo(Enum):
    contribuicao = 0
    beneficio = 1


class TipoBotaoResumo(Enum):
    deletar = ':/opcoes/redDeletar.png'
    editar = ':/opcoes/blueEditar.png'
