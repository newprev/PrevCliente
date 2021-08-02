from math import ceil

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from Daos.daoConfiguracoes import DaoConfiguracoes
from Daos.tabelas import TabelasConfig
from Telas.splashScreen import Ui_MainWindow
from heart.login.loginController import LoginController
from connections import ConfigConnection
from newPrevEnums import TiposConexoes

from modelos.modelsORM import *


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

        tabelas = TabelasConfig(tipoBanco=self.tipoConexao)

        listaLoading = [
            'telaLoading'
            'advogados',
            'escritorios',
            'processos',
            'ppp',
            'expSobrevida',
            'cliente',
            'telefones',
            'cnisRemuneracoes',
            'cnisContribuicoes',
            'cnisBeneficios',
            'cnisCabecalhos',
            'especieBenef',
            'indicadores',
            'tetosPrev',
            'convMon',
            'indiceAtuMonetaria',
        ]

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
            TetosPrev: 'CRIANDO TABELA DE TETOS PREVIDENCIÁRIOS...'
        }

        # percentLoading = ceil(100 / len(listaLoading))
        percentLoading = ceil(100 / len(listaTabelas))

        for instancia, label in listaTabelas.items():
            self.lbInfo.setText(label)
            instancia.create_table()
            self.progresso(add=percentLoading)


        # self.lbInfo.setText('CRIANDO TABELA DOS ADVOGADOS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateAdvogados, nomeTabela='advogados'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DOS ESCRITORIOS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateEscritorios, nomeTabela='escritorios'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DOS PROCESSOS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateProcessos, nomeTabela='processos'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DOS PPP...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreatePpp, nomeTabela='ppp'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DOS ÍNDICES DE ATUALIZAÇÃO MONETARIA...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateIndicesAtuMonetaria, nomeTabela='indicesAtuMonetaria'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DAS EXPECTATIVAS DE SOBREVIDA...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateExpSobrevida, nomeTabela='expSobrevida'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DO CLIENTE...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateCliente, nomeTabela='cliente'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE TELEFONES...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateTelefones, nomeTabela='telefones'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE REMUNERAÇÕES...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisRemuneracoes, nomeTabela='cnisRemuneracoes'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE CONTRIBUIÇÕES...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisContribuicoes, nomeTabela='cnisContribuicoes'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE BENEFÍCIOS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisBeneficios, nomeTabela='cnisBeneficios'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE CABEÇALHOS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateCnisCabecalhos, nomeTabela='cnisCabecalhos'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE ESPÉCIES DE BENEFÍCIOS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateEspecieBenef, nomeTabela='especieBenef'):
        #     self.progresso(add=1)
        #     self.daoConfigs.verificaTblEspecieBenef()
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE INDICADORES...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateIndicadores, nomeTabela='indicadores'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE TETOS PREVIDENCIÁRIOS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateTetosPrev, nomeTabela='tetosPrev'):
        #     self.progresso(add=1)
        # else:
        #     return False
        #
        # self.lbInfo.setText('CRIANDO TABELA DE CONVERSÕES MONETÁRIAS...')
        # if self.daoConfigs.criaTabela(tabelas.sqlCreateConvMon, nomeTabela='convMon'):
        #     self.progresso(add=percentLoading)
        # else:
        #     return False
        #
        self.lbInfo.setText('CRIANDO TELA DE LOGIN...')
        self.loginPage = LoginController(db=self.db)
        self.progresso(add=percentLoading)

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
