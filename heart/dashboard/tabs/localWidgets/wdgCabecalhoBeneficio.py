import datetime

from PyQt5.QtWidgets import QWidget, QMessageBox
from Telas.wdgCabecalhoBeneficio import Ui_wdgCabecalhoBeneficio
from helpers import strToDate, situacaoBeneficio, dictEspecies

from modelos.cabecalhoORM import CnisCabecalhos


class WdgBeneficio(QWidget, Ui_wdgCabecalhoBeneficio):

    def __init__(self, cabecalho: CnisCabecalhos, parent=None):
        super(WdgBeneficio, self).__init__(parent=parent)
        self.setupUi(self)
        self.cabecalho = cabecalho

        self.pbCancelar.clicked.connect(lambda: self.close())
        self.carregaCampos()
        self.pbCancelar.clicked.connect(lambda: self.close())
        self.pbConfirmar.clicked.connect(lambda: self.popUpSimCancela('Você deseja salvar suas alterações?', funcao=self.salvaAlteracoesESai))
        self.leNb.textChanged.connect(lambda: self.getInfo('leNb'))

    def carregaCampos(self):
        self.cbxSituacao.addItems([''] + situacaoBeneficio)
        self.cbxNomeBeneficio.addItems(sorted(dictEspecies.values()))

        if self.cabecalho.especie is not None and self.cabecalho.especie != '':
            index = str(int(self.cabecalho.especie[:3]))
            self.cbxNomeBeneficio.setCurrentText(dictEspecies[index])

        if self.cabecalho.situacao is not None and self.cabecalho.situacao != '':
            self.cbxSituacao.setCurrentText(self.cabecalho.situacao.title())

        if self.cabecalho.dataInicio is None or self.cabecalho.dataInicio == '':
            self.dtDataInicio.setDate(datetime.datetime.min)
        else:
            self.dtDataInicio.setDate(strToDate(self.cabecalho.dataInicio))

        if self.cabecalho.dataFim is None or self.cabecalho.dataFim == '':
            self.dtDataFim.setDate(datetime.datetime.min)
        else:
            self.dtDataFim.setDate(strToDate(self.cabecalho.dataFim))

    def getInfo(self, dado: str):
        if dado == 'leNb':
            self.cabecalho.nb = self.leNb.text()

    def salvaAlteracoesESai(self):
        self.cabecalho.save()
        self.close()

    def popUpSimCancela(self, mensagem, titulo: str = 'Atenção!', funcao=None):
        pop = QMessageBox()
        pop.setWindowTitle(titulo)
        pop.setText(mensagem)
        pop.setIcon(QMessageBox.Warning)
        pop.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        pop.setDefaultButton(QMessageBox.Cancel)

        x = pop.exec_()
        if x == QMessageBox.Yes:
            funcao()
        elif x == QMessageBox.Cancel:
            return False
        else:
            raise Warning(f'Ocorreu um erro inesperado')


