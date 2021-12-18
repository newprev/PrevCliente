import datetime
from peewee import SqliteDatabase

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout
from Design.pyUi.tabResumoCNIS import Ui_wdgTabResumoCNIS
from typing import List, Union, Generator

from SQLs.itensContribuicao import remuEContrib
from heart.dashboard.tabs.localStyleSheet.styleResumo import frInfoStatus
from heart.dashboard.tabs.localWidgets.itemResumoCNIS import ItemResumoCnis
from heart.buscaClientePage import BuscaClientePage
from heart.insereContribuicaoPage import InsereContribuicaoPage

from Design.pyUi.efeitos import Efeitos
from Design.DesignSystem.botoes import NewButton, NewButtonHover
from Design.CustomWidgets.newDropMenu import NewSubMenu
from Design.CustomWidgets.newTagFiltro import NewTagFiltro

from util.dateHelper import strToDate
from util.enums.logEnums import StatusInfo
from util.helpers import mascaraDinheiro, mascaraCPF, dataUSAtoBR, comparaFiltrosAny
from util.enums.newPrevEnums import TipoContribuicao, TipoFiltro
from util.enums.tabsEnums import TabsResumo
from util.layoutHelpers import limpaLayout

from modelos.clienteORM import Cliente
from modelos.cabecalhoORM import CnisCabecalhos
from modelos.itemContribuicao import ItemContribuicao
from modelos.Auxiliares.remuEContribs import RemuEContribs

from Daos.daoCalculos import DaoCalculos


