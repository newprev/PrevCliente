def desabilita(nomeBotao: str, desabilita: bool) -> str:
    background = ''
    backgroundHover = ''

    if not desabilita:
        if nomeBotao == 'pbCancelar':
            background = "background-color: rgb(196, 160, 0);"
            backgroundHover = "background-color: rgb(216, 190, 30);"

        elif nomeBotao == 'pbConfirmar':
            background = "background-color: rgb(78, 154, 6);"
            backgroundHover = "background-color: rgb(108, 184, 36);"

        else:
            background = "background-color: rgb(52, 73, 94);"
            backgroundHover = "background-color: rgb(72, 93, 114);"

    else:
        background = "background-color: grey;"
        backgroundHover = "background-color: grey;"

    return f"""#{nomeBotao}""" + """{
        font-family: "TeX Gyre Adventor";
        font-size: 14px;
        color: white;
    
        border-radius: 4px;
        """ + background + """
    }
        """ + f"""#{nomeBotao}:hover""" + """{
        font-family: "TeX Gyre Adventor";
        font-size: 14px;
        color: white;
    
        border-radius: 4px;
        border: 1px solid;
        """ + backgroundHover + """
    }"""