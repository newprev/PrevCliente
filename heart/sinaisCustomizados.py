from PyQt5.QtCore import QObject
from PyQt5 import QtCore


class Sinais(QObject):
    sTrocaWidgetCentral = QtCore.pyqtSignal(int, name='pagina')