from util.enums.newPrevEnums import TipoFiltro
from Design.DesignSystem.colors import NewColorsPrimary, NewColorsSuccess, NewColorsGrey, NewColorsWhite
from util.enums.designEnums import FontSize


def tipoTagFiltro(tipo: TipoFiltro) -> str:
    if tipo == TipoFiltro.indicador:
        backgroundColor = NewColorsPrimary.p200.value
        borderColor = NewColorsPrimary.p300.value

    elif tipo == TipoFiltro.data:
        backgroundColor = NewColorsSuccess.green200.value
        borderColor = NewColorsSuccess.green100.value
    else:
        backgroundColor = """"""
        borderColor = """"""

    frameStyle = f"""
    #frMain {{
        background-color: {backgroundColor};
        border-color: {borderColor};
        border-radius: 4px;
        border-style: solid;
        border-width: 2px;
    }}
    """
    return frameStyle


def textTagFiltro(tipo: TipoFiltro) -> str:
    if tipo == TipoFiltro.indicador:
        textColor = NewColorsWhite.white400.value

    elif tipo == TipoFiltro.data:
        textColor = NewColorsGrey.grey200.value
    else:
        textColor = """"""

    textStyle = f"""
    QLabel {{
        {FontSize.H3.value}
        color: {textColor};
    }}
    """
    return textStyle