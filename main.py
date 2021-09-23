from math import ceil

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from Daos.daoConfiguracoes import DaoConfiguracoes
from Design.pyUi.splashScreen import Ui_MainWindow
from heart.login.loginController import LoginController
from connections import ConfigConnection
from modelos.convMonORM import ConvMon
from modelos.especieBenefORM import EspecieBenef
from modelos.expSobrevidaORM import ExpSobrevida
from modelos.indicadoresORM import Indicadores
from modelos.indiceAtuMonetariaORM import IndiceAtuMonetaria
from modelos.pppORM import Ppp
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from modelos.tetosPrevORM import TetosPrev
from modelos.escritoriosORM import Escritorios
from modelos.advogadoORM import Advogados
from modelos.clienteORM import Cliente
from modelos.beneficiosORM import CnisBeneficios
from modelos.cabecalhoORM import CnisCabecalhos
from modelos.contribuicoesORM import CnisContribuicoes
from modelos.remuneracaoORM import CnisRemuneracoes
from modelos.carenciasLei91 import CarenciaLei91
from modelos.configGeraisORM import ConfigGerais
from modelos.itemContribuicao import ItemContribuicao
from util.enums.newPrevEnums import TiposConexoes
from cache.cachingLogin import CacheLogin


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

        if self.contador == 100:
            self.lbInfo.setText('INICIANDO SUBMERSAO...')

    def iniciaBancosETelas(self):

        listaTabelas = {
            Escritorios: 'CRIANDO TABELA DOS ESCRITORIOS...',
            Advogados: 'CRIANDO TABELA DOS ADVOGADOS...',
            Cliente: 'CRIANDO TABELA DO CLIENTE...',
            CnisBeneficios: 'CRIANDO TABELA DE BENEFÍCIOS...',
            CnisCabecalhos: 'CRIANDO TABELA DE CABEÇALHOS...',
            CnisContribuicoes: 'CRIANDO TABELA DE CONTRIBUIÇÕES...',
            CnisRemuneracoes: 'CRIANDO TABELA DE REMUNERAÇÕES...',
            ConvMon: 'CRIANDO TABELA DE CONVERSÕES MONETÁRIAS...',
            EspecieBenef: 'CRIANDO TABELA DE ESPÉCIES DE BENEFÍCIOS...',
            ExpSobrevida: 'CRIANDO TABELA DAS EXPECTATIVAS DE SOBREVIDA...',
            Indicadores: 'CRIANDO TABELA DE INDICADORES...',
            IndiceAtuMonetaria: 'CRIANDO TABELA DOS ÍNDICES DE ATUALIZAÇÃO MONETARIA...',
            Ppp: 'CRIANDO TABELA DOS PPP...',
            Processos: 'CRIANDO TABELA DOS PROCESSOS...',
            Telefones: 'CRIANDO TABELA DE TELEFONES...',
            TetosPrev: 'CRIANDO TABELA DE TETOS PREVIDENCIÁRIOS...',
            CarenciaLei91: 'CRIANDO TABELA DE CARÊNCIAS LEI 8.213/91...',
            ConfigGerais: 'CRIANDO TABELA DE CONFIGURAÇÕES GERAIS...',
            ItemContribuicao: 'CRIANDO TABELA DE ITENS DE CONTRIBUIÇÃO...',
        }

        # percentLoading = ceil(100 / len(listaLoading))
        percentLoading = ceil(100 / len(listaTabelas))

        for instancia, label in listaTabelas.items():
            self.lbInfo.setText(label)
            instancia.create_table()
            self.progresso(add=percentLoading)

        self.lbInfo.setText('CRIANDO TELA DE LOGIN...')
        self.progresso(add=percentLoading)

        # self.iniciaNewPrev()
        self.avaliaAbrirTelaLogin()

    def avaliaAbrirTelaLogin(self):
        advogado = CacheLogin().carregarCache()
        self.loginPage = LoginController(db=self.db)

        if advogado:
            try:
                configGeral: ConfigGerais = ConfigGerais().get(ConfigGerais.advogadoId == advogado.advogadoId)

                if configGeral.iniciaAuto:
                    self.loginPage.verificaRotinaDiaria()
                    self.loginPage.iniciaDashboard()
                    self.close()
                else:
                    self.iniciaNewPrev()

            except ConfigGerais.DoesNotExist:
                print('Não encontrou configurações')
                self.iniciaNewPrev()
        else:
            self.iniciaNewPrev()

    def iniciaNewPrev(self):
        self.loginPage.show()
        self.close()

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
