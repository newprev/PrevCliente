from enum import Enum


class NewColorsPrimary(Enum):
    primary = "#292D40"
    p100 = "#3A405A"
    p200 = "#3F4E8C"
    p300 = "#566BBF"
    p400 = "#3F64FF"


class NewColorsSuccess(Enum):
    green100 = "#009E38"
    green200 = "#23E386"
    green300 = "#CFF2DC"


class NewColorsError(Enum):
    red100 = "#E70000"
    red200 = "#FF345E"


class NewColorsWarning(Enum):
    yellow100 = "#F2ED6F"


class NewColorsGrey(Enum):
    grey100 = "#040D14"
    grey200 = "#1F1E29"
    grey300 = "#373641"
    grey400 = "#3D464D"
    grey500 = "#52555A"
    grey600 = "#606970"
    grey700 = "#6F757B"
    grey800 = "#AFAFAF"
    grey900 = "#DDDEDF"


class NewColorsWhite(Enum):
    white100 = "#F2F2F2"
    white200 = "#F4F5F8"
    white300 = "#F9F9F9"
    white400 = "#FFFFFF"


class NewTextColor(Enum):
    normalText = "#040D14"
    whiteText = "#FFFFFF"
