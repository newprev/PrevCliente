from util.enums.newPrevEnums import TipoFiltro


def tipoTagFiltro(tipo: TipoFiltro) -> str:
    if tipo == TipoFiltro.indicador:
        backgroundColor = """rgb(207, 242, 220)"""
        borderColor = """rgb(0, 158, 56)"""

    elif tipo == TipoFiltro.data:
        backgroundColor = """rgb(255, 220, 149)"""
        borderColor = """rgb(255, 186, 47)"""
    else:
        backgroundColor = """"""
        borderColor = """"""

    style = f"""
    #frMain {{
        background-color: {backgroundColor};
        border-color: {borderColor};
        border-radius: 4px;
        border-style: solid;
        border-width: 2px;
    }}
    """
    return style
