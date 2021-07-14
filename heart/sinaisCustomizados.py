from PyQt5.QtCore import QObject
from PyQt5 import QtCore
from newPrevEnums import TelaPosicao
from modelos.advogadoModelo import AdvogadoModelo
from modelos.clienteModelo import ClienteModelo


class Sinais(QObject):
    sTrocaWidgetCentral = QtCore.pyqtSignal(TelaPosicao, name='pagina')
    sTrocaPrimeiroAcesso = QtCore.pyqtSignal(AdvogadoModelo, name='advogado')
    sTrocaTelaEntrevista = QtCore.pyqtSignal(list, name='tela')
    sTrocaInfoLateral = QtCore.pyqtSignal(dict, name='infoLateral')
    sEnviaCliente = QtCore.pyqtSignal(name='enviaCliente')
    sBuscaCliente = QtCore.pyqtSignal(name='buscaCliente')
    sEnviaIndicadores = QtCore.pyqtSignal(list, name='enviaIndicador')