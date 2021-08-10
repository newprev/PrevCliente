from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from typing import List

from Daos.daoCalculos import DaoCalculos
from Daos.daoCliente import DaoCliente
from Telas.tabCalculos import Ui_wdgTabCalculos
from heart.buscaClientePage import BuscaClientePage
from heart.insereContribuicaoPage import InsereContribuicaoPage

from helpers import mascaraDataPequena, mascaraDinheiro, mascaraCPF, strToDatetime, dataUSAtoBR

from modelos.clienteORM import Cliente
from modelos.beneficiosORM import CnisBeneficios
from newPrevEnums import TamanhoData, TipoContribuicao


class TabCalculos(QWidget, Ui_wdgTabCalculos):

    def __init__(self, parent=None, db=None, origemEntrevista: bool = False):
        super(TabCalculos, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        self.cliente = Cliente()
        self.daoCalculos = DaoCalculos(db=db)
        self.daoCliente = DaoCliente(db=db)

        self.buscaClientePage = None
        self.inserirContribuicao = None

        self.tblCalculos.hideColumn(0)
        self.tblBeneficios.hideColumn(0)
        self.tblCalculos.doubleClicked.connect(lambda: self.avaliaEdicao('tblCalculos'))
        self.tblBeneficios.doubleClicked.connect(lambda: self.avaliaEdicao('tblBeneficios'))

        self.pbBuscarCliente.clicked.connect(self.abreBuscaClientePage)
        self.pbBuscarClienteBen.clicked.connect(self.abreBuscaClientePage)
        self.pbEditar.clicked.connect(lambda: self.avaliaEdicao('tblCalculos'))
        self.pbEditarBen.clicked.connect(lambda: self.avaliaEdicao('tblBeneficios'))
        self.pbExcluir.clicked.connect(lambda: self.avaliaExclusao('pbExcluir'))
        self.pbExcluirBen.clicked.connect(lambda: self.avaliaExclusao('pbExcluirBen'))

        self.pbInserir.clicked.connect(self.abreInsereContribuicoes)
        self.pbInserirBen.clicked.connect(self.abreInsereContribuicoes)

        if origemEntrevista:
            self.pbBuscarClienteBen.hide()
            self.pbBuscarCliente.hide()

        self.tblCalculos.resizeColumnsToContents()

    def avaliaEdicao(self, tabela: str):
        if tabela == 'tblCalculos':
            numLinha: int = self.tblCalculos.selectedIndexes()[0].row()
            contribuicaoId = int(self.tblCalculos.item(numLinha, 0).text())
            tipoContribuicao: str = self.tblCalculos.item(numLinha, 5).text()
            if tipoContribuicao == 'Contribuição':
                self.abreInsereContribuicoes(contribuicaoId, TipoContribuicao.contribuicao)
            else:
                self.abreInsereContribuicoes(contribuicaoId, TipoContribuicao.remuneracao)

        elif tabela == 'tblBeneficios':
            numLinha: int = self.tblBeneficios.selectedIndexes()[0].row()
            contribuicaoId = int(self.tblBeneficios.item(numLinha, 0).text())
            self.abreInsereContribuicoes(contribuicaoId, TipoContribuicao.beneficio)

    def avaliaExclusao(self, tipoBotao: str):
        if tipoBotao == 'pbExcluir':
            numLinha: int = self.tblCalculos.selectedIndexes()[0].row()
            contribuicaoId = int(self.tblCalculos.item(numLinha, 0).text())
            tipoContribuicao: str = self.tblCalculos.item(numLinha, 5).text()

            if tipoContribuicao == 'Contribuição':
                self.popUpSimCancela(
                    f"Você deseja excluir a contribuição {contribuicaoId}",
                    funcao=lambda: self.excluir(TipoContribuicao.contribuicao, contribuicaoId),
                )
            else:
                self.popUpSimCancela(
                    f"Você deseja excluir a remuneração {contribuicaoId}",
                    funcao=lambda:self.excluir(TipoContribuicao.remuneracao, contribuicaoId),
                )

        elif tipoBotao == 'pbExcluirBen':
            numLinha: int = self.tblBeneficios.selectedIndexes()[0].row()
            beneficioId = int(self.tblBeneficios.item(numLinha, 0).text())
            self.popUpSimCancela(
                f"Você deseja excluir o benefício {beneficioId}",
                funcao=lambda: self.excluir(TipoContribuicao.beneficio, beneficioId),
            )

    def excluir(self, tipo: TipoContribuicao, contribuicaoId: int):
        if tipo == TipoContribuicao.contribuicao:
            self.daoCalculos.delete(tipo, contribuicaoId)
        elif tipo == TipoContribuicao.remuneracao:
            self.daoCalculos.delete(tipo, contribuicaoId)
        elif tipo == TipoContribuicao.beneficio:
            self.daoCalculos.delete(tipo, contribuicaoId)

        self.carregarTblContribuicoes(self.cliente.clienteId)
        self.carregarTblBeneficios(self.cliente.clienteId)

    def carregarTblContribuicoes(self, clienteId: int):
        dados = self.daoCalculos.getRemECon(clienteId)

        self.tblCalculos.setRowCount(0)

        for contLinha, infoLinha in enumerate(dados):
            self.tblCalculos.insertRow(contLinha)

            for contColuna, info in enumerate(infoLinha):

                # RemuneracaoId/ContribuiçãoId - Coluna 0 (escondida)
                if contColuna == 0:
                    strItem = QTableWidgetItem(str(info))
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                # Seq - Coluna 1 (ativa)
                elif contColuna == 1:
                    strItem = QTableWidgetItem(str(info))
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                # Competência - Coluna 2 (ativa)
                elif contColuna == 2:
                    strItem = QTableWidgetItem(dataUSAtoBR(info))
                    strItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                # Salário de contribuição - Coluna 3 (escondida)
                elif contColuna == 3:
                    strItem = QTableWidgetItem(mascaraDinheiro(info, simbolo=infoLinha[6]))
                    strItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna, strItem)

                # Natureza dos dados (Remuneração/Contribuição) - Coluna 4 (ativa)
                elif contColuna == 4:
                    strItem = QTableWidgetItem(info)
                    strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, contColuna+1, strItem)

                # Natureza dos dados (Remuneração/Contribuição) - Coluna 6 (ativa)
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

                    if strIndicadores.endswith('\n'):
                        strIndicadores = strIndicadores[:len(strIndicadores)-2]

                    strItem = QTableWidgetItem(strIndicadores)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
                    self.tblCalculos.setItem(contLinha, contColuna+1, strItem)

                # Tetos previdenciários - Coluna 4 (ativa)
                elif contColuna == 10:
                    strItem = QTableWidgetItem(mascaraDinheiro(info, simbolo=infoLinha[6]))
                    strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
                    self.tblCalculos.setItem(contLinha, 4, strItem)

        self.tblCalculos.resizeColumnsToContents()
        self.tblCalculos.resizeRowsToContents()

    def carregarTblBeneficios(self, clienteId: int):

        # dados = self.daoCalculos.getBeneficiosPor(clienteId)
        dados: List[CnisBeneficios] = CnisBeneficios.select().where(CnisBeneficios.clienteId == clienteId)

        self.tblBeneficios.setRowCount(0)

        for contLinha, beneficio in enumerate(dados):
            self.tblBeneficios.insertRow(contLinha)

            # BenefícioId - Coluna 0 (escondida)
            strBeneficioId = QTableWidgetItem(str(beneficio.beneficiosId))
            strBeneficioId.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 0, strBeneficioId)

            # seq - Coluna 1 (ativa)
            strSeq = QTableWidgetItem(str(beneficio.seq))
            strSeq.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            strSeq.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 1, strSeq)

            # Nb (Número do benefício) - Coluna 2 (ativa)
            if str(beneficio.nb) == '':
                strNb = QTableWidgetItem('-')
            else:
                strNb = QTableWidgetItem(str(beneficio.nb))
            strNb.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strNb.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 2, strNb)

            # DataInício - Coluna 3 (ativa)
            strDataInicio = QTableWidgetItem(dataUSAtoBR(beneficio.dataInicio))
            strDataInicio.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strDataInicio.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 3, strDataInicio)

            # DataFim - Coluna 4 (ativa)
            strDataFim = QTableWidgetItem(dataUSAtoBR(beneficio.dataFim))
            strDataFim.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strDataFim.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 4, strDataFim)

            # Situação do benefício - Coluna 5 (ativa)
            strSituacao = QTableWidgetItem(beneficio.situacao)
            strSituacao.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strSituacao.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 5, strSituacao)

            # Dado Origem - Coluna 6 (ativa)
            strOrigem = QTableWidgetItem(beneficio.dadoOrigem)
            strOrigem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strOrigem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 6, strOrigem)

        self.tblBeneficios.resizeColumnsToContents()
        self.tblBeneficios.resizeRowsToContents()

    def carregarInfoCliente(self, clientId: int = 1, clienteModel: Cliente = None):
        if clienteModel is None:
            self.carregarTblContribuicoes(clientId)
            self.carregarTblBeneficios(clientId)
            self.cliente = Cliente.get_by_id(clientId)
            self.lbNome.setText(self.cliente.nomeCliente + ' ' + self.cliente.sobrenomeCliente)
            self.lbNomeBen.setText(self.cliente.nomeCliente + ' ' + self.cliente.sobrenomeCliente)
            self.lbDocumento.setText(mascaraCPF(self.cliente.cpfCliente))
            self.lbDocumentoBen.setText(mascaraCPF(self.cliente.cpfCliente))
        else:
            self.cliente = clienteModel
            self.carregarTblContribuicoes(clienteModel.clienteId)
            self.carregarTblBeneficios(clienteModel.clienteId)
            self.lbNome.setText(clienteModel.nomeCliente + ' ' + clienteModel.sobrenomeCliente)
            self.lbNomeBen.setText(clienteModel.nomeCliente + ' ' + clienteModel.sobrenomeCliente)
            self.lbDocumento.setText(mascaraCPF(clienteModel.cpfCliente))
            self.lbDocumentoBen.setText(mascaraCPF(clienteModel.cpfCliente))

    def abreBuscaClientePage(self):
        self.buscaClientePage = BuscaClientePage(parent=self, db=self.db)
        self.buscaClientePage.show()

    def abreInsereContribuicoes(self, contribuicaoId: int, tipo: TipoContribuicao = None):
        if self.cliente.nomeCliente is not None:
            self.inserirContribuicao = InsereContribuicaoPage(parent=self, db=self.db, cliente=self.cliente, contribuicaoId=contribuicaoId, tipo=tipo)
            self.inserirContribuicao.show()

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
