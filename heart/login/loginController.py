import datetime
import sys

import pymysql
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Daos.daoConfiguracoes import DaoConfiguracoes
from Daos.daoFerramentas import DaoFerramentas
from repositorios.clienteRepositorio import UsuarioRepository
from repositorios.ferramentasRepositorio import ApiFerramentas
from modelos.escritorioModelo import EscritorioModelo
from Telas.loginPage import Ui_mwLogin
from heart.login.wdgAdvController import WdgAdvController
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
        self.usuarioRepositorio = UsuarioRepository()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pbEntrar.clicked.connect(self.entrar)
        self.daoConfigs = DaoConfiguracoes(self.db)
        self.dashboard: DashboardController = None
        # self.daoServidor = DaoServidor(db=db)

        self.stkPrimeiroAcesso.setCurrentIndex(1)
        self.pbPrimeiroAcesso.clicked.connect(lambda: self.stkPrimeiroAcesso.setCurrentIndex(0))
        self.pbBuscar.clicked.connect(self.buscaEmpresa)

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def buscaEmpresa(self):
        nomeEscritorio = self.leCdEscritorio.text()
        if nomeEscritorio != '':
            escritorio: EscritorioModelo = self.usuarioRepositorio.buscaEscritorioPrimeiroAcesso(nomeEscritorio)
            if escritorio is not None and escritorio.nomeEscritorio == nomeEscritorio:
                self.lbNomeDoEscritorio.setText(escritorio.nomeFantasia)
                self.carregaAdvNaoCadastrados(escritorio.escritorioId)
            else:
                self.leCdEscritorio.setText('')
                self.lbNomeDoEscritorio.setText('')

    def carregaAdvNaoCadastrados(self, escritorioId: int):
        for i in reversed(range(self.vlAdv.count())):
            self.vlAdv.itemAt(i).widget().setParent(None)

        listaAdvs = self.usuarioRepositorio.buscaAdvNaoCadastrados(escritorioId)
        listaWdgAdv = [WdgAdvController(adv, parent=self) for adv in listaAdvs]

        for adv in listaWdgAdv:
            self.vlAdv.addWidget(adv)

    def entrar(self):
        if ApiFerramentas().conexaoOnline():
            self.verificaRotinaDiaria()
        else:
            self.showPopupAlerta('Sem conexão com o servidor.')
            sys.exit()

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
                        self.atualizaFerramentas(convMon=True)
                    else:
                        syncJson['syncConvMon'] = syncDict['syncConvMon']

                    if (datetime.datetime.now() - dateSyncTetosPrev).days != 0:
                        self.atualizaFerramentas(tetos=True)
                    else:
                        syncJson['syncTetosPrev'] = syncDict['syncTetosPrev']

            with open(pathFile, encoding='utf-8', mode='w') as syncFile:
                syncFile.write(json.dumps(syncJson))
        else:
            self.atualizaFerramentas(tetos=True, convMon=True)
            with open(pathFile, encoding='utf-8', mode='w') as syncFile:
                syncFile.write(json.dumps(syncJson))

    def atualizaFerramentas(self, tetos: bool = False, convMon: bool = False):
        daoFerramentas = DaoFerramentas(self.db)
        tetosFromApi: list = []
        convMonFromApi: list = []

        if tetos:
            tetosFromApi = ApiFerramentas().getAllTetosPrevidenciarios()
            if daoFerramentas.contaQtdTetos() < len(tetosFromApi):
                daoFerramentas.insereListaTetos(tetosFromApi)

        if convMon:
            convMonFromApi = ApiFerramentas().getAllTetosConvMon()
            if daoFerramentas.contaQtdMoedas() < len(convMonFromApi):
                daoFerramentas.insereListaConvMonModel(convMonFromApi)

    def showPopupAlerta(self, mensagem, titulo='Atenção!'):
        dialogPopup = QMessageBox()
        dialogPopup.setWindowTitle(titulo)
        dialogPopup.setText(mensagem)
        dialogPopup.setIcon(QMessageBox.Warning)
        dialogPopup.setStandardButtons(QMessageBox.Ok)

        close = dialogPopup.exec_()

    def getDB(self):

        return pymysql.connect(
            host=self.config.host,
            user=self.config.user,
            passwd=self.config.passwd,
            db=self.config.banco,
            port=self.config.port
        )