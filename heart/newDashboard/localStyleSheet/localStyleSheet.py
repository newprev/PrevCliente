from Design.DesignSystem.colors import NewColorsPrimary
from Design.DesignSystem.fonts import Fonts
from Design.DesignSystem.designEnums import FontColor

def btnOpcoesStyle():
    return """
        QPushButton {
            background-image: url(:/opcoes/opcoes.png);
            background-position: center;
            background-repeat: no-repeat;
        
            background-color: transparent;
            border-radius: 0px;
        }"""


def styleTooltip():
    return f"""
        QToolTip {{
            {Fonts.avenirStd.value}
            {FontColor.white.value}
        
            background-color: {NewColorsPrimary.p400.value};
            padding: 5px;
            border: 0px solid black;
            border-radius: 8px;
        }}        
"""
