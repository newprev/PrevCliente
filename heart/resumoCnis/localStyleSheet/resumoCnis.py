from util.enums.resumoCnisEnums import TelaResumo


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
