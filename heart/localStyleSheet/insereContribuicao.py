def habilita(tipo: str, habilitar: bool):
    nomeFrame = ''
    background = ''

    if tipo == 'beneficio':
        nomeFrame = '#frInfoBeneficio'
    else:
        nomeFrame = '#frInfoRemCont'

    if habilitar:
        background = "background-color: white;"
    else:
        background = "background-color: rgb(232, 230, 215);"

    return nomeFrame + """{
	border-radius: 8px;
	border: 1px solid black;
	""" + background + """
	}"""

def habilitaBotao(nomeBotao: str, habilitar: bool):
    background = ''

    if habilitar:
        background = "background-color: white;"
    else:
        background = "background-color: rgb(232, 230, 215);"

    return f"""#{nomeBotao}""" + """{
	border-radius: 8px;
	border: 1px solid black;
	""" + background + """
	}"""