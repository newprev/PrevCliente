from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout

from Design.pyUi.dashboard import Ui_mwDashBoard
from heart.menuLateral.configuracoesPage import ConfiguracoesPage
from heart.dashboard.localWidgets.cardFuncionalidade import CardFuncionalidade
from heart.dashboard.tabs.clienteController import TabCliente
from heart.dashboard.tabs.tabResumoCNIS import TabResumoCNIS
from heart.informacoesTelas.informacoesGerais import InformacoesGerais
from heart.menuLateral.ferramentasPage import FerramentasPage
from heart.dashboard.entrevista.entrevistaController import EntrevistaController
from heart.dashboard.processos.processoController import ProcessosController
from heart.sinaisCustomizados import Sinais
from cache.cachingLogin import CacheLogin

from util.enums.telaEnums import TelaPosicao


class DashboardController(QMainWindow, Ui_mwDashBoard):

    def __init__(self, parent=None, db=None):
        super(DashboardController, self).__init__(parent=parent)
        self.setupUi(self)
        self.boxLayout = QHBoxLayout()
        self.db = db
        self.sinais = Sinais()
        self.parent = parent
        self.cacheLogin = CacheLogin()

        self.setWindowTitle('Dashboard - [dashboardController]')

        self.funcCliente = CardFuncionalidade(tipo=TelaPosicao.Cliente, parent=self)
        self.funcEntrevista = CardFuncionalidade(tipo=TelaPosicao.Entrevista, parent=self)
        self.funcResumo = CardFuncionalidade(tipo=TelaPosicao.Resumo, parent=self)
        self.funcProcesso = CardFuncionalidade(tipo=TelaPosicao.Processo, parent=self)

        self.pbConfig.setToolTip('Configurações')
        self.pbFerramentas.setToolTip('Ferramentas')
        self.pbInfoGerais.setToolTip('Informações')
        self.pbHome.setToolTip('Dashboard')

        self.pbConfig.clicked.connect(lambda: self.trocarParaPagina(TelaPosicao.Configuracoes))
        self.pbFerramentas.clicked.connect(lambda: self.trocarParaPagina(TelaPosicao.Ferramentas))
        self.pbHome.clicked.connect(lambda: self.trocarParaPagina(TelaPosicao.Cliente))
        self.pbInfoGerais.clicked.connect(lambda: self.trocarParaPagina(TelaPosicao.InformacoesGerais))

        self.tabCliente = TabCliente(parent=self)
        self.tabResumo = TabResumoCNIS(parent=self, db=db)
        self.configuracoesPage = ConfiguracoesPage(parent=self)
        self.ferramentasPage = FerramentasPage(parent=self, db=db)
        self.informacoePage = InformacoesGerais(parent=self)

        self.stkMainDashBoard.addWidget(self.tabCliente)
        self.stkMainDashBoard.addWidget(self.tabResumo)
        self.stkMainDashBoard.addWidget(self.configuracoesPage)
        self.stkMainDashBoard.addWidget(self.ferramentasPage)
        self.stkMainDashBoard.addWidget(self.informacoePage)

        self.stkMainDashBoard.setCurrentIndex(TelaPosicao.Cliente.value)
        # self.funcOutra1 = CardFuncionalidade()
        self.funcOutra2 = CardFuncionalidade()
        self.funcOutra3 = CardFuncionalidade()
        self.funcOutra4 = CardFuncionalidade()
        self.funcOutra5 = CardFuncionalidade()

        self.boxLayout.addWidget(self.funcCliente)
        self.boxLayout.addWidget(self.funcEntrevista)
        self.boxLayout.addWidget(self.funcResumo)
        self.boxLayout.addWidget(self.funcProcesso)
        self.boxLayout.addWidget(self.funcOutra3)
        self.boxLayout.addWidget(self.funcOutra4)
        self.boxLayout.addWidget(self.funcOutra5)

        self.scaTelas.setLayout(self.boxLayout)

    def trocarParaPagina(self, telaAlvo: TelaPosicao):
        if telaAlvo == TelaPosicao.Entrevista:
            EntrevistaController(parent=self).showMaximized()
        elif telaAlvo == TelaPosicao.Processo:
            ProcessosController(parent=self).showMaximized()
        elif telaAlvo == TelaPosicao.Resumo:
            self.tabResumo.limpaTudo()
            self.stkMainDashBoard.setCurrentIndex(telaAlvo.value)
        elif telaAlvo == TelaPosicao.InformacoesGerais:
            self.stkMainDashBoard.setCurrentIndex(telaAlvo.value - 1)
        else:
            self.tabCliente.tabMain.setCurrentIndex(0)
            self.stkMainDashBoard.setCurrentIndex(telaAlvo.value)

    def atualizaTabClientes(self):
        self.tabCliente.atualizaTblClientes()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.cacheLogin.limpaTemporarios()
