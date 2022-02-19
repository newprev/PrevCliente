from PyQt5.QtCore import QObject
from PyQt5 import QtCore

from modelos.advogadoORM import Advogados
from modelos.clienteORM import Cliente
from util.enums.dashboardEnums import TelaPosicao


class Sinais(QObject):
    sTrocaWidgetCentral = QtCore.pyqtSignal(TelaPosicao, name='pagina')
    sEnviaPath = QtCore.pyqtSignal(str, name='path')
    sEnviaInfo = QtCore.pyqtSignal(str, name='info')
    sAbreToast = QtCore.pyqtSignal(name='toast')
    sVoltaTela = QtCore.pyqtSignal(name='voltaTela')
    sEnviaFiltro = QtCore.pyqtSignal(name='enviaFiltro')
    sDeletaVinculo = QtCore.pyqtSignal(name='deletaVinculo')
    sEditaVinculo = QtCore.pyqtSignal(name='editaVinculo')
    sAtualizaVinculo = QtCore.pyqtSignal(name='AtualizaCabecalho')
    sAbreResumoCnis = QtCore.pyqtSignal(name='resumoCnis')
    sTrocaPrimeiroAcesso = QtCore.pyqtSignal(Advogados, name='advogado')
    sTrocaTelaEntrevista = QtCore.pyqtSignal(list, name='tela')
    sTrocaInfoLateral = QtCore.pyqtSignal(dict, name='infoLateral')
    sIniciaEntrevista = QtCore.pyqtSignal(name='iniciaEntrevista')
    sEnviaCliente = QtCore.pyqtSignal(name='enviaCliente')
    sEnviaInfoCliente = QtCore.pyqtSignal(Cliente, name='enviaInfoCliente')
    sEnviaClienteParam = QtCore.pyqtSignal(Cliente, name='enviaClienteParam')
    sBuscaCliente = QtCore.pyqtSignal(name='buscaCliente')
    sEnviaIndicadores = QtCore.pyqtSignal(list, name='enviaIndicador')
    sAtualizaListaClientes = QtCore.pyqtSignal(name='atualizaListaClientes')
    sAtualizaParams = QtCore.pyqtSignal(name='AtualizaParams')
    sEnviaProcesso = QtCore.pyqtSignal(name='enviaProcesso')
    sExcluiFiltro = QtCore.pyqtSignal(name='excluiFiltro')
