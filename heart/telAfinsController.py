from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from Telas.tabTelAfins import Ui_wdgTelAfins

from modelos.clienteModelo import ClienteModelo
from helpers import getTipoTelefone, getPessoalRecado, mascaraTelCel, getTipoTelefoneBySigla, getPessoalRecadoBySigla
from Daos.daoTelAfins import DaoTelAfins
from modelos.telefoneModelo import TelefoneModelo
from heart.localStyleSheet.teleAfins import desabilita


class TelAfinsController(QMainWindow, Ui_wdgTelAfins):

    def __init__(self, cliente: ClienteModelo, db=None, parent=None):
        super(TelAfinsController, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.daoTelAfins = DaoTelAfins(db=db)
        self.clienteAtivo = cliente
        self.telefoneAtual = TelefoneModelo()

        self.editando = False

        self.pbInserir.clicked.connect(self.iniciandoInsercao)
        self.pbConfirmar.clicked.connect(self.insereNovoTelefone)
        self.pbCancelar.clicked.connect(self.limpaTudo)
        self.pbEditar.clicked.connect(self.editarTelefone)
        self.pbExcluir.clicked.connect(self.excluirTelefone)
        self.tblTelefones.itemClicked.connect(lambda: self.habilitaEdicao(True, apenasEditar=True))

        self.tblTelefones.hideColumn(0)

        self.leNumero.setReadOnly(True)
        self.leNumero.textChanged.connect(lambda: self.getInfo("leNumero"))
        self.cbxPouR.editTextChanged.connect(lambda: self.getInfo("cbxPouR"))
        self.cbxTipoTel.editTextChanged.connect(lambda: self.getInfo("cbxTipoTel"))

        self.carregaInfoCliente()
        self.carregaCombos()
        self.atualizaTabela()
        self.tblTelefones.doubleClicked.connect(self.pegaLinhaSelecionada)
        self.habilitaEdicao(False)

    def avaliaInsercao(self) -> bool:
        if self.leNumero.text() != '':
            self.telefoneAtual.clienteId = self.clienteAtivo.clienteId
            if self.telefoneAtual.pessoalRecado not in getPessoalRecado().keys():
                self.telefoneAtual.pessoalRecado = getPessoalRecado()[self.cbxPouR.currentText()]
            if self.telefoneAtual.tipoTelefone not in getTipoTelefone().keys():
                self.telefoneAtual.tipoTelefone = getTipoTelefone()[self.cbxTipoTel.currentText()]
            return True
        else:
            self.showPopupAlerta("Para inserir um novo telefone, é preciso preencher o campo 'Número'.")
            self.leNumero.setFocus()
            return False

    def insereNovoTelefone(self):
        if self.avaliaInsercao():
            self.daoTelAfins.inserirAtualizaTelefone(self.telefoneAtual)
            self.atualizaTabela()
            self.habilitaEdicao(False)
        else:
            return False

    def carregaCombos(self):
        self.cbxTipoTel.addItems(getTipoTelefone().keys())
        self.cbxPouR.addItems(getPessoalRecado().keys())

    def carregaInfoCliente(self):
        self.lbNome.setText(f"{self.clienteAtivo.nomeCliente} {self.clienteAtivo.sobrenomeCliente}")
        self.lbDocumento.setText(f"{self.clienteAtivo.clienteId}")

    def editarTelefone(self):
        linha: int = self.tblTelefones.selectedIndexes()[0]
        self.pegaLinhaSelecionada(linha)

    def excluirTelefone(self):
        self.popUpSimCancela(f"Você deseja excluir permanentemente o telefone selecionado? \n{self.telefoneAtual.numero}", funcao=self.confirmaExclusao)

    def confirmaExclusao(self):
        self.daoTelAfins.excluirTelefone(self.telefoneAtual)
        self.habilitaEdicao(False)
        self.atualizaTabela()

    def getInfo(self, strInfo: str):

        if strInfo == "leNumero":
            self.telefoneAtual.numero = self.leNumero.text()

        elif strInfo == "cbxPouR":
            pessoalRecado = getPessoalRecado()[self.cbxPouR.currentText()]
            self.telefoneAtual.pessoalRecado = pessoalRecado

        elif strInfo == "cbxTipoTel":
            tipoTel = getTipoTelefone()[self.cbxTipoTel.currentText()]
            self.telefoneAtual.tipoTelefone = tipoTel

    def limpaTudo(self):

        self.leNumero.clear()
        self.habilitaEdicao(False)

    def iniciandoInsercao(self):
        self.telefoneAtual = TelefoneModelo()
        self.habilitaEdicao(True)
        self.leNumero.setFocus()

    def limpaCombos(self):
        self.cbxPouR.clear()
        self.cbxTipoTel.clear()

    def atualizaTabela(self):
        if self.clienteAtivo.clienteId not in [None, 'None']:
            listaTelefones = self.daoTelAfins.telByClienteId(self.clienteAtivo.clienteId)

            self.tblTelefones.setRowCount(0)
            for numLinha, telefone in enumerate(listaTelefones):
                self.tblTelefones.insertRow(numLinha)

                telefoneId = QTableWidgetItem(str(telefone.telefoneId))
                telefoneId.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                self.tblTelefones.setItem(numLinha, 0, telefoneId)

                telefoneNumero = QTableWidgetItem(mascaraTelCel(telefone.numero))
                telefoneNumero.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                self.tblTelefones.setItem(numLinha, 1, telefoneNumero)

                telefoneTipo = QTableWidgetItem(getTipoTelefoneBySigla(telefone.tipoTelefone))
                telefoneTipo.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                self.tblTelefones.setItem(numLinha, 2, telefoneTipo)

                telefonePessoaRecado = QTableWidgetItem(getPessoalRecadoBySigla(telefone.pessoalRecado))
                telefonePessoaRecado.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                self.tblTelefones.setItem(numLinha, 3, telefonePessoaRecado)

            self.tblTelefones.resizeColumnsToContents()

    def pegaLinhaSelecionada(self, *args):
        self.habilitaEdicao(True)
        numLinha: int = args[0].row()
        self.telefoneAtual.telefoneId = int(self.tblTelefones.item(numLinha, 0).text())
        self.telefoneAtual.numero = self.tblTelefones.item(numLinha, 1).text()
        if self.tblTelefones.item(numLinha, 2).text() != '':
            self.telefoneAtual.tipoTelefone = getTipoTelefone()[self.tblTelefones.item(numLinha, 2).text()]
        if self.tblTelefones.item(numLinha, 3).text() != '':
            self.telefoneAtual.pessoalRecado = getPessoalRecado()[self.tblTelefones.item(numLinha, 3).text()]

        self.leNumero.setText(self.telefoneAtual.numero)
        self.cbxTipoTel.setCurrentText(self.tblTelefones.item(numLinha, 2).text())
        self.cbxPouR.setCurrentText(self.tblTelefones.item(numLinha, 3).text())

    def habilitaEdicao(self, valor: bool, apenasEditar: bool = False):
        self.editando = valor

        if not apenasEditar:

            if valor:
                self.pbCancelar.setStyleSheet(desabilita("pbCancelar", False))
                self.pbCancelar.setDisabled(False)

                self.pbEditar.setStyleSheet(desabilita("pbEditar", False))
                self.pbEditar.setDisabled(False)

                self.pbExcluir.setStyleSheet(desabilita("pbExcluir", False))
                self.pbExcluir.setDisabled(False)

                self.pbInserir.setStyleSheet(desabilita("pbInserir", True))
                self.pbInserir.setDisabled(True)

                self.pbConfirmar.setStyleSheet(desabilita("pbConfirmar", False))
                self.pbConfirmar.setDisabled(False)

                self.carregaCombos()
                self.leNumero.setDisabled(False)
                self.leNumero.setReadOnly(False)

            else:
                self.tblTelefones.clearSelection()

                self.pbCancelar.setStyleSheet(desabilita("pbCancelar", True))
                self.pbCancelar.setDisabled(True)

                self.pbEditar.setStyleSheet(desabilita("pbEditar", True))
                self.pbEditar.setDisabled(True)

                self.pbExcluir.setStyleSheet(desabilita("pbExcluir", True))
                self.pbExcluir.setDisabled(True)

                self.pbInserir.setStyleSheet(desabilita("pbInserir", False))
                self.pbInserir.setDisabled(False)

                self.pbConfirmar.setStyleSheet(desabilita("pbConfirmar", True))
                self.pbConfirmar.setDisabled(True)

                self.limpaCombos()
                self.leNumero.setDisabled(True)
                self.leNumero.setReadOnly(True)
        else:
            self.pbEditar.setStyleSheet(desabilita("pbEditar", False))
            self.pbEditar.setDisabled(False)

            self.pbCancelar.setStyleSheet(desabilita("pbCancelar", False))
            self.pbCancelar.setDisabled(False)

    def showPopupAlerta(self, mensagem, titulo='Atenção!'):
        dialogPopup = QMessageBox()
        dialogPopup.setWindowTitle(titulo)
        dialogPopup.setText(mensagem)
        dialogPopup.setIcon(QMessageBox.Warning)
        dialogPopup.setStandardButtons(QMessageBox.Ok)

        close = dialogPopup.exec_()

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
