import pymysql

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from Daos.daoConfiguracoes import DaoConfiguracoes
from Daos.tabelas import TabelasConfig
from Telas.splashScreen import Ui_MainWindow
from heart.login.loginController import LoginController
from connections import ConfigConnection
from newPrevEnums import TiposConexoes


class Main(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.contador = 0
        self.tipoConexao = TiposConexoes.sqlite
        self.dbConnection = ConfigConnection(instanciaBanco=self.tipoConexao)
        self.db = self.dbConnection.getDatabase()
        self.daoConfigs = DaoConfiguracoes(db=self.db)
        self.loginPage = None
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

        if self.contador == 10:
            self.timer.stop()
            self.iniciaBancosETelas()
            # self.cadastraClientePage.show()
            # self.dashboard.show()
            # self.loginPage.show()
            # self.close()

        if self.contador == 100:
            self.lbInfo.setText('INICIANDO SUBMERSAO...')

    def iniciaBancosETelas(self):

        tabelas = TabelasConfig(tipoBanco=self.tipoConexao)

        self.lbInfo.setText('CRIANDO TABELA DOS ADVOGADOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateAdvogados, nomeTabela='advogados'):
            self.progresso(add=8)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DOS ESCRITORIOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateEscritorios, nomeTabela='escritorios'):
            self.progresso(add=8)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DOS PROCESSOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateProcessos, nomeTabela='processos'):
            self.progresso(add=8)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DO CLIENTE...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCliente, nomeTabela='cliente'):
            self.progresso(add=8)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE REMUNERAÇÕES...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisRemuneracoes, nomeTabela='cnisRemuneracoes'):
            self.progresso(add=8)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE CONTRIBUIÇÕES...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisContribuicoes, nomeTabela='cnisContribuicoes'):
            self.progresso(add=7)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE BENEFÍCIOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisBeneficios, nomeTabela='cnisBeneficios'):
            self.progresso(add=7)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE CABEÇALHOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisCabecalhos, nomeTabela='cnisCabecalhos'):
            self.progresso(add=7)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE ESPÉCIES DE BENEFÍCIOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateEspecieBenef, nomeTabela='especieBenef'):
            self.progresso(add=2)
            self.daoConfigs.verificaTblEspecieBenef()
            self.progresso(add=7)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE INDICADORES...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateIndicadores, nomeTabela='indicadores'):
            self.progresso(add=2)
            self.daoConfigs.verificaTblIndicadores()
            self.progresso(add=7)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE TETOS PREVIDENCIÁRIOS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateTetosPrev, nomeTabela='tetosPrev'):
            self.progresso(add=7)
        else:
            return False

        self.lbInfo.setText('CRIANDO TABELA DE CONVERSÕES MONETÁRIAS...')
        if self.daoConfigs.criaTabela(tabelas.sqlCreateConvMon, nomeTabela='convMon'):
            self.progresso(add=7)
        else:
            return False

        self.lbInfo.setText('CRIANDO TELA DE LOGIN...')
        self.loginPage = LoginController(db=self.db)
        self.progresso(add=7)

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
