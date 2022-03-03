from typing import Any


class InformacaoModel:
    tipoInfo: Any
    descricao: str

    def __init__(self, descricao: str = None, tipoInfo: Any = None):
        self.descricao = descricao
        self.tipoInfo = tipoInfo

    def __str__(self):
        return f"""
        InformacaoModel:
            - descricao: {self.descricao}
            - tipoInfo: {type(self.tipoInfo)}
            - repr(tipoInfo): {repr(self.tipoInfo)}
    """
