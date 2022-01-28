from Design.DesignSystem.colors import NewColorsPrimary


def firulaHover(valor: bool):
    if valor:
        backgroundColor = NewColorsPrimary.p400.value
    else:
        backgroundColor = NewColorsPrimary.p300.value

    return f"""
    #frFirula {{
        background-color: {backgroundColor};
    
        border-top-left-radius: 4px;
        border-top-right-radius: 0px;
        border-bottom-right-radius: 0px;
        border-bottom-left-radius: 4px;
    }}"""