class TabResumoCNIS(QWidget, Ui_wdgTabResumoCNIS):
    filtros: dict

    def __init__(self, parent=None, db=None, origemEntrevista: bool = False):
        super(TabResumoCNIS, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        self.cliente = Cliente()
        self.efeito = Efeitos()
        self.vlResumos = QVBoxLayout()
        self.daoCalculos = DaoCalculos(db=self.db)

        self.buscaClientePage = None
        self.inserirContribuicao = None

        self.iniciaLayout()

        self.tblContribuicoes.doubleClicked.connect(lambda: self.avaliaEdicao('tblContribuicoes'))
        self.tblBeneficios.doubleClicked.connect(lambda: self.avaliaEdicao('tblBeneficios'))

        self.pbBuscarCliente.clicked.connect(self.abreBuscaClientePage)
        self.pbBuscarClienteBen.clicked.connect(self.abreBuscaClientePage)
        self.pbBuscarClienteResumo.clicked.connect(self.abreBuscaClientePage)
        self.pbEditar.clicked.connect(lambda: self.avaliaEdicao('tblContribuicoes'))
        self.pbEditarBen.clicked.connect(lambda: self.avaliaEdicao('tblBeneficios'))
        self.pbExcluir.clicked.connect(lambda: self.avaliaExclusao('pbExcluir'))
        self.pbExcluirBen.clicked.connect(lambda: self.avaliaExclusao('pbExcluirBen'))
        self.pbAddFiltro.clicked.connect(self.abreMenuFiltros)
        self.pbAddFiltroBene.clicked.connect(self.abreMenuFiltros)

        self.filtros = {
            TipoFiltro.data: [None, None],
            TipoFiltro.indicador: [],
        }

        self.atualizaMenuInfo(inicio=True)

        self.tabMain.currentChanged.connect(self.limpaFiltros)

        self.pbInserir.clicked.connect(lambda: self.abreInsereContribuicoes(0, TipoContribuicao.contribuicao))
        self.pbInserirBen.clicked.connect(lambda: self.abreInsereContribuicoes(0, TipoContribuicao.beneficio))

        if origemEntrevista:
            self.pbBuscarClienteBen.hide()
            self.pbBuscarCliente.hide()

        self.tblContribuicoes.resizeColumnsToContents()

    def iniciaLayout(self):
        # Hide and show
        self.tblContribuicoes.hideColumn(0)
        self.tblBeneficios.hideColumn(0)
        self.frBordaFiltros.hide()

        self.pbBuscarCliente.setStyleSheet(NewButton.padrao.value + NewButtonHover.padrao.value)
        self.pbBuscarClienteBen.setStyleSheet(NewButton.padrao.value + NewButtonHover.padrao.value)
        self.pbBuscarClienteResumo.setStyleSheet(NewButton.padrao.value + NewButtonHover.padrao.value)

    def abreBuscaClientePage(self):
        self.buscaClientePage = BuscaClientePage(parent=self)
        self.buscaClientePage.show()

    def abreInsereContribuicoes(self, itemId: int, tipo: TipoContribuicao = None):
        if self.cliente.nomeCliente is not None:
            self.inserirContribuicao = InsereContribuicaoPage(parent=self, cliente=self.cliente, itemConrtibuicaoId=itemId, tipo=tipo)
            self.inserirContribuicao.show()

    def avaliaAtualizacaoInfoMenu(self):
        tabAtual: TabsResumo = TabsResumo(self.tabMain.currentIndex())

        if tabAtual == TabsResumo.resumos:
            contEntradas = self.vlResumos.count()
            self.atualizaMenuInfo(info=f'Quantidade de entradas no CNIS: {contEntradas}', status=StatusInfo.info)

    def avaliaEdicao(self, tabela: str):
        if tabela == 'tblContribuicoes':
            if len(self.tblContribuicoes.selectedIndexes()) <= 0:
                self.popUpOkAlerta('Nenhuma remuneração selecionada. Selecione alguma linha e tente novamente')
                return False

            numLinha: int = self.tblContribuicoes.selectedIndexes()[0].row()
            itemId = int(self.tblContribuicoes.item(numLinha, 0).text())
            tipoContribuicao: str = self.tblContribuicoes.item(numLinha, 5).text()
            if tipoContribuicao == 'Contribuição':
                self.abreInsereContribuicoes(itemId, TipoContribuicao.contribuicao)
            else:
                self.abreInsereContribuicoes(itemId, TipoContribuicao.remuneracao)

        elif tabela == 'tblBeneficios':
            if len(self.tblBeneficios.selectedIndexes()) <= 0:
                self.popUpOkAlerta('Nenhum benefício selecionado. Selecione alguma linha e tente novamente')
                return False

            print(self.tblBeneficios.selectedIndexes())
            numLinha: int = self.tblBeneficios.selectedIndexes()[0].row()
            itemId = int(self.tblBeneficios.item(numLinha, 0).text())
            print(f"itemId: {itemId}")
            self.abreInsereContribuicoes(itemId, TipoContribuicao.beneficio)

    def avaliaExclusao(self, tipoBotao: str):
        if tipoBotao == 'pbExcluir':
            numLinha: int = self.tblContribuicoes.selectedIndexes()[0].row()
            itemId = int(self.tblContribuicoes.item(numLinha, 0).text())
            tipoContribuicao: str = self.tblContribuicoes.item(numLinha, 5).text()

            if tipoContribuicao == 'Contribuição':
                self.popUpSimCancela(
                    f"Você deseja excluir a contribuição {itemId}",
                    funcao=lambda: self.excluir(TipoContribuicao.contribuicao, itemId),
                )
            else:
                self.popUpSimCancela(
                    f"Você deseja excluir a remuneração {itemId}",
                    funcao=lambda:self.excluir(TipoContribuicao.remuneracao, itemId),
                )

        elif tipoBotao == 'pbExcluirBen':
            numLinha: int = self.tblBeneficios.selectedIndexes()[0].row()
            beneficioId = int(self.tblBeneficios.item(numLinha, 0).text())
            self.popUpSimCancela(
                f"Você deseja excluir o benefício {beneficioId}",
                funcao=lambda: self.excluir(TipoContribuicao.beneficio, beneficioId),
            )

    def atualizaMenuInfo(self, info: str = None, status: StatusInfo = None, inicio: bool = False):
        if inicio:
            self.lbInfo1.setText('')
            self.lbInfo2.setText('')
            self.frInfo1.hide()
            self.frInfo2.hide()

        else:
            if self.lbInfo1.text() == '':
                self.lbInfo1.setText(info)
                self.frInfo1.setStyleSheet(frInfoStatus(nomeFrame='frIcon1', tipoInfo=status))
                self.frInfo1.show()
            else:
                self.lbInfo2.setText(info)
                self.frInfo2.setStyleSheet(frInfoStatus(nomeFrame='frIcon2', tipoInfo=status))
                self.frInfo2.show()

    def excluir(self, tipo: TipoContribuicao, itemId: int):
        if tipo == TipoContribuicao.contribuicao:
            ItemContribuicao.delete_by_id(itemId)
        elif tipo == TipoContribuicao.remuneracao:
            ItemContribuicao.delete_by_id(itemId)
        elif tipo == TipoContribuicao.beneficio:
            ItemContribuicao.delete_by_id(itemId)

        self.carregarTblContribuicoes(self.cliente.clienteId)
        self.carregarTblBeneficios(self.cliente.clienteId)

    def carregarTblContribuicoes(self, clienteId: int):
        # dados = self.daoCalculos.getRemECon(clienteId)
        dbInst: SqliteDatabase = CnisCabecalhos._meta.database
        dados = dbInst.execute_sql(remuEContrib(clienteId))
        listaItens: Generator[RemuEContribs] = (RemuEContribs(info) for info in dados)

        self.tblContribuicoes.setRowCount(0)

        for contLinha, item in enumerate(listaItens):
            self.tblContribuicoes.insertRow(contLinha)

            # RemuneracaoId/ContribuiçãoId - Coluna 0 (escondida)
            strItem = QTableWidgetItem(str(item.itemContribuicaoId))
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 0, strItem)

            # Seq - Coluna 1 (ativa)
            strItem = QTableWidgetItem(str(item.seq))
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 1, strItem)

            # Competência - Coluna 2 (ativa)
            # strItem = QTableWidgetItem(dataUSAtoBR(info))
            strItem = QTableWidgetItem(item.competencia)
            strItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 2, strItem)

            # Salário de contribuição - Coluna 3 (ativa)
            strItem = QTableWidgetItem(mascaraDinheiro(item.salContribuicao, simbolo=item.sinal))
            strItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 3, strItem)

            # Tetos previdenciários - Coluna 4 (ativa)
            strItem = QTableWidgetItem(str(item.valor))
            strItem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 4, strItem)

            # Natureza dos dados (Remuneração/Contribuição) - Coluna 5 (ativa)
            strItem = QTableWidgetItem(item.natureza)
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 5, strItem)

            # Indicadores - Coluna 6 (ativa)
            # if info is None:
            #     strItem = QTableWidgetItem(QIcon(QPixmap('Resources/atencao.png')), 'aaaaa')
            #     # strItem.setIcon(QIcon('Resources/atencao.png'))
            #     strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
            #     self.tblContribuicoes.setItem(contLinha, 6, strItem)
            #     continue
            #
            # elif ',' in info:
            #     indicadores = info.split(', ')
            #     strIndicadores = ''
            #     for indicador in indicadores:
            #         strIndicadores += '- ' + indicador + '\n'
            # elif info != '':
            #     strIndicadores = '- ' + info
            # else:
            #     strIndicadores = info
            #
            # if strIndicadores.endswith('\n'):
            #     strIndicadores = strIndicadores[:len(strIndicadores)-2]
            #
            # strItem = QTableWidgetItem(strIndicadores)
            # strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            # strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
            # self.tblContribuicoes.setItem(contLinha, contColuna+1, strItem)

            # elif contColuna == 8:
            #     strItem = QTableWidgetItem(str(info))
            #     strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            #     strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter | Qt.AlignCenter)
            #     self.tblContribuicoes.setItem(contLinha, 8, strItem)
            #
            # # Tetos previdenciários - Coluna 4 (ativa)
            # elif contColuna == 10:
            #     strItem = QTableWidgetItem(mascaraDinheiro(info, simbolo=infoLinha[6]))
            #     strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            #     strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            #     self.tblContribuicoes.setItem(contLinha, 4, strItem)

        self.tblContribuicoes.resizeColumnsToContents()
        self.tblContribuicoes.resizeRowsToContents()

    def carregarTblBeneficios(self, clienteId: int):

        # TODO: ALTERAR FILTRO PARA SELECIONAR APENAS LINHAS QUE TENHAM NB
        # dictCabecalhos: List[dict] = CnisCabecalhos.select().where(CnisCabecalhos.clienteId == clienteId & CnisCabecalhos.nb.is_null(False)).dicts()
        dados: List[ItemContribuicao] = ItemContribuicao.select().where(
            ItemContribuicao.clienteId == clienteId,
            ItemContribuicao.tipo == TipoContribuicao.beneficio.value,
        )

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

            # Competência - Coluna 3 (ativa)
            strDataInicio = QTableWidgetItem(dataUSAtoBR(beneficio.competencia))
            strDataInicio.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strDataInicio.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 3, strDataInicio)

            # Valor do benefício - Coluna 4 (ativa)
            strRemuneracao = QTableWidgetItem(mascaraDinheiro(beneficio.remuneracao))
            strRemuneracao.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strRemuneracao.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 4, strRemuneracao)

        self.tblBeneficios.resizeColumnsToContents()
        self.tblBeneficios.resizeRowsToContents()

    def carregarInfoCliente(self, clientId: int = 1, clienteModel: Cliente = None):
        if clienteModel is None:
            self.carregarTblContribuicoes(clientId)
            self.carregarTblBeneficios(clientId)
            self.carregarResumos(clientId)
            self.cliente = Cliente.get_by_id(clientId)
            self.lbNome.setText(self.cliente.nomeCliente + ' ' + self.cliente.sobrenomeCliente)
            self.lbNomeBen.setText(self.cliente.nomeCliente + ' ' + self.cliente.sobrenomeCliente)
            self.lbNomeResumo.setText(self.cliente.nomeCliente + ' ' + self.cliente.sobrenomeCliente)
            self.lbDocumento.setText(mascaraCPF(self.cliente.cpfCliente))
            self.lbDocumentoBen.setText(mascaraCPF(self.cliente.cpfCliente))
            self.lbDocumentoResumo.setText(mascaraCPF(self.cliente.cpfCliente))
        else:
            self.cliente = clienteModel
            self.carregarTblContribuicoes(clienteModel.clienteId)
            self.carregarTblBeneficios(clienteModel.clienteId)
            self.lbNome.setText(clienteModel.nomeCliente + ' ' + clienteModel.sobrenomeCliente)
            self.lbNomeBen.setText(clienteModel.nomeCliente + ' ' + clienteModel.sobrenomeCliente)
            self.lbNomeResumo.setText(clienteModel.nomeCliente + ' ' + clienteModel.sobrenomeCliente)
            self.lbDocumento.setText(mascaraCPF(clienteModel.cpfCliente))
            self.lbDocumentoBen.setText(mascaraCPF(clienteModel.cpfCliente))
            self.lbDocumentoResumo.setText(mascaraCPF(clienteModel.cpfCliente))

        self.atualizaMenuInfo(inicio=True)
        self.avaliaAtualizacaoInfoMenu()

    def carregarResumos(self, clienteId: int):

        self.limpaLayoutResumos()

        listaCabecalhos: List[CnisCabecalhos] = CnisCabecalhos.select().where(CnisCabecalhos.clienteId == clienteId)

        if listaCabecalhos is not None:
            for cabecalho in listaCabecalhos:
                item = ItemResumoCnis(cabecalho, parent=self)
                self.efeito.shadowCards([item])
                self.vlResumos.addWidget(item)

        if self.vlResumos.count():
            self.scaResumos.setLayout(self.vlResumos)

    def limpaLayoutResumos(self):
        for index in reversed(range(self.vlResumos.count())):
            self.vlResumos.takeAt(index).widget().setParent(None)

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

    def popUpOkAlerta(self, mensagem, titulo: str = 'Atenção!'):
        pop = QMessageBox()
        pop.setWindowTitle(titulo)
        pop.setText(mensagem)
        pop.setIcon(QMessageBox.Warning)
        pop.setStandardButtons(QMessageBox.Ok)

        x = pop.exec_()

    def limpaTudo(self):
        self.tblContribuicoes.setRowCount(0)
        self.tblBeneficios.setRowCount(0)
        self.lbNomeResumo.setText('')
        self.lbNome.setText('')
        self.lbNomeBen.setText('')
        self.lbDocumentoResumo.setText('')
        self.lbDocumento.setText('')
        self.lbDocumentoBen.setText('')
        self.limpaLayoutResumos()
        self.limpaFiltros()
        self.atualizaMenuInfo(inicio=True)

    ############################## Filtros

    def abreMenuFiltros(self):
        menu = NewSubMenu(self.filtros[TipoFiltro.indicador], parent=self)
        self.efeito.shadowCards([menu], offset=(0, 0))
        menu.show()

    def limpaFiltros(self):
        self.filtros[TipoFiltro.indicador] = []
        self.filtros[TipoFiltro.data] = [None, None]

        self.atualizaFiltros()

    def limpaTabelaDeFiltros(self):
        if TabsResumo(self.tabMain.currentIndex()) == TabsResumo.contribuicao:
            for index in range(self.tblContribuicoes.rowCount()):
                self.tblContribuicoes.showRow(index)
        else:
            for index in range(self.tblBeneficios.rowCount()):
                self.tblBeneficios.showRow(index)

    def atualizaFiltros(self, indicadores: List[str] = None, datas: List[datetime.date] = None):
        if indicadores:
            self.filtros[TipoFiltro.indicador] = indicadores
        if datas:
            # Se o filtro da data "De" for escolhido, apenas adiciona ao filtro da data "Até" já existente, ou vice-versa.
            # Caso contrário, anula as duas datas
            # if datas[0] is None and datas[1] is None:
            #     self.filtros[TipoFiltro.data] = [None, None]
            # else:
            if self.filtros[TipoFiltro.data][0] is None and datas[0] is not None:
                self.filtros[TipoFiltro.data][0] = datas[0]

            if self.filtros[TipoFiltro.data][1] is None and datas[1] is not None:
                self.filtros[TipoFiltro.data][1] = datas[1]

        limpaLayout(self.hlFiltros)
        limpaLayout(self.hlFiltrosBene)

        for indicador in self.filtros[TipoFiltro.indicador]:
            tagIndicador = NewTagFiltro(indicador, TipoFiltro.indicador, parent=self)
            self.hlFiltros.addWidget(tagIndicador)

        for pos, dt in enumerate(self.filtros[TipoFiltro.data]):
            if dt is not None:
                primeiroRegistro: bool = pos == 0
                tagData = NewTagFiltro(dt, TipoFiltro.data, dataInicio=primeiroRegistro, parent=self)
                self.hlFiltros.addWidget(tagData)

        self.atualizaBordaFiltros()
        self.avaliaFiltraTabela()

    def atualizaBordaFiltros(self):
        if self.filtros[TipoFiltro.data][0] is not None or len(self.filtros[TipoFiltro.indicador]) > 0:
            self.frBordaFiltros.show()
        else:
            self.frBordaFiltros.hide()

    def avaliaFiltraTabela(self):
        # index == 1: TabContribuicoes
        # index == 2: TabBenefícios

        self.filtraTabela(TabsResumo(self.tabMain.currentIndex()))

    def filtraTabela(self, tabAtual: TabsResumo):
        self.limpaTabelaDeFiltros()

        dtDe = strToDate(self.filtros[TipoFiltro.data][0]) if self.filtros[TipoFiltro.data][0] is not None else datetime.date.min
        dtAte = strToDate(self.filtros[TipoFiltro.data][1]) if self.filtros[TipoFiltro.data][1] is not None else datetime.date.max

        if tabAtual == TabsResumo.contribuicao:
            if not self.filtros[TipoFiltro.indicador] and not self.filtros[TipoFiltro.data][0] and not self.filtros[TipoFiltro.data][1]:
                for index in range(self.tblContribuicoes.rowCount()):
                    self.tblContribuicoes.showRow(index)
                return True

            for index in range(self.tblContribuicoes.rowCount()):
                indicadorLinha: Union[str, List[str]] = self.tblContribuicoes.item(index, 6).text().replace('- ', '').split('\n')
                dataLinha: datetime.date = strToDate(self.tblContribuicoes.item(index, 2).text())

                if len(self.filtros[TipoFiltro.indicador]) > 0 and not comparaFiltrosAny(indicadorLinha, self.filtros[TipoFiltro.indicador]):
                    self.tblContribuicoes.hideRow(index)
                if not dtDe <= dataLinha <= dtAte:
                    self.tblContribuicoes.hideRow(index)

    def excluiuFiltro(self, filtroAExcluir, tipoFiltro: TipoFiltro):
        if tipoFiltro == TipoFiltro.data:
            if 'De:' in filtroAExcluir:
                self.filtros[tipoFiltro][0] = None
            else:
                self.filtros[tipoFiltro][1] = None
        else:
            self.filtros[tipoFiltro].remove(filtroAExcluir)

        self.atualizaBordaFiltros()
        self.avaliaFiltraTabela()
