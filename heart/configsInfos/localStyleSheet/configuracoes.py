from util.enums.configEnums import CategoriaConfig


def configSelecionada(categoria: CategoriaConfig, habilita: bool = True):
    if categoria == CategoriaConfig.geral:
        pbSelecionado = "#pbGeral"
        frFirula = "#frFirulaGeral"

    elif categoria == CategoriaConfig.backup:
        pbSelecionado = "#pbBackup"
        frFirula = "#frFirulaBackup"

    else:
        return ""

    if habilita:
        backgroundColor = "#3F4E8C"
        fontWeight = 750
    else:
        backgroundColor = "transparent"
        fontWeight = "normal"

    return f"""
    {frFirula} {{
        background-color: {backgroundColor};
        border-radius: 2px;
    }}

    {pbSelecionado} {{
        font-weight: {fontWeight};
    }}
"""