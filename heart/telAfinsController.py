from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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
        self.pbCancelar.clicked.connect(self.limpaTudo)

        self.tblTelefones.hideColumn(0)

        self.leNumero.setReadOnly(True)

        self.carregaCombos()
        self.atualizaTabela()
        self.tblTelefones.doubleClicked.connect(self.pegaLinhaSelecionada)
        self.habilitaEdicao(False)

    def carregaCombos(self):
        self.cbxTipoTel.addItems(getTipoTelefone().keys())
        self.cbxPouR.addItems(getPessoalRecado().keys())

    def limpaTudo(self):

        self.leNumero.clear()
        self.habilitaEdicao(False)

    def iniciandoInsercao(self):
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
        self.telefoneAtual.tipoTelefone = getTipoTelefone()[self.tblTelefones.item(numLinha, 2).text()]
        self.telefoneAtual.pessoalRecado = getPessoalRecado()[self.tblTelefones.item(numLinha, 3).text()]

        self.leNumero.setText(self.telefoneAtual.numero)
        self.cbxTipoTel.setCurrentText(self.tblTelefones.item(numLinha, 2).text())
        self.cbxPouR.setCurrentText(self.tblTelefones.item(numLinha, 3).text())

    def habilitaEdicao(self, valor: bool):
        self.editando = valor

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
