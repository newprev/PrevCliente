from enum import Enum
from Design.DesignSystem.fonts import Fonts, FontSize


class BorderRadius(Enum):
    r4 = "border-radius: 4px;"
    r8 = "border-radius: 8px;"
    r12 = "border-radius: 12px;"
    r16 = "border-radius: 16px;"
    r20 = "border-radius: 20px;"


class FontColor(Enum):
    from Design.DesignSystem.colors import NewColorsGrey, NewColorsWhite
    white = "color: " + NewColorsWhite.white400.value + ";"
    black = "color: " + NewColorsGrey.grey200.value + ";"


class FontStyle(Enum):
    titulo = "QLabel{ " + Fonts.bebasStd.value + FontSize.H1.value + "}"
    subTitulo = "QLabel{ " + Fonts.bebasStd.value + FontSize.H3.value + "}"
    tagWhite = "QLabel{ " + Fonts.avenirStd.value + FontSize.H3.value + FontColor.white.value + "}"
    tagBlack = "QLabel{ " + Fonts.avenirStd.value + FontSize.H3.value + FontColor.black.value + "}"
