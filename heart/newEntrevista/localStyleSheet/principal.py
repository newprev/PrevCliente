from util.enums.entrevistaEnums import EtapaEntrevista
from Design.DesignSystem.colors import NewColorsSuccess

def styleEtapaEntrevista(etapa: EtapaEntrevista) -> str:
    if etapa == EtapaEntrevista.naturezaProcesso:
        framesOn = "#frPrimeiraEtapa"
        framesOff = "#frSegundaEtapa, #frTerceiraEtapa, #frQuartaEtapa, #frQuintaEtapa"
    elif etapa == EtapaEntrevista.tipoBeneficio:
        framesOn = "#frPrimeiraEtapa, #frSegundaEtapa"
        framesOff = "#frTerceiraEtapa, #frQuartaEtapa, #frQuintaEtapa"
    elif etapa == EtapaEntrevista.tipoProcesso:
        framesOn = "#frPrimeiraEtapa, #frSegundaEtapa, #frTerceiraEtapa"
        framesOff = "#frQuartaEtapa, #frQuintaEtapa"
    elif etapa == EtapaEntrevista.quizEntrevista:
        framesOn = "#frPrimeiraEtapa, #frSegundaEtapa, #frTerceiraEtapa, #frQuartaEtapa"
        framesOff = "#frQuintaEtapa"
    else:
        return ""

    return f"""
    {framesOn} {{
        border-radius: 8px;
	    background-color: {NewColorsSuccess.green100.value};
    }}
    
    {framesOff} {{
        border-radius: 8px;
	    background-color: {NewColorsSuccess.green300.value};
    }}
    """