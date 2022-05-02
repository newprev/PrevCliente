import os.path
from math import ceil
from typing import List

from aiohttp import ClientConnectorError
import asyncio as aio
from peewee import SqliteDatabase

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

from Design.pyUi.splashScreen import Ui_MainWindow
from heart.login.loginController import LoginController
from connections import ConfigConnection
from modelos.clienteInfoBanco import ClienteInfoBanco
from modelos.clienteProfissao import ClienteProfissao

from modelos.convMonORM import ConvMon
from modelos.baseModelORM import database
from modelos.especieBenefORM import EspecieBene
from modelos.expSobrevidaORM import ExpSobrevida
from modelos.incidenteProcessual import IncidenteProcessual
from modelos.indicadoresORM import Indicadores
from modelos.indiceAtuMonetariaORM import IndiceAtuMonetaria
from modelos.pppORM import Ppp
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from modelos.tetosPrevORM import TetosPrev
from modelos.escritoriosORM import Escritorios
from modelos.advogadoORM import Advogados
from modelos.clienteORM import Cliente
from modelos.vinculoORM import CnisVinculos
from modelos.carenciasLei91 import CarenciaLei91
from modelos.configGeraisORM import ConfigGerais
from modelos.itemContribuicao import ItemContribuicao
from modelos.salarioMinimoORM import SalarioMinimo
from modelos.aposentadoriaORM import Aposentadoria
from modelos.ipcaMensalORM import IpcaMensal
from modelos.tipoBeneficioORM import TipoBeneficioModel
from modelos.tiposESubtipos.tipoAposentadoriaORM import TipoAposentadoria

from repositorios.informacoesRepositorio import ApiInformacoes
from systemLog.logs import NewLogging
from util.enums.databaseEnums import DatabaseEnum
from util.enums.ferramentasEInfoEnums import FerramentasEInfo
from util.enums.newPrevEnums import TiposConexoes
from util.popUps import popUpOkAlerta

from cache.cachingLogin import CacheLogin
from crypt.newRsa import Crypt


class Main(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.contador = 0
        self.tipoConexao = TiposConexoes.sqlite
        self.dbConnection = ConfigConnection(instanciaBanco=self.tipoConexao)
        self.db = self.dbConnection.getDatabase()
        self.newLogger = None
        self.loginPage = None
        self.center()
        self.show()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progresso)
        self.timer.start(1)

    def buscaPathTriggers(self) -> str:
        pathTriggers = os.path.join("SQLs", "triggers")
        if os.path.isdir(pathTriggers):
            return pathTriggers
        else:
            return ""

    def carregaLogsConfig(self):
        self.newLogger = NewLogging()

    async def carregaTabelasIniciais(self):
        if TipoBeneficioModel.select().count() == 0:
            asyncTasks = []
            asyncTasks.append(aio.ensure_future(ApiInformacoes().getAllInformacoes(FerramentasEInfo.tipoBeneficio)))

            apiInfo: List[dict] = await aio.gather(*asyncTasks)
            tiposBeneficio = apiInfo[0]
            TipoBeneficioModel.insert_many(tiposBeneficio).execute()

        return True

    def progresso(self, add=None):
        if add is None:
            self.contador += 1
        else:
            self.contador += add

        self.pbarSplash.setValue(self.contador)

        if 0 < self.contador < 2:
            self.carregaLogsConfig()

        elif 10 <= self.contador < 70:
            if self.contador == 10:
                self.timer.stop()
                self.iniciaBancosETelas()
                self.verificaBackups()
            return True

        elif 70 <= self.contador < 90:
            self.lbInfo.setText('GERANDO CHAVES DE CRIPTOGRAFIA...')
            if self.precisaGerarChaves():
                Crypt().gerarChaves()

            self.progresso(add=90 - self.contador)
            return True

        elif self.contador == 90:
            self.lbInfo.setText('INICIANDO SUBMERSAO...')
            self.avaliaAbrirTelaLogin()
            return True

    def verificaBackups(self):
        qtdTipos = TipoAposentadoria.select().count()
        database = SqliteDatabase(DatabaseEnum.producao.value)
        if qtdTipos == 0:
            tipoAposPath = os.path.join(os.getcwd(), 'Banco', 'backup', 'cTipoAposentadoria.sql')
            sqlScript: str = buscaSql(tipoAposPath)
            database.execute_sql(sqlScript)

        return True

    def iniciaBancosETelas(self):
        try:
            loop = aio.get_event_loop()
            pathTriggers = self.buscaPathTriggers()
            fileDropTriggers = os.path.join(pathTriggers, "dropTriggers.sql")

            listaTabelas = {
                Escritorios: 'CRIANDO TABELA DOS ESCRITORIOS...',
                Advogados: 'CRIANDO TABELA DOS ADVOGADOS...',
                Cliente: 'CRIANDO TABELA DO CLIENTE...',
                CnisVinculos: 'CRIANDO TABELA DE VÍNCULOS...',
                ConvMon: 'CRIANDO TABELA DE CONVERSÕES MONETÁRIAS...',
                EspecieBene: 'CRIANDO TABELA DE ESPÉCIES DE BENEFÍCIOS...',
                ExpSobrevida: 'CRIANDO TABELA DAS EXPECTATIVAS DE SOBREVIDA...',
                Indicadores: 'CRIANDO TABELA DE INDICADORES...',
                IndiceAtuMonetaria: 'CRIANDO TABELA DOS ÍNDICES DE ATUALIZAÇÃO MONETARIA...',
                IncidenteProcessual: 'CRIANDO TABELA DE INCIDENTES PROCESSUAIS...',
                Ppp: 'CRIANDO TABELA DOS PPP...',
                Processos: 'CRIANDO TABELA DOS PROCESSOS...',
                Telefones: 'CRIANDO TABELA DE TELEFONES...',
                TetosPrev: 'CRIANDO TABELA DE TETOS PREVIDENCIÁRIOS...',
                CarenciaLei91: 'CRIANDO TABELA DE CARÊNCIAS LEI 8.213/91...',
                ConfigGerais: 'CRIANDO TABELA DE CONFIGURAÇÕES GERAIS...',
                ItemContribuicao: 'CRIANDO TABELA DE ITENS DE CONTRIBUIÇÃO...',
                SalarioMinimo: 'CRIANDO TABELA DE SALÁRIOS MÍNIMOS...',
                Aposentadoria: 'CRIANDO TABELA DE APOSENTADORIAS...',
                IpcaMensal: 'CRIANDO TABELA DE IPCA MENSAL...',
                TipoAposentadoria: 'CRIANDO TABELA DE TIPOS DE APOSENTADORIAS...',
                ClienteInfoBanco: 'CRIANDO TABLEA DE INFORMAÇÕES BANCÁRIAS',
                ClienteProfissao: 'CRIANDO TABLEA DE INFORMAÇÕES PROFISSIONAIS',
                TipoBeneficioModel: 'CRIANDO TABLEA DE TIPOS DE BENEFÍCIOS',
            }

            percentLoading = ceil(60 / len(listaTabelas))

            for instancia, label in listaTabelas.items():
                self.lbInfo.setText(label)
                instancia.create_table()
                self.progresso(add=percentLoading)

            if not os.path.isfile(fileDropTriggers):
                popUpOkAlerta("Não foi possível encontrar os scripts do banco de dados. Entre em contato com o suporte.", funcao=self.close)
                return False
            else:
                with open(fileDropTriggers, encoding='utf-8', mode='r') as f:
                    queries = f.readlines()
                    for drop in queries:
                        resultado = database.execute_sql(drop)

                for trigger in os.listdir(pathTriggers):
                    query = os.path.join(pathTriggers, trigger)
                    if fileDropTriggers == query:
                        continue

                    with open(query, encoding='utf-8', mode='r') as trig:
                        resultado = database.execute_sql(trig.read())

            self.lbInfo.setText('CRIANDO TELA DE LOGIN...')
            self.progresso(add=percentLoading)

            loop.run_until_complete(self.carregaTabelasIniciais())
        except ClientConnectorError as err:
            popUpOkAlerta(
                "O NewPrev não conseguiu se conectar com o servidor. Entre em contato com o suporte.",
                "Sem conexão!",
                erro=err.strerror,
                funcao=self.close(),
            )
            print(f"{err=}")

    def avaliaAbrirTelaLogin(self):
        advogado = CacheLogin().carregarCache()
        self.loginPage = LoginController(db=self.db)

        if advogado:
            try:
                configGeral: ConfigGerais = ConfigGerais().get(ConfigGerais.advogadoId == advogado.advogadoId)

                if configGeral.iniciaAuto:
                    self.loginPage.verificaRotinaAtualizacao()
                    self.loginPage.iniciaDashboard()
                    self.close()
                else:
                    self.iniciaNewPrev()

            except ConfigGerais.DoesNotExist:
                print('Não encontrou configurações')
                self.iniciaNewPrev()
            except ClientConnectorError as err:
                popUpOkAlerta(
                    'Não foi possível se comunicar com o servidor. \nVerifique sua conexão com internet e tente abrir o programa novamente.',
                    erro=f"{err=}",
                    funcao=self.close
                )
        else:
            self.iniciaNewPrev()

    def iniciaNewPrev(self):
        self.loginPage.show()
        self.close()

    def precisaGerarChaves(self):
        chavePrivada = os.path.join(os.getcwd(), os.pardir, 'PrevCliente', 'crypt', '.privateKey.txt')
        chavePrivada = os.path.normpath(chavePrivada)

        chavePublica = os.path.join(os.getcwd(), os.pardir, 'PrevCliente', 'crypt', 'publicKey.txt')
        chavePublica = os.path.normpath(chavePublica)

        existChavePublica = os.path.exists(chavePublica) and os.path.isfile(chavePublica)
        existChavePrivada = os.path.exists(chavePrivada) and os.path.isfile(chavePrivada)

        return not (existChavePublica and existChavePrivada)

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == '__main__':
    import sys
    from os.path import join
    from util.helpers.helpers import pathTo, buscaSql
    from util.enums.configEnums import ImportantPaths

    PATH_FONTS = pathTo(ImportantPaths.fonts)

    app = QtWidgets.QApplication(sys.argv)

    _idAvenir = QtGui.QFontDatabase.addApplicationFont(join(PATH_FONTS, 'Avenir', 'AvenirLTStd-Roman.otf'))
    _idBebas = QtGui.QFontDatabase.addApplicationFont(join(PATH_FONTS, 'Bebas', 'BebasNeue-Regular.ttf'))
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
