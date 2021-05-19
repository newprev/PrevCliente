from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTabBar
from Telas.entrevistaPage import Ui_mwEntrevistaPage
from connections import ConfigConnection
from heart.dashboard.entrevista.naturezaController import NaturezaController
from heart.dashboard.tabs.clienteController import TabCliente
from newPrevEnums import TiposConexoes, TelasEntrevista, EtapaEntrevista
from heart.sinaisCustomizados import Sinais
from heart.dashboard.entrevista.localStyleSheet.cabecalho import *


class EntrevistaController(QMainWindow, Ui_mwEntrevistaPage):

    def __init__(self, parent=None, db=None):
        super(EntrevistaController, self).__init__(parent)
        self.setupUi(self)
        self.tipoConexao = TiposConexoes.nuvem
        self.dbConnection = ConfigConnection(instanciaBanco=self.tipoConexao)
        self.db = db
        self.sinais = Sinais()
        self.telaAtual = TelasEntrevista.cadastro

        self.clienteController = TabCliente(db=self.db, entrevista=True)
        self.naturezaPg = NaturezaController(parent=self, db=self.db)
        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTelaCentral)

        self.stackedWidget.addWidget(self.clienteController)
        self.stackedWidget.addWidget(self.naturezaPg)
        # self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())
        # self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())

        self.pbProxEtapa.clicked.connect(lambda: self.avaliaTrocaTela())
        self.pbVoltaEtapa.clicked.connect(lambda: self.avaliaTrocaTela(proxima=False))

        self.atualizaEtapa(EtapaEntrevista.infoPessoais, False)
        self.atualizaEtapa(EtapaEntrevista.infoProcessual, False)
        self.atualizaEtapa(EtapaEntrevista.detalhamento, False)
        self.atualizaEtapa(EtapaEntrevista.documentacao, False)

        self.stackedWidget.setCurrentIndex(self.telaAtual.value)

    def avaliaTrocaTela(self, proxima=True):
        if proxima:
            if self.telaAtual == TelasEntrevista.cadastro:
                self.sinais.sTrocaTelaEntrevista.emit(TelasEntrevista.natureza)
                self.telaAtual = TelasEntrevista.natureza
                self.atualizaEtapa(EtapaEntrevista.infoPessoais, completo=True)
        else:
            if self.telaAtual == TelasEntrevista.natureza:
                self.sinais.sTrocaTelaEntrevista.emit(TelasEntrevista.cadastro)
                self.telaAtual = TelasEntrevista.cadastro
                self.atualizaEtapa(EtapaEntrevista.infoPessoais, completo=False)

    def trocaTelaCentral(self, *args):
        print(' ---------> trocaTelaCentral')
        print(args[0])
        tela: TelasEntrevista = args[0]
        self.stackedWidget.setCurrentIndex(tela.value)

    def atualizaEtapa(self, etapa: EtapaEntrevista, completo: bool):
        if etapa == EtapaEntrevista.infoPessoais:
            self.lbInfoPessoais.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa1.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))
            self.frProg1.setStyleSheet(infoPontinhosCabecalho(etapa, completo=completo))
        if etapa == EtapaEntrevista.infoProcessual:
            self.lbInfoProcessuais.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa2.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))
            self.frProg2.setStyleSheet(infoPontinhosCabecalho(etapa, completo=completo))
        if etapa == EtapaEntrevista.detalhamento:
            self.lbInfoDetalhamento.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa3.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))
            self.frProg3.setStyleSheet(infoPontinhosCabecalho(etapa, completo=completo))
        if etapa == EtapaEntrevista.documentacao:
            self.lbInfoFinalizacao.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa4.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = EntrevistaController()
    ui.show()
    sys.exit(app.exec_())
