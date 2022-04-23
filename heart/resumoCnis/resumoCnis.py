from logging import info, error
from typing import List, Generator
from peewee import SqliteDatabase, fn
from datetime import datetime
from dateutil.relativedelta import relativedelta
from time import time

from PyQt5.QtCore import Qt, QSize, QModelIndex
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QPushButton, QHBoxLayout, QLineEdit, QDateEdit

from Design.CustomWidgets.newToast import QToaster
from Design.pyUi.wdgResumoCNIS import Ui_wdgResumoCnis
from Design.efeitos import Efeitos
from SQLs.itensContribuicao import remuEContrib
from modelos.especieBenefORM import EspecieBene

from util.enums.aposentadoriaEnums import FatorTmpInsalubridade, GrauDeficiencia
from util.enums.dashboardEnums import TelaAtual
from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import TipoContribuicao, TipoEdicao, Prioridade, ItemOrigem
from util.enums.periodosImportantesEnum import Evento
from util.enums.resumoCnisEnums import TelaResumo, TipoBotaoResumo, TipoContribuicao, TipoVinculo
from util.enums.databaseEnums import DatabaseEnum
from util.helpers.calculos import tempoContribPorVinculo, tempoContribPorCompetencias

from .localStyleSheet.resumoCnis import selecionaBotao, botaoOpcoes, cadDataEdit, bgFirulaResumo
from .localWidgets.duplicadorController import DuplicadorController
from .localWidgets.wdgItemCabecalho import ItemResumoCnis
from .localWidgets.itemVazioResumoCnis import ItemVazioCnis

from modelos.clienteORM import Cliente
from modelos.vinculoORM import CnisVinculos
from modelos.Auxiliares.remuEContribs import RemuEContribs
from modelos.itemContribuicao import ItemContribuicao
from modelos.clienteProfissao import ClienteProfissao

from util.helpers.helpers import mascaraCPF, mascaraCNPJ, mascaraDinheiro, dataUSAtoBR, situacaoBeneficio, strToFloat
from util.helpers.layoutHelpers import limpaLayout
from util.popUps import popUpSimCancela, popUpOkAlerta
from util.helpers.dateHelper import mascaraData, strToDate, mascaraDataPequena

from ..configsInfos.indicadoresTela import IndicadoresController


class ResumoCnisController(QWidget, Ui_wdgResumoCnis):
    cliente: Cliente
    clienteInfoProf: ClienteProfissao
    telaAtual: TelaResumo
    vinculoAtual: CnisVinculos
    vlResumos: QVBoxLayout = QVBoxLayout()
    toasty: QToaster

    def __init__(self, parent=None):
        super(ResumoCnisController, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent

        self.telaAtual = TelaResumo.resumos
        self.vinculoAtual = None
        self.toasty = None
        self.efeitos = Efeitos()
        self.cliente = None

        self.tblContribuicoes.horizontalHeader().show()
        self.tblContribuicoes.hideColumn(0)

        self.tblBeneficios.horizontalHeader().show()
        self.tblBeneficios.hideColumn(0)

        self.tblCadBene.resizeColumnsToContents()
        self.tblCadContrib.resizeColumnsToContents()

        self.efeitos.shadowCards(
            [self.pbAddContrib, self.pbAddBene, self.frBgFirula, self.frBgFirulaBene],
            radius=10,
            offset=(1, 4),
            color=(63, 63, 63, 100),
        )
        self.efeitos.shadowCards([self.frTempoEspecial, self.frRightInfo], radius=20, offset=(0, 0), color=(80, 80, 80, 100))

        self.iniciaCampos()

        self.pbEmpresas.clicked.connect(lambda: self.trocaTela(TelaResumo.resumos))
        self.pbContrib.clicked.connect(lambda: self.trocaTela(TelaResumo.contribuicoes))
        self.pbBeneficios.clicked.connect(lambda: self.trocaTela(TelaResumo.beneficios))
        self.pbVoltar.clicked.connect(self.avaliaVoltar)
        self.pbInserirResumo.clicked.connect(self.avaliaInserirVinculo)
        self.rbBeneficio.clicked.connect(lambda: self.avaliaTrocaVinculo(TipoContribuicao.beneficio))
        self.rbContribuicao.clicked.connect(lambda: self.avaliaTrocaVinculo(TipoContribuicao.contribuicao))
        self.pbSeguir.clicked.connect(self.avaliaSalvarVinculo)
        self.pbCancelar.clicked.connect(self.avaliaCancelar)
        self.pbInserirContrib.clicked.connect(lambda: self.trocaTela(TelaResumo.addContriBene, tipoContribuicao=TipoContribuicao.contribuicao))
        self.pbInserirBeneficios.clicked.connect(lambda: self.trocaTela(TelaResumo.addContriBene, tipoContribuicao=TipoContribuicao.beneficio))
        self.pbAddContrib.clicked.connect(lambda: self.adicionaLinhaCadastro(TipoContribuicao.contribuicao))
        self.pbAddBene.clicked.connect(lambda: self.adicionaLinhaCadastro(TipoContribuicao.beneficio))
        self.pbBuscaIndicador.clicked.connect(lambda: IndicadoresController(retornaIndicadores=True, parent=self).show())
        self.pbFinalizar.clicked.connect(self.avaliaAddContrib)
        self.pbSalvarSelecionados.clicked.connect(self.atualizaCompEspecial)

        self.trocaTela(self.telaAtual)

    def adicionaLinhaCadastro(self, tipo: TipoContribuicao, valorContribuicao: float = 0.0):
        if tipo == TipoContribuicao.contribuicao:
            linhaDeInsercao = self.tblCadContrib.rowCount()
            self.tblCadContrib.insertRow(linhaDeInsercao)

            # seq - Coluna 1 (aparente)
            leSeqVinculo = QLineEdit()
            leSeqVinculo.setDisabled(True)
            leSeqVinculo.setMinimumHeight(35)
            leSeqVinculo.setMaximumHeight(40)
            if self.vinculoAtual is not None:
                leSeqVinculo.setText(str(self.vinculoAtual.seq))
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 0, leSeqVinculo)

            # Competência - Coluna 2 (aparente)
            dtCompetencia = QDateEdit()

            if linhaDeInsercao != 0:
                # -- Adiciona um mês à próxima competência
                competenciaAnterior = self.tblCadContrib.cellWidget(linhaDeInsercao - 1, 1).date().toPyDate()
                dtCompetencia.setDate(competenciaAnterior + relativedelta(months=1))

            dtCompetencia.setStyleSheet(cadDataEdit())
            dtCompetencia.setCalendarPopup(True)
            dtCompetencia.setMinimumHeight(35)
            dtCompetencia.setMinimumWidth(140)
            dtCompetencia.setMaximumHeight(40)
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 1, dtCompetencia)

            # Salário de contribuição - Coluna 2 (aparente)
            leSalContrib = QLineEdit()
            # leSalContrib.setStyleSheet(cadLineEdit())
            leSalContrib.setMinimumHeight(35)
            leSalContrib.setMaximumHeight(40)
            if valorContribuicao != 0:
                leSalContrib.setText(str(valorContribuicao))
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 2, leSalContrib)

            # Indicadores - Coluna 3 (aparente)
            leIndicadores = QLineEdit()
            # leIndicadores.setStyleSheet(cadLineEdit())
            leIndicadores.setMinimumHeight(35)
            leIndicadores.setMaximumHeight(40)
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 3, leIndicadores)

            # Ações - Coluna 4 (Aparente)
            hlOpcoes = QHBoxLayout()
            hlOpcoes.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

            pbDeletar = QPushButton()
            pbDeletar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.deletar))
            pbDeletar.setFixedSize(QSize(25, 25))
            pbDeletar.clicked.connect(lambda state, item=linhaDeInsercao: self.avaliaOpcoesAddContribBene(linhaDeInsercao, TipoBotaoResumo.deletar))

            pbDuplicar = QPushButton()
            pbDuplicar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.duplicar))
            pbDuplicar.setFixedSize(QSize(25, 25))
            pbDuplicar.clicked.connect(lambda state, item=linhaDeInsercao: self.avaliaOpcoesAddContribBene(linhaDeInsercao, TipoBotaoResumo.duplicar))

            hlOpcoes.addWidget(pbDeletar)
            hlOpcoes.addWidget(pbDuplicar)

            wdgAuxiliar = QWidget()
            wdgAuxiliar.setLayout(hlOpcoes)
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 4, wdgAuxiliar)

            self.tblCadContrib.resizeColumnsToContents()
            self.tblCadContrib.resizeRowsToContents()

        else:
            linhaDeInsercao = self.tblCadBene.rowCount()
            self.tblCadBene.insertRow(linhaDeInsercao)

            # Número do benefício - Coluna 1 (aparente)
            leNumBene = QLineEdit()
            leNumBene.setMinimumHeight(35)
            leNumBene.setMaximumHeight(40)
            leNumBene.setDisabled(True)
            if self.vinculoAtual is not None:
                leNumBene.setText(str(self.vinculoAtual.nb))
            self.tblCadBene.setCellWidget(linhaDeInsercao, 0, leNumBene)

            # Competência - Coluna 2 (aparente)
            dtCompetencia = QDateEdit()

            if linhaDeInsercao != 0:
                # -- Adiciona um mês à próxima competência
                competenciaAnterior = self.tblCadBene.cellWidget(linhaDeInsercao - 1, 1).date().toPyDate()
                dtCompetencia.setDate(competenciaAnterior + relativedelta(months=1))

            dtCompetencia.setStyleSheet(cadDataEdit())
            dtCompetencia.setCalendarPopup(True)
            dtCompetencia.setMinimumHeight(35)
            dtCompetencia.setMinimumWidth(140)
            dtCompetencia.setMaximumHeight(40)
            self.tblCadBene.setCellWidget(linhaDeInsercao, 1, dtCompetencia)

            # Valor do benefício - Coluna 2 (aparente)
            leValBene = QLineEdit()
            leValBene.setMinimumHeight(35)
            leValBene.setMaximumHeight(40)
            if valorContribuicao != 0:
                leValBene.setText(str(valorContribuicao))
            self.tblCadBene.setCellWidget(linhaDeInsercao, 2, leValBene)

            # Ações - Coluna 3 (Aparente)
            hlOpcoes = QHBoxLayout()
            hlOpcoes.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

            pbDeletar = QPushButton()
            pbDeletar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.deletar))
            pbDeletar.setFixedSize(QSize(25, 25))
            pbDeletar.clicked.connect(lambda state, item=linhaDeInsercao: self.avaliaOpcoesAddContribBene(linhaDeInsercao, TipoBotaoResumo.deletar))

            pbDuplicar = QPushButton()
            pbDuplicar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.duplicar))
            pbDuplicar.setFixedSize(QSize(25, 25))
            pbDuplicar.clicked.connect(lambda state, item=linhaDeInsercao: self.avaliaOpcoesAddContribBene(linhaDeInsercao, TipoBotaoResumo.duplicar))

            hlOpcoes.addWidget(pbDeletar)
            hlOpcoes.addWidget(pbDuplicar)

            wdgAuxiliar = QWidget()
            wdgAuxiliar.setLayout(hlOpcoes)
            self.tblCadBene.setCellWidget(linhaDeInsercao, 3, wdgAuxiliar)

            self.tblCadBene.resizeColumnsToContents()
            self.tblCadBene.resizeRowsToContents()

    def atualizaCompEspecial(self):
        if self.vinculoAtual.nb is None:
            fatorInsalubridade = self.getFatorInsalubridade()
            grauDeficiencia = self.getGrauDeficiencia()
            linhasSelecionadas: List[QModelIndex] = self.tblContribuicoes.selectionModel().selectedRows()
            itemIds: List[int] = []

            for linha in linhasSelecionadas:
                itemIds.append(int(self.tblContribuicoes.item(linha.row(), 0).text()))

            if fatorInsalubridade is None:
                pass
            elif fatorInsalubridade != -1:
                ItemContribuicao.update(fatorInsalubridade=fatorInsalubridade).where(ItemContribuicao.itemContribuicaoId.in_(itemIds)).execute()
            else:
                ItemContribuicao.update(fatorInsalubridade=None).where(ItemContribuicao.itemContribuicaoId.in_(itemIds)).execute()

            if grauDeficiencia is None:
                pass
            elif grauDeficiencia != -1:
                ItemContribuicao.update(grauDeficiencia=grauDeficiencia).where(ItemContribuicao.itemContribuicaoId.in_(itemIds)).execute()
            else:
                ItemContribuicao.update(grauDeficiencia=None).where(ItemContribuicao.itemContribuicaoId.in_(itemIds)).execute()

            self.carregaTblContribuicoes()
            self.atualizaTmpContrib()
            self.carregaDadoFaltanteInsalubridade(None)

            self.cbxDeficiencia.setCurrentIndex(0)
            self.cbxInsalubridade.setCurrentIndex(0)
        else:
            pass

    def atualizaInfoBeneficios(self):
        # Nome da empresa ou do benefícios
        self.lbNomeEmpBene.setText(self.vinculoAtual.especie[5:])
        self.lbCNPJouNBBene.setText(f"Núm. Benefício: {self.vinculoAtual.nb}")

        # Data de início
        if self.vinculoAtual.dataInicio is not None and len(self.vinculoAtual.dataInicio) > 0:
            self.lbDataInicioBene.setText(f"Início: {mascaraData(self.vinculoAtual.dataInicio)}")
        else:
            self.lbDataInicio.setText('')

        # Data de fim
        if self.vinculoAtual.dataFim is not None and len(self.vinculoAtual.dataFim) > 0:
            self.lbDataFimBene.setText(f"Fim: {mascaraData(self.vinculoAtual.dataFim)}")
        else:
            self.lbDataFim.setText('')

        # Situação
        self.lbSituacao.setText(f"Situação: {self.vinculoAtual.situacao}")

    def atualizaInfoContrib(self):
        # Nome da empresa ou do benefícios
        self.lbNomeEmp.setText(f"{self.vinculoAtual.seq} - {self.vinculoAtual.nomeEmp}")
        self.lbCNPJouNB.setText("CNPJ: " + mascaraCNPJ(self.vinculoAtual.cdEmp))

        # Data de início
        if self.vinculoAtual.dataInicio is not None and len(self.vinculoAtual.dataInicio) > 0:
            self.lbDataInicio.setText(f"Início: {mascaraData(self.vinculoAtual.dataInicio)}")
        else:
            self.lbDataInicio.setText('Início: -')

        # Data de fim
        if self.vinculoAtual.dataFim is not None and len(self.vinculoAtual.dataFim) > 0:
            self.lbDataFim.setText(f"Fim: {mascaraData(self.vinculoAtual.dataFim)}")
        else:
            self.lbDataFim.setText('Fim: -')

    def atualizaVinculoEditado(self):
        if self.rbContribuicao.isChecked():
            self.vinculoAtual.nomeEmp = self.leNomeEmp.text()
            self.vinculoAtual.cdEmp = self.leCnpj.text()
            self.vinculoAtual.dataInicio = self.dtDataInicio.date().toPyDate()
            self.vinculoAtual.dataFim = self.dtDataFim.date().toPyDate()
            self.vinculoAtual.dataUltAlt = datetime.now()
            self.vinculoAtual.atualizaDadoFaltante()
        else:
            self.vinculoAtual.nb = self.leNb.text()
            self.vinculoAtual.dataInicio = self.dtDataInicioBene.date().toPyDate()
            self.vinculoAtual.dataFim = self.dtDataFimBene.date().toPyDate()
            self.vinculoAtual.dataUltAlt = datetime.now()
            self.vinculoAtual.atualizaDadoFaltante()
        self.vinculoAtual.save()

    def atualizaTmpContrib(self):
        if self.vinculoAtual.nb is None:
            listaCompetencias: List[ItemContribuicao] = ItemContribuicao.select().where(
                ItemContribuicao.clienteId == self.cliente.clienteId,
                ItemContribuicao.seq == self.vinculoAtual.seq
            )
            tempoNormal: relativedelta = tempoContribPorCompetencias(listaCompetencias)
            tempoEspecial: relativedelta = tempoContribPorCompetencias(listaCompetencias, tempoEspecial=True)

            if tempoNormal.days != 0:
                self.lbTpNormal.setText(f"{tempoNormal.years} anos, {tempoNormal.months} meses e {tempoNormal.days} dias")
            else:
                self.lbTpNormal.setText(f"{tempoNormal.years} anos e {tempoNormal.months} meses")

            if tempoEspecial.years == 0 and tempoEspecial.months == 0:
                self.lbTpEspecial.setText("-")
            else:
                self.lbTpEspecial.setText(f"{tempoEspecial.months} meses")

    def avaliaAddContrib(self):
        # Se nb é None, então é uma contribuição. Caso contrário, é um benefício
        if self.vinculoAtual.nb is None:
            listaContrib: List[ItemContribuicao] = self.contribsParaCadastrar()
            if len(listaContrib) == 0:
                return False
            mensagemConfirmacao = f"Você está inserindo as seguintes competências:\n\n {'Competência': ^14} {'Salário de contribuição':}\n"

            for item in listaContrib:
                mensagemConfirmacao += f"{mascaraDataPequena(item.competencia): >14}   {mascaraDinheiro(item.salContribuicao): >23}\n"

            popUpSimCancela(mensagemConfirmacao, funcaoSim=lambda: self.insereContribuicoes(listaContrib))
        else:
            listaBene: List[ItemContribuicao] = self.beneficiosParaCadastrar()
            if len(listaBene) == 0:
                return False
            mensagemConfirmacao = f"Você está inserindo as seguintes competências:\n\n {'Competência': ^14} {'Valor da contribuição':}\n"

            for item in listaBene:
                mensagemConfirmacao += f"{mascaraDataPequena(item.competencia): >14}   {mascaraDinheiro(item.salContribuicao): >23}\n"

            popUpSimCancela(mensagemConfirmacao, funcaoSim=lambda: self.insereContribuicoes(listaBene))

    def avaliaInserirVinculo(self):
        if self.cliente is not None:
            self.limpaVinculos()
            self.trocaTela(TelaResumo.addVinculo)

    def avaliaCancelar(self):
        if self.leNb.text() != '' or self.leCnpj.text() != '' or self.leNomeEmp.text() != '':
            popUpSimCancela("Deseja voltar para a tela de vínculos? Suas alterações não serão salvas.", funcaoSim=self.avaliaVoltar)
            return True

        self.avaliaVoltar()

    def avaliaOpcoes(self, itemTabela: RemuEContribs, acao: TipoBotaoResumo):
        itemId: int = itemTabela.itemContribuicaoId

        itemContribuicao: ItemContribuicao = ItemContribuicao.get_by_id(itemId)

        if acao == TipoBotaoResumo.editar:
            tipoContrib = TipoContribuicao.contribuicao if self.vinculoAtual.nb is None else TipoContribuicao.beneficio
            self.trocaTela(TelaResumo.addContriBene, tipoContribuicao=tipoContrib, itemContribuicao=itemContribuicao)
        else:
            popUpSimCancela(
                f"Você deseja excluir a competência {mascaraData(itemContribuicao.competencia)}?",
                funcaoSim=lambda: self.excluirItem(itemContribuicao),
            )

    def avaliaOpcoesAddContribBene(self, linha: int, tipoBotao: TipoBotaoResumo):
        if tipoBotao == TipoBotaoResumo.deletar:
            if self.vinculoAtual.nb is None:
                self.tblCadContrib.removeRow(linha)
            else:
                self.tblCadBene.removeRow(linha)
        else:
            if self.vinculoAtual.nb is None:
                if self.tblCadContrib.cellWidget(linha, 2).text() == '':
                    popUpOkAlerta(
                        "Para usar a ferramenta de replicação, é preciso informar o salário de contribuição.",
                        funcao=self.tblCadContrib.cellWidget(linha, 2).setFocus()
                    )
                    return None

                salContrib = self.tblCadContrib.cellWidget(linha, 2).text()
            else:
                if self.tblCadBene.cellWidget(linha, 2).text() == '':
                    popUpOkAlerta(
                        "Para usar a ferramenta de replicação, é preciso informar o valor do benefício.",
                        funcao=self.tblCadBene.cellWidget(linha, 2).setFocus()
                    )
                    return None
                salContrib = self.tblCadBene.cellWidget(linha, 2).text()

            duplicador = DuplicadorController(salContrib, parent=self)
            duplicador.show()

    def avaliaSalvarVinculo(self):
        if not self.datasCorretas():
            popUpOkAlerta("As datas de início e de fim não estão corretas. Verifique e tente novamente.")
            return False

        if self.vinculoAtual is not None:
            self.atualizaVinculoEditado()

        elif self.rbContribuicao.isChecked():
            if self.leNomeEmp.text() != "" and self.leCnpj.text() != "":
                self.criaVinculo(TipoContribuicao.contribuicao)
            else:
                popUpOkAlerta("Não foi possível salvar o vínculo editado pois o nome da empresa ou o CNPJ não foram inseridos")
                if self.leNomeEmp == '':
                    self.leNomeEmp.setFocus()
                else:
                    self.leCnpj.setFocus()
        else:
            if self.leNb.text() != "":
                self.criaVinculo(TipoContribuicao.beneficio)
            else:
                popUpOkAlerta("Não foi possível salvar o vínculo editado pois o número do benefício não foi inserido")
                self.leNb.setFocus()

        if self.toasty is None:
            self.toasty = QToaster(self)
        self.toasty.showMessage(self, 'Vínculos atualizados com sucesso!')

        self.trocaTela(TelaResumo.resumos)
        self.limpaVinculos()
        self.limpaCabecalhos()
        self.carregaResumos()

        return True

    def avaliaTrocaVinculo(self, tipo: TipoContribuicao):
        # Verifica se o usuário não clicou sem querer em algum dos radioButton
        if tipo == TipoContribuicao.contribuicao:
            if self.leNb.text() != '':
                popUpSimCancela(
                    "Você adicionou o número do benefício, deseja prosseguir? Sua alteração será perdida.",
                    funcaoSim=lambda: self.trocaVinculo(tipo),
                    funcaoCancela=lambda: self.rbBeneficio.setChecked(True)
                )
            else:
                self.trocaVinculo(tipo)

        else:
            if self.leNomeEmp.text() != '' or self.leCnpj.text() != '':
                popUpSimCancela(
                    "Você adicionou algumas informações, deseja prosseguir? Suas alterações serão perdidas",
                    funcaoSim=lambda: self.trocaVinculo(tipo),
                    funcaoCancela=lambda: self.rbContribuicao.setChecked(True)
                )
            else:
                self.trocaVinculo(tipo)

    def atualizarVinculos(self):
        self.limpaCabecalhos()
        self.carregaResumos()

    def avaliaVoltar(self):
        if self.telaAtual == TelaResumo.resumos:
            self.dashboard.trocaTela(TelaAtual.Cliente)
            self.limpaCabecalhos()
        elif self.telaAtual == TelaResumo.addContriBene:
            if self.vinculoAtual.nb is None:
                self.trocaTela(TelaResumo.contribuicoes)
            else:
                self.trocaTela(TelaResumo.beneficios)
        else:
            self.limpaCabecalhos()
            self.carregaResumos()
            self.trocaTela(TelaResumo.resumos)

    def beneficiosParaCadastrar(self):
        listaBene: List[ItemContribuicao] = []

        for linha in range(self.tblCadBene.rowCount()):
            salContribuicao = strToFloat(self.tblCadBene.cellWidget(linha, 2).text())
            if salContribuicao == '':
                popUpOkAlerta("O valor do benefício precisa ser informado.", funcao=self.tblCadBene.cellWidget(linha, 2).setFocus)
                return []

            listaBene.append(
                ItemContribuicao(
                    clienteId=self.cliente,
                    tipo=TipoContribuicao.beneficio.value,
                    seq=self.vinculoAtual.seq,
                    competencia=self.tblCadBene.cellWidget(linha, 1).date().toPyDate(),
                    salContribuicao=salContribuicao,
                    contribuicao=salContribuicao * 0.2,
                    dadoOrigem=ItemOrigem.NEWPREV.value,
                    geradoAutomaticamente=False,
                )
            )
        return listaBene

    def buscaNovoSeq(self) -> int:
        try:
            maxSeq = CnisVinculos.select(fn.MAX(CnisVinculos.seq)).where(
                CnisVinculos.clienteId == self.cliente.clienteId
            ).scalar()
            if maxSeq is None:
                return 1
            return maxSeq
        except Exception as err:
            # TODO: LOG
            return 999

    def carregaClienteNaTela(self):
        self.lbNomeCliente.setText(f"{self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}")
        self.lbCpfCliente.setText(f"CPF: {mascaraCPF(self.cliente.cpfCliente)}")

    def carregaContribBeneEdicao(self, tipoContrib: TipoContribuicao, item: ItemContribuicao):
        if tipoContrib == TipoContribuicao.contribuicao:
            leSeq: QLineEdit = self.tblCadContrib.cellWidget(0, 0)
            leSeq.setText(str(item.seq))

            dtCompetencia: QDateEdit = self.tblCadContrib.cellWidget(0, 1)
            dtCompetencia.setDate(strToDate(item.competencia))

            leSalContrib: QLineEdit = self.tblCadContrib.cellWidget(0, 2)
            leSalContrib.setText(str(item.salContribuicao))

            leIndicadores: QLineEdit = self.tblCadContrib.cellWidget(0, 3)
            leIndicadores.setText('' if item.indicadores is None else item.indicadores)
        else:
            leNb: QLineEdit = self.tblCadBene.cellWidget(0, 0)
            leNb.setText(str(self.vinculoAtual.nb))

            dtCompetencia: QDateEdit = self.tblCadBene.cellWidget(0, 1)
            dtCompetencia.setDate(strToDate(item.competencia))

            leValorBeneficio: QLineEdit = self.tblCadBene.cellWidget(0, 2)
            leValorBeneficio.setText(str(item.salContribuicao))

    def carregaDadoFaltanteInsalubridade(self, wdgCardResumo: ItemResumoCnis):
        if wdgCardResumo is not None:
            mostraInsalubridade = wdgCardResumo.insalubridade
            mostraDadoFaltante = wdgCardResumo.dadoFaltante
        else:
            mostraInsalubridade = self.getInsalubridadeDaTabela()
            mostraDadoFaltante = self.vinculoAtual.dadoFaltante

        if self.telaAtual == TelaResumo.contribuicoes:
            self.frImportante.show()

            if not mostraInsalubridade:
                self.frInsalubridade.hide()
            else:
                self.frInsalubridade.setToolTip('Existem contribuições em situação de insalubridade.')
                self.frInsalubridade.show()

            if not mostraDadoFaltante:
                self.frFaltaData.hide()
            else:
                self.frFaltaData.setToolTip('A data de início ou de fim deste vínculo não foi informada.')
                self.frFaltaData.show()

            if not mostraInsalubridade and not mostraDadoFaltante:
                self.frImportante.hide()
            elif (not mostraInsalubridade and mostraDadoFaltante) or (mostraInsalubridade and not mostraDadoFaltante):
                self.lineImportante.hide()
            elif mostraInsalubridade and mostraDadoFaltante:
                self.lineImportante.show()

    def carregaFirula(self):
        if self.vinculoAtual.nb is None:
            self.frBgFirula.setStyleSheet(bgFirulaResumo(TipoContribuicao.contribuicao, 'frBgFirula'))
        else:
            self.frBgFirulaBene.setStyleSheet(bgFirulaResumo(TipoContribuicao.beneficio, 'frBgFirulaBene'))

    def carregaTblContribuicoes(self):
        dbInst: SqliteDatabase = SqliteDatabase(DatabaseEnum.producao.value)
        dados = dbInst.execute_sql(remuEContrib(self.cliente.clienteId, self.vinculoAtual.seq))
        listaItens: Generator[RemuEContribs] = (RemuEContribs(info) for info in dados)

        self.tblContribuicoes.setRowCount(0)

        for contLinha, item in enumerate(listaItens):
            self.tblContribuicoes.insertRow(contLinha)

            # itemContribId - Coluna 0 (escondida)
            strItem = QTableWidgetItem(str(item.itemContribuicaoId))
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 0, strItem)

            # Nº - Coluna 1 (ativa)
            strItem = QTableWidgetItem(str(contLinha + 1))
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

            # Indicadores do CNIS - Coluna 4 (ativa)
            strItem = QTableWidgetItem(item.indicadores)
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 4, strItem)

            # Fator insalubridade - Coluna 5 (ativa)
            strItem = QTableWidgetItem(str(item.fatorInsalubridade) if item.fatorInsalubridade is not None else "-")
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 5, strItem)

            # Fator deficiência - Coluna 6 (ativa)
            strItem = QTableWidgetItem(GrauDeficiencia(item.grauDeficiencia).name.title() if item.grauDeficiencia is not None else "-")
            strItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            strItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblContribuicoes.setItem(contLinha, 6, strItem)

            # Botões de edição (Ações) - Coluna 7 <Aparente>
            hlOpcoes = QHBoxLayout()
            hlOpcoes.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

            pbEditar = QPushButton()
            pbEditar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.editar))
            pbEditar.setFixedSize(QSize(25, 25))
            pbEditar.clicked.connect(lambda state, item=item: self.avaliaOpcoes(item, TipoBotaoResumo.editar))

            pbDeletar = QPushButton()
            pbDeletar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.deletar))
            pbDeletar.setFixedSize(QSize(25, 25))
            pbDeletar.clicked.connect(lambda state, item=item: self.avaliaOpcoes(item, TipoBotaoResumo.deletar))

            hlOpcoes.addWidget(pbDeletar)
            hlOpcoes.addWidget(pbEditar)

            wdgAuxiliar = QWidget()
            wdgAuxiliar.setLayout(hlOpcoes)

            self.tblContribuicoes.setCellWidget(contLinha, 7, wdgAuxiliar)

        self.tblContribuicoes.resizeColumnsToContents()
        self.tblContribuicoes.resizeRowsToContents()

    def carregaTblBeneficios(self):
        dados: List[ItemContribuicao] = ItemContribuicao.select().where(
            ItemContribuicao.clienteId == self.cliente.clienteId,
            ItemContribuicao.tipo == TipoContribuicao.beneficio.value,
            ItemContribuicao.seq == self.vinculoAtual.seq
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
            if str(self.vinculoAtual.nb) == '':
                strNb = QTableWidgetItem('-')
            else:
                strNb = QTableWidgetItem(str(self.vinculoAtual.nb))
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

            # Botões de edição (Ações) - Coluna 5 <Aparente>
            hlOpcoes = QHBoxLayout()
            hlOpcoes.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

            pbEditar = QPushButton()
            pbEditar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.editar))
            pbEditar.setFixedSize(QSize(25, 25))
            pbEditar.clicked.connect(lambda state, beneficio=beneficio: self.avaliaOpcoes(beneficio, TipoBotaoResumo.editar))

            pbDeletar = QPushButton()
            pbDeletar.setStyleSheet(botaoOpcoes(TipoBotaoResumo.deletar))
            pbDeletar.setFixedSize(QSize(25, 25))
            pbDeletar.clicked.connect(lambda state, beneficio=beneficio: self.avaliaOpcoes(beneficio, TipoBotaoResumo.editar))

            hlOpcoes.addWidget(pbDeletar)
            hlOpcoes.addWidget(pbEditar)

            wdgAuxiliar = QWidget()
            wdgAuxiliar.setLayout(hlOpcoes)

            self.tblBeneficios.setCellWidget(contLinha, 5, wdgAuxiliar)

        self.tblBeneficios.resizeColumnsToContents()
        self.tblBeneficios.resizeRowsToContents()

    def carregaResumos(self):
        listaCabecalhos: List[CnisVinculos] = CnisVinculos.select().where(CnisVinculos.clienteId == self.cliente.clienteId)
        if len(listaCabecalhos) > 0:
            for cabecalho in listaCabecalhos:
                cabecalho = ItemResumoCnis(cabecalho, parent=self)
                self.vlResumos.addWidget(cabecalho)
        else:
            self.vlResumos.addWidget(ItemVazioCnis(self))

        self.wdgScroll.setLayout(self.vlResumos)
        self.carregaTempoVinculosNaTela()

    def carregaTempoVinculosNaTela(self):
        listaVinculos: List[CnisVinculos] = CnisVinculos.select().where(
            CnisVinculos.clienteId == self.cliente.clienteId,
            CnisVinculos.dataInicio is not None,
            CnisVinculos.dataFim is not None,
            CnisVinculos.dadoFaltante == False,
        ).order_by(
            CnisVinculos.dataInicio
        )

        tempoAte94 = tempoContribPorVinculo(listaVinculos, dataLimite=Evento.trocaMoedaRS.value)
        tempoAte98 = tempoContribPorVinculo(listaVinculos, dataLimite=datetime(1998, 1, 1).date())
        tempoAte2019 = tempoContribPorVinculo(listaVinculos, dataLimite=Evento.reforma2019.value)
        tempoAteHoje = tempoContribPorVinculo(listaVinculos, dataLimite=datetime.today().date())

        # Até a troca de moeda em 1994
        if tempoAte94.years <= 0:
            self.lbTpAte94.setText('-')
        elif tempoAte94.days >= 0:
            self.lbTpAte94.setText(f"{tempoAte94.years} anos, {tempoAte94.months} meses e {tempoAte94.days} dias")
        else:
            self.lbTpAte94.setText(f"{tempoAte94.years} anos e {tempoAte94.months} meses")

        # Até a reforma em 1998
        if tempoAte98.years <= 0:
            self.lbTpAte98.setText('-')
        elif tempoAte98.days >= 0:
            self.lbTpAte98.setText(f"{tempoAte98.years} anos, {tempoAte98.months} meses e {tempoAte98.days} dias")
        else:
            self.lbTpAte98.setText(f"{tempoAte98.years} anos e {tempoAte98.months} meses")

        # Até a reforma de 2019
        if tempoAte2019.years <= 0:
            self.lbTpAte2019.setText('-')
        elif tempoAte2019.days >= 0:
            self.lbTpAte2019.setText(f"{tempoAte2019.years} anos, {tempoAte2019.months} meses e {tempoAte2019.days} dias")
        else:
            self.lbTpAte2019.setText(f"{tempoAte2019.years} anos e {tempoAte2019.months} meses")

        # Até hoje
        if tempoAteHoje.years <= 0:
            self.lbTpAteHoje.setText('-')
        elif tempoAteHoje.days >= 0:
            self.lbTpAteHoje.setText(f"{tempoAteHoje.years} anos, {tempoAteHoje.months} meses e {tempoAteHoje.days} dias")
        else:
            self.lbTpAteHoje.setText(f"{tempoAteHoje.years} anos e {tempoAteHoje.months} meses")

    def contribsParaCadastrar(self) -> List:
        listaContrib: List[ItemContribuicao] = []

        for linha in range(self.tblCadContrib.rowCount()):
            if self.tblCadContrib.cellWidget(linha, 2).text() == '':
                popUpOkAlerta("O campo 'Salário de contribuição' não pode estar vazio.")
                return []
            salContribuicao = strToFloat(self.tblCadContrib.cellWidget(linha, 2).text())

            competencia = self.tblCadContrib.cellWidget(linha, 1).date().toPyDate()
            if not strToDate(self.vinculoAtual.dataInicio) < competencia < strToDate(self.vinculoAtual.dataFim, seErroVoltaHoje=competencia):
                dataFim = strToDate(self.vinculoAtual.dataFim, seErroVoltaHoje=competencia)

                popUpOkAlerta(
                    f"A competência {mascaraDataPequena(competencia)} está fora das datas de início e fim do vínculo.\n\n"
                    f"Data início: {mascaraData(self.vinculoAtual.dataInicio)}\n"
                    f"Data Fim: {mascaraData(dataFim)}"
                )
                return []

            listaContrib.append(
                ItemContribuicao(
                    clienteId=self.cliente,
                    tipo=TipoContribuicao.contribuicao.value,
                    seq=self.tblCadContrib.cellWidget(linha, 0).text(),
                    competencia=self.tblCadContrib.cellWidget(linha, 1).date().toPyDate(),
                    salContribuicao=salContribuicao,
                    contribuicao=salContribuicao * 0.2,
                    ativPrimaria=True,
                    dadoOrigem=ItemOrigem.NEWPREV.value,
                    indicadores=self.tblCadContrib.cellWidget(linha, 3).text()
                )
            )
        return listaContrib

    def criaVinculo(self, tipo: TipoContribuicao):
        try:
            seqMax: int = self.buscaNovoSeq()

            if tipo == TipoContribuicao.contribuicao:
                CnisVinculos.create(
                    clienteId=self.cliente,
                    seq=seqMax + 1,
                    cdEmp=self.leCnpj.text(),
                    dadoOrigem=ItemOrigem.NEWPREV.value,
                    dataInicio=self.dtDataInicio.date().toPyDate(),
                    dataFim=self.dtDataFim.date().toPyDate(),
                    # especie=self.cbxEspecie.currentText() if self.cbxEspecie.currentText() != '' else None,
                    # indicadores=self.leIndicadores.text() if self.leIndicadores.text() != '' else None,
                    indicadores=None,
                    nit=self.clienteInfoProf.nit,
                    nomeEmp=self.leNomeEmp.text().upper(),
                    tipoVinculo=self.cbxTipoVinculo.currentText(),
                    ultRem=self.dtDataFim.date().toPyDate())
            else:
                CnisVinculos.create(
                    clienteId=self.cliente,
                    seq=seqMax + 1,
                    dadoOrigem=ItemOrigem.NEWPREV.value,
                    dataFim=self.dtDataFimBene.date().toPyDate(),
                    dataInicio=self.dtDataInicioBene.date().toPyDate(),
                    especie=self.cbxEspecie.currentText(),
                    nb=int(self.leNb.text()),
                    nit=self.clienteInfoProf.nit,
                    orgVinculo='BENEFICIO',
                    situacao=self.cbxSituacao.currentText(),
                    ultRem=self.dtDataFimBene.date().toPyDate(),
                )

        except Exception as err:
            # TODO: LOG
            print(f"criaVinculo: {err=}")
            popUpOkAlerta("Não foi possível salvar o vínculo editado. Entre em contato com o suporte.", erro=f"{err}")
            return False
        return True

    def datasCorretas(self):
        if self.rbContribuicao.isChecked():
            return self.dtDataFim.date() > self.dtDataInicio.date()
        else:
            return self.dtDataFimBene.date() > self.dtDataInicioBene.date()

    def excluirItem(self, itemTabela: ItemContribuicao):
        try:
            info(f'{TipoLog.DataBase.value}::excluirItem _________________ {itemTabela.itemContribuicaoId}')
            ItemContribuicao.delete_by_id(itemTabela.itemContribuicaoId)
            if self.toasty is None:
                self.toasty = QToaster(self)
            self.toasty.showMessage(self, f"Competência {mascaraData(itemTabela.competencia)} excluída com sucesso")
            self.carregaTblContribuicoes()

        except Exception as err:
            error(f"{TipoLog.Cache.value}::excluirItem", extra={"err": err})
        finally:
            return True

    def getFatorInsalubridade(self) -> float:
        try:
            if self.cbxInsalubridade.currentText() == 'Zerar':
                return -1.0

            index = self.cbxInsalubridade.currentText().find('|')
            return float(self.cbxInsalubridade.currentText()[index + 1:])
        except ValueError as err:
            return None

    def getGrauDeficiencia(self) -> int:
        if self.cbxDeficiencia.currentText() == 'Zerar':
            return -1

        for grau in GrauDeficiencia:
            if grau.name.title() == self.cbxDeficiencia.currentText():
                return grau.value

        return None

    def getInsalubridadeDaTabela(self) -> bool:
        temInsalubridade: bool = False

        for numLinha in range(self.tblContribuicoes.rowCount()):
            if self.tblContribuicoes.item(numLinha, 5).text() != '-':
                temInsalubridade = True
                break

        return temInsalubridade

    def iniciaCampos(self):
        listaEspecies: List[EspecieBene] = EspecieBene.select()
        self.cbxEspecie.clear()
        for especie in listaEspecies:
            self.cbxEspecie.addItem(f"{especie.especieId} - {especie.descricao}")

        self.cbxSituacao.addItems(sorted(situacaoBeneficio))

        listaTipoVinculos = (vinculo.value for vinculo in TipoVinculo)
        self.cbxTipoVinculo.clear()
        self.cbxTipoVinculo.addItems(sorted(listaTipoVinculos))

        if self.cliente is not None:

            # ComboBox insalubridade
            self.cbxInsalubridade.clear()
            self.cbxInsalubridade.addItem('-')
            if self.cliente.genero == 'M':
                for fator in FatorTmpInsalubridade:
                    if 'M' in fator.name:
                        self.cbxInsalubridade.addItem(f"{fator.name[:len(fator.name) - 1].title()} | {fator.value}")
            else:
                for fator in FatorTmpInsalubridade:
                    if 'F' in fator.name:
                        self.cbxInsalubridade.addItem(f"{fator.name[:len(fator.name) - 1].title()} | {fator.value}")
            self.cbxInsalubridade.addItem('Zerar')

            # ComboBox deficiência
            self.cbxDeficiencia.clear()
            self.cbxDeficiencia.addItem('-')
            for grau in GrauDeficiencia:
                self.cbxDeficiencia.addItem(f'{grau.name.title()}')
            self.cbxDeficiencia.addItem('Zerar')

    def insereContribuicoes(self, listaContribuicoes: List[ItemContribuicao]) -> bool:
        try:
            for item in listaContribuicoes:
                item.save()

            if self.vinculoAtual.nb is None:
                self.trocaTela(TelaResumo.contribuicoes)
            else:
                self.trocaTela(TelaResumo.beneficios)
            return True
        except Exception as err:
            print(f"insereContribuicoes: {err=}")
            popUpOkAlerta("Não foi possível inserir uma competência. \nVerifique as datas e os salários de contribuição.")
            return False

    def limpaCabecalhos(self):
        limpaLayout(self.vlResumos)

    def limpaVinculos(self):
        self.leNb.setText("")
        self.leCnpj.setText("")
        self.leNomeEmp.setText("")
        self.cbxTipoVinculo.setCurrentIndex(0)
        self.cbxSituacao.setCurrentIndex(0)
        self.cbxEspecie.setCurrentIndex(0)

    def permiteTrocaTela(self, tela: TelaResumo) -> bool:
        if self.telaAtual == TelaResumo.resumos:
            # Mensagem, caso não permita trocar a tela
            if tela == TelaResumo.beneficios:
                mensagem = f"A entrada selecionada não é um benefício."
            else:
                mensagem = f"A entrada selecionada é um benefício e não uma contribuição."

            # Resumos -> Contribuições
            if tela == TelaResumo.contribuicoes:
                for index in range(self.vlResumos.count()):
                    wdgCabecalho: ItemResumoCnis = self.vlResumos.itemAt(index).widget()
                    if wdgCabecalho.selecionado and wdgCabecalho.vinculoAtual.vinculoId == self.vinculoAtual.vinculoId:
                        ehBeneficio: bool = self.vinculoAtual.nb is not None
                        if ehBeneficio:
                            if self.toasty is None:
                                self.toasty = QToaster(self)
                            self.toasty.showMessage(self, mensagem)

                        return not ehBeneficio

            # Resumos -> Benefícios
            elif tela == TelaResumo.beneficios:
                for index in range(self.vlResumos.count()):
                    wdgCabecalho: ItemResumoCnis = self.vlResumos.itemAt(index).widget()
                    if wdgCabecalho.selecionado and wdgCabecalho.vinculoAtual.vinculoId == self.vinculoAtual.vinculoId:
                        ehBeneficio: bool = self.vinculoAtual.nb is not None
                        if not ehBeneficio:
                            if self.toasty is None:
                                self.toasty = QToaster(self)
                            self.toasty.showMessage(self, mensagem)
                        return ehBeneficio

            elif tela == TelaResumo.addVinculo:
                return True

        # Qualquer tela -> Resumo
        else:
            return True

        return False

    def recebeCliente(self, cliente: Cliente):
        if cliente is not None:
            self.cliente = cliente
            self.clienteInfoProf = ClienteProfissao.get_by_id(self.cliente.dadosProfissionais)
            self.carregaClienteNaTela()
            self.carregaResumos()
            self.iniciaCampos()

    def recebeIndicadores(self, listaIndicadores: List[str]):
        if len(listaIndicadores) > 0:
            self.cbxIndicadores.clear()
            for indicador in listaIndicadores:
                self.cbxIndicadores.addItem(indicador)

    def recebeVinculoSelecionado(self, cabecalho: CnisVinculos):
        self.vinculoAtual = cabecalho
        for index in range(self.vlResumos.count()):
            wdgCabecalho: ItemResumoCnis = self.vlResumos.itemAt(index).widget()
            if wdgCabecalho.selecionado:
                if wdgCabecalho.vinculoAtual.vinculoId != cabecalho.vinculoId:
                    wdgCabecalho.desselecionaCabecalho()
                break

        self.atualizaTmpContrib()
        self.carregaFirula()

        if self.vinculoAtual.nb is None:
            self.trocaTela(TelaResumo.contribuicoes)
        else:
            self.trocaTela(TelaResumo.beneficios)

        self.carregaDadoFaltanteInsalubridade(wdgCabecalho)

    def replicarInsercao(self, qtdReplicacao: int, salContrib: int):
        tipoContrib = TipoContribuicao.contribuicao if self.vinculoAtual.nb is None else TipoContribuicao.beneficio

        for seqContrib in range(qtdReplicacao):
            self.adicionaLinhaCadastro(tipoContrib, salContrib)

    def trocaVinculo(self, tipo: TipoContribuicao):
        if tipo == TipoContribuicao.contribuicao:
            self.rbContribuicao.setChecked(True)
            self.rbBeneficio.setChecked(False)
        else:
            self.rbContribuicao.setChecked(False)
            self.rbBeneficio.setChecked(True)

        self.stkVinculo.setCurrentIndex(tipo.value)

    def trocaTela(self, tela: TelaResumo, tipoContribuicao: TipoContribuicao = TipoContribuicao.contribuicao, itemContribuicao: ItemContribuicao = None):
        if not self.permiteTrocaTela(tela):
            # TODO: Responder a negação com as devidas mensagens explicando por que não foi possível trocar de tela
            return False

        self.telaAtual = tela
        self.frBotoes.show()

        if tela == TelaResumo.resumos:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, True))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, False))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, False))
            self.vinculoAtual = None

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

        elif tela == TelaResumo.addVinculo:
            self.frBotoes.hide()
            self.trocaVinculo(tipoContribuicao)

        elif tela == TelaResumo.addContriBene:
            self.frBotoes.hide()
            self.tblCadContrib.setRowCount(0)
            self.tblCadBene.setRowCount(0)
            self.stkCadastro.setCurrentIndex(tipoContribuicao.value)
            self.adicionaLinhaCadastro(tipoContribuicao)

            if tipoContribuicao == TipoContribuicao.contribuicao:
                self.lbInfoCadastrar.setText("Cadastrar contribuições")
            else:
                self.lbInfoCadastrar.setText("Cadastrar benefícios")

            if itemContribuicao is not None:
                self.carregaContribBeneEdicao(tipoContribuicao, itemContribuicao)

        self.stkCliente.setCurrentIndex(tela.value)

    def vinculoParaEdicao(self, vinculo: CnisVinculos):
        if vinculo is not None:
            self.vinculoAtual = vinculo
            self.limpaVinculos()

            if vinculo.nb is not None:
                # É um benefício
                tipoVinculo = TipoContribuicao.beneficio
                self.leNb.setText(str(vinculo.nb))

                if vinculo.dataInicio is not None and vinculo.dataInicio != '':
                    self.dtDataInicioBene.setDate(strToDate(vinculo.dataInicio))

                if vinculo.dataFim is not None and vinculo.dataFim != '':
                    self.dtDataFimBene.setDate(strToDate(vinculo.dataFim))

            else:
                # É uma contribuição
                tipoVinculo = TipoContribuicao.contribuicao
                self.leNomeEmp.setText(vinculo.nomeEmp)
                self.leCnpj.setText(mascaraCNPJ(vinculo.cdEmp))

                if vinculo.dataInicio is not None:
                    self.dtDataInicio.setDate(strToDate(vinculo.dataInicio))

                if vinculo.dataFim is not None and vinculo.dataFim != '':
                    self.dtDataFim.setDate(strToDate(vinculo.dataFim))

                if vinculo.indicadores is not None and vinculo.dataFim != '':
                    # TODO: ADICIONAR INDICADORES VINDOS DO CNIS
                    pass

            self.trocaTela(TelaResumo.addVinculo, tipoContribuicao=tipoVinculo)
