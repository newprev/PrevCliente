from enum import Enum


class TipoTelefone(Enum):
    Celular = 'C'
    Fixo = 'F'
    Whatsapp = 'W'


class TelefonePesoal(Enum):
    Pessoal = 'P'
    Recado = 'R'