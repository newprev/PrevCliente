def estadoInfoFinalizado(etapa: str, completo=False):
    if completo:
        icone = "background-image: url(:/check/check.png);"
    else:
        icone = "background-image: url(:/dots/d3-white.png);"

    if etapa == 'pessoais':
        nomeWdg = "#frInfo1Icon"
    elif etapa == 'residenciais':
        nomeWdg = "#frInfo2Icon"
    elif etapa == 'profissionais':
        nomeWdg = "#frInfo3Icon"
    else:
        nomeWdg = "#frInfo4Icon"

    return """
    """ + nomeWdg + """  {
	""" + icone + """
	background-repeat: no-repeat;
	background-position: center;
}"""