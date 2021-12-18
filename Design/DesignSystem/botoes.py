from enum import Enum
from Design.DesignSystem.colors import NewColorsPrimary, NewColorsWhite
from Design.DesignSystem.designEnums import BorderRadius
from Design.DesignSystem.fonts import Fonts, FontSize


class NewButton(Enum):
    padrao = f"""
        QPushButton{{
            {Fonts.bebasStd.value}
            {FontSize.H2.value}
            color: {NewColorsWhite.white400.value};
            
            {BorderRadius.r4.value}
            background-color: {NewColorsPrimary.p100.value};         
        }}"""


class NewButtonHover(Enum):
    padrao = f"""
        QPushButton:hover{{
            {Fonts.bebasStd.value}
            {FontSize.H2.value}
            color: {NewColorsWhite.white400.value};

            {BorderRadius.r4.value}
            background-color: {NewColorsPrimary.p200.value};         
        }}"""