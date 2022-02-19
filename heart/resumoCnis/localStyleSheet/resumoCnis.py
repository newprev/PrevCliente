from util.enums.resumoCnisEnums import TelaResumo, TipoBotaoResumo


def selecionaBotao(tela: TelaResumo, seleciona: bool) -> str:
    if tela == TelaResumo.resumos:
        nomeBotao = '#pbEmpresas'
        nomeFirula = '#frFirulaEmpresa'
    elif tela == TelaResumo.contribuicoes:
        nomeBotao = '#pbContrib'
        nomeFirula = '#frFirulaContrib'
    elif tela == TelaResumo.beneficios:
        nomeBotao = '#pbBeneficios'
        nomeFirula = '#frFirulaBeneficios'

    if seleciona:
        style = f"""
        {nomeBotao} {{
            font: 12pt "Avenir LT Std";
            color: #3F4E8C;
            font-weight: 750;
        
            background-color: transparent;
            border: 0px solid none;
        
            margin: 4px;
        }}
        
        {nomeFirula} {{
            background-color: #3F4E8C;
            border: 0px solid none;
            border-radius: 2px;
        }}
        """
    else:
        style = f"""
        {nomeBotao} {{
            font: 12pt "Avenir LT Std";
            color: #3F4E8C;
            font-weight: 750;
        
            background-color: transparent;
            border: 0px solid none;
        
            margin: 4px;
    }}

    {nomeFirula} {{
        background-color: white;
        border: 0px solid none;
        border-radius: 2px;
    }}"""

    return style


def botaoOpcoes(botao: TipoBotaoResumo) -> str:
    return f"""
    QPushButton {{
        background-image: url({botao.value});
        background-position: center;
        background-repeat: no-repeat;
    
        background-color: transparent;
        border-radius: 0px;
    }}
    """


def cadLineEdit() -> str:
    return """
        QLineEdit {
            font: 12pt "Avenir LT Std";
            border: 0px solid gray;
            border-radius: 8px;
            padding: 0 8px;
            background: #F9F9F9;
            selection-background-color: darkgray;
        }"""


def cadDataEdit() -> str:
    return """
     QDateEdit {
        border: 0px solid gray;
        border-radius: 8px;
        padding: 1px 18px 1px 8px;
        
        font: 12pt "Avenir LT Std";
        color: #606970;
    
        background-color: #F9F9F9;
    }
    
    QDateEdit::down-button {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        padding: 0px 8px 0px 0px;
    
        border-left-width: 0px;
    }
    
    QDateEdit::down-arrow {
        image: url(:/upDown/down.png);
    }
    
    QDateEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        padding: 0px 8px 0px 0px;
    
        border-left-width: 0px;
}"""