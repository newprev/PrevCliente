from logging import Logger
from typing import List

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

from Design.pyUi.processoPage import Ui_wdgProcessoPage
from Design.efeitos import Efeitos
from Design.CustomWidgets.newToast import QToaster
from geracaoDocumentos.geraDocsGerais import GeracaoDocumentos
from heart.buscaClientePage import BuscaClientePage
from heart.processos.localStyleSheet.processo import habDesCheckBox
from heart.processos.localWidgets.cardIncidenteProcessual import CardIncidenteProcessual
from modelos.clienteORM import Cliente
from modelos.incidenteProcessual import IncidenteProcessual
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from sinaisCustomizados import Sinais
from systemLog.logs import NewLogging
from heart.buscaProcessoPage import BuscaProcessosPage

from util.enums.dashboardEnums import TelaAtual
from util.enums.geracaoDocumentos import EnumDocumento
from util.enums.processoEnums import SituacaoTela
from util.ferramentas.layout import limpaLayout
from util.helpers.helpers import strNatureza, strTipoBeneficio, strTipoProcesso, mascaraTelCel
from util.popUps import popUpSimCancela, popUpOkAlerta


class ProcessoPage(QWidget, Ui_wdgProcessoPage):
    situacaoTela: SituacaoTela = SituacaoTela.clienteFaltante
    clienteAtual: Cliente
    telefoneAtual: Telefones
    apiLogger: Logger
    processoAtual: Processos
    efeitos: Efeitos
    
    docsHabilitados: dict = {
        EnumDocumento.procuracao: True,
        EnumDocumento.decHipossuficiencia: True,
        EnumDocumento.decPensionista: False,
        EnumDocumento.docsComprobatorios: True,
        EnumDocumento.honorarios: False,
        EnumDocumento.requerimento: False,
    }
    
    docsGerar: dict = {
        EnumDocumento.procuracao: False,
        EnumDocumento.decHipossuficiencia: False,
        EnumDocumento.decPensionista: False,
        EnumDocumento.docsComprobatorios: False,
        EnumDocumento.honorarios: False,
        EnumDocumento.requerimento: False,        
    }

    def __init__(self, cliente: Cliente = None, parent=None):
        super(ProcessoPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.apiLogger = NewLogging().buscaLogger()
        self.efeitos = Efeitos()
        self.clienteAtual = cliente
        self.sinais = Sinais()
        self.dashboard = parent
        self.toasty: QToaster = None

        self.efeitos.shadowCards([self.frBotoesDocs], color=(63, 63, 63, 80), radius=5, offset=(1, 1))
        self.atualizaCheckboxDocumentos()
        self.iniciaCheckboxes()

        self.pbBuscarCliente.clicked.connect(self.abreTelaBuscaCliente)
        self.pbAlterarProcesso.clicked.connect(self.abreBuscaProcesso)
        self.pbVoltar.clicked.connect(self.voltarDashboard)
        self.sinais.sVoltaTela.connect(self.avaliaVoltar)
        self.pbGeraPdf.clicked.connect(self.avaliaGerarPdfs)

        if self.clienteAtual is not None:
            self.carregarInfoCliente(self.clienteAtual.clienteId)
            self.atualizaSituacaoTela(SituacaoTela.processoFaltante)
        else:
            self.atualizaSituacaoTela(SituacaoTela.clienteFaltante)

    def abreBuscaProcesso(self):
        if self.clienteAtual.clienteId is not None:
            buscaProcessoPage = BuscaProcessosPage(self.clienteAtual, parent=self)
            buscaProcessoPage.show()
            buscaProcessoPage.raise_()
        else:
            self.apiLogger.warning("Buscou processo sem nenhum cliente selecionado.")

    def abreTelaBuscaCliente(self):
        buscaClienteTela = BuscaClientePage(parent=self)
        buscaClienteTela.show()
        buscaClienteTela.raise_()

    def atualizaSituacaoTela(self, situacao: SituacaoTela):
        # stkInfoCliente[0] = Botão para buscar cliente
        # stkInfoCliente[1] = Informações do cliente buscado

        if situacao == SituacaoTela.clienteFaltante:
            self.stkInfoCliente.setCurrentIndex(0)
            self.limpaCliente()

            self.frCardProcesso.hide()

        elif situacao == SituacaoTela.processoFaltante:
            self.stkInfoCliente.setCurrentIndex(1)
            self.carregaClienteNaTela()
            self.limpaProcesso()

        else:
            self.carregaClienteNaTela()
            self.stkInfoCliente.setCurrentIndex(1)
            self.frCardProcesso.show()
            
    def avaliaGerarPdfs(self) -> bool:
        if not any(self.docsGerar.values()):
            popUpOkAlerta("Você não selecionou nenhum documento para ser gerado.\nSelecione um documento e tente novamente.")
            return False

        mensagemPopup: str = "Você irá gerar os arquivos PDFs dos seguintes documentos:\n"
        for chave, selecionado in self.docsGerar.items():
            if chave == EnumDocumento.requerimento and selecionado:
                mensagemPopup += '\n-Requerimento do processo'

            elif chave == EnumDocumento.procuracao and selecionado:
                mensagemPopup += '\n  -Procuração'

            elif chave == EnumDocumento.honorarios and selecionado:
                mensagemPopup += '\n  -Declaração de honorários'

            elif chave == EnumDocumento.decPensionista and selecionado:
                mensagemPopup += '\n  -Declaração de pensionista'

            elif chave == EnumDocumento.docsComprobatorios and selecionado:
                mensagemPopup += '\n  -Documentos coprobatórios'

            elif chave == EnumDocumento.decHipossuficiencia and selecionado:
                mensagemPopup += '\n  -Declaração de hipossuficiência'

        mensagemPopup += '\n\nDeseja continuar?'
        popUpSimCancela(mensagemPopup, funcaoSim=self.geraPdfs)
        return True

    def avaliaVoltar(self):
        self.dashboard.trocaTela(TelaAtual.Cliente)

    def carregaClienteNaTela(self):
        self.lbNomeCliente.setText(f"{self.clienteAtual.nomeCliente} {self.clienteAtual.sobrenomeCliente}")
        self.lbClienteTelefone.setText(mascaraTelCel(self.telefoneAtual.numero))
        self.lbClienteEmail.setText(self.clienteAtual.email)

        mapFoto = QPixmap('/home/israeldev/Imagens/photo_2022-03-25_21-28-00.jpg')
        self.lbClienteFoto.setPixmap(mapFoto)
        self.lbClienteFoto.setScaledContents(True)
        
    def atualizaCheckboxDocumentos(self):
        for chave, valor in self.docsHabilitados.items():
            if chave == EnumDocumento.decHipossuficiencia:
                self.cbDecHipossuficiencia.setDisabled(not valor)
                self.cbDecHipossuficiencia.setStyleSheet(habDesCheckBox('cbDecHipossuficiencia', not valor))

            elif chave == EnumDocumento.honorarios:
                self.cbHonorarios.setDisabled(not valor)
                self.cbHonorarios.setStyleSheet(habDesCheckBox('cbHonorarios', not valor))

            elif chave == EnumDocumento.requerimento:
                self.cbRequerimento.setDisabled(not valor)
                self.cbRequerimento.setStyleSheet(habDesCheckBox('cbRequerimento', not valor))

            elif chave == EnumDocumento.decPensionista:
                self.cbDecPensionista.setDisabled(not valor)
                self.cbDecPensionista.setStyleSheet(habDesCheckBox('cbDecPensionista', not valor))

            elif chave == EnumDocumento.procuracao:
                self.cbProcuracao.setDisabled(not valor)
                self.cbProcuracao.setStyleSheet(habDesCheckBox('cbProcuracao', not valor))

            elif chave == EnumDocumento.docsComprobatorios:
                self.cbDocsComprobatorios.setDisabled(not valor)
                self.cbDocsComprobatorios.setStyleSheet(habDesCheckBox('cbDocsComprobatorios', not valor))

    def alteraEstadoCheckbox(self, tipoDoc: EnumDocumento, estado: int):
        # estado = 2 -> A checkbox está checada
        self.docsGerar[tipoDoc] = estado == 2

    def carregarInfoCliente(self, clienteId: int = 0):
        try:
            self.clienteAtual = Cliente.get_by_id(clienteId)
            self.telefoneAtual = Telefones.select().where(Telefones.clienteId == self.clienteAtual.clienteId).get()
            listaProcessos: List[Processos] = Processos.select().where(
                Processos.clienteId == self.clienteAtual.clienteId
            ).order_by(
                Processos.processoId.desc()
            )

            if len(listaProcessos):
                self.processoAtual = listaProcessos[0]
                if self.processoAtual.numeroProcesso is None:
                    self.lbNumProcesso.setText(" - ")
                else:
                    self.lbNumProcesso.setText(f"{self.processoAtual.numeroProcesso}")

                self.lbNatureza.setText(strNatureza(self.processoAtual.natureza))
                self.lbTpBeneficio.setText(strTipoBeneficio(self.processoAtual.tipoBeneficio, self.processoAtual.regraAposentadoria))
                self.lbTpProcesso.setText(strTipoProcesso(self.processoAtual.tipoProcesso))
                self.atualizaSituacaoTela(SituacaoTela.processoEncontrado)

        except Cliente.DoesNotExist as err:
            self.apiLogger.error("Não encontrou o cliente", extra={'err': err, 'clienteId': clienteId})

        except Exception as err:
            print(f"{err=}")

    def carregaIncidentesNaTela(self):
        if self.wdgListaAndamentos.layout() is None:
            vlIncidentes = QVBoxLayout()
        else:
            vlIncidentes = self.wdgListaAndamentos.layout()
            limpaLayout(vlIncidentes)

        listaIncidentes: List[IncidenteProcessual] = IncidenteProcessual.select().where(
            IncidenteProcessual.processoId == self.processoAtual.processoId
        ).order_by(
            IncidenteProcessual.seq
        )

        listaCardsIncidentes = (CardIncidenteProcessual(incidente, parent=self) for incidente in listaIncidentes)

        for wdgIncidente in listaCardsIncidentes:
            vlIncidentes.addWidget(wdgIncidente)

        self.wdgListaAndamentos.setLayout(vlIncidentes)
        vlIncidentes.addStretch()

    def geraPdfs(self):
        try:
            geradorDocs = GeracaoDocumentos(self.processoAtual, self.clienteAtual)

            for tipoDoc, geraDoc in self.docsGerar.items():
                if tipoDoc == EnumDocumento.procuracao and geraDoc:
                    geradorDocs.criaProcuracao()
                elif tipoDoc == EnumDocumento.decHipossuficiencia and geraDoc:
                    geradorDocs.criaDeclaracaoHipo()
                elif tipoDoc == EnumDocumento.docsComprobatorios and geraDoc:
                    geradorDocs.criaDocumentosComprobatorios()

            if self.toasty is None:
                self.toasty = QToaster(self)
            self.toasty.showMessage(self, "Documentos gerados com sucesso")

        except Exception as err:
            print(f"Não foi possível gerar o(s) PDFs: {err}")
            self.apiLogger.error("Não foi possível gerar o(s) PDFs", extra={'err': err})

    def iniciaCheckboxes(self):
        self.cbProcuracao.stateChanged.connect(lambda state: self.alteraEstadoCheckbox(EnumDocumento.procuracao, state))
        self.cbRequerimento.stateChanged.connect(lambda state: self.alteraEstadoCheckbox(EnumDocumento.requerimento, state))
        self.cbHonorarios.stateChanged.connect(lambda state: self.alteraEstadoCheckbox(EnumDocumento.honorarios, state))
        self.cbDecPensionista.stateChanged.connect(lambda state: self.alteraEstadoCheckbox(EnumDocumento.decPensionista, state))
        self.cbDocsComprobatorios.stateChanged.connect(lambda state: self.alteraEstadoCheckbox(EnumDocumento.docsComprobatorios, state))
        self.cbDecHipossuficiencia.stateChanged.connect(lambda state: self.alteraEstadoCheckbox(EnumDocumento.decHipossuficiencia, state))

    def recebeProcesso(self, processoId: int):
        try:
            self.processoAtual = Processos.get_by_id(processoId)

            self.lbNatureza.setText(strNatureza(self.processoAtual.natureza))
            self.lbTpBeneficio.setText(strTipoBeneficio(self.processoAtual.tipoBeneficio, self.processoAtual.regraAposentadoria))
            self.lbTpProcesso.setText(strTipoProcesso(self.processoAtual.tipoProcesso))
            if self.processoAtual.numeroProcesso is None:
                self.lbNumProcesso.setText(" - ")
            else:
                self.lbNumProcesso.setText(f"{self.processoAtual.numeroProcesso}")

            self.frCardProcesso.show()
            self.carregaIncidentesNaTela()
        except Exception as err:
            self.apiLogger.error("Tentou carregar o processo, mas não foi possível", extra={"err": err})

    def limpaCliente(self):
        self.lbNomeCliente.setText('')
        self.lbClienteEmail.setText('')
        self.lbClienteTelefone.setText('')

    def limpaProcesso(self):
        print('limpaProcesso')

    def voltarDashboard(self):
        self.sinais.sVoltaTela.emit()


