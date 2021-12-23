from PyQt5.QtCore import QObject
from PyQt5 import QtCore

from modelos.advogadoORM import Advogados
from util.enums.dashboardEnums import TelaPosicao


class Sinais(QObject):
    sTrocaWidgetCentral = QtCore.pyqtSignal(TelaPosicao, name='pagina')
    sEnviaPath = QtCore.pyqtSignal(str, name='path')
    # sTrocaPrimeiroAcesso = QtCore.pyqtSignal(AdvogadoModelo, name='advogado')
    sTrocaPrimeiroAcesso = QtCore.pyqtSignal(Advogados, name='advogado')
    sTrocaTelaEntrevista = QtCore.pyqtSignal(list, name='tela')
    sTrocaInfoLateral = QtCore.pyqtSignal(dict, name='infoLateral')
    sEnviaCliente = QtCore.pyqtSignal(name='enviaCliente')
    sBuscaCliente = QtCore.pyqtSignal(name='buscaCliente')
    sEnviaIndicadores = QtCore.pyqtSignal(list, name='enviaIndicador')
    sAtualizaListaClientes = QtCore.pyqtSignal(name='atualizaListaClientes')
    sAtualizaCabecalho = QtCore.pyqtSignal(name='AtualizaCabecalho')
    sAtualizaParams = QtCore.pyqtSignal(name='AtualizaParams')
    sEnviaProcesso = QtCore.pyqtSignal(name='enviaProcesso')
    sExcluiFiltro = QtCore.pyqtSignal(name='excluiFiltro')
