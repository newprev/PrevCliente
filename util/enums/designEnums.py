from enum import Enum


class Fonts(Enum):
    bebasStd = "font-family: 'Bebas Neue';"
    avenirStd = "font-family: 'Avenir LT Std';"


class FontSize(Enum):
    H1 = "font-size: 24px;"
    H2 = "font-size: 18px;"
    H3 = "font-size: 12px;"


class FontColor(Enum):
    from Design.DesignSystem.colors import NewColorsGrey, NewColorsWhite
    white = "color: " + NewColorsWhite.white400.value + ";"
    black = "color: " + NewColorsGrey.grey200.value + ";"


class FontStyle(Enum):
    titulo = "QLabel{ " + Fonts.bebasStd.value + FontSize.H1.value + "}"
    subTitulo = "QLabel{ " + Fonts.bebasStd.value + FontSize.H3.value + "}"
    tagWhite = "QLabel{ " + Fonts.avenirStd.value + FontSize.H3.value + FontColor.white.value + "}"
    tagBlack = "QLabel{ " + Fonts.avenirStd.value + FontSize.H3.value + FontColor.black.value + "}"
