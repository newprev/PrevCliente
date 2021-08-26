import datetime
from PyQt5.QtWidgets import QWidget, QMessageBox

from Telas.wdgCabecalhoContribuicao import Ui_wdgCabecalhoContribuicao
from util.helpers import strToDate, unmaskAll
from heart.sinaisCustomizados import Sinais

from modelos.cabecalhoORM import CnisCabecalhos


class WdgContribuicao(QWidget, Ui_wdgCabecalhoContribuicao):

    def __init__(self, cabecalho: CnisCabecalhos, parent=None):
        super(WdgContribuicao, self).__init__(parent=parent)
        self.setupUi(self)
        self.cabecalho = cabecalho
        self.itemResumo = parent
        self.tabCalculo = parent.parent()
        self.parent = parent

        self.sinais = Sinais()
        self.sinais.sAtualizaCabecalho.connect(self.enviaAtualizaCabecalho)

        self.carregaCampos()
        self.pbCancelar.clicked.connect(lambda: self.close())
        self.pbConfirmar.clicked.connect(lambda: self.popUpSimCancela('Você deseja salvar suas alterações?', funcao=self.salvaAlteracoesESai))

        self.dtDataInicio.dateChanged.connect(lambda: self.getInfo('dtDataInicio'))
        self.dtDataFim.dateChanged.connect(lambda: self.getInfo('dtDataFim'))
        self.leNomeEmp.textChanged.connect(lambda: self.getInfo('leNomeEmp'))
        self.leCNPJ.textChanged.connect(lambda: self.getInfo('leCNPJ'))

        self.ajustandoTamanho()

    def carregaCampos(self):
        self.leCNPJ.setText(self.cabecalho.cdEmp)
        self.leNomeEmp.setText(self.cabecalho.nomeEmp)

        if self.cabecalho.dataInicio is None or self.cabecalho.dataInicio == '':
            self.dtDataInicio.setDate(datetime.datetime.min)
        else:
            self.dtDataInicio.setDate(strToDate(self.cabecalho.dataInicio))

        if self.cabecalho.dataFim is None or self.cabecalho.dataFim == '':
            self.dtDataFim.setDate(datetime.datetime.min)
        else:
            self.dtDataFim.setDate(strToDate(self.cabecalho.dataFim))

    def getInfo(self, dado: str):
        if dado == 'leNomeEmp':
            self.cabecalho.nomeEmp = self.leNomeEmp.text()

        elif dado == 'leCNPJ':
            self.cabecalho.cdEmp = unmaskAll(self.leCNPJ.text())

        elif dado == 'dtDataInicio':
            self.cabecalho.dataInicio = self.dtDataInicio.date().toPyDate()

        elif dado == 'dtDataFim':
            self.cabecalho.dataFim = self.dtDataFim.date().toPyDate()

    def salvaAlteracoesESai(self):
        self.cabecalho.save()
        self.sinais.sAtualizaCabecalho.emit()
        self.close()

    def enviaAtualizaCabecalho(self):
        self.itemResumo.carregaInformacoes()

    def ajustandoTamanho(self):
        parentWidth = self.parent.size().width()
        parentHeight = self.parent.size().height()

        self.resize(parentWidth, parentHeight)
        self.frMain.resize(parentWidth, parentHeight)

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
