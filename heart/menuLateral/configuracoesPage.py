from pathlib import Path
import re
import fitz
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate

from Daos.daoFerramentas import DaoInfoImportante
from helpers import meses, strToFloat, strToDatetime, mascaraDinheiro, dinheiroToFloat, mascaraDataPequena
import datetime as dt
from heart.localStyleSheet.configuracoes import desabilitaPB

from PyQt5.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QMessageBox
from Telas.configuracoesPage import Ui_wdgTabConfiguracoes
from modelos.tetosPrevModelo import TetosPrevModelo
from newPrevEnums import TamanhoData


class ConfiguracoesPage(QWidget, Ui_wdgTabConfiguracoes):

    def __init__(self, parent=None, db=None):
        super(ConfiguracoesPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.pathTetosPrev = ''
        self.editando = False
        self.inserindo = False
        self.tetoPrev = TetosPrevModelo()

        self.tblTetos.hideColumn(0)
        self.daoInfoImportante = DaoInfoImportante(db=db)

        self.dashboard = parent
        self.db = db
        self.dictTetos = {
            'Ano': [],
            'Mes': [],
            'Valor': []
        }
        self.leValor.setDisabled(True)
        self.dtData.setDisabled(True)
        self.pbEfetivar.setDisabled(True)
        self.pbEfetivar.setStyleSheet(desabilitaPB("pbEfetivar", True))
        self.pbCancelar.setDisabled(True)
        self.pbCancelar.setStyleSheet(desabilitaPB("pbCancelar", True))
        self.pbInserir.clicked.connect(self.habilitarInserir)
        self.leValor.textChanged.connect(self.getInfo)
        self.dtData.dateChanged.connect(self.getInfo)

        self.expRegAno = "[0-9]{4}"
        self.infoAPular = ['Período', 'Mês', 'Valores Correntes', 'Maior Valor-Teto do', 'Salário-de-Benefício']

        self.atualizaTbl()
        self.pbEditar.clicked.connect(self.habilitarEditar)
        self.pbEfetivar.clicked.connect(self.trataEfetiva)
        self.pbExcluir.clicked.connect(self.trataExclui)

        self.pbBuscarArq.clicked.connect(self.buscaArquivoTetos)
        self.tblTetos.doubleClicked.connect(self.carregaTetoTabela)
        self.pbCancelar.clicked.connect(self.limpaTudo)

    def buscaArquivoTetos(self):
        home = str(Path.home())
        pathAux = None

        # Ambiente de desenvolvimento
        pathAux = QFileDialog.getOpenFileName(directory=home, options=QFileDialog.DontUseNativeDialog)

        # Ambiente de produção
        # pathAux = QFileDialog.getOpenFileName(directory=home)

        if pathAux[0] is not None and pathAux[0] != '':
            self.pathTetosPrev = pathAux[0]

        if self.pathTetosPrev is not None and self.pathTetosPrev != '':
            self.extraiTetos(self.pathTetosPrev)
        else:
            return None

    def extraiTetos(self, path: str):
        documento = fitz.open(path)
        qtdPaginas = documento.page_count
        self.dictTetos = {
            'Ano': [],
            'Mes': [],
            'Valor': []
        }
        Ano = ''
        Mes = ''
        dataTeto = {
            "data": [],
            "valor": []
        }

        for pag in range(0, qtdPaginas):
        # for pag in range(14, 15):
            page = documento.load_page(pag)
            conteudo: str = page.get_text()
            info: list = conteudo.splitlines()
            if pag == 14:
                pass

            for index in range(0, len(info)):
                if info[index] not in self.infoAPular:
                    if re.fullmatch(self.expRegAno, info[index].strip()) is not None:
                        Ano = info[index].strip()
                    elif info[index].isalpha():
                        Mes = info[index].strip()
                    elif ',' in info[index] or '.' in info[index]:
                        self.dictTetos["Ano"].append(Ano)
                        self.dictTetos["Mes"].append(Mes)
                        self.dictTetos["Valor"].append(dinheiroToFloat(info[index].strip()))

        documento.close()
        for index in range(0, len(self.dictTetos['Valor'])):
            for numMes, nomeMes in meses.items():
                if self.dictTetos['Mes'][index] in nomeMes:
                    numeroMes = numMes
                    break

            dataTeto['data'].append(dt.datetime(int(self.dictTetos['Ano'][index]), numeroMes, 1))
            dataTeto['valor'].append(self.dictTetos['Valor'][index])

        if len(dataTeto['data']) == len(dataTeto['valor']):
            self.daoInfoImportante.deletarTabela()
            self.daoInfoImportante.insereListaTetos(dataTeto)
            self.atualizaTbl()
        else:
            print('Erro')

    def atualizaTbl(self, tetos:list = None):

        if tetos is None:
            listaTetos = self.daoInfoImportante.getAllTetos()
            tetos = [TetosPrevModelo().fromList(teto, retornaInst=True) for teto in listaTetos]
        elif tetos[0] is not TetosPrevModelo:
            return False

        self.tblTetos.setRowCount(0)

        for linha, tetoPrev in enumerate(tetos):
            self.tblTetos.insertRow(linha)

            tetoIdItem = QTableWidgetItem(str(tetoPrev.tetosPrevId))
            tetoIdItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            tetoIdItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblTetos.setItem(linha, 0, tetoIdItem)

            dataItem = QTableWidgetItem(mascaraDataPequena(tetoPrev.dataValidade))
            dataItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            dataItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblTetos.setItem(linha, 1, dataItem)

            valorItem = QTableWidgetItem(mascaraDinheiro(tetoPrev.valor))
            valorItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblTetos.setItem(linha, 2, valorItem)

    def habilitarInserir(self):
        self.editando = False
        self.inserindo = True
        self.tetoPrev = TetosPrevModelo()

        texto = self.lbInfoAcao.text()
        self.lbInfoAcao.setText(texto.replace('Editar', 'Inserir'))
        self.habilitaFuncao('e')
        self.dtData.setFocus()

    def habilitarEditar(self):
        if len(self.tblTetos.selectedIndexes()) == 0:
            self.popUpOkAlerta("Para editar uma linha, é preciso selecioná-la e clicar em 'Editar' ou dar um duplo-clique na linha desejada")
            return False
        else:
            texto = self.lbInfoAcao.text()
            self.lbInfoAcao.setText(texto.replace('Inserir', 'Editar'))
            self.habilitaFuncao('e')

            linhaSelecionada = self.tblTetos.selectedIndexes()[0].row()
            self.tetoPrev.tetosPrevId = int(self.tblTetos.item(linhaSelecionada, 0).text())
            self.tetoPrev.data = strToDatetime(self.tblTetos.item(linhaSelecionada, 1).text(), short=True)
            self.tetoPrev.valor = dinheiroToFloat(self.tblTetos.item(linhaSelecionada, 2).text())

            self.dtData.setDate(self.tetoPrev.data)
            self.leValor.setText(mascaraDinheiro(self.tetoPrev.valor))

            self.dtData.setFocus()

    def habilitaFuncao(self, funcao: str):
        if funcao.lower() == 'edicao' or funcao.lower() == 'e':
            self.leValor.setDisabled(False)
            self.dtData.setDisabled(False)

            self.pbEfetivar.setDisabled(False)
            self.pbEfetivar.setStyleSheet(desabilitaPB("pbEfetivar", False))

            self.pbCancelar.setDisabled(False)
            self.pbCancelar.setStyleSheet(desabilitaPB("pbCancelar", False))

            self.pbBuscarArq.setDisabled(True)
            self.pbBuscarArq.setStyleSheet(desabilitaPB("pbBuscarArq", True))

            self.pbExcluir.setDisabled(True)
            self.pbExcluir.setStyleSheet(desabilitaPB("pbExcluir", True))

            self.pbInserir.setDisabled(True)
            self.pbInserir.setStyleSheet(desabilitaPB("pbInserir", True))

            self.pbEditar.setDisabled(True)
            self.pbEditar.setStyleSheet(desabilitaPB("pbEditar", True))

        else:
            self.editando = False
            self.leValor.setDisabled(True)
            self.dtData.setDisabled(True)

            self.pbEfetivar.setDisabled(True)
            self.pbEfetivar.setStyleSheet(desabilitaPB("pbEfetivar", True))

            self.pbCancelar.setDisabled(True)
            self.pbCancelar.setStyleSheet(desabilitaPB("pbCancelar", True))

            self.pbBuscarArq.setDisabled(False)
            self.pbBuscarArq.setStyleSheet(desabilitaPB("pbBuscarArq", False))

            self.pbExcluir.setDisabled(False)
            self.pbExcluir.setStyleSheet(desabilitaPB("pbExcluir", False))

            self.pbInserir.setDisabled(False)
            self.pbInserir.setStyleSheet(desabilitaPB("pbInserir", False))

            self.pbEditar.setDisabled(False)
            self.pbEditar.setStyleSheet(desabilitaPB("pbEditar", False))

    def trataEfetiva(self):
        if self.editando:
            self.daoInfoImportante.atualizaTeto(self.tetoPrev)
        elif self.inserindo:
            self.daoInfoImportante.insereTeto(self.tetoPrev.toDict())

        self.limpaTudo()
        self.atualizaTbl()

    def trataExclui(self, *args):
        if len(self.tblTetos.selectedIndexes()) == 0:
            self.popUpOkAlerta('Nenhuma linha selecionada')
        else:
            linhaSelecionada = self.tblTetos.selectedIndexes()[0].row()
            self.tetoPrev.tetosPrevId = int(self.tblTetos.item(linhaSelecionada, 0).text())
            self.tetoPrev.data = strToDatetime(self.tblTetos.item(linhaSelecionada, 1).text(), TamanhoData.g)
            self.tetoPrev.valor = dinheiroToFloat(self.tblTetos.item(linhaSelecionada, 2).text())

            self.popUpSimCancela(
                f"Você deseja excluir permanentemente o item: \nData: {mascaraDataPequena(self.tetoPrev.data)}\nValor: {mascaraDinheiro(self.tetoPrev.valor)} ?",
                funcao=self.excluiTeto
            )

    def getInfo(self, *args):
        if isinstance(args[0], QDate):
            self.tetoPrev.dataValidade = dt.datetime(args[0].toPyDate().year, args[0].toPyDate().month, args[0].toPyDate().day)
        elif isinstance(args[0], str):
            self.tetoPrev.valor = strToFloat(args[0])

    def carregaTetoTabela(self, *args):
        self.habilitaFuncao('e')
        self.editando = True
        self.inserindo = False

        self.tetoPrev.tetosPrevId = int(self.tblTetos.item(args[0].row(), 0).text())
        self.tetoPrev.data = strToDatetime(self.tblTetos.item(args[0].row(), 1).text(), short=True)
        self.tetoPrev.valor = dinheiroToFloat(self.tblTetos.item(args[0].row(), 2).text())

        self.dtData.setDate(self.tetoPrev.data)
        self.leValor.setText(mascaraDinheiro(self.tetoPrev.valor))

        self.dtData.setFocus()

    def limpaTudo(self):
        self.editando = False
        self.inserindo = False
        self.habilitaFuncao('leitura')
        self.tblTetos.clearSelection()
        self.leValor.clear()

    def excluiTeto(self):
        self.daoInfoImportante.deletaTetoById(self.tetoPrev.tetosPrevId)
        self.tetoPrev = TetosPrevModelo()
        self.atualizaTbl()
        self.limpaTudo()

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
            # self.parent.menssagemSistema('Ocorreu um erro inesperado')
            raise Warning(f'Ocorreu um erro inesperado')

    def popUpOkAlerta(self, mensagem, titulo: str = 'Atenção!'):
        pop = QMessageBox()
        pop.setWindowTitle(titulo)
        pop.setText(mensagem)
        pop.setIcon(QMessageBox.Warning)
        pop.setStandardButtons(QMessageBox.Ok)

        x = pop.exec_()