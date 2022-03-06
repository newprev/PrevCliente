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


def iconeInfoCliente(mostra: bool):
    if mostra:
        backgroundImage = "url(:/voltar/backWhite.png)"
    else:
        backgroundImage = "url(:/proximo/next.png)"

    return f"""
        #pbInfoCliente {{
            font: 12pt "Avenir LT Std";
        
            background-color: rgba(63, 78, 140, 190);
            color: white;
            border: 0px solid none;
        
            background-image: {backgroundImage};
            background-position: center;
            background-repeat: no-repeat;
        }}
        """