from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Daos.daoCalculos import DaoCalculos
from Daos.daoCliente import DaoCliente
from Telas.tabCalculos import Ui_wdgTabCalculos
from heart.buscaClientePage import BuscaClientePage
from heart.insereContribuicaoPage import InsereContribuicaoPage
from helpers import mascaraDataPequena, mascaraDinheiro, mascaraCPF, strToDatetime
from modelos.clienteModelo import ClienteModelo
from newPrevEnums import TamanhoData


class TabCalculos(QWidget, Ui_wdgTabCalculos):

    def __init__(self, parent=None, db=None):
        super(TabCalculos, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        self.cliente = ClienteModelo()
        self.daoCalculos = DaoCalculos(db=db)
        self.daoCliente = DaoCliente(db=db)

        self.buscaClientePage = None
        self.inserirContribuicao = None

        self.tblCalculos.hideColumn(0)
        self.pbBuscarCliente.clicked.connect(self.abreBuscaClientePage)
        self.pbInserir.clicked.connect(self.abreInsereContribuicoes)

        self.tblCalculos.resizeColumnsToContents()

    def carregarTabela(self, clienteId: int):
        dados = self.daoCalculos.getRemECon(clienteId)

        self.tblCalculos.setRowCount(0)

        for contLinha, infoLinha in enumerate(dados):
            self.tblCalculos.insertRow(contLinha)
            if contLinha == 1:
                print(infoLinha)

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
                    strItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 3:
                    strItem = QTableWidgetItem(mascaraDinheiro(info, simbolo=infoLinha[-1]))
                    strItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 4:
                    strItem = QTableWidgetItem(info)
                    strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                elif contColuna == 5:
                    if ',' in info:
                        indicadores = info.split(', ')
                        strIndicadores = ''
                        for indicador in indicadores:
                            strIndicadores += '- ' + indicador + '\n'
                    elif info != '':
                        strIndicadores = '- ' + info
                    else:
                        strIndicadores = info
                    strItem = QTableWidgetItem(strIndicadores)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)


        self.tblCalculos.resizeColumnsToContents()
        self.tblCalculos.resizeRowsToContents()

    def carregarInfoCliente(self, clientId: int = 1):
        self.carregarTabela(clientId)
        self.cliente.fromList(self.daoCliente.buscaClienteById(clientId)[0])
        self.lbNome.setText(self.cliente.nomeCliente + ' ' + self.cliente.sobrenomeCliente)
        self.lbDocumento.setText(mascaraCPF(self.cliente.cpfCliente))

    def abreBuscaClientePage(self):
        self.buscaClientePage = BuscaClientePage(parent=self, db=self.db)
        self.buscaClientePage.show()

    def abreInsereContribuicoes(self):
        if self.cliente.nomeCliente is not None:
            self.inserirContribuicao = InsereContribuicaoPage(parent=self, db=self.db, cliente=self.cliente)
            self.inserirContribuicao.show()
