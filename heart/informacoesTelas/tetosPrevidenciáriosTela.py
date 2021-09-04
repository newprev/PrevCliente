from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from typing import List

from Design.pyUi.pgTetosPrevidenciarios import Ui_mwTetosPrev
from modelos.tetosPrevORM import TetosPrev
from util.dateHelper import mascaraDataPequena
from util.helpers import mascaraDinheiro
from Design.DesignSystem.tables import newStyleSheetTable


class TetosPrevidenciarios(QMainWindow, Ui_mwTetosPrev):
    listaTetosPrev: TetosPrev
    
    def __init__(self, parent=None):
        super(TetosPrevidenciarios, self).__init__(parent=parent)

        self.setupUi(self)

        self.tblInfo.hideColumn(0)

        self.carregaTabela()
        # self.carregaNewLayout()

    def carregaNewLayout(self):
        print(newStyleSheetTable('tblInfo'))
        self.tblInfo.setStyleSheet(newStyleSheetTable('tblInfo'))
        
    def carregaTabela(self, listaTetosPrev: List[TetosPrev] = None):
        if listaTetosPrev is not None:
            listaDaTabela = listaTetosPrev
        else:
            listaDaTabela: List[TetosPrev] = TetosPrev.select()

        self.tblInfo.setRowCount(0)

        for contLinha, teto in enumerate(listaDaTabela):
            self.tblInfo.insertRow(contLinha)

            # TetosId - Coluna 0 (escondida)
            strTetosPrevId = QTableWidgetItem(str(teto.tetosPrevId))
            strTetosPrevId.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 0, strTetosPrevId)

            # Ano - Coluna 1 (ativa)
            strAno = QTableWidgetItem(mascaraDataPequena(teto.dataValidade))
            strAno.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            strAno.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 1, strAno)

            # Valor - Coluna 2 (ativa)
            strValor = QTableWidgetItem(mascaraDinheiro(teto.valor))
            strValor.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strValor.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblInfo.setItem(contLinha, 2, strValor)

        self.tblInfo.resizeColumnsToContents()
        self.tblInfo.resizeRowsToContents()

