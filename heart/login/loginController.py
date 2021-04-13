import datetime

import pymysql
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Daos.daoConfiguracoes import DaoConfiguracoes
from Daos.daoServidor import DaoServidor
from Telas.loginPage import Ui_mwLogin
from heart.dashboard.dashboardController import DashboardController
import os
import json

from helpers import datetimeToSql, strToDatetime
from newPrevEnums import TamanhoData


class LoginController(QMainWindow, Ui_mwLogin):

    def __init__(self, db=None):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.db = db

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pbEntrar.clicked.connect(self.entrar)
        self.daoConfigs = DaoConfiguracoes(self.db)
        self.dashboard: DashboardController = None
        self.daoServidor = DaoServidor(db=db)

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def entrar(self):
        self.verificaRotinaDiaria()
        self.dashboard = DashboardController(db=self.db)
        self.dashboard.show()
        self.close()

    def verificaRotinaDiaria(self):

        pathFile = os.path.join(os.getcwd(), 'sync', 'syncFile')
        syncJson = {
            'syncConvMon': datetimeToSql(datetime.datetime.now()),
            'syncTetosPrev': datetimeToSql(datetime.datetime.now())
        }

        if os.path.isfile(pathFile):
            with open(pathFile, encoding='utf-8', mode='r') as syncFile:
                if len(syncFile.readlines()) == 0:
                    os.remove(pathFile)
                    self.verificaRotinaDiaria()
                    return True
                else:
                    syncFile.seek(0)
                    syncDict = json.load(syncFile)

                    dateSyncConvMon = strToDatetime(syncDict['syncConvMon'], TamanhoData.g)
                    dateSyncTetosPrev = strToDatetime(syncDict['syncTetosPrev'], TamanhoData.g)

                    if (datetime.datetime.now() - dateSyncConvMon).days != 0:
                        self.daoServidor.syncConvMon()
                    else:
                        syncJson['syncConvMon'] = syncDict['syncConvMon']

                    if (datetime.datetime.now() - dateSyncTetosPrev).days != 0:
                        self.daoServidor.syncTetosPrev()
                    else:
                        syncJson['syncTetosPrev'] = syncDict['syncTetosPrev']

            with open(pathFile, encoding='utf-8', mode='w') as syncFile:
                syncFile.write(json.dumps(syncJson))
        else:
            self.daoServidor.syncConvMon()
            self.daoServidor.syncTetosPrev()
            with open(pathFile, encoding='utf-8', mode='w') as syncFile:
                syncFile.write(json.dumps(syncJson))

    def getDB(self):

        return pymysql.connect(
            host=self.config.host,
            user=self.config.user,
            passwd=self.config.passwd,
            db=self.config.banco,
            port=self.config.port
        )