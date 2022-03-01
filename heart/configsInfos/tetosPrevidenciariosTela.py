from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from typing import List

from Design.pyUi.pgTetosPrevidenciarios import Ui_mwTetosPrev
from modelos.tetosPrevORM import TetosPrev
from util.dateHelper import mascaraDataPequena, strToDate
from util.helpers import mascaraDinheiro, dinheiroToFloat


class TetosPrevidenciarios(QMainWindow, Ui_mwTetosPrev):
    listaTetosPrev: TetosPrev
    filtros: dict = {}
    
    def __init__(self, parent=None):
        super(TetosPrevidenciarios, self).__init__(parent=parent)

        self.setupUi(self)
        self.desativaFiltros(True)
        self.setWindowTitle('Tetos previdenciários - [tetosPrevidenciariosTela]')

        self.dtDe.dateChanged.connect(lambda: self.editandoFiltro('dtDe'))
        self.dtAte.dateChanged.connect(lambda: self.editandoFiltro('dtAte'))
        self.leDe.textChanged.connect(lambda: self.editandoFiltro('leDe'))
        self.leAte.textChanged.connect(lambda: self.editandoFiltro('leAte'))

        self.tblInfo.hideColumn(0)

        self.carregaTabela()

    def avaliaFiltros(self):
        for chave, valor in self.filtros.items():
            for linha in range(self.tblInfo.rowCount()):
                ano = strToDate(self.tblInfo.item(linha, 1).text())
                valorTeto = dinheiroToFloat(self.tblInfo.item(linha, 2).text())

                if chave == 'dtDe':
                    if (ano - valor).days < 0:
                        self.tblInfo.hideRow(linha)

                elif chave == 'dtAte':
                    if (valor - ano).days < 0:
                        self.tblInfo.hideRow(linha)

                elif chave == 'leDe':
                    if valorTeto < valor:
                        self.tblInfo.hideRow(linha)

                elif chave == 'leAte':
                    if valorTeto > valor:
                        self.tblInfo.hideRow(linha)

    def editandoFiltro(self, info: str):
        if info == 'dtDe':
            self.filtros['dtDe'] = self.dtDe.date().toPyDate()
        elif info == 'dtAte':
            self.filtros['dtAte'] = self.dtAte.date().toPyDate()
        elif info == 'leDe':
            self.filtros['leDe'] = dinheiroToFloat(self.leDe.text())
        elif info == 'leAte':
            self.filtros['leAte'] = dinheiroToFloat(self.leAte.text())

    def desativaFiltros(self, valor: bool):
        if valor:
            self.frDtReferente.hide()
            self.frValor.hide()
        else:
            self.frDtReferente.show()
            self.frValor.show()
        
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

        # self.tblInfo.resizeColumnsToContents()
        self.tblInfo.resizeRowsToContents()

    def avaliaEstadoFiltros(self):
        self.desativaFiltros(not self.cbAtivaFiltros.isChecked())

    def limpaFiltros(self):
        self.lbValorDe.clear()
        self.lbValorPara.clear()
        self.carregaTabela()
        self.filtros.clear()

