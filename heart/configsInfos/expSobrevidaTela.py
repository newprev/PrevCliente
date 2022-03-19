from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from typing import List

from Design.pyUi.pgExpSobrevida import Ui_mwExpSobrevida
from modelos.expSobrevidaORM import ExpSobrevida
from util.helpers.dateHelper import mascaraDataPequena, strToDate


class ExpSobrevidaTela(QMainWindow, Ui_mwExpSobrevida):
    filtros: dict = {}

    def __init__(self, parent=None):
        super(ExpSobrevidaTela, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle('Experiência de sobrevida - [expSobrevidaTela]')

        self.tblInfo.hideColumn(0)
        self.rbAmbos.setChecked(True)

        self.desativarFiltros(True)

        self.carregaTabela()
        self.dtDeDataRef.dateChanged.connect(lambda: self.editandoFiltro('dtDeDataRef'))
        self.dtAteDataRef.dateChanged.connect(lambda: self.editandoFiltro('dtAteDataRef'))
        self.sbDeExp.textChanged.connect(lambda: self.editandoFiltro('sbDeExp'))
        self.sbAteExp.textChanged.connect(lambda: self.editandoFiltro('sbAteExp'))
        self.sbDe.valueChanged.connect(lambda: self.editandoFiltro('sbDe'))
        self.sbPara.valueChanged.connect(lambda: self.editandoFiltro('sbPara'))

    def avaliaFiltros(self):
        for linha in range(self.tblInfo.rowCount()):
            self.tblInfo.showRow(linha)

        for chave, valor in self.filtros.items():
            for linha in range(self.tblInfo.rowCount()):
                ano = strToDate(self.tblInfo.item(linha, 1).text())
                idade = int(self.tblInfo.item(linha, 2).text())
                expSobrevida = int(self.tblInfo.item(linha, 3).text())
                genero = self.tblInfo.item(linha, 4).text()[0].upper()

                if self.rbFeminino.isChecked() and genero == 'M' or self.rbMasculino.isChecked() and genero == 'F':
                    self.tblInfo.hideRow(linha)

                if chave == 'dtDeDataRef' and valor:
                    if (ano - valor).days < 0:
                        self.tblInfo.hideRow(linha)

                elif chave == 'dtAteDataRef' and valor:
                    if (valor - ano).days < 0:
                        self.tblInfo.hideRow(linha)

                elif chave == 'sbDe' and valor:
                    if idade < valor:
                        self.tblInfo.hideRow(linha)

                elif chave == 'sbPara' and valor:
                    if idade > valor:
                        self.tblInfo.hideRow(linha)

                elif chave == 'sbDeExp' and valor:
                    if expSobrevida < valor:
                        self.tblInfo.hideRow(linha)

                elif chave == 'sbAteExp' and valor:
                    if expSobrevida > valor:
                        self.tblInfo.hideRow(linha)

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

        self.tblInfo.resizeColumnToContents(3)
        self.tblInfo.resizeRowsToContents()

    def desativarFiltros(self, valor: bool):
        if valor:
            self.frDtReferente.hide()
            self.frIdade.hide()
            self.frGenero.hide()
            self.frExpectativa.hide()
        else:
            self.frDtReferente.show()
            self.frIdade.show()
            self.frGenero.show()
            self.frExpectativa.show()

    def editandoFiltro(self, info: str):
        if info == 'dtDeDataRef':
            self.filtros['dtDeDataRef'] = self.dtDeDataRef.date().toPyDate()
        elif info == 'dtAteDataRef':
            self.filtros['dtAteDataRef'] = self.dtAteDataRef.date().toPyDate()
        elif info == 'sbDeExp':
            self.filtros['sbDeExp'] = self.sbDeExp.value()
        elif info == 'sbAteExp':
            self.filtros['sbAteExp'] = self.sbAteExp.value()
        elif info == 'sbDe':
            self.filtros['sbDe'] = self.sbDe.value()
        elif info == 'sbPara':
            self.filtros['sbPara'] = self.sbPara.value()

    def limpaFiltros(self):
        self.filtros.clear()
        self.sbDeExp.setValue(0)
        self.sbAteExp.setValue(0)
        self.sbDe.setValue(0)
        self.sbPara.setValue(0)
        self.rbAmbos.setChecked(True)
