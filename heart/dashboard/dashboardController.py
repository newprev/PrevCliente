from PyQt5.QtWidgets import QMainWindow, QHBoxLayout

from Telas.dashboard import Ui_mwDashBoard
from heart.dashboard.localWidgets.cardFuncionalidade import CardFuncionalidade
from heart.dashboard.tabsClientes.clienteController import TabCliente


class DashboardController(QMainWindow, Ui_mwDashBoard):

    def __init__(self, db=None):
        super(DashboardController, self).__init__()
        self.setupUi(self)
        self.boxLayout = QHBoxLayout()
        self.db = db
        self.funcCliente = CardFuncionalidade(tipo='cliente')
        self.funcEntrevista = CardFuncionalidade(tipo='Entrevista')
        self.tabCadastro = TabCliente(parent=self, db=db)
        self.stkMainDashBoard.addWidget(self.tabCadastro)
        # self.stkMainDashBoard.setCurrentIndex(0)
        self.funcOutra1 = CardFuncionalidade()
        self.funcOutra2 = CardFuncionalidade()
        self.funcOutra3 = CardFuncionalidade()
        self.funcOutra4 = CardFuncionalidade()
        self.funcOutra5 = CardFuncionalidade()

        self.boxLayout.addWidget(self.funcCliente)
        self.boxLayout.addWidget(self.funcEntrevista)
        self.boxLayout.addWidget(self.funcOutra1)
        self.boxLayout.addWidget(self.funcOutra2)
        self.boxLayout.addWidget(self.funcOutra3)
        self.boxLayout.addWidget(self.funcOutra4)
        self.boxLayout.addWidget(self.funcOutra5)

        self.scaTelas.setLayout(self.boxLayout)