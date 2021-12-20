from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QTableWidgetItem

from Design.pyUi.newListaClientes import Ui_wdgListaClientes
from modelos.clienteORM import Cliente
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from util.helpers import mascaraTelCel, strTipoBeneficio


class NewListaClientes(QFrame, Ui_wdgListaClientes):

    def __init__(self, parent=None):
        super(NewListaClientes, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent

        self.tblClientes.hideColumn(0)

        self.atualizaTblClientes()

    def atualizaTblClientes(self, clientes: list = None):
        if clientes is None:
            clientesModels: list = Cliente.select().order_by(Cliente.nomeCliente)
        else:
            clientesModels = []

        self.tblClientes.setRowCount(0)
        for numLinha, cliente in enumerate(clientesModels):
            self.tblClientes.insertRow(numLinha)
            processo: Processos = Processos.get_or_none(Processos.clienteId == cliente.clienteId)
            telefone: Telefones = Telefones.get_or_none(Telefones.clienteId == cliente.clienteId)

            if processo is None:
                processo = Processos()
            if telefone is None:
                telefone = Telefones()

            cdClienteItem = QTableWidgetItem(str(cliente.clienteId))
            cdClienteItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 0, cdClienteItem)

            nomeCompletoItem = QTableWidgetItem(f"{cliente.nomeCliente} {cliente.sobrenomeCliente}")
            nomeCompletoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 1, nomeCompletoItem)

            if cliente.email is None:
                emailItem = QTableWidgetItem('')
            else:
                emailItem = QTableWidgetItem(f"{cliente.email}")
            emailItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 2, emailItem)

            telefoneItem = QTableWidgetItem(f"{mascaraTelCel(telefone.numero)}")
            telefoneItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 3, telefoneItem)

            if cliente.cidade is None:
                cidadeItem = QTableWidgetItem('')
            else:
                cidadeItem = QTableWidgetItem(f"{cliente.cidade}")
            cidadeItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 4, cidadeItem)

            tipoProcessoItem = QTableWidgetItem(strTipoBeneficio(processo.tipoBeneficio, processo.subTipoApos))
            tipoProcessoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 5, tipoProcessoItem)

        self.tblClientes.resizeColumnsToContents()


if __name__ == '__main__':
    from PyQt5 import QtWidgets, QtGui
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = NewListaClientes()
    w.show()
    sys.exit(app.exec_())