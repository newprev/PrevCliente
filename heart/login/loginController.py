import pymysql
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Daos.daoConfiguracoes import DaoConfiguracoes
from Telas.loginPage import Ui_mwLogin
from connections import ConfigConnection
from heart.dashboard.dashboardController import DashboardController


class LoginController(QMainWindow, Ui_mwLogin):

    def __init__(self):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.config = ConfigConnection(carregaBanco=True)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pbEntrar.clicked.connect(self.entrar)
        self.db = self.getDB()
        self.daoConfigs = DaoConfiguracoes(self.db)
        self.dashboard = DashboardController()

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def entrar(self):
        self.dashboard.show()
        self.close()

    def getDB(self):

        return pymysql.connect(
            host=self.config.host,
            user=self.config.user,
            passwd=self.config.passwd,
            db=self.config.banco,
            port=self.config.port
        )