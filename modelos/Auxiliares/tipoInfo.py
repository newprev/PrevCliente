from typing import Any


class InformacaoModel:
    tipoInfo: Any
    descricao: str
    nivel:int

    def __init__(self, descricao: str = None, tipoInfo: Any = None, nivel: int = 0):
        self.descricao = descricao
        self.tipoInfo = tipoInfo
        self.nivel = nivel

    def __str__(self):
        return f"""
        InformacaoModel:
            - descricao: {self.descricao}
            - nivel: {self.nivel}
            - tipoInfo: {type(self.tipoInfo)}
            - repr(tipoInfo): {repr(self.tipoInfo)}
    """
