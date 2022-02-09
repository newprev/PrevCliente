from Design.pyUi.newDashboard import Ui_newDashboard
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui

from modelos.clienteORM import Cliente
from util.popUps import popUpOkAlerta

from Design.pyUi.efeitos import Efeitos
from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio
from sinaisCustomizados import Sinais

from util.enums.dashboardEnums import TelaAtual

from modelos.escritoriosORM import Escritorios
from modelos.advogadoORM import Advogados

from heart.newDashboard.localWidgets.newMenuPrincipal import NewMenuPrincipal
from heart.newDashboard.localWidgets.newListaClientes import NewListaClientes
from heart.wdgCadastroCliente import NewCadastraCliente
from heart.newDashboard.localWidgets.newInfoCliente import NewInfoCliente
from heart.newEntrevista.principal import NewEntrevistaPrincipal


class NewDashboard(QMainWindow, Ui_newDashboard):
    clienteController: NewListaClientes
    escritorioAtual: Escritorios
    advogadoAtual: Advogados
    wdgCadastroCliente: NewCadastraCliente
    wdgInfoCliente: NewInfoCliente
    wdgEntrevista: NewEntrevistaPrincipal

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
            self.advogadoAtual = self.cacheLogin.carregarCacheTemporario()

            if self.advogadoAtual is None or self.advogadoAtual.escritorioId is None:
                popUpOkAlerta("Não foi possível carregar as informações do advogado. Tente fazer o login novamente.")
                self.cacheLogin.limpaCache()
                self.cacheLogin.limpaTemporarios()
                return False

        return True

    def iniciaDash(self):
        if self.buscaEscritorio():
            self.lbNomeEscritorio.setText(self.escritorioAtual.nomeEscritorio)
        if self.buscaAdvogado():
            self.lbNomeAdvogado.setText(self.advogadoAtual.nomeAdvogado + ' ' + self.advogadoAtual.sobrenomeAdvogado)
            self.lbOAB.setText('OAB: ' + self.advogadoAtual.numeroOAB + '/' + self.escritorioAtual.estado)

        self.clienteController = NewListaClientes(self.escritorioAtual, self.advogadoAtual, parent=self)
        self.wdgCadastroCliente = NewCadastraCliente(parent=self)
        self.wdgInfoCliente = NewInfoCliente(parent=self)
        self.wdgEntrevista = NewEntrevistaPrincipal(self.escritorioAtual, parent=self)

        self.stkPrincipal.addWidget(self.clienteController)
        self.stkPrincipal.addWidget(self.wdgCadastroCliente)
        self.stkPrincipal.addWidget(self.wdgInfoCliente)
        self.stkPrincipal.addWidget(self.wdgEntrevista)

        self.stkPrincipal.setCurrentIndex(TelaAtual.Cliente.value)

    def navegaInfoCliente(self, cliente: Cliente):
        self.wdgInfoCliente.carregaClienteNaTela(cliente)
        self.trocaTela(TelaAtual.InfoCliente)

    def recebeCliente(self, cliente: Cliente, **kwargs):
        if cliente is not None:
            self.wdgCadastroCliente.iniciaTela()
            if 'info' in kwargs.keys():
                self.wdgCadastroCliente.carregaClienteNaTela(cliente, tela=kwargs['info'])
            else:
                self.wdgCadastroCliente.carregaClienteNaTela(cliente)
            self.trocaTela(TelaAtual.CadastroCliente)

    def recarregaListaClientes(self):
        self.clienteController.atualizaTblClientes()

    def trocaTela(self, tela: TelaAtual, *args):
        if len(args) != 0:
            if isinstance(args[0], Cliente):
                self.wdgEntrevista.defineCliente(args[0])

        self.stkPrincipal.setCurrentIndex(tela.value)

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
