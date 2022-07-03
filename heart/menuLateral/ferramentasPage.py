from PyQt5.QtWidgets import QWidget

from Design.pyUi.ferramentasPage import Ui_wdgFerramentas
from modelos.convMonORM import ConvMon

from util.helpers.helpers import dinheiroToFloat, getConversoesMonetarias, datetimeToSql, strToFloat
from datetime import datetime


class FerramentasPage(QWidget, Ui_wdgFerramentas):

    def __init__(self, parent=None, db=None):
        super(FerramentasPage, self).__init__(parent=parent)
        self.setupUi(self)

        self.db = db
        self.dashboard = parent
        self.convMonModelo = ConvMon()
        self.convMonDe = ConvMon()
        self.convMonPara = ConvMon()

        self.pbLimpar.clicked.connect(self.limpaTudo)
        # self.carregaComboBoxes()
        # self.carregaConvMonIniciais()

        self.cbMoedaCorrente.setChecked(True)
        self.dtDataFim.setDisabled(True)

        self.lbValorPara.setText('R$ 0,00')

        self.leNomeMoeda.textChanged.connect(lambda: self.getInfo('leNomeMoeda'))
        self.leFator.textChanged.connect(lambda: self.getInfo('leFator'))
        self.leSinal.textChanged.connect(lambda: self.getInfo('leSinal'))
        self.dtDataInicio.dateChanged.connect(lambda: self.getInfo('dtDataInicio'))
        self.dtDataFim.dateChanged.connect(lambda: self.getInfo('dtDataFim'))
        self.cbxConversao.activated.connect(lambda: self.getInfo('cbxConversao'))
        self.cbMoedaCorrente.clicked.connect(lambda: self.getInfo('cbMoedaCorrente'))
        self.cbxDe.currentTextChanged.connect(lambda: self.atualizaConvMon('cbxDe'))
        self.cbxPara.currentTextChanged.connect(lambda: self.atualizaConvMon('cbxPara'))
        self.leValorDe.textChanged.connect(self.atualizaValor)

        self.pbInserir.clicked.connect(self.trataInserir)

    def carregaComboBoxes(self):
        convMon: list = []

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

        elif info == 'leSinal':
            self.convMonModelo.sinal = self.leSinal.text()

        elif info == 'dtDataInicio':
            self.convMonModelo.dataInicial = self.dtDataInicio.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'dtDataFim':
            self.convMonModelo.dataFinal = self.dtDataFim.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'cbxConversao':
            self.convMonModelo.conversao = self.cbxConversao.currentText()

        elif info == 'cbMoedaCorrente':
            self.dtDataFim.setDisabled(self.cbMoedaCorrente.isChecked())
            self.convMonModelo.moedaCorrente = self.cbMoedaCorrente.isChecked()

    def trataInserir(self):
        if self.convMonModelo.nomeMoeda is not None:
            if self.convMonModelo.moedaCorrente:
                if self.convMonModelo.dataInicial is None:
                    self.convMonModelo.dataInicial = self.dtDataInicio.date().toPyDate().strftime('%Y-%m-%d %H:%M')
                self.convMonModelo.dataFinal = datetimeToSql(datetime.now())
            # self.daoFerramentas.insereConvMon(self.convMonModelo)
            self.carregaComboBoxes()
            self.limpaTudo()

    def carregaConvMonIniciais(self):
        if self.cbxDe.currentText() != '' and self.cbxDe.currentText() is not None:
            pass
            # self.convMonDe = ConvMon().fromList(self.daoFerramentas.getConvMonByNomeMoeda(self.cbxDe.currentText()), retornaInst=True)
            # self.convMonPara = ConvMon().fromList(self.daoFerramentas.getConvMonByNomeMoeda(self.cbxPara.currentText()), retornaInst=True)

    def atualizaConvMon(self, info):
        if self.cbxDe.currentText() != '' and self.cbxDe.currentText() is not None:
            if info == 'cbxDe':
                pass
                # self.convMonDe = ConvMon().fromList(self.daoFerramentas.getConvMonByNomeMoeda(self.cbxDe.currentText()), retornaInst=True)
            else:
                # self.convMonPara = ConvMon().fromList(self.daoFerramentas.getConvMonByNomeMoeda(self.cbxPara.currentText()), retornaInst=True)
                self.lbValorPara.setText(f'{self.convMonPara.sinal} 0,00')

    def atualizaValor(self):
        if self.leValorDe.text() != '':
            if self.convMonDe.dataFinal is not None and self.convMonPara.dataInicial:
                valor = strToFloat(self.leValorDe.text())
                valorAtuzliado = round((valor / self.convMonDe.fator) * self.convMonPara.fator, 2)

                self.lbValorPara.setText(f'R$ {valorAtuzliado}')

    def limpaTudo(self):
        self.leValorDe.clear()
        self.leNomeMoeda.clear()
        self.leFator.clear()
        self.leSinal.clear()
        self.lbValorPara.setText('R$ 0,00')
