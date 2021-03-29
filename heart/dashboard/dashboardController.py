from PyQt5.QtWidgets import QMainWindow, QHBoxLayout

from Telas.dashboard import Ui_mwDashBoard
from heart.menuLateral.configuracoesPage import ConfiguracoesPage
from heart.dashboard.localWidgets.cardFuncionalidade import CardFuncionalidade
from heart.dashboard.tabs.clienteController import TabCliente
from heart.dashboard.tabs.tabCalculos import TabCalculos
from heart.menuLateral.ferramentasPage import FerramentasPage
from heart.sinaisCustomizados import Sinais

from newPrevEnums import TelaPosicao


class DashboardController(QMainWindow, Ui_mwDashBoard):

    def __init__(self, parent=None, db=None):
        super(DashboardController, self).__init__(parent=parent)
        self.setupUi(self)
        self.boxLayout = QHBoxLayout()
        self.db = db
        self.sinais = Sinais()
        self.parent = parent

        self.funcCliente = CardFuncionalidade(tipo='cliente', parent=self)
        self.funcEntrevista = CardFuncionalidade(tipo='Entrevista', parent=self)
        self.funcCalculos = CardFuncionalidade(tipo='Calculos', parent=self)
        self.pbConfig.clicked.connect(lambda: self.trocarParaPagina(TelaPosicao.Configuracoes))
        self.pbFerramentas.clicked.connect(lambda: self.trocarParaPagina(TelaPosicao.Ferramentas))

        self.tabCadastro = TabCliente(parent=self, db=db)
        self.tabCalculos = TabCalculos(parent=self, db=db)
        self.configuracoesPage = ConfiguracoesPage(parent=self, db=db)
        self.ferramentasPage = FerramentasPage(parent=self, db=db)

        self.stkMainDashBoard.addWidget(self.tabCadastro)
        self.stkMainDashBoard.addWidget(self.tabCalculos)
        self.stkMainDashBoard.addWidget(self.configuracoesPage)
        self.stkMainDashBoard.addWidget(self.ferramentasPage)

        self.stkMainDashBoard.setCurrentIndex(TelaPosicao.Cliente.value)
        # self.funcOutra1 = CardFuncionalidade()
        self.funcOutra2 = CardFuncionalidade()
        self.funcOutra3 = CardFuncionalidade()
        self.funcOutra4 = CardFuncionalidade()
        self.funcOutra5 = CardFuncionalidade()

        self.boxLayout.addWidget(self.funcCliente)
        self.boxLayout.addWidget(self.funcEntrevista)
        self.boxLayout.addWidget(self.funcCalculos)
        self.boxLayout.addWidget(self.funcOutra2)
        self.boxLayout.addWidget(self.funcOutra3)
        self.boxLayout.addWidget(self.funcOutra4)
        self.boxLayout.addWidget(self.funcOutra5)

        self.scaTelas.setLayout(self.boxLayout)

    def trocarParaPagina(self, *args):
        tela = int(args[0].value)
        self.stkMainDashBoard.setCurrentIndex(tela)
