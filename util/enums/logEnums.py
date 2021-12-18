from enum import Enum


class TipoLog(Enum):
    Rest = 0,
    DataBase = 1,
    Cache = 2


class StatusInfo(Enum):
    warning = 0
    info = 1

