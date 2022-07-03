from enum import Enum


class TipoConexao(Enum):
    producao = 0
    desenvolvimento = 1


class ImportantPaths(Enum):
    design = 0
    fonts = 1


class TipoConfiguracao(Enum):
    sistema = 0


class CategoriaConfig(Enum):
    geral = 0
    backup = 1

