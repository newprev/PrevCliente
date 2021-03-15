import pymysql

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

from Daos.daoConfiguracoes import DaoConfiguracoes
from Daos.tabelas import TabelasConfig
from Telas.splashScreen import Ui_MainWindow
from heart.login.loginController import LoginController
from connections import ConfigConnection
from heart.cadastraClienteController import CadastraClientePage

from heart.dashboard.dashboardController import DashboardController


class Main(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.contador = 0
        self.dbConnection = ConfigConnection(instanciaBanco='Local')
        self.db = self.dbConnection.getDatabase()
        self.daoConfigs = DaoConfiguracoes(db=self.db)
        self.loginPage = LoginController(db=self.db)
        self.center()
        self.show()

        # self.cadastraClientePage = CadastraClientePage(db=self.db)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progresso)
        self.timer.start(35)

    def progresso(self, add=None):
        if add is None:
            self.contador += 1
        else:
            self.contador += add

        self.pbarSplash.setValue(self.contador)

        if self.contador == 20:
            self.timer.stop()
            self.iniciaBancos()
            # self.cadastraClientePage.show()
            # self.dashboard.show()
            # self.loginPage.show()
            # self.close()

        if self.contador == 100:
            self.lbInfo.setText('INICIANDO SUBMERSAO...')

    def iniciaBancos(self):

        tabelas = TabelasConfig()

        self.lbInfo.setText('CRIANDO TABELA DO CLIENTE...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCliente):
            self.progresso(add=20)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE REMUNERAÇÕES...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisRemuneracoes):
            self.progresso(add=20)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE CONTRIBUIÇÕES...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisContribuicoes):
            self.progresso(add=20)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE BENEFÍCIOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisBeneficios):
            self.progresso(add=20)
        else:
            return False
    #
    #     self.lbInfo.setText('CRIANDO BANCO DOS PARTICIPANTES...')
    #     if self.daoConfigs.criaTblParticipantes():
    #         self.progresso(add=10)
    #
    #     self.lbInfo.setText('CRIANDO BANCO DAS CATEGORIAS...')
    #     if self.daoConfigs.criaTblCategoria():
    #         self.progresso(add=10)
    #
    #     self.lbInfo.setText('CRIANDO BANCO DOS ESTADOS...')
    #     if self.daoConfigs.criaTblEstado():
    #         self.progresso(add=10)
    #
    #     self.lbInfo.setText('LEMBRANDO DOS ESTADOS DO BRASIL...')
    #     # Se alguma coisa de errada acontecer com a table a "estados"
    #     # ele deleta a tabela (DROP TABLE), recria e insere todos os estados de novo
    #     if not self.daoConfigs.verificaEstados():
    #         self.lbInfo.setText('EITA! DEU PROBLEMA NA TABELA. VOU ARRUMAR...')
    #         self.progresso(add=5)
    #         self.daoConfigs.criaTblEstado()
    #         self.lbInfo.setText('ESTOU ARRUMANDO RAPIDINHO...')
    #         if self.daoConfigs.addEstados():
    #             self.lbInfo.setText('PRONTO! TUDO CERO!')
    #             self.progresso(add=5)
    #     else:
    #         self.progresso(add=10)
    #
        self.iniciaNewPrev()

    def iniciaNewPrev(self):
        self.loginPage.show()
        self.close()
        # self.close()
        # LoginPage(self.db).show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
