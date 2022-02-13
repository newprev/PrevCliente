from typing import List, Generator

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from peewee import SqliteDatabase

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QScrollBar
from Design.pyUi.wdgResumoCNIS import Ui_wdgResumoCnis
from SQLs.itensContribuicao import remuEContrib
from modelos.Auxiliares.remuEContribs import RemuEContribs
from modelos.itemContribuicao import ItemContribuicao
from util.dateHelper import mascaraData
from util.enums.dashboardEnums import TelaAtual
from util.enums.newPrevEnums import TipoContribuicao
from .localStyleSheet.resumoCnis import selecionaBotao

from .localWidgets.wdgItemCabecalho import ItemResumoCnis

from modelos.clienteORM import Cliente
from modelos.cabecalhoORM import CnisCabecalhos

from util.helpers import mascaraCPF, mascaraCNPJ, mascaraDinheiro, dataUSAtoBR
from util.enums.resumoCnisEnums import TelaResumo
from util.enums.databaseEnums import DatabaseEnum


class ResumoCnisController(QWidget, Ui_wdgResumoCnis):
    cliente: Cliente
    telaAtual: TelaResumo
    cabecalhoAtual: CnisCabecalhos
    vlResumos: QVBoxLayout = QVBoxLayout()

    def __init__(self, parent=None):
        super(ResumoCnisController, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent

        self.telaAtual = TelaResumo.resumos
        self.cabecalhoAtual = None

        self.tblContribuicoes.horizontalHeader().show()
        self.tblContribuicoes.hideColumn(0)

        self.tblBeneficios.horizontalHeader().show()
        self.tblBeneficios.hideColumn(0)

        self.pbEmpresas.clicked.connect(lambda: self.trocaTela(TelaResumo.resumos))
        self.pbContrib.clicked.connect(lambda: self.trocaTela(TelaResumo.contribuicoes))
        self.pbBeneficios.clicked.connect(lambda: self.trocaTela(TelaResumo.beneficios))
        self.pbVoltar.clicked.connect(self.avaliaVoltar)

        self.trocaTela(self.telaAtual)

    def atualizaInfoBeneficios(self):
        # Nome da empresa ou do benefícios
        self.lbNomeEmpBene.setText(self.cabecalhoAtual.especie[5:])
        self.lbCNPJouNBBene.setText(f"Núm. Benefício: {self.cabecalhoAtual.nb}")

        # Data de início
        if self.cabecalhoAtual.dataInicio is not None and len(self.cabecalhoAtual.dataInicio) > 0:
            self.lbDataInicioBene.setText(f"Início: {mascaraData(self.cabecalhoAtual.dataInicio)}")
        else:
            self.lbDataInicio.setText('')

        # Data de fim
        if self.cabecalhoAtual.dataFim is not None and len(self.cabecalhoAtual.dataFim) > 0:
            self.lbDataFimBene.setText(f"Fim: {mascaraData(self.cabecalhoAtual.dataFim)}")
        else:
            self.lbDataFim.setText('')

        # Situação
        self.lbSituacao.setText(f"Situação: {self.cabecalhoAtual.situacao}")

    def atualizaInfoContrib(self):
        # Nome da empresa ou do benefícios
        self.lbNomeEmp.setText(self.cabecalhoAtual.nomeEmp)
        self.lbCNPJouNB.setText("CNPJ: " + mascaraCNPJ(self.cabecalhoAtual.cdEmp))

        # Data de início
        if self.cabecalhoAtual.dataInicio is not None and len(self.cabecalhoAtual.dataInicio) > 0:
            self.lbDataInicio.setText(f"Início: {mascaraData(self.cabecalhoAtual.dataInicio)}")
        else:
            self.lbDataInicio.setText('')

        # Data de fim
        if self.cabecalhoAtual.dataFim is not None and len(self.cabecalhoAtual.dataFim) > 0:
            self.lbDataFim.setText(f"Fim: {mascaraData(self.cabecalhoAtual.dataFim)}")
        else:
            self.lbDataFim.setText('')

    def atualizaCabecalhoSelecionado(self, cabecalho: CnisCabecalhos):
        self.cabecalhoAtual = cabecalho
        for index in range(self.vlResumos.count()):
            wdgCabecalho: ItemResumoCnis = self.vlResumos.itemAt(index).widget()
            if wdgCabecalho.selecionado and wdgCabecalho.cabecalhoAtual.cabecalhosId != cabecalho.cabecalhosId:
                wdgCabecalho.desselecionaCabecalho()

        if self.cabecalhoAtual.nb is None:
            self.trocaTela(TelaResumo.contribuicoes)
        else:
            self.trocaTela(TelaResumo.beneficios)

    def avaliaVoltar(self):
        if self.telaAtual == TelaResumo.resumos:
            self.dashboard.trocaTela(TelaAtual.Cliente)
        else:
            self.trocaTela(TelaResumo.resumos)

    def carregaClienteNaTela(self):
        self.lbNomeCliente.setText(f"{self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}")
        self.lbCpfCliente.setText(f"CPF: {mascaraCPF(self.cliente.cpfCliente)}")

    def carregaTblContribuicoes(self):
        dbInst: SqliteDatabase = SqliteDatabase(DatabaseEnum.producao.value)
        dados = dbInst.execute_sql(remuEContrib(self.cliente.clienteId, self.cabecalhoAtual.seq))
        listaItens: Generator[RemuEContribs] = (RemuEContribs(info) for info in dados)

        self.tblContribuicoes.setRowCount(0)

        for contLinha, item in enumerate(listaItens):
            self.tblContribuicoes.insertRow(contLinha)

            # itemContribId - Coluna 0 (escondida)
            strItem = QTableWidgetItem(str(item.itemContribuicaoId))
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 0, strItem)

            # Seq - Coluna 1 (ativa)
            strItem = QTableWidgetItem(str(item.seq))
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 1, strItem)

            # Competência - Coluna 2 (ativa)
            strItem = QTableWidgetItem(item.competencia)
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 2, strItem)

            # Salário de contribuição - Coluna 3 (ativa)
            strItem = QTableWidgetItem(mascaraDinheiro(item.salContribuicao, simbolo=item.sinal))
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 3, strItem)

            # Tetos previdenciários - Coluna 4 (ativa)
            strItem = QTableWidgetItem(mascaraDinheiro(item.valor, simbolo=item.sinal))
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 4, strItem)

            # Natureza dos dados (Remuneração/Contribuição) - Coluna 5 (ativa)
            strItem = QTableWidgetItem(item.natureza)
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 5, strItem)

            # Indicadores do CNIS - Coluna 6 (ativa)
            strItem = QTableWidgetItem(item.indicadores)
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 6, strItem)

        self.tblContribuicoes.resizeColumnsToContents()
        self.tblContribuicoes.resizeRowsToContents()

    def carregaTblBeneficios(self):
        dados: List[ItemContribuicao] = ItemContribuicao.select().where(
            ItemContribuicao.clienteId == self.cliente.clienteId,
            ItemContribuicao.tipo == TipoContribuicao.beneficio.value,
            ItemContribuicao.seq == self.cabecalhoAtual.seq
        )

        self.tblBeneficios.setRowCount(0)

        for contLinha, beneficio in enumerate(dados):
            self.tblBeneficios.insertRow(contLinha)

            # BenefícioId - Coluna 0 (escondida)
            strBeneficioId = QTableWidgetItem(str(beneficio.itemContribuicaoId))
            strBeneficioId.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 0, strBeneficioId)

            # Entrada (seq) - Coluna 1 (ativa)
            strSeq = QTableWidgetItem(str(beneficio.seq))
            strSeq.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            strSeq.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 1, strSeq)

            # Nb (Número do benefício) - Coluna 2 (ativa)
            if str(self.cabecalhoAtual.nb) == '':
                strNb = QTableWidgetItem('-')
            else:
                strNb = QTableWidgetItem(str(self.cabecalhoAtual.nb))
            strNb.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strNb.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 2, strNb)

            # Competência - Coluna 3 (ativa)
            strDataInicio = QTableWidgetItem(dataUSAtoBR(beneficio.competencia))
            strDataInicio.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strDataInicio.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 3, strDataInicio)

            # Valor do benefício - Coluna 4 (ativa)
            strRemuneracao = QTableWidgetItem(mascaraDinheiro(beneficio.salContribuicao))
            strRemuneracao.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strRemuneracao.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblBeneficios.setItem(contLinha, 4, strRemuneracao)

        self.tblBeneficios.resizeColumnsToContents()
        self.tblBeneficios.resizeRowsToContents()

    def carregaResumos(self):
        listaCabecalhos: List[CnisCabecalhos] = CnisCabecalhos.select().where(CnisCabecalhos.clienteId == self.cliente.clienteId)
        for cabecalho in listaCabecalhos:
            cabecalho = ItemResumoCnis(cabecalho, parent=self)
            self.vlResumos.addWidget(cabecalho)

        self.wdgScroll.setLayout(self.vlResumos)

    def permiteTrocaTela(self, tela: TelaResumo) -> bool:
        if self.telaAtual == TelaResumo.resumos:
            # Resumos -> Contribuições
            if tela == TelaResumo.contribuicoes:
                for index in range(self.vlResumos.count()):
                    wdgCabecalho: ItemResumoCnis = self.vlResumos.itemAt(index).widget()
                    if wdgCabecalho.selecionado and wdgCabecalho.cabecalhoAtual.cabecalhosId == self.cabecalhoAtual.cabecalhosId:
                        return self.cabecalhoAtual.nb is None

            # Resumos -> Benefícios
            elif tela == TelaResumo.beneficios:
                for index in range(self.vlResumos.count()):
                    wdgCabecalho: ItemResumoCnis = self.vlResumos.itemAt(index).widget()
                    if wdgCabecalho.selecionado and wdgCabecalho.cabecalhoAtual.cabecalhosId == self.cabecalhoAtual.cabecalhosId:
                        return self.cabecalhoAtual.nb is not None

        # Qualquer tela -> Resumo
        else:
            return True

        return False

    def recebeCliente(self, cliente: Cliente):
        if cliente is not None:
            self.cliente = cliente
            self.carregaClienteNaTela()
            self.carregaResumos()

    def trocaTela(self, tela: TelaResumo):
        if not self.permiteTrocaTela(tela):
            # TODO: Responder a negação com as devidas mensagens explicando por que não foi possível trocar de tela
            return False

        self.telaAtual = tela

        if tela == TelaResumo.resumos:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, True))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, False))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, False))

        elif tela == TelaResumo.contribuicoes:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, False))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, True))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, False))

            self.atualizaInfoContrib()
            self.carregaTblContribuicoes()

        elif tela == TelaResumo.beneficios:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, False))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, False))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, True))

            self.atualizaInfoBeneficios()
            self.carregaTblBeneficios()

        self.stkCliente.setCurrentIndex(tela.value)


