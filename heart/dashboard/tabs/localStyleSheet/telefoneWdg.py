from util.enums.newPrevEnums import TipoIcone


def tipoTelefone(tipo: str) -> str:
    if tipo.upper() == 'W':
        icone: str = """background-image: url(:/tipo/whatsapp.png);"""
    elif tipo.upper() == 'C':
        icone: str = """background-image: url(:/tipo/celular.png);"""
    else:
        icone: str = """background-image: url(:/tipo/telefone.png);"""

    return """#frTipo {
    	""" + icone + """
    	background-position: center;
    	background-repeat: no-repeat;
    }"""

def telefonePrincipal(principal: bool) -> str:
    if principal:
        corTitulo: str = """background-color: #3A405A;"""
    else:
        corTitulo: str = """background-color: #048BA8;"""

    return """QGroupBox::title {
	subcontrol-position: top left;
	""" + corTitulo + """
	border-top-left-radius: 8px;
	border-top-right-radius: 8px;
	color: white;
	padding: 4px 4px 4px 4px;
	left: 1px;
	top: 2px;
}"""

def telefonePessoal(pessoal: bool) -> str:
    if pessoal == "P":
        icone: str = """background-image: url(:/pessoal/personal.png);"""
    else:
        icone: str = """background-image: url(:/pessoal/recado.png);"""

    return """#frPessoal{
	""" + icone + """
	background-position: center;
	background-repeat: no-repeat;
}"""