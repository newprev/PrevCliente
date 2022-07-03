def layoutBotaoGuia(siglaBotao:str, selecionado: bool = False) -> str:
    hover: str = """
        #""" + siglaBotao + """:hover {
        font-family: "TeX Gyre Adventor";
        font-size: 12px;
        color: lightgrey;
    
        background-color: rgba(142, 157, 220, 200);
        border-radius: 4px 4px 4px 4px;
        border-width: 0px 0px 0px 2px;
        border-color: transparent transparent transparent white;
        border-style: solid solid solid solid;
        } 
    """
    if selecionado:
        style = """
        #""" + siglaBotao + """{
        font-family: "TeX Gyre Adventor";
        font-size: 12px;
        color: lightgrey;
    
        background-color: rgba(142, 157, 220, 200);
        border-radius: 4px 4px 4px 4px;
        border-width: 0px 0px 0px 2px;
        border-color: transparent transparent transparent white;
        border-style: solid solid solid solid;
        } 
        """
    else:
        style = """
        #""" + siglaBotao + """{
        background-color: rgba(0,0,0,0);
	    font-family: "TeX Gyre Adventor";
	    font-size: 12px;
	    border: 0px;
	    color: lightgrey;
	    }"""

    if selecionado:
        return style
    else:
        return style + hover


def habDesCheckBox(cbNome: str, desabilita: bool) -> str:
    if desabilita:
        return f"""
            #{cbNome}::indicator:disabled {{
	            image: url(:/checkbox/checkBoxDisable.png);
            }}
        """
    else:
        return f"""
            #{cbNome}::indicator:unchecked {{
	            image: url(:/checkbox/CheckBoxFalse.png);
            }}

            #{cbNome}::indicator:checked {{
                image: url(:/checkbox/checkBoxTrue.png);
            }}
        """