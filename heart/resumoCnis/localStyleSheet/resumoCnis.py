from Design.DesignSystem.colors import NewColorsPrimary, NewColorsSuccess
from util.enums.resumoCnisEnums import TelaResumo, TipoBotaoResumo, TipoContribuicao


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


def backgroundAlerta(dadoFaltante: bool = False) -> str:
    # bgColor: str = "#F9F9F9"
    bgColor: str = "#CFF2DC"

    if dadoFaltante:
        bgColor = "#F9F9F9"

    return f"""
    #gbMain {{
        background-color: { bgColor };
        border-radius: 8px;
        border: 1px solid #3F4E8C;
    }}
    """


def bgFirulaResumo(tipo: TipoContribuicao, nomeFrame: str):
    if tipo == TipoContribuicao.contribuicao:
         bgColor = NewColorsPrimary.p400.value
    else:
        bgColor = NewColorsSuccess.green100.value

    return f"""
    #{nomeFrame} {{
        background-color: { bgColor };
        border-radius: 8px;
        border: 0px solid none;
    }}"""


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
        image: url(:/upDown/calendar.png);
    }
    
    QDateEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        padding: 0px 8px 0px 0px;
    
        border-left-width: 0px;
}"""