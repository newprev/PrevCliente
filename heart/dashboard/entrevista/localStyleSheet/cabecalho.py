from util.enums.newPrevEnums import EtapaEntrevista


def infoLabelCabecalho(etapa: EtapaEntrevista, completo=False):
    if completo:
        corDaFonte = "color: rgb(32, 74, 135);"
    else:
        corDaFonte = "color: grey;"

    if etapa == EtapaEntrevista.infoPessoais:
        nomeWdg = "#lbInfoPessoais"
    elif etapa == EtapaEntrevista.infoProcessual:
        nomeWdg = "#lbInfoProcessuais"
    elif etapa == EtapaEntrevista.detalhamento:
        nomeWdg = "#lbInfoDetalhamento"
    else:
        nomeWdg = "#lbInfoFinalizacao"

    return """
    """ + nomeWdg + """ {
	font-family: "TeX Gyre Adventor";
	font-size: 12px;

	""" + corDaFonte + """
}"""


def infoIconeCabecalho(etapa: EtapaEntrevista, completo=False):
    if etapa == EtapaEntrevista.infoPessoais:
        nomeWdg = "#frEtapa1"
        numeroEtapa = 1
    elif etapa == EtapaEntrevista.infoProcessual:
        nomeWdg = "#frEtapa2"
        numeroEtapa = 2
    elif etapa == EtapaEntrevista.detalhamento:
        nomeWdg = "#frEtapa3"
        numeroEtapa = 3
    else:
        nomeWdg = "#frEtapa4"
        numeroEtapa = 4

    if completo:
        corIcone = f"background-image: url(:/Etapa{numeroEtapa}/n{numeroEtapa}-blue.png);"
    else:
        corIcone = f"background-image: url(:/Etapa{numeroEtapa}/n{numeroEtapa}-grey.png);"

    return """
    """ + nomeWdg + """ {
	""" + corIcone + """
	background-repeat: no-repeat;
	background-position: center;
}"""

def infoPontinhosCabecalho(etapa: EtapaEntrevista, completo=False):
    if etapa == EtapaEntrevista.infoPessoais:
        nomeWdg = "#frProg1"
    elif etapa == EtapaEntrevista.infoProcessual:
        nomeWdg = "#frProg2"
    else:
        nomeWdg = "#frProg3"

    if completo:
        corIcone = f"background-image: url(:/dots/d3-blue.png);"
    else:
        corIcone = f"background-image: url(:/dots/d3-grey.png);"

    return """
    """ + nomeWdg + """ {
	""" + corIcone + """
	background-repeat: no-repeat;
	background-position: top;
}"""
