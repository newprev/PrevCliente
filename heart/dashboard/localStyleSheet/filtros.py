def ativaFiltro(boolean: bool, nomeFiltro):
    if boolean:
        icone = "background-image: url(:/arrowDown/arrowDown.png);"
    else:
        icone = "background-image: url(:/arrowUp/arrowUp.png);"


    return """#""" + nomeFiltro + """ {
	"""+ icone +""" 
	background-repeat: no-repeat;
	background-position: center;

	background-color: transparent;
}"""

def estiloBotoesFiltro():
    return """
        QPushButton {
            background-color: transparent;
            border: 0px;
            font-size: 12px;
            font-family: Ubuntu;
        }
        QPushButton::hover{
            border: 0px solid;
            border-radius: 10px;
            background-color: #838689;
            color: #fff;
            font-size: 16px;
            font-family: Ubuntu;  
        }"""

def estiloLabelFiltro():
    return """
        QLabel {
            background-color: transparent;
            border: 0px;
        }
        """