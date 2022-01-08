from enum import Enum

from PyQt5.QtGui import QColor


class NewColorsPrimary(Enum):
    primary = "#292D40"
    primaryQt = QColor(41, 45, 64)

    p100 = "#3A405A"
    p100Qt = QColor(58, 64, 90)

    p200 = "#3F4E8C"
    p200Qt = QColor(63, 78, 140)

    p300 = "#566BBF"
    p300Qt = QColor(86, 107, 191)

    p400 = "#3F64FF"
    p400Qt = QColor(63, 100, 255)


class NewColorsSuccess(Enum):
    green100 = "#009E38"
    green100Qt = QColor(0, 158, 56)

    green200 = "#23E386"
    green200Qt = QColor(35, 227, 134)

    green300 = "#CFF2DC"
    green300Qt = QColor(207, 242, 220)


class NewColorsError(Enum):
    red100 = "#E70000"
    red100Qt = QColor(231, 0, 0)

    red200 = "#FF345E"
    red200Qt = QColor(255, 52, 94)


class NewColorsWarning(Enum):
    yellow100 = "#F2ED6F"
    yellow100Qt = QColor(242, 237, 111)


class NewColorsGrey(Enum):
    grey100 = "#040D14"
    grey100Qt = QColor(4, 13, 20)

    grey200 = "#1F1E29"
    grey200Qt = QColor(31, 30, 41)

    grey300 = "#373641"
    grey300Qt = QColor(55, 54, 65)

    grey400 = "#3D464D"
    grey400Qt = QColor(61, 70, 77)

    grey500 = "#52555A"
    grey500Qt = QColor(82, 85, 90)

    grey600 = "#606970"
    grey600Qt = QColor(96, 105, 112)

    grey700 = "#6F757B"
    grey700Qt = QColor(111, 117, 123)

    grey800 = "#AFAFAF"
    grey800Qt = QColor(175, 175, 175)

    grey900 = "#DDDEDF"
    grey900Qt = QColor(221, 222, 223)


class NewColorsWhite(Enum):
    white100 = "#F2F2F2"
    white100Qt = QColor(242, 242, 242)

    white200 = "#F4F5F8"
    white200Qt = QColor(244, 245, 248)

    white300 = "#F9F9F9"
    white300Qt = QColor(249, 249, 249)

    white400 = "#FFFFFF"
    white400Qt = QColor(255, 255, 255)


class NewTextColor(Enum):
    normalText = "#040D14"
    white400Qt = QColor(4, 13, 20)

    whiteText = "#FFFFFF"
    whiteTextQt = QColor(255, 255, 255)
