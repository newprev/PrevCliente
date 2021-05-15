import datetime
import sys

import pymysql
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Daos.daoConfiguracoes import DaoConfiguracoes
from Daos.daoFerramentas import DaoFerramentas
from cache.cachingLogin import CacheLogin
from repositorios.clienteRepositorio import UsuarioRepository
from repositorios.escritorioRepositorio import EscritorioRepositorio
from repositorios.ferramentasRepositorio import ApiFerramentas
from modelos.escritorioModelo import EscritorioModelo
from modelos.advogadoModelo import AdvogadoModelo
from Telas.loginPage import Ui_mwLogin
from heart.login.wdgAdvController import WdgAdvController
from heart.dashboard.dashboardController import DashboardController
from newPrevEnums import *
import os
import json

from helpers import datetimeToSql, strToDatetime
from newPrevEnums import TamanhoData


class LoginController(QMainWindow, Ui_mwLogin):

    def __init__(self, db=None):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.db = db
        # self.sinais = Sinais()
        self.usuarioRepositorio = UsuarioRepository()
        self.escritorio: EscritorioModelo = None
        self.advogado: AdvogadoModelo = AdvogadoModelo()
        self.escritorioRepositorio = EscritorioRepositorio()
        self.tentativasSenha = 3
        self.edittingFinished = True

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pbarLoading.hide()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.escondeLoading)

        self.daoConfigs = DaoConfiguracoes(self.db)
        self.dashboard: DashboardController = None
        self.cacheLogin = CacheLogin()

        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.inicio.value)
        self.pbPrimeiroAcesso.clicked.connect(self.iniciarPrimeiroAcesso)
        self.pbBuscar.clicked.connect(self.buscaEscritorio)
        self.pbCancelar.clicked.connect(self.cancelaCadastro)
        self.pbCadastrar.clicked.connect(self.avaliaConfirmacaoCadastro)
        self.pbFechar.clicked.connect(self.close)
        self.pbEntrar.clicked.connect(self.entrar)
        # self.leSenha.editingFinished.connect(self.resolveBugEntrar)

        self.iniciaCampos()
        self.carregaCacheLogin()

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def resolveBugEntrar(self):
        if self.edittingFinished:
            self.edittingFinished = not self.edittingFinished
            self.entrar()

    def iniciarPrimeiroAcesso(self):
        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.buscaEscritorio.value)
        self.leCdEscritorio.setFocus()

    def carregaCacheLogin(self):
        self.advogado = self.cacheLogin.carregarCache()
        if self.advogado.numeroOAB is not None:
            self.escritorio = self.escritorioRepositorio.buscaEscritorio(self.advogado.escritorioId)
            if isinstance(self.escritorio, ErroConexao):
                self.apresentandoErros(self.escritorio)
                return False
            self.lbNomeDoEscritorio.setText(self.escritorio.nomeFantasia)
            self.leLogin.setText(self.advogado.numeroOAB)
            self.leSenha.setText(self.advogado.senha)
            self.cbSalvarSenha.setChecked(True)
        else:
            self.advogado = AdvogadoModelo()
            self.leLogin.setFocus()

    def trocaPagina(self, *args):
        advogado: AdvogadoModelo = args[0]
        self.advogado = advogado
        senhaProvisoria = self.usuarioRepositorio.buscaSenhaProvisoria(advogado.advogadoId)

        if "erro" in senhaProvisoria.keys():
            self.showPopupAlerta(f"Advogado(a) não encontrado(a). Favor acessar o cadastro do escritório ou o contratante do sistema.")
            return False
        else:
            self.advogado.senha = senhaProvisoria['senha']

        self.lePrimCadLogin.setText(advogado.login)
        self.leNome.setText(advogado.nomeUsuario)
        self.leSobrenome.setText(advogado.sobrenomeUsuario.strip())
        self.leEmail.setText(advogado.email[0])
        self.leNacionalidade.setText(advogado.nacionalidade)
        self.leEstadoCivil.setText(advogado.estadoCivil)
        self.lbNumeroDaOAB.setText(advogado.numeroOAB)
        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.cadastro.value)

    def cancelaCadastro(self):
        self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.inicio.value)
        self.limpa()
        self.limpaListaAdv()

    def buscaEscritorio(self):
        nomeEscritorio = self.leCdEscritorio.text()
        if nomeEscritorio != '':
            escritorio: EscritorioModelo = self.usuarioRepositorio.buscaEscritorioPrimeiroAcesso(nomeEscritorio)
            self.escritorio = escritorio
            if escritorio is not None and escritorio.nomeEscritorio == nomeEscritorio:
                self.lbNomeDoEscritorio.setText(escritorio.nomeFantasia)
                self.carregaAdvNaoCadastrados(escritorio.escritorioId)
            else:
                self.leCdEscritorio.setText('')
                self.lbNomeDoEscritorio.setText('')

    def carregaAdvNaoCadastrados(self, escritorioId: int):
        self.limpaListaAdv()

        listaAdvs = self.usuarioRepositorio.buscaAdvNaoCadastrados(escritorioId)
        listaWdgAdv = [WdgAdvController(adv, parent=self) for adv in listaAdvs]

        for adv in listaWdgAdv:
            self.vlAdv.addWidget(adv)

    def avaliaConfirmacaoCadastro(self):

        if self.leSenhaProvisoria.text() != self.advogado.senha:
            self.tentativasSenha -= 1
            self.showPopupAlerta(f"Senha provisória diferente da cadastrada. Tente novamente. \nTentativas faltantes: {self.tentativasSenha}")
            if self.tentativasSenha == 0:
                self.close()
        elif self.lePrimCadSenha.text() != self.leConfirmarSenha.text():
            self.showPopupAlerta(f"Senhas não coincidem. Tente novamente.")
        else:
            self.loading(20)
            senhaConfirmada = self.usuarioRepositorio.atualizaSenha(self.advogado.advogadoId, self.leConfirmarSenha.text())
            self.loading(10)
            if 'statusCode' not in senhaConfirmada.keys():
                self.loading(10)
                self.advogado.senha = senhaConfirmada['senha']
                self.loading(10)
                self.advogado.confirmado = True
                self.loading(10)
                self.leLogin.setText(self.advogado.numeroOAB)
                self.loading(10)
                self.leSenha.setText(self.advogado.senha)
                self.loading(10)
                self.stkPrimeiroAcesso.setCurrentIndex(TelaLogin.inicio.value)
                self.loading(10)
                self.cacheLogin.salvarCache(self.advogado)
                self.loading(10)
            else:
                self.loading(100)
                self.showPopupAlerta(f"Não foi possível confirmar o cadastro. Tente novamente.")

    def entrar(self):

        self.loading(20)
        if self.advogado is not None and self.advogado.escritorioId is not None:
            self.loading(10)
            autenticado = self.usuarioRepositorio.loginAuthFromCache(self.advogado)
            self.loading(30)

            if autenticado:
                self.loading(10)
                if ApiFerramentas().conexaoOnline():
                    self.loading(10)
                    self.verificaRotinaDiaria()
                    self.loading(20)
                else:
                    self.showPopupAlerta('Sem conexão com o servidor.')
                    sys.exit()

                self.dashboard = DashboardController(db=self.db)
                self.dashboard.show()
                self.close()
            else:
                self.showPopupAlerta(f"Usuário {self.advogado.nomeUsuario} não confirmado. \nFavor confirmar senha clicando em 'Primeiro acesso'.")
        else:
            self.loading(10)
            self.advogado = self.procuraAdvogado()
            self.loading(10)
            if self.advogado is None:
                self.loading(10)
                self.tentativasSenha -= 1
                self.showPopupAlerta(f'Usuário não encontrado. Tente novamente. \nNúmero de tentativas faltantes {self.tentativasSenha}')
                self.advogado = AdvogadoModelo()
                self.loading(100)
                self.limpa()
                if self.tentativasSenha == 0:
                    self.close()
            else:
                self.loading(10)
                if self.cbSalvarSenha.isChecked():
                    self.loading(10)
                    self.verificaRotinaDiaria()
                    self.loading(20)
                    self.dashboard = DashboardController(db=self.db)
                    self.loading(20)
                    self.dashboard.show()
                    self.close()
                    self.cacheLogin.salvarCache(self.advogado)
                else:
                    self.loading(10)
                    self.cacheLogin.salvarCacheTemporario(self.advogado)
                    self.loading(10)
                    self.dashboard = DashboardController(db=self.db)
                    self.loading(30)
                    self.dashboard.show()
                    self.close()
        self.edittingFinished = True


    def procuraAdvogado(self) -> AdvogadoModelo:
        senha = self.leSenha.text()

        if self.leLogin.text().isdecimal():
            numeroOAB = self.leLogin.text()
            return self.usuarioRepositorio.loginAuth(senha, numeroOAB=numeroOAB)
        else:
            email = self.leLogin.text()
            return self.usuarioRepositorio.loginAuth(senha, email=email)


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

    def iniciaCampos(self):
        self.lePrimCadLogin.setReadOnly(True)
        self.leNome.setReadOnly(True)
        self.leSobrenome.setReadOnly(True)
        self.leNacionalidade.setReadOnly(True)
        self.leEstadoCivil.setReadOnly(True)
        self.leEmail.setReadOnly(True)

    def loading(self, value: int):
        self.pbarLoading.show()
        valor: int = value + self.pbarLoading.value()
        self.pbarLoading.setValue(valor)

        if valor >= 100:
            self.timer.start(500)

    def escondeLoading(self):
        self.pbarLoading.hide()
        self.pbarLoading.setValue(0)
        self.timer.stop()

    def limpa(self):
        self.leNome.clear()
        self.leSobrenome.clear()
        self.leEmail.clear()
        self.lePrimCadSenha.clear()
        self.leSenhaProvisoria.clear()
        self.leNacionalidade.clear()
        self.leEstadoCivil.clear()
        self.leSenha.clear()
        self.leCdEscritorio.clear()

        self.limpaListaAdv()

    def limpaListaAdv(self):
        for i in reversed(range(self.vlAdv.count())):
            self.vlAdv.itemAt(i).widget().setParent(None)

    def getDB(self):

        return pymysql.connect(
            host=self.config.host,
            user=self.config.user,
            passwd=self.config.passwd,
            db=self.config.banco,
            port=self.config.port
        )

    def apresentandoErros(self, tipoErro):
        if isinstance(tipoErro, ErroConexao):
            if tipoErro == ErroConexao.ConnectionError:
                self.showPopupAlerta('Não há conexão com a internet ou com o servidor. \nVerifique se há acesso à internet.')