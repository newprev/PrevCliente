from typing import List

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from Design.pyUi.wdgResumoCNIS import Ui_wdgResumoCnis
from util.dateHelper import mascaraData
from .localStyleSheet.resumoCnis import selecionaBotao

from .localWidgets.wdgItemCabecalho import ItemResumoCnis

from modelos.clienteORM import Cliente
from modelos.cabecalhoORM import CnisCabecalhos
from modelos.itemContribuicao import ItemContribuicao

from util.helpers import mascaraCPF, mascaraCNPJ
from util.enums.resumoCnisEnums import TelaResumo


class ResumoCnisController(QWidget, Ui_wdgResumoCnis):
    cliente: Cliente
    telaAtual: TelaResumo
    cabecalhoAtual: CnisCabecalhos
    vlResumos: QVBoxLayout = QVBoxLayout()

    def __init__(self, parent=None):
        super(ResumoCnisController, self).__init__(parent=parent)
        self.setupUi(self)

        self.telaAtual = TelaResumo.resumos
        self.cabecalhoAtual = None

        self.pbEmpresas.clicked.connect(lambda: self.trocaTela(TelaResumo.resumos))
        self.pbContrib.clicked.connect(lambda: self.trocaTela(TelaResumo.contribuicoes))
        self.pbBeneficios.clicked.connect(lambda: self.trocaTela(TelaResumo.beneficios))

    def atualizaInfoContrib(self):
        # Nome da empresa ou do benefícios
        if self.cabecalhoAtual.especie is not None:
            self.lbNomeEmp.setText(self.cabecalhoAtual.especie[5:])
            self.lbCNPJouNB.setText(f"Núm. Benefício: {self.cabecalhoAtual.nb}")
        else:
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

    def carregaClienteNaTela(self):
        self.lbNomeCliente.setText(f"{self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}")
        self.lbCpfCliente.setText(f"CPF: {mascaraCPF(self.cliente.cpfCliente)}")

    def carregaTabelaContrib(self):
        listaItens: List[ItemContribuicao] = ItemContribuicao.select().where(
            ItemContribuicao.clienteId == self.cliente.clienteId,
            ItemContribuicao.seq == self.cabecalhoAtual.seq,
        ).order_by(ItemContribuicao.competencia)

        for item in listaItens:
            print(f"{item.competencia=} {item.itemContribuicaoId=}")

    def carregaResumos(self):
        listaCabecalhos: List[CnisCabecalhos] = CnisCabecalhos.select().where(CnisCabecalhos.clienteId == self.cliente.clienteId)
        for cabecalho in listaCabecalhos:
            cabecalho = ItemResumoCnis(cabecalho, parent=self)
            self.vlResumos.addWidget(cabecalho)

        self.wdgScroll.setLayout(self.vlResumos)

    def permiteTrocaTela(self, tela: TelaResumo) -> bool:
        if self.cabecalhoAtual is None:
            return False

        return True

    def recebeCliente(self, cliente: Cliente):
        if cliente is not None:
            self.cliente = cliente
            self.carregaClienteNaTela()
            self.carregaResumos()

    def trocaTela(self, tela: TelaResumo):
        self.telaAtual = tela
        if not self.permiteTrocaTela(tela):
            # TODO: Responder a negação com as devidas mensagens explicando por que não foi possível trocar de tela
            return False

        if tela == TelaResumo.resumos:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, True))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, False))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, False))

        elif tela == TelaResumo.contribuicoes:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, False))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, True))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, False))

            self.atualizaInfoContrib()
            self.carregaTabelaContrib()

        elif tela == TelaResumo.beneficios:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, False))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, False))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, True))

        self.stkCliente.setCurrentIndex(tela.value)


