from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFrame

from Design.pyUi.wdgMenuPrincipal import Ui_wdgMenuPrincipal
from heart.informacoesTelas.indicadoresTela import IndicadoresController
from heart.informacoesTelas.tetosPrevidenciariosTela import TetosPrevidenciarios
from heart.informacoesTelas.expSobrevidaTela import ExpSobrevidaTela
from heart.processos.processoController import ProcessosController

from Design.CustomWidgets.newToast import QToaster
from util.enums.dashboardEnums import TelaAtual


class NewMenuPrincipal(QFrame, Ui_wdgMenuPrincipal):
    toasty: QToaster

    def __init__(self, parent=None, **kwargs):
        super(NewMenuPrincipal, self).__init__(parent=parent, **kwargs)
        self.setupUi(self)
        self.parent = parent
        self.dashboard = parent
        self.toasty = None

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.adicionaBotoes()

    def adicionaBotoes(self):
        # Ferramentas
        #Calculadora
        self.pbCalculadora.clicked.connect(self.openFaltaImplementacao)

        # Consultas
        # Indicadores, Tetos, Expectativas de sobrevida
        self.pbIndicadores.clicked.connect(self.openIndicadores)
        self.pbTetos.clicked.connect(self.openTetos)
        self.pbExpSobrevida.clicked.connect(self.openExpSobrevida)
        self.pbResumoCnis.clicked.connect(self.openFaltaImplementacao)

        # Escritorio
        # Clientes, entrevista, processos
        self.pbProcessos.clicked.connect(self.openProcessos)
        self.pbCliente.clicked.connect(self.openCliente)
        self.pbEntrevista.clicked.connect(self.openEntrevista)

    def openIndicadores(self):
        indicadoresPage = IndicadoresController(parent=self)
        indicadoresPage.raise_()
        indicadoresPage.show()

    def openTetos(self):
        tetosPage = TetosPrevidenciarios(parent=self)
        tetosPage.raise_()
        tetosPage.show()

    def openExpSobrevida(self):
        expSobrevidaPage = ExpSobrevidaTela(parent=self)
        expSobrevidaPage.raise_()
        expSobrevidaPage.show()

    def openProcessos(self):
        processosPage = ProcessosController(cliente=None, processo=None, parent=self)
        processosPage.raise_()
        processosPage.show()
        self.close()

    def openEntrevista(self):
        self.dashboard.trocaTela(TelaAtual.Entrevista)
        self.close()

    def openCliente(self):
        self.dashboard.trocaTela(TelaAtual.Cliente)
        self.close()

    def openFaltaImplementacao(self):
        self.toasty = QToaster()
        self.toasty.showMessage(self.dashboard, "Funcionalidade ainda não implementada")

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        geo = self.geometry()
        parentRect = self.parent.rect()
        geo.moveTopLeft(parentRect.topRight() - self.rect().topRight() + QtCore.QPoint(-20, 20))

        self.setGeometry(geo)
        self.show()

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.close()
