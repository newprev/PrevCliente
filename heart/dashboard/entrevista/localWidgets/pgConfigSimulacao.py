from Design.pyUi.pgConfigSimulacao import Ui_mwConfigSimulacao
from PyQt5.QtWidgets import QMainWindow

from Design.pyUi.efeitos import Efeitos
from util.enums.aposentadoriaEnums import *


class PgConfigSimulacao(Ui_mwConfigSimulacao, QMainWindow):
    entrevistaParams: dict

    def __init__(self, entrevistaParams: dict, parent=None):
        super(PgConfigSimulacao, self).__init__(parent)
        self.setupUi(self)
        self.efeitos = Efeitos()
        self.entrevistaParams = entrevistaParams

        self.efeitos.shadowCards(
            [self.frTop, self.gbPorcentagem, self.gbContFuturas, self.gbIndicesReajuste],
            radius=8,
            offset=(0, 6),
            color=(63, 63, 63, 90),
        )
        self.leValorCustomizado.setDisabled(True)
        self.iniciaCombos()
        self.cbContribFuturas.currentIndexChanged.connect(self.avaliaTrocaContrFuturas)
        self.cbPorcentagem.currentIndexChanged.connect(self.avaliaTrocaPorcentagem)
        self.cbContribFuturas.currentIndexChanged.connect(self.avaliaTrocaContrFuturas)
        self.cbContribFuturas.currentIndexChanged.connect(self.avaliaTrocaContrFuturas)

    def iniciaCombos(self):
        listaContFuturas = ['Último salário', 'Salário mínimo', 'Teto INSS', 'Customizado']
        listaIndiceReajuste = ['IPCA', 'Selic', 'IGPM', 'IBOVESPA']
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

        if self.entrevistaParams['IndiceReajuste'] == IndiceReajuste.Ipca:
            self.cbIndiceReajuste.setCurrentIndex(0)
        elif self.entrevistaParams['IndiceReajuste'] == IndiceReajuste.Selic:
            self.cbIndiceReajuste.setCurrentIndex(1)
        elif self.entrevistaParams['IndiceReajuste'] == IndiceReajuste.Igpm:
            self.cbIndiceReajuste.setCurrentIndex(2)
        else:
            self.cbIndiceReajuste.setCurrentIndex(3)
        if self.entrevistaParams['valorSimulacao'] != 0:
            self.leValorCustomizado.setText(str(self.entrevistaParams['valorSimulacao']))

    def avaliaTrocaContrFuturas(self):
        if self.cbContribFuturas.currentText() == 'Customizado':
            self.leValorCustomizado.setDisabled(False)
        else:
            self.leValorCustomizado.setDisabled(True)

    def avaliaTrocaPorcentagem(self):
        self.entrevistaParams['porcentagemCont'] = int(self.cbPorcentagem.currentText().replace('%', ''))

