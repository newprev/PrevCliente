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
    bgHover = ''

    if habilitar:
        bgNormal = "background-color: rgb(52, 73, 94);"
        bgHover = "background-color: rgb(72, 93, 114);"
    else:
        bgNormal = "background-color: grey;"

    btnNormal = f"""#{nomeBotao}""" + """{
	font-family: "TeX Gyre Adventor";
	font-size: 14px;
	color: white;

	border-radius: 4px;
	""" + bgNormal + """
	}"""

    btnHover = f"""#{nomeBotao}:hover""" + """{
	font-family: "TeX Gyre Adventor";
	font-size: 14px;
	color: white;

	border-radius: 4px;
	""" + bgHover + """
	}"""

    return bgNormal + '\n' + bgHover