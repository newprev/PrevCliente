from PyQt5.QtWidgets import QWidget, QMessageBox
from Telas.itemResumoCNIS import Ui_WdgItemRes
from util.helpers import dataUSAtoBR, mascaraCNPJ, mascaraNB

from heart.dashboard.tabs.localWidgets.wdgCabecalhoBeneficio import WdgBeneficio
from heart.dashboard.tabs.localWidgets.wdgCabecalhoContribuicao import WdgContribuicao
from modelos.cabecalhoORM import CnisCabecalhos
from heart.dashboard.tabs.localStyleSheet.iconesResumo import iconeItem
from util.enums.newPrevEnums import TipoIcone


class ItemResumoCnis(QWidget, Ui_WdgItemRes):

    def __init__(self, cabecalho: CnisCabecalhos, parent=None):
        super(ItemResumoCnis, self).__init__(parent=parent)
        self.setupUi(self)
        self.frDadoFaltante.hide()
        self.tabCalculo = parent

        self.cabecalho = cabecalho

        self.pbEditar.clicked.connect(self.abrirEditarCabecalho)
        self.pbRemover.clicked.connect(lambda: self.popUpSimCancela(f'Você deseja excluir as contribuições da empresa\n {self.cabecalho.nomeEmp}?'))

        self.carregaInformacoes()
        self.avaliaDadoFaltante()

    def carregaInformacoes(self):
        if self.cabecalho is not None:
            if self.cabecalho.orgVinculo is not None and self.cabecalho.nb is not None:
                # self.lbCdEmp.setText(f"Benefício: {self.cabecalho.nb}")
                self.lbCNPJouNB.setText(mascaraNB(self.cabecalho.nb))
                self.lbCdEmp.setText(self.cabecalho.especie[5:])
                self.frIcone.setStyleSheet(iconeItem(TipoIcone.beneficio))
                self.lbSituacao.setText(self.cabecalho.situacao)

            elif self.cabecalho.nomeEmp == 'RECOLHIMENTO':
                self.lbCdEmp.setText(self.cabecalho.tipoVinculo)
                self.lbCNPJouNB.setText(self.cabecalho.nb)
                self.lbSituacao.hide()
                self.lbInfoSituacao.hide()
            else:
                self.lbCdEmp.setText(self.cabecalho.nomeEmp)
                self.lbCNPJouNB.setText(mascaraCNPJ(self.cabecalho.cdEmp))
                self.lbSituacao.hide()
                self.lbInfoSituacao.hide()

            self.lbDataInicio.setText(dataUSAtoBR(self.cabecalho.dataInicio, comDias=True))
            self.lbDataFim.setText(dataUSAtoBR(self.cabecalho.dataFim, comDias=True))

    def abrirEditarCabecalho(self):
        if self.cabecalho.nb is not None:
            wdgBenef = WdgBeneficio(self.cabecalho, parent=self)
            wdgBenef.show()
        else:
            wdgContrib = WdgContribuicao(self.cabecalho, parent=self)
            wdgContrib.show()

    def avaliaDadoFaltante(self):
        possuiDadoFaltante: bool = False
        msgDadoFaltante: str = 'É necessário inserir as informações abaixo:'

        if self.cabecalho.dataFim is None or self.cabecalho.dataFim == '':
            possuiDadoFaltante = True
            msgDadoFaltante += '\n - Data fim;'
        if self.cabecalho.dataInicio is None or self.cabecalho.dataInicio == '':
            possuiDadoFaltante = True
            msgDadoFaltante += '\n - Data início;'

        if possuiDadoFaltante:
            self.frDadoFaltante.show()
            self.frDadoFaltante.setToolTip(msgDadoFaltante)

        if self.cabecalho.dadoFaltante != possuiDadoFaltante:
            self.cabecalho.dadoFaltante = possuiDadoFaltante
            self.cabecalho.save()

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

