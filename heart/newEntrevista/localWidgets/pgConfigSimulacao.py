from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from Design.pyUi.pgConfigSimulacao import Ui_mwConfigSimulacao
from PyQt5.QtWidgets import QMainWindow
from typing import List

from Design.efeitos import Efeitos
from sinaisCustomizados import Sinais
from util.enums.aposentadoriaEnums import *


class PgConfigSimulacao(Ui_mwConfigSimulacao, QMainWindow):
    entrevistaParams: dict
    clicouNoSalvar: bool = False

    def __init__(self, entrevistaParams: dict, parent=None):
        super(PgConfigSimulacao, self).__init__(parent)
        self.setupUi(self)
        self.efeitos = Efeitos()
        self.sinais = Sinais()
        self.entrevistaPg = parent
        self.entrevistaParams = entrevistaParams

        self.efeitos.shadowCards(
            [self.frTop],
            radius=8,
            offset=(0, 6),
            color=(63, 63, 63, 90),
        )

        self.leValorCustomizado.setDisabled(True)
        self.iniciaCombos()
        self.cbContribFuturas.currentIndexChanged.connect(self.avaliaTrocaContrFuturas)
        self.cbPorcentagem.currentIndexChanged.connect(self.avaliaTrocaPorcentagem)
        self.cbIndiceReajuste.currentIndexChanged.connect(self.avaliaTrocaContrFuturas)
        self.pbSalvarFechar.clicked.connect(self.avaliaEnvioParams)
        # self.sinais.sAtualizaParams.connect(self.enviaParams)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def iniciaCombos(self):
        listaContFuturas = ['Último salário', 'Salário mínimo', 'Teto INSS', 'Customizado']
        listaIndiceReajuste = ['IPCA', 'SELIC', 'IGPM', 'IBOVESPA']
        listaPorcentagem = ['11%', '15%', '20%']

        self.cbContribFuturas.addItems(listaContFuturas)
        self.cbIndiceReajuste.addItems(listaIndiceReajuste)
        self.cbPorcentagem.addItems(listaPorcentagem)

        self.atualizaCombos()

    def atualizaCombos(self):
        if self.entrevistaParams['contribSimulacao'] == ContribSimulacao.ULTI:
            self.cbContribFuturas.setCurrentIndex(0)
        elif self.entrevistaParams['contribSimulacao'] == ContribSimulacao.SMIN:
            self.cbContribFuturas.setCurrentIndex(1)
        elif self.entrevistaParams['contribSimulacao'] == ContribSimulacao.TETO:
            self.cbContribFuturas.setCurrentIndex(2)
        else:
            self.cbContribFuturas.setCurrentIndex(3)

        if self.entrevistaParams['porcentagemCont'] == 11:
            self.cbPorcentagem.setCurrentIndex(0)
        elif self.entrevistaParams['porcentagemCont'] == 15:
            self.cbPorcentagem.setCurrentIndex(1)
        else:
            self.cbPorcentagem.setCurrentIndex(2)

        if self.entrevistaParams['indiceReajuste'] == IndiceReajuste.Ipca:
            self.cbIndiceReajuste.setCurrentIndex(0)
        elif self.entrevistaParams['indiceReajuste'] == IndiceReajuste.Selic:
            self.cbIndiceReajuste.setCurrentIndex(1)
        elif self.entrevistaParams['indiceReajuste'] == IndiceReajuste.Igpm:
            self.cbIndiceReajuste.setCurrentIndex(2)
        else:
            self.cbIndiceReajuste.setCurrentIndex(3)

        if self.entrevistaParams['valorSimulacao'] != 0:
            self.leValorCustomizado.setText(str(self.entrevistaParams['valorSimulacao']))

    def avaliaEnvioParams(self):
        contribSimulacao: List[ContribSimulacao] = [
            ContribSimulacao.ULTI,
            ContribSimulacao.SMIN,
            ContribSimulacao.TETO,
            ContribSimulacao.MANU
        ]
        porcentagemCont: List[int] = [
            11,
            15,
            20
        ]
        indiceReajuste: List[IndiceReajuste] = [
            IndiceReajuste.Ipca,
            IndiceReajuste.Selic,
            IndiceReajuste.Igpm,
            IndiceReajuste.Ibovespa
        ]
        self.clicouNoSalvar = True

        self.entrevistaParams['contribSimulacao'] = contribSimulacao[self.cbContribFuturas.currentIndex()]
        self.entrevistaParams['porcentagemCont'] = porcentagemCont[self.cbPorcentagem.currentIndex()]
        self.entrevistaParams['indiceReajuste'] = indiceReajuste[self.cbIndiceReajuste.currentIndex()]
        if self.cbContribFuturas.currentText() == 'Customizado':
            self.entrevistaParams['valorSimulacao'] = float(self.leValorCustomizado.text().replace(',', '.'))
        else:
            self.entrevistaParams['valorSimulacao'] = 0.0

        # self.sinais.sAtualizaParams.emit()
        self.close()

    def avaliaTrocaContrFuturas(self):
        if self.cbContribFuturas.currentText() == 'Customizado':
            self.leValorCustomizado.setDisabled(False)
        else:
            self.leValorCustomizado.setDisabled(True)

    def avaliaTrocaPorcentagem(self):
        self.entrevistaParams['porcentagemCont'] = int(self.cbPorcentagem.currentText().replace('%', ''))

    def enviaParams(self):
        self.entrevistaPg.atualizaParams(self.entrevistaParams)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if not self.clicouNoSalvar:
            self.avaliaEnvioParams()
