from PyQt5.QtGui import QFont

from Design.pyUi.newDashboard import Ui_newDashboard
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtGui

from modelos.clienteORM import Cliente
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from util.helpers import mascaraTelCel, strTipoBeneficio
from util.popUps import popUpOkAlerta

from Design.pyUi.efeitos import Efeitos
from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio
from sinaisCustomizados import Sinais

from util.enums.dashboardEnums import TelaPosicao

from modelos.escritoriosORM import Escritorios
from modelos.advogadoORM import Advogados

from heart.newDashboard.localWidgets.newMenuPrincipal import NewMenuPrincipal
from heart.newDashboard.localWidgets.newListaClientes import NewListaClientes


class NewDashboard(QMainWindow, Ui_newDashboard):
    clienteController: NewListaClientes
    escritorioAtual: Escritorios
    advogadoAtual: Advogados

    def __init__(self, parent=None):
        super(NewDashboard, self).__init__(parent=parent)
        self.setupUi(self)
        self.sinais = Sinais()
        self.parent = parent
        self.cacheLogin = CacheLogin()
        self.cacheEscritorio = CacheEscritorio()

        self.setWindowTitle('Dashboard - [dashboardController]')

        self.pbMenuPrincipal.clicked.connect(self.abreMenuPrincipal)

    def abreMenuPrincipal(self):
        efeitos = Efeitos()
        menuPrincipal = NewMenuPrincipal(parent=self)
        efeitos.shadowCards([menuPrincipal])
        menuPrincipal.show()

    def buscaEscritorio(self):
        self.escritorioAtual = self.cacheEscritorio.carregarCache()
        if self.escritorioAtual is None or self.escritorioAtual.escritorioId is None:
            self.escritorioAtual = self.cacheEscritorio.carregarCacheTemporario()

            if self.escritorioAtual is None or self.escritorioAtual.escritorioId is None:
                popUpOkAlerta("Não foi possível carregar as informações do escritório. Tente fazer o login novamente.")
                self.cacheEscritorio.limpaCache()
                self.cacheEscritorio.limpaTemporarios()

        return True

    def buscaAdvogado(self):
        self.advogadoAtual = self.cacheLogin.carregarCache()
        if self.advogadoAtual is None or self.advogadoAtual.advogadoId is None:
            self.escritorioAtual = self.cacheLogin.carregarCacheTemporario()

            if self.advogadoAtual is None or self.advogadoAtual.escritorioId is None:
                popUpOkAlerta("Não foi possível carregar as informações do advogado. Tente fazer o login novamente.")
                self.cacheLogin.limpaCache()
                self.cacheLogin.limpaTemporarios()
                return False

        return True

    def iniciaDash(self):
        self.clienteController = NewListaClientes()

        self.stkPrincipal.addWidget(self.clienteController)
        self.stkPrincipal.setCurrentIndex(0)

        if self.buscaEscritorio():
            self.lbNomeEscritorio.setText(self.escritorioAtual.nomeEscritorio)
        if self.buscaAdvogado():
            self.lbNomeAdvogado.setText(self.advogadoAtual.nomeUsuario + ' ' + self.advogadoAtual.sobrenomeUsuario)
            self.lbOAB.setText('OAB: ' + self.advogadoAtual.numeroOAB + '/' + self.escritorioAtual.estado)

    def trocaTela(self, tela: TelaPosicao):
        pass

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.cacheLogin.limpaTemporarios()
        self.cacheEscritorio.limpaTemporarios()


if __name__ == '__main__':
    from PyQt5 import QtWidgets, QtGui
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = NewDashboard()
    w.show()
    sys.exit(app.exec_())
