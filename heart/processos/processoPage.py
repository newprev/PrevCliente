from logging import Logger
from typing import List

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from Design.efeitos import Efeitos
from Design.pyUi.processoPage import Ui_wdgProcessoPage
from heart.buscaClientePage import BuscaClientePage
from heart.processos.localWidgets.cardIncidenteProcessual import CardIncidenteProcessual
from modelos.clienteORM import Cliente
from modelos.incidenteProcessual import IncidenteProcessual
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from sinaisCustomizados import Sinais
from systemLog.logs import NewLogging
from heart.buscaProcessoPage import BuscaProcessosPage
from util.enums.dashboardEnums import TelaAtual

from util.enums.processoEnums import SituacaoTela
from util.ferramentas.layout import limpaLayout
from util.helpers.helpers import strNatureza, strTipoBeneficio, strTipoProcesso, mascaraTelCel


class ProcessoPage(QWidget, Ui_wdgProcessoPage):
    situacaoTela: SituacaoTela = SituacaoTela.clienteFaltante
    clienteAtual: Cliente
    telefoneAtual: Telefones
    apiLogger: Logger
    processoAtual: Processos
    efeitos: Efeitos

    def __init__(self, cliente: Cliente = None, parent=None):
        super(ProcessoPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.apiLogger = NewLogging().buscaLogger()
        self.efeitos = Efeitos()
        self.clienteAtual = cliente
        self.sinais = Sinais()
        self.dashboard = parent

        self.efeitos.shadowCards([self.frBotoesDocs], color=(63, 63, 63, 80), radius=5, offset=(1, 1))

        self.pbBuscarCliente.clicked.connect(self.abreTelaBuscaCliente)
        self.pbAlterarProcesso.clicked.connect(self.abreBuscaProcesso)
        self.pbVoltar.clicked.connect(self.voltarDashboard)
        self.sinais.sVoltaTela.connect(self.avaliaVoltar)

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

    def avaliaVoltar(self):
        self.dashboard.trocaTela(TelaAtual.Cliente)

    def carregaClienteNaTela(self):
        self.lbNomeCliente.setText(f"{self.clienteAtual.nomeCliente} {self.clienteAtual.sobrenomeCliente}")
        self.lbClienteTelefone.setText(mascaraTelCel(self.telefoneAtual.numero))
        self.lbClienteEmail.setText(self.clienteAtual.email)

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
                self.lbNumProcesso.setText(f"{self.processoAtual.numeroProcesso}")
                self.lbNatureza.setText(strNatureza(self.processoAtual.natureza))
                self.lbTpBeneficio.setText(strTipoBeneficio(self.processoAtual.tipoBeneficio, self.processoAtual.subTipoApos))
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

    def recebeProcesso(self, processoId: int):
        try:
            self.processoAtual = Processos.get_by_id(processoId)
            self.lbNumProcesso.setText(f"{self.processoAtual.numeroProcesso}")
            self.lbNatureza.setText(strNatureza(self.processoAtual.natureza))
            self.lbTpBeneficio.setText(strTipoBeneficio(self.processoAtual.tipoBeneficio, self.processoAtual.subTipoApos))
            self.lbTpProcesso.setText(strTipoProcesso(self.processoAtual.tipoProcesso))

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


