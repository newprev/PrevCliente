def desabilitaPB(nomeBotao: str, desabilita=True):
    if desabilita:
        background = "background-color: rgb(186, 189, 182);"
        color = "color: black;"
    else:
        if nomeBotao == 'pbCancelar':
            background = "background - color: rgb(225, 224, 53);"
            color = "color: white;"
        else:
            background = "background-color: rgb(52, 73, 94);"
            color = "color: white;"

    return """#""" + nomeBotao + """ {
	font-family: 'TeX Gyre Adventor';
	font-size: 14px;
	""" + color + """

	border-radius: 4px;
	""" + background + """
}"""
