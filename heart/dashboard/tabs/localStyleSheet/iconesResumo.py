from util.enums.newPrevEnums import TipoIcone


def iconeItem(icone: TipoIcone) -> str:
    if icone == TipoIcone.remuneracao:
        background: str = """background: url(:/remuneracao/remuneracao.png);"""
    else:
        background: str = """background: url(:/beneficio/beneficio.png);"""

    return """#frIcone {
	""" + background + """
	background-repeat: no-repeat;
	background-position: center;
}"""