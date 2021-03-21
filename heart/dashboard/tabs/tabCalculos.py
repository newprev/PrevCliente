from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Daos.daoCalculos import DaoCalculos
from Daos.daoCliente import DaoCliente
from Telas.tabCalculos import Ui_wdgTabCalculos
from helpers import mascaraDataPequena, mascaraDinheiro, mascaraCPF
from modelos.clienteModelo import ClienteModelo


class TabCalculos(QWidget, Ui_wdgTabCalculos):

    def __init__(self, parent=None, db=None):
        super(TabCalculos, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        self.cliente = ClienteModelo()
        self.daoCalculos = DaoCalculos(db=db)
        self.daoCliente = DaoCliente(db=db)

        self.tblCalculos.hideColumn(0)
        self.pbBuscarCliente.clicked.connect(lambda: self.carregarInfoCliente())

        self.tblCalculos.resizeColumnsToContents()

    def carregarTabela(self, clienteId: int):
        dados = self.daoCalculos.getRemECon(clienteId)

        self.tblCalculos.setRowCount(0)

        for contLinha, infoLinha in enumerate(dados):
            self.tblCalculos.insertRow(contLinha)

            for contColuna, info in enumerate(infoLinha):
                if contColuna == 0:
                    strItem = QTableWidgetItem(str(info))
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 1:
                    strItem = QTableWidgetItem(str(info))
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 2:
                    strItem = QTableWidgetItem(mascaraDataPequena(info))
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 3:
                    strItem = QTableWidgetItem(mascaraDinheiro(info))
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 4:
                    strItem = QTableWidgetItem(info)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 5:
                    strItem = QTableWidgetItem(info)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

    def carregarInfoCliente(self, clientId: int = 3):
        self.carregarTabela(clientId)
        self.cliente.fromList(self.daoCliente.buscaClienteById(clientId)[0])
        self.lbInfoNome.setText(self.cliente.nomeCliente + ' ' + self.cliente.sobrenomeCliente)
        self.lbInfoDocumento.setText(mascaraCPF(self.cliente.cpfCliente))