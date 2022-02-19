from typing import List, Generator
from peewee import SqliteDatabase, fn
from datetime import datetime

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem, QPushButton, QHBoxLayout, QLineEdit, QDateEdit, QComboBox

from Design.CustomWidgets.newToast import QToaster
from Design.pyUi.wdgResumoCNIS import Ui_wdgResumoCnis
from Design.pyUi.efeitos import Efeitos
from SQLs.itensContribuicao import remuEContrib
from modelos.especieBenefORM import EspecieBene

from util.enums.dashboardEnums import TelaAtual
from util.enums.newPrevEnums import TipoContribuicao, TipoEdicao, Prioridade, ItemOrigem
from util.enums.resumoCnisEnums import TelaResumo, TipoBotaoResumo, TipoVinculo
from util.enums.databaseEnums import DatabaseEnum

from .localStyleSheet.resumoCnis import selecionaBotao, botaoOpcoes, cadDataEdit
from .localWidgets.wdgItemCabecalho import ItemResumoCnis
from .localWidgets.itemVazioResumoCnis import ItemVazioCnis

from modelos.clienteORM import Cliente
from modelos.cabecalhoORM import CnisCabecalhos
from modelos.Auxiliares.remuEContribs import RemuEContribs
from modelos.itemContribuicao import ItemContribuicao
from modelos.clienteProfissao import ClienteProfissao

from util.helpers import mascaraCPF, mascaraCNPJ, mascaraDinheiro, dataUSAtoBR, situacaoBeneficio
from util.layoutHelpers import limpaLayout
from util.popUps import popUpSimCancela, popUpOkAlerta
from util.dateHelper import mascaraData, strToDate

from systemLog.logs import logPrioridade
from ..informacoesTelas.indicadoresTela import IndicadoresController


class ResumoCnisController(QWidget, Ui_wdgResumoCnis):
    cliente: Cliente
    clienteInfoProf: ClienteProfissao
    telaAtual: TelaResumo
    cabecalhoAtual: CnisCabecalhos
    vlResumos: QVBoxLayout = QVBoxLayout()
    toasty: QToaster

    def __init__(self, parent=None):
        super(ResumoCnisController, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent

        self.telaAtual = TelaResumo.resumos
        self.cabecalhoAtual = None
        self.toasty = None

        self.tblContribuicoes.horizontalHeader().show()
        self.tblContribuicoes.hideColumn(0)

        self.tblBeneficios.horizontalHeader().show()
        self.tblBeneficios.hideColumn(0)

        self.tblCadBene.hideColumn(0)
        self.tblCadBene.resizeColumnsToContents()
        self.tblCadContrib.resizeColumnsToContents()

        Efeitos().shadowCards([self.pbAddContrib, self.pbAddBene], radius=10, offset=(1, 4), color=(63, 63, 63, 100))
        
        self.iniciaCampos()

        self.pbEmpresas.clicked.connect(lambda: self.trocaTela(TelaResumo.resumos))
        self.pbContrib.clicked.connect(lambda: self.trocaTela(TelaResumo.contribuicoes))
        self.pbBeneficios.clicked.connect(lambda: self.trocaTela(TelaResumo.beneficios))
        self.pbVoltar.clicked.connect(self.avaliaVoltar)
        self.pbInserirResumo.clicked.connect(self.avaliaInserirVinculo)
        self.rbBeneficio.clicked.connect(lambda: self.avaliaTrocaVinculo(TipoVinculo.beneficio))
        self.rbContribuicao.clicked.connect(lambda: self.avaliaTrocaVinculo(TipoVinculo.contribuicao))
        self.pbSeguir.clicked.connect(self.avaliaSalvarVinculo)
        self.pbCancelar.clicked.connect(self.avaliaCancelar)
        self.pbInserirContrib.clicked.connect(lambda: self.trocaTela(TelaResumo.addContriBene, tipoVinculo=TipoVinculo.contribuicao))
        self.pbInserirBeneficios.clicked.connect(lambda: self.trocaTela(TelaResumo.addContriBene, tipoVinculo=TipoVinculo.beneficio))
        self.pbAddContrib.clicked.connect(lambda: self.adicionaLinhaCadastro(TipoVinculo.contribuicao))
        self.pbAddBene.clicked.connect(lambda: self.adicionaLinhaCadastro(TipoVinculo.beneficio))
        self.pbBuscaIndicador.clicked.connect(lambda: IndicadoresController(retornaIndicadores=True, parent=self).show())

        self.trocaTela(self.telaAtual)

    def adicionaLinhaCadastro(self, tipo: TipoVinculo):
        if tipo == TipoVinculo.contribuicao:
            linhaDeInsercao = self.tblCadContrib.rowCount()
            self.tblCadContrib.insertRow(linhaDeInsercao)

            # seq - Coluna 1 (aparente)
            leSeqVinculo = QLineEdit()
            leSeqVinculo.setDisabled(True)
            leSeqVinculo.setMinimumHeight(35)
            leSeqVinculo.setMaximumHeight(40)
            if self.cabecalhoAtual is not None:
                leSeqVinculo.setText(str(self.cabecalhoAtual.seq))
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 0, leSeqVinculo)

            # Competência - Coluna 2 (aparente)
            dtCompetencia = QDateEdit()
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
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 2, leSalContrib)

            # Indicadores - Coluna 3 (aparente)
            leIndicadores = QLineEdit()
            # leIndicadores.setStyleSheet(cadLineEdit())
            leIndicadores.setMinimumHeight(35)
            leIndicadores.setMaximumHeight(40)
            self.tblCadContrib.setCellWidget(linhaDeInsercao, 3, leIndicadores)

            self.tblCadContrib.resizeColumnsToContents()
            self.tblCadContrib.resizeRowsToContents()

        else:
            pass

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

    def atualizaVinculoEditado(self):
        if self.rbContribuicao.isChecked():
            self.cabecalhoAtual.nomeEmp = self.leNomeEmp.text()
            self.cabecalhoAtual.cdEmp = self.leCnpj.text()
            self.cabecalhoAtual.dataInicio = self.dtDataInicio.date().toPyDate()
            self.cabecalhoAtual.dataFim = self.dtDataFim.date().toPyDate()
            # self.cabecalhoAtual.indicadores = self.leIndicadores.text()
            self.cabecalhoAtual.dataUltAlt = datetime.now()
        else:
            self.cabecalhoAtual.nb = self.leNb.text()
            self.cabecalhoAtual.dataInicio = self.dtDataInicioBene.date().toPyDate()
            self.cabecalhoAtual.dataFim = self.dtDataFimBene.date().toPyDate()
            self.cabecalhoAtual.dataUltAlt = datetime.now()
        self.cabecalhoAtual.save()

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

    def avaliaInserirVinculo(self):
        if self.cliente is not None:
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
            print(f"Editou o item {itemContribuicao.competencia}")
        else:
            popUpSimCancela(
                f"Você deseja excluir a competência {mascaraData(itemContribuicao.competencia)}?",
                funcaoSim=lambda: self.excluirItem(itemContribuicao),
            )

    def avaliaSalvarVinculo(self):
        # TODO: criar validação da data de inicio e/ou fim
        if self.cabecalhoAtual is not None:
            self.atualizaVinculoEditado()

        elif self.rbContribuicao.isChecked():
            if self.leNomeEmp.text() != "" and self.leCnpj.text() != "":
                self.criaVinculo(TipoVinculo.contribuicao)
            else:
                popUpOkAlerta("Não foi possível salvar o vínculo editado pois o nome da empresa ou o CNPJ não foram inseridos")
                if self.leNomeEmp == '':
                    self.leNomeEmp.setFocus()
                else:
                    self.leCnpj.setFocus()
        else:
            if self.leNb.text() != "":
                self.criaVinculo(TipoVinculo.beneficio)
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

    def avaliaTrocaVinculo(self, tipo: TipoVinculo):
        # Verifica se o usuário não clicou sem querer em algum dos radioButton
        if tipo == TipoVinculo.contribuicao:
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
            # TODO: Criar lógica para voltar para a tela das contribuições/benefícios que o advogado estava
            self.trocaTela(TelaResumo.resumos)
        else:
            self.trocaTela(TelaResumo.resumos)

    def buscaNovoSeq(self) -> int:
        try:
            maxSeq = ItemContribuicao.select(fn.MAX(ItemContribuicao.seq)).where(
                ItemContribuicao.clienteId == self.cliente.clienteId
            ).scalar()
            if maxSeq is None:
                return 1
        except Exception as err:
            # TODO: LOG
            return 999
        return 999

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
        listaCabecalhos: List[CnisCabecalhos] = CnisCabecalhos.select().where(CnisCabecalhos.clienteId == self.cliente.clienteId)
        if len(listaCabecalhos) > 0:
            for cabecalho in listaCabecalhos:
                cabecalho = ItemResumoCnis(cabecalho, parent=self)
                self.vlResumos.addWidget(cabecalho)
        else:
            self.vlResumos.addWidget(ItemVazioCnis(self))

        self.wdgScroll.setLayout(self.vlResumos)

    def criaVinculo(self, tipo: TipoVinculo):
        try:
            seqMax: int = self.buscaNovoSeq()

            if tipo == TipoVinculo.contribuicao:
                CnisCabecalhos.create(
                    clienteId=self.cliente,
                    seq=seqMax,
                    cdEmp=self.leCnpj.text(),
                    dadoOrigem=ItemOrigem.NEWPREV.value,
                    dataInicio=self.dtDataInicio.date().toPyDate(),
                    dataFim=self.dtDataFim.date().toPyDate(),
                    especie=self.cbxEspecie.currentText() if self.cbxEspecie.currentText() != '' else None,
                    # indicadores=self.leIndicadores.text() if self.leIndicadores.text() != '' else None,
                    indicadores=None,
                    nit=self.clienteInfoProf.nit,
                    nomeEmp=self.leNomeEmp.text(),
                    tipoVinculo=self.cbxTipoVinculo.currentText(),
                    ultRem=self.dtDataFim.date().toPyDate())
            else:
                CnisCabecalhos.create(
                    clienteId=self.cliente,
                    seq=seqMax,
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

    def excluirItem(self, itemTabela: ItemContribuicao):
        try:
            logPrioridade(f'DELETE<excluirItem>___________________{itemTabela.itemContribuicaoId=}', tipoEdicao=TipoEdicao.insert, priodiade=Prioridade.saidaComum)
            ItemContribuicao.delete_by_id(itemTabela.itemContribuicaoId)
            if self.toasty is None:
                self.toasty = QToaster(self)
            self.toasty.showMessage(self, f"Competência {mascaraData(itemTabela.competencia)} excluída com sucesso")
            self.carregaTblContribuicoes()
        except Exception as err:
            logPrioridade(f'DELETE<excluirItem>::erro ___________________{err=}', tipoEdicao=TipoEdicao.insert, priodiade=Prioridade.saidaComum)
        finally:
            return True
        
    def iniciaCampos(self):
        listaEspecies: List[EspecieBene] = EspecieBene.select()
        for especie in listaEspecies:
            self.cbxEspecie.addItem(f"{especie.especieId} - {especie.descricao}")

        self.cbxSituacao.addItems(sorted(situacaoBeneficio))

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
                    if wdgCabecalho.selecionado and wdgCabecalho.cabecalhoAtual.cabecalhosId == self.cabecalhoAtual.cabecalhosId:
                        ehBeneficio: bool = self.cabecalhoAtual.nb is not None
                        if ehBeneficio:
                            if self.toasty is None:
                                self.toasty = QToaster(self)
                            self.toasty.showMessage(self, mensagem)

                        return not ehBeneficio

            # Resumos -> Benefícios
            elif tela == TelaResumo.beneficios:
                for index in range(self.vlResumos.count()):
                    wdgCabecalho: ItemResumoCnis = self.vlResumos.itemAt(index).widget()
                    if wdgCabecalho.selecionado and wdgCabecalho.cabecalhoAtual.cabecalhosId == self.cabecalhoAtual.cabecalhosId:
                        ehBeneficio: bool = self.cabecalhoAtual.nb is not None
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

    def recebeIndicadores(self, listaIndicadores: List[str]):
        if len(listaIndicadores) > 0:
            self.cbxIndicadores.clear()
            for indicador in listaIndicadores:
                self.cbxIndicadores.addItem(indicador)

    def trocaVinculo(self, tipo: TipoVinculo):
        if tipo == TipoVinculo.contribuicao:
            self.rbContribuicao.setChecked(True)
            self.rbBeneficio.setChecked(False)
        else:
            self.rbContribuicao.setChecked(False)
            self.rbBeneficio.setChecked(True)

        self.stkVinculo.setCurrentIndex(tipo.value)

    def trocaTela(self, tela: TelaResumo, tipoVinculo: TipoVinculo = TipoVinculo.contribuicao):
        if not self.permiteTrocaTela(tela):
            # TODO: Responder a negação com as devidas mensagens explicando por que não foi possível trocar de tela
            return False

        self.telaAtual = tela
        self.frBotoes.show()

        if tela == TelaResumo.resumos:
            self.frEmpresas.setStyleSheet(selecionaBotao(TelaResumo.resumos, True))
            self.frContrib.setStyleSheet(selecionaBotao(TelaResumo.contribuicoes, False))
            self.frBeneficios.setStyleSheet(selecionaBotao(TelaResumo.beneficios, False))
            self.cabecalhoAtual = None

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
            self.trocaVinculo(tipoVinculo)

        elif tela == TelaResumo.addContriBene:
            self.frBotoes.hide()
            self.tblCadContrib.setRowCount(0)
            self.tblCadBene.setRowCount(0)
            self.stkCadastro.setCurrentIndex(tipoVinculo.value)
            self.adicionaLinhaCadastro(tipoVinculo)

        self.stkCliente.setCurrentIndex(tela.value)

    def vinculoParaEdicao(self, vinculo: CnisCabecalhos):
        if vinculo is not None:
            self.cabecalhoAtual = vinculo
            self.limpaVinculos()

            if vinculo.nb is not None:
                # É um benefício
                tipoVinculo = TipoVinculo.beneficio
                self.leNb.setText(str(vinculo.nb))

                if vinculo.dataInicio is not None and vinculo.dataInicio != '':
                    self.dtDataInicioBene.setDate(strToDate(vinculo.dataInicio))

                if vinculo.dataFim is not None and vinculo.dataFim != '':
                    self.dtDataFimBene.setDate(strToDate(vinculo.dataFim))

            else:
                # É uma contribuição
                tipoVinculo = TipoVinculo.contribuicao
                self.leNomeEmp.setText(vinculo.nomeEmp)
                self.leCnpj.setText(mascaraCNPJ(vinculo.cdEmp))

                if vinculo.dataInicio is not None:
                    self.dtDataInicio.setDate(strToDate(vinculo.dataInicio))

                if vinculo.dataFim is not None and vinculo.dataInicio != '':
                    self.dtDataFim.setDate(strToDate(vinculo.dataFim))

                if vinculo.indicadores is not None and vinculo.dataFim != '':
                    # TODO: ADICIONAR INDICADORES VINDOS DO CNIS
                    pass

            self.trocaTela(TelaResumo.addVinculo, tipoVinculo=tipoVinculo)

