from PyQt5.QtWidgets import QWidget

from Daos.daoInfoImportante import DaoInfoImportante
from Telas.ferramentasPage import Ui_wdgFerramentas
from modelos.convMonModelo import ConvMonModelo

from helpers import dinheiroToFloat, getConversoesMonetarias
from datetime import datetime


class FerramentasPage(QWidget, Ui_wdgFerramentas):

    def __init__(self, parent=None, db=None):
        super(FerramentasPage, self).__init__(parent=parent)
        self.setupUi(self)

        self.db = db
        self.dashboard = parent
        self.daoInfoImportante = DaoInfoImportante(db=db)
        self.convMonModelo = ConvMonModelo()
        self.convMonDe = ConvMonModelo()
        self.convMonPara = ConvMonModelo()

        self.pbLimpar.clicked.connect(self.limpaTudo)
        self.carregaComboBoxes()
        self.carregaConvMonIniciais()

        self.cbMoedaCorrente.setChecked(True)
        self.dtDataFim.setDisabled(True)

        self.leNomeMoeda.textChanged.connect(lambda: self.getInfo('leNomeMoeda'))
        self.leFator.textChanged.connect(lambda: self.getInfo('leFator'))
        self.dtDataInicio.dateChanged.connect(lambda: self.getInfo('dtDataInicio'))
        self.dtDataFim.dateChanged.connect(lambda: self.getInfo('dtDataFim'))
        self.cbxConversao.activated.connect(lambda: self.getInfo('cbxConversao'))
        self.cbMoedaCorrente.clicked.connect(lambda: self.getInfo('cbMoedaCorrente'))
        self.cbxDe.currentTextChanged.connect(lambda: self.atualizaConvMon('cbxDe'))
        self.cbxPara.currentTextChanged.connect(lambda: self.atualizaConvMon('cbxPara'))

        self.pbInserir.clicked.connect(self.trataInserir)

    def carregaComboBoxes(self):
        convMon: list = self.daoInfoImportante.getAllMoedas()

        apenasNome = []
        for moeda in convMon:
            apenasNome.append(moeda[1])
        self.cbxDe.clear()
        self.cbxPara.clear()
        self.cbxDe.addItems(apenasNome)
        self.cbxPara.addItems(apenasNome)

        self.cbxConversao.addItems(getConversoesMonetarias())

    def getInfo(self, info):
        if info == 'leNomeMoeda':
            self.convMonModelo.nomeMoeda = self.leNomeMoeda.text()

        elif info == 'leFator':
            self.convMonModelo.fator = dinheiroToFloat(self.leFator.text())

        elif info == 'dtDataInicio':
            self.convMonModelo.dataInicial = self.dtDataInicio.date().toPyDate()

        elif info == 'dtDataFim':
            self.convMonModelo.dataFinal = self.dtDataFim.date().toPyDate()

        elif info == 'cbxConversao':
            self.convMonModelo.conversao = self.cbxConversao.currentText()

        elif info == 'cbMoedaCorrente':
            self.dtDataFim.setDisabled(self.cbMoedaCorrente.isChecked())
            self.convMonModelo.moedaCorrente = self.cbMoedaCorrente.isChecked()

    def trataInserir(self):
        if self.convMonModelo.nomeMoeda is not None:
            if self.convMonModelo.moedaCorrente:
                self.convMonModelo.dataFinal = datetime.now()
            self.daoInfoImportante.insereConvMon(self.convMonModelo)
            self.carregaComboBoxes()

    def carregaConvMonIniciais(self):
        if self.cbxDe.currentText() != '' and self.cbxDe.currentText() is not None:
            self.convMonDe = ConvMonModelo().fromList(self.daoInfoImportante.getConvMonByNomeMoeda(self.cbxDe.currentText()), retornaInst=True)
            self.convMonPara = ConvMonModelo().fromList(self.daoInfoImportante.getConvMonByNomeMoeda(self.cbxPara.currentText()), retornaInst=True)

    def atualizaConvMon(self, info):
        if self.cbxDe.currentText() != '' and self.cbxDe.currentText() is not None:
            if info == 'cbxDe':
                self.convMonDe = ConvMonModelo().fromList(self.daoInfoImportante.getConvMonByNomeMoeda(self.cbxDe.currentText()), retornaInst=True)
            else:
                self.convMonPara = ConvMonModelo().fromList(self.daoInfoImportante.getConvMonByNomeMoeda(self.cbxPara.currentText()), retornaInst=True)


    def limpaTudo(self):
        self.leValorDe.clear()
        self.leValorPara.clear()