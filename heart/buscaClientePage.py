from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from typing import List

from Daos.daoCliente import DaoCliente
from Design.pyUi.buscaCliente import Ui_mwBuscaCliente
from Design.pyUi.efeitos import Efeitos
from util.helpers import mascaraTelCel, mascaraNit
from modelos.clienteORM import Cliente
from modelos.telefonesORM import Telefones


class BuscaClientePage(QMainWindow, Ui_mwBuscaCliente):

    def __init__(self, parent=None):
        super(BuscaClientePage, self).__init__(parent=parent)
        self.setupUi(self)

        # self.db = db
        self.parent = parent

        # self.daoCliente = DaoCliente(db=db)
        self.clientes: list = None
        self.clienteSelecionadoId = 0
        self.efeito = Efeitos()

        self.tblListaClientes.clicked.connect(self.carregaInfoClienteNaTela)
        self.tblListaClientes.doubleClicked.connect(self.enviaCliente)
        self.pbLimpa.clicked.connect(self.limpaTudo)
        self.pbSeleciona.clicked.connect(self.enviaCliente)
        self.pbCancela.clicked.connect(self.close)

        self.atualizaTabelaClientes()

    def atualizaTabelaClientes(self, clientes: list = None):

        if clientes is None:
            # clientes = [ClienteModelo().fromList(cliente, retornaInst=True) for cliente in self.daoCliente.buscaTodos()]
            listaClientes: List[Cliente] = Cliente.select()

            for cliente in listaClientes:
                # cliente.telefoneId = Telefones.get(Telefones.clienteId == cliente.clienteId)
                try:
                    cliente.telefoneId = Telefones.get(Telefones.clienteId == cliente.clienteId)
                except Telefones.DoesNotExist:
                    cliente.telefoneId = Telefones()

            self.clientes = listaClientes
        else:
            return False

        self.tblListaClientes.setRowCount(0)

        for linha, cliente in enumerate(listaClientes):
            self.tblListaClientes.insertRow(linha)

            cdClienteItem = QTableWidgetItem(str(cliente.clienteId))
            cdClienteItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            cdClienteItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblListaClientes.setItem(linha, 0, cdClienteItem)

            nomeCompletoItem = QTableWidgetItem(f"{cliente.nomeCliente} {cliente.sobrenomeCliente}")
            nomeCompletoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblListaClientes.setItem(linha, 1, nomeCompletoItem)

            if cliente.cidade is None or cliente.cidade == 'None':
                cidadeItem = QTableWidgetItem('')
            else:
                cidadeItem = QTableWidgetItem(str(cliente.cidade))
            cidadeItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblListaClientes.setItem(linha, 2, cidadeItem)

            if cliente.telefoneId is None:
                telefoneItem = QTableWidgetItem('')
            else:
                telefoneItem = QTableWidgetItem(mascaraTelCel(cliente.telefoneId.numero))
            telefoneItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblListaClientes.setItem(linha, 3, telefoneItem)

        self.tblListaClientes.resizeColumnsToContents()

    def enviaCliente(self):
        clienteSelecionado: Cliente = None

        if self.clienteSelecionadoId != 0:
            if self.lbCdCliente.text() == '':
                self.parent.cliente = None
            else:
                for cliente in self.clientes:
                    if cliente.clienteId == int(self.lbCdCliente.text()):
                        clienteSelecionado = cliente
                        break
                self.parent.cliente = clienteSelecionado

            self.parent.carregarInfoCliente(clientId=clienteSelecionado.clienteId)
            self.close()

    def carregaInfoClienteNaTela(self, *args):
        clienteId = int(self.tblListaClientes.item(args[0].row(), 0).text())
        clienteSelecionado = Cliente()

        for cliente in self.clientes:
            if cliente.clienteId == clienteId:
                clienteSelecionado = cliente
                self.clienteSelecionadoId = clienteSelecionado.clienteId
                break

        self.lbTel.setText(mascaraTelCel(clienteSelecionado.telefoneId.numero))
        self.lbCdCliente.setText(str(clienteSelecionado.clienteId))
        self.lbNit.setText(mascaraNit(int(clienteSelecionado.nit)))
        self.lbIdade.setText(str(clienteSelecionado.idade))
        self.lbEmail.setText(clienteSelecionado.email)
        self.lbNomeCompleto.setText(f"{clienteSelecionado.nomeCliente} {clienteSelecionado.sobrenomeCliente}")

    def limpaTudo(self):
        self.clienteSelecionadoId = 0
        
        self.lbNomeCompleto.clear()
        self.lbTel.clear()
        self.lbNit.clear()
        self.lbEmail.clear()
        self.lbCdCliente.clear()
        self.lbIdade.clear()

        self.leBuscaNome.clear()
        self.leBuscaRgcpf.clear()
        self.leBuscaEmail.clear()
        self.leBuscaTelefone.clear()