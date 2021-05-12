from PyQt5.QtCore import QObject
from PyQt5 import QtCore
from newPrevEnums import TelaPosicao
from modelos.advogadoModelo import AdvogadoModelo


class Sinais(QObject):
    sTrocaWidgetCentral = QtCore.pyqtSignal(TelaPosicao, name='pagina')
    sTrocaPrimeiroAcesso = QtCore.pyqtSignal(AdvogadoModelo, name='advogado')