from util.enums.dashboardEnums import EtapaCadastraCliente

from Design.DesignSystem.colors import NewColorsSuccess


def etapaCadatro(etapa: EtapaCadastraCliente, sucesso: bool=True):
    if etapa == EtapaCadastraCliente.profissional:
        frame = "#frSegundaEtapa"
    elif etapa == EtapaCadastraCliente.bancarias:
        frame = "#frTerceiraEtapa"
    else:
        frame = "#frQuartaEtapa"

    if sucesso:
        backgroundColor = NewColorsSuccess.green100.value
    else:
        backgroundColor = NewColorsSuccess.green300.value

    return f"""
    {frame} {{
	    border-radius: 8px;
	    background-color: {backgroundColor};
    }}
    """
