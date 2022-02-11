from PyQt5.QtWidgets import QWidget
from Design.pyUi.itemResumoCNIS import Ui_WdgItemRes
from Design.pyUi.efeitos import Efeitos

from modelos.cabecalhoORM import CnisCabecalhos
from sinaisCustomizados import Sinais
from util.dateHelper import mascaraData
from util.helpers import mascaraCNPJ


class ItemResumoCnis(QWidget, Ui_WdgItemRes):
    cabecalhoAtual: CnisCabecalhos
    selecionado: bool = False

    def __init__(self, cabecalhoCnis: CnisCabecalhos, parent=None):
        super(ItemResumoCnis, self).__init__(parent=parent)
        self.setupUi(self)
        self.resumoPage = parent

        self.cabecalhoAtual = cabecalhoCnis
        self.carregaCabecalho()
        self.sinais = Sinais()
        self.sinais.sAtualizaCabecalho.connect(self.enviaCabecalho)

        self.gbMain.toggled.connect(self.cabecalhoselecionado)

    def carregaCabecalho(self):
        # Nome da empresa ou do benefícios
        if self.cabecalhoAtual.especie is not None:
            self.lbCdEmp.setText(self.cabecalhoAtual.especie[5:])
            self.lbCNPJouNB.setText(f"Núm. Benefício: {self.cabecalhoAtual.nb}")
        else:
            self.lbCdEmp.setText(self.cabecalhoAtual.nomeEmp)
            self.lbCNPJouNB.setText("CNPJ: " + mascaraCNPJ(self.cabecalhoAtual.cdEmp))

        # Data de início
        if self.cabecalhoAtual.dataInicio is not None and len(self.cabecalhoAtual.dataInicio) > 0:
            self.lbDataInicio.setText(mascaraData(self.cabecalhoAtual.dataInicio))
        else:
            self.lbDataInicio.setText('')

        # Data de fim
        if self.cabecalhoAtual.dataFim is not None and len(self.cabecalhoAtual.dataFim) > 0:
            self.lbDataFim.setText(mascaraData(self.cabecalhoAtual.dataFim))
        else:
            self.lbDataFim.setText('')

        # Situação do benefício
        if self.cabecalhoAtual.situacao is not None and len(self.cabecalhoAtual.situacao) > 0:
            self.lbSituacao.setText(self.cabecalhoAtual.situacao)
        else:
            self.lbSituacao.setText("")
            self.lbInfoSituacao.setText("")

        # Dado faltante
        if not self.cabecalhoAtual.dadoFaltante:
            self.frDadoFaltante.hide()

    def cabecalhoselecionado(self):
        self.selecionado = self.gbMain.isChecked()

        if self.selecionado:
            Efeitos().shadowCards([self])
            self.sinais.sAtualizaCabecalho.emit()
        else:
            Efeitos().desativarSombra([self])

    def enviaCabecalho(self):
        self.resumoPage.atualizaCabecalhoSelecionado(self.cabecalhoAtual)

    def desselecionaCabecalho(self):
        Efeitos().desativarSombra([self])
        self.selecionado = False
        self.gbMain.setChecked(False)
