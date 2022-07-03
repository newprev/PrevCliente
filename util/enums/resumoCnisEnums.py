from enum import Enum


class TelaResumo(Enum):
    resumos = 0
    contribuicoes = 1
    beneficios = 2
    addVinculo = 3
    addContriBene = 4


class TipoContribuicao(Enum):
    contribuicao = 0
    beneficio = 1


class TipoVinculo(Enum):
    empregado = 'EMPREGADO'
    contribIndividual = 'CONTRIBUINTE INDIVIDUAL'
    seguradoEspecial = 'SEGURADO ESPECIAL'
    facultativo = 'FACULTATIVO'
    autonomo = 'AUTÔNOMO'


class TipoBotaoResumo(Enum):
    deletar = ':/opcoes/redDeletar.png'
    editar = ':/opcoes/blueEditar.png'
    duplicar = ':/opcoes/duplicate.png'
