from util.enums.logEnums import StatusInfo
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


def frInfo(tipo: TipoIcone) -> str:
    if tipo == TipoIcone.beneficio:
        background: str = """background-color: rgb(0, 170, 127);"""
    else:
        background: str = """background-color: rgb(255, 167, 81);"""

    return """#frIndicador{
	""" + background + """
	border-top-left-radius: 5px;
	border-top-right-radius: 5px;
	border-bottom-right-radius: 5px;
	border-bottom-left-radius: 5px;
}"""


def frInfoStatus(nomeFrame: str, tipoInfo: StatusInfo) -> str:
    if tipoInfo == StatusInfo.warning:
        backgroundIcon: str = """url(:/alerta/atencao.png)"""
    elif tipoInfo == StatusInfo.info:
        backgroundIcon: str = """url(:/alerta/info.png)"""
    else:
        backgroundIcon: str = """"""

    style: str = f"""
    #{nomeFrame} {{
	background-image: {backgroundIcon};
	background-repeat: no-repeat;
	background-position: center;
    }}"""

    return style