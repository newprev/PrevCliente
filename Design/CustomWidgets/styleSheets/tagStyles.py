from util.enums.newPrevEnums import TipoFiltro
from Design.DesignSystem.colors import NewColorsPrimary, NewColorsSuccess, NewColorsGrey, NewColorsWhite
from Design.DesignSystem.designEnums import FontStyle


def tipoTagFiltro(tipo: TipoFiltro) -> str:
    if tipo == TipoFiltro.indicador:
        backgroundColor = NewColorsPrimary.p200.value
        borderColor = NewColorsPrimary.p300.value
        pbTextColor = NewColorsWhite.white400.value

    elif tipo == TipoFiltro.data:
        backgroundColor = NewColorsSuccess.green200.value
        borderColor = NewColorsSuccess.green100.value
        pbTextColor = NewColorsGrey.grey200.value
    else:
        backgroundColor = """"""
        borderColor = """"""
        pbTextColor = """"""

    frameStyle = f"""
    #frMain {{
        background-color: {backgroundColor};
        border-color: {borderColor};
        border-radius: 4px;
        border-style: solid;
        border-width: 2px;
    }}
    
    #frLinha {{
        background-color: {borderColor};
    }}
    
    #pbExcluir {{
	    border: 0px solid grey;
	    background-color: {backgroundColor};
	    color: {pbTextColor};
    }}
    """
    return frameStyle


def textTagFiltro(tipo: TipoFiltro) -> str:
    if tipo == TipoFiltro.indicador:
        return FontStyle.tagWhite.value

    elif tipo == TipoFiltro.data:
        return FontStyle.tagBlack.value
    else:
        return FontStyle.tagWhite.value
