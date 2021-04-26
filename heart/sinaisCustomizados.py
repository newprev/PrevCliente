from PyQt5.QtCore import QObject
from PyQt5 import QtCore
from newPrevEnums import TelaPosicao


class Sinais(QObject):
    sTrocaWidgetCentral = QtCore.pyqtSignal(TelaPosicao, name='pagina')