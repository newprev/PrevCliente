from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from typing import List

from Design.pyUi.pgExpSobrevida import Ui_mwExpSobrevida
from Design.CustomWidgets.newCheckBox import NewCheckBox
from Design.DesignSystem.colors import NewColors
from modelos.expSobrevidaORM import ExpSobrevida
from util.dateHelper import mascaraDataPequena


class ExpSobrevidaTela(QMainWindow, Ui_mwExpSobrevida):

    def __init__(self, parent=None):
        super(ExpSobrevidaTela, self).__init__(parent=parent)
        self.setupUi(self)

        self.cbFiltro = NewCheckBox(active_color=NewColors.primary.value)

        self.tblInfo.hideColumn(0)

        self.vlChecBox.addWidget(self.cbFiltro)

        self.desativarFiltros(True)
        self.cbFiltro.stateChanged.connect(self.avaliaDesativaFiltros)

        self.carregaTabela()

    def desativarFiltros(self, valor: bool):
        if valor:
            self.frDtReferente.hide()
            self.frIdade.hide()
            self.frGenero.hide()
            self.frExpectativa.hide()
            self.pbFiltrar.hide()
        else:
            self.frDtReferente.show()
            self.frIdade.show()
            self.frGenero.show()
            self.frExpectativa.show()
            self.pbFiltrar.show()

    def avaliaDesativaFiltros(self):
        self.desativarFiltros(not self.cbFiltro.isChecked())

    def carregaTabela(self, listaExpSobrevida: [ExpSobrevida] = None):
        if listaExpSobrevida is not None:
            listaDaTabela = listaExpSobrevida
        else:
            listaDaTabela: List[ExpSobrevida] = ExpSobrevida.select()

        self.tblInfo.setRowCount(0)

        for contLinha, expectativa in enumerate(listaDaTabela):
            self.tblInfo.insertRow(contLinha)

            # infoId - Coluna 0 (escondida)
            strExpectativaId = QTableWidgetItem(str(expectativa.infoId))
            strExpectativaId.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 0, strExpectativaId)

            # Ano - Coluna 1 (ativa)
            strAno = QTableWidgetItem(mascaraDataPequena(expectativa.dataReferente))
            strAno.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            strAno.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 1, strAno)

            # Expectativa - Coluna 2 (ativa)
            strExpectativa = QTableWidgetItem(str(expectativa.expectativaSobrevida))
            strExpectativa.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strExpectativa.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 2, strExpectativa)

            # Idade - Coluna 3 (ativa)
            strIdade = QTableWidgetItem(str(expectativa.idade))
            strIdade.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strIdade.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 3, strIdade)

            # Gênero - Coluna 4 (ativa)
            if expectativa.genero == 'M':
                strGenero = QTableWidgetItem("Masculino")
            else:
                strGenero = QTableWidgetItem("Feminino")

            strGenero.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strGenero.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 4, strGenero)

        # self.tblInfo.resizeColumnsToContents()
        self.tblInfo.resizeColumnToContents(3)
        self.tblInfo.resizeRowsToContents()
