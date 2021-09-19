from datetime import datetime
from connections import ConfigConnection

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Design.pyUi.entrevistaPage import Ui_mwEntrevistaPage

from heart.dashboard.entrevista.localStyleSheet.lateral import estadoInfoFinalizado
from heart.dashboard.entrevista.naturezaController import NaturezaController
from heart.dashboard.entrevista.tipoProcessoAdmController import TipoProcessoAdmController
from heart.dashboard.entrevista.tipoBeneficioController import TipoBeneficioConcController
from heart.dashboard.entrevista.tipoAtividadeController import TipoAtividadeController
from heart.dashboard.tabs.clienteController import TabCliente
from heart.dashboard.gerarDocsPage import GerarDocsPage
from heart.dashboard.entrevista.localStyleSheet.cabecalho import *
from heart.sinaisCustomizados import Sinais

# from Daos.daoProcessos import DaoProcessos
# from Daos.daoCliente import DaoCliente

from modelos.processosORM import Processos
from modelos.clienteORM import Cliente

from processos.aposentadoria import CalculosAposentadoria

from util.enums.newPrevEnums import *


class EntrevistaController(QMainWindow, Ui_mwEntrevistaPage):

    def __init__(self, parent=None, db=None):
        super(EntrevistaController, self).__init__(parent)
        self.setupUi(self)
        self.tipoConexao = TiposConexoes.nuvem
        self.dbConnection = ConfigConnection(instanciaBanco=self.tipoConexao)
        self.db = db
        self.parent = parent
        self.sinais = Sinais()
        self.telaAtual = MomentoEntrevista.cadastro
        self.clienteAtual = Cliente()
        self.processoModelo = Processos()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.escondeLoading)

        self.setWindowTitle("Entrevista - [entrevistaController]")

        self.clienteController = TabCliente(parent=self, db=self.db, entrevista=True)
        self.naturezaPg = NaturezaController(parent=self, db=self.db)
        self.tipoProcessoAdmPg = TipoProcessoAdmController(parent=self, db=self.db)
        self.tipoBeneficioConcPg = TipoBeneficioConcController(parent=self, db=self.db)
        self.tipoAtividadePg = TipoAtividadeController(parent=self, db=self.db)
        self.impressaoDocsPg = GerarDocsPage(None, None, parent=self, db=self.db)
        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTelaCentral)
        self.sinais.sAtualizaListaClientes.connect(self.atualizaClientes)

        self.stackedWidget.addWidget(self.clienteController)  # tela: cadastro - 0
        self.stackedWidget.addWidget(self.naturezaPg)  # tela: naturezaProcesso - 1
        self.stackedWidget.addWidget(self.tipoProcessoAdmPg)  # tela: tipos de processos admnistrativos - 2
        self.stackedWidget.addWidget(self.tipoBeneficioConcPg)  # tela: tipos de benefícios Concessão -  3
        self.stackedWidget.addWidget(self.tipoAtividadePg)  # tela: tipos de atividade Aposentadoria - 4
        self.stackedWidget.addWidget(self.impressaoDocsPg)  # tela: tipos de geração de documentos - 5

        self.pbProxEtapa.clicked.connect(lambda: self.avaliaTrocaTela())
        self.pbVoltaEtapa.clicked.connect(lambda: self.avaliaTrocaTela(proxima=False))

        self.pbarProgresso.hide()
        self.frame.show()

        self.atualizaEtapa(EtapaEntrevista.infoPessoais, False)
        self.atualizaEtapa(EtapaEntrevista.infoProcessual, False)
        self.atualizaEtapa(EtapaEntrevista.detalhamento, False)
        self.atualizaEtapa(EtapaEntrevista.documentacao, False)

        self.lbInfo1.setText('Informações \npessoais')
        self.lbInfo2.setText('Informações \nresidenciais')
        self.lbInfo3.setText('Informações \nprofissionais')
        self.lbInfo4.setText('Informações \nbancárias')

        self.stackedWidget.setCurrentIndex(self.telaAtual.value)

    def avaliaTrocaTela(self, proxima=True):
        """
        QtCore.pyqtSignal([MomentoEntrevista, Tipo] name='tela')
        :cvar
        """
        if not self.clienteAtual:
            self.loading(20)
            self.showPopupAlerta("Para seguir para a próxima estapa da entrevista, é necessário definir um cliente.")
            self.loading(100)
            return False
        if proxima:
            if self.telaAtual == MomentoEntrevista.cadastro:

                self.loading(20)
                self.processoModelo.clienteId = self.clienteAtual.clienteId

                self.loading(20)
                self.clienteController.verificaDados()

                self.loading(20)
                self.clienteController.trataAtualizaCliente()

                self.loading(20)
                self.sinais.sTrocaTelaEntrevista.emit([MomentoEntrevista.cadastro, None])
                self.telaAtual = MomentoEntrevista.naturezaProcesso
                self.atualizaEtapa(EtapaEntrevista.infoPessoais, completo=True)
                self.loading(20)

            elif self.telaAtual == MomentoEntrevista.tipoBeneficio:
                self.telaAtual = MomentoEntrevista.naturezaProcesso
                self.sinais.sTrocaTelaEntrevista.emit([None, None])
                # TODO: Processar as atividades checadas/conferidas
                pass

            elif self.telaAtual == MomentoEntrevista.tipoAtividade:
                self.loading(20)
                self.processoModelo.subTipoApos = 0

                self.loading(20)
                self.processoModelo.dib = self.calculaDib()

                self.loading(20)
                self.processoModelo.der = self.calculaDer()

                self.loading(10)
                # self.processoModelo.tempoContribuicao = self.calculaTempoContribuicao()

                self.loading(10)
                # self.processoModelo.processosId = self.daoProcesso.insereProcesso(self.processoModelo)
                try:
                    self.processoModelo.processosId = Processos().insert(**self.processoModelo.toDict()).on_conflict_replace().execute()
                except Processos.DoesNotExist:
                    print('Fudeu aqui!')

                self.loading(10)
                self.impressaoDocsPg.atualizaInformacoes(self.processoModelo, self.clienteAtual)

                self.loading(10)
                self.sinais.sTrocaTelaEntrevista.emit([MomentoEntrevista.tipoAtividade, MomentoEntrevista.telaGeraDocs])

            else:
                self.impressaoDocsPg.gerarDocumentosSelecionados()
                self.sinais.sTrocaTelaEntrevista.emit([MomentoEntrevista.telaGeraDocs, MomentoEntrevista.cadastro])

        else:
            self.loading(20)
            if self.telaAtual == MomentoEntrevista.naturezaProcesso:
                self.sinais.sTrocaTelaEntrevista.emit([None, None])
                self.telaAtual = MomentoEntrevista.cadastro
                self.atualizaEtapa(EtapaEntrevista.infoPessoais, completo=False)

            elif self.telaAtual == MomentoEntrevista.tipoProcesso:
                self.sinais.sTrocaTelaEntrevista.emit([None, None])
                self.telaAtual = MomentoEntrevista.naturezaProcesso

            elif self.telaAtual == MomentoEntrevista.tipoBeneficio:
                self.sinais.sTrocaTelaEntrevista.emit([None, None])
                self.telaAtual = MomentoEntrevista.tipoProcesso

            elif self.telaAtual == MomentoEntrevista.tipoAtividade:
                self.sinais.sTrocaTelaEntrevista.emit([None, None])
                self.telaAtual = MomentoEntrevista.tipoBeneficio

            elif self.telaAtual == MomentoEntrevista.telaGeraDocs:
                self.sinais.sTrocaTelaEntrevista.emit([None, None])
                self.telaAtual = MomentoEntrevista.tipoAtividade

    def trocaTelaCentral(self, *args):
        wdgAtual: MomentoEntrevista = args[0][0]
        wdgFuturo = args[0][1]
        self.pbProxEtapa.setText('Próxima etapa')

        if wdgAtual is None:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

        # O usuário está na wdgAtual de cadastro
        elif wdgAtual == MomentoEntrevista.cadastro:
            if wdgFuturo is None:
                self.stackedWidget.setCurrentIndex(1)
            else:
                self.stackedWidget.setCurrentIndex(0)

        # O usuário está na wdgAtual sobre a natureza do processo
        elif wdgAtual == MomentoEntrevista.naturezaProcesso:
            self.telaAtual = MomentoEntrevista.naturezaProcesso
            if wdgFuturo == NaturezaProcesso.administrativo:
                self.processoModelo.natureza = NaturezaProcesso.administrativo.value
                self.stackedWidget.setCurrentIndex(2)
            elif wdgFuturo == NaturezaProcesso.judicial:
                self.processoModelo.natureza = NaturezaProcesso.judicial.value
                # TODO: wdgAtual dos tipos de processos judiciais
                pass
            else:
                self.stackedWidget.setCurrentIndex(0)

        # O usuário está na wdgAtual sobre o tipo de processo
        elif wdgAtual == MomentoEntrevista.tipoProcesso:

            self.telaAtual = MomentoEntrevista.tipoProcesso
            if wdgFuturo == TipoProcesso.Concessao:
                self.processoModelo.tipoProcesso = TipoProcesso.Concessao.value
                self.stackedWidget.setCurrentIndex(3)
            elif wdgFuturo == TipoProcesso.Revisao:
                self.processoModelo.tipoProcesso = TipoProcesso.Revisao.value
                # TODO: Tela dos tipos de benefícios de revisão
                pass
            elif wdgFuturo == TipoProcesso.RecOrdinario:
                self.processoModelo.tipoProcesso = TipoProcesso.RecOrdinario.value
                # TODO: Tela dos tipos de benefícios de recurso ordinário
                pass
            elif wdgFuturo == TipoProcesso.RecEspecial:
                self.processoModelo.tipoProcesso = TipoProcesso.RecEspecial.value
                # TODO: Tela dos tipos de benefícios de recurso especial
                pass
            else:
                self.stackedWidget.setCurrentIndex(1)

        # O usuário está na wdgAtual sobre o tipo de benefícios
        elif wdgAtual == MomentoEntrevista.tipoBeneficio:

            self.telaAtual = MomentoEntrevista.tipoBeneficio
            self.pbProxEtapa.setText('Concluir')

            if wdgFuturo == TipoBeneficio.Aposentadoria:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.Aposentadoria.value
                self.tipoAtividadePg.pegaClienteAtual(self.clienteAtual)
                self.stackedWidget.setCurrentIndex(4)
            elif wdgFuturo == TipoBeneficio.AposTempoContr:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.AposTempoContr.value
                # TODO: wdgAtual dos tipos de atividades aposentadoria por tempo de contribuição
                pass
            elif wdgFuturo == TipoBeneficio.AuxDoenca:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.AuxDoenca.value
                # TODO: wdgAtual dos tipos de atividades auxílio doença
                pass
            elif wdgFuturo == TipoBeneficio.AuxReclusao:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.AuxReclusao.value
                # TODO: wdgAtual dos tipos de atividades auxílio reclusão
                pass
            elif wdgFuturo == TipoBeneficio.BeneIdoso:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.BeneIdoso.value
                # TODO: wdgAtual dos tipos de atividades benefício idoso
                pass
            elif wdgFuturo == TipoBeneficio.BeneDeficiencia:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.BeneDeficiencia.value
                # TODO: wdgAtual dos tipos de atividades benefício deficientes
                pass
            elif wdgFuturo == TipoBeneficio.PensaoMorte:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.PensaoMorte.value
                # TODO: wdgAtual dos tipos de atividades pensão por morte
                pass
            elif wdgFuturo == TipoBeneficio.SalMaternidade:
                self.telaAtual = MomentoEntrevista.tipoAtividade
                self.processoModelo.tipoBeneficio = TipoBeneficio.SalMaternidade.value
                # TODO: wdgAtual dos tipos de atividades salário maternidade
                pass
            else:
                self.stackedWidget.setCurrentIndex(2)

        elif wdgAtual == MomentoEntrevista.tipoAtividade:
            self.telaAtual = MomentoEntrevista.telaGeraDocs
            self.pbProxEtapa.setText('Gerar documentos')
            self.stackedWidget.setCurrentIndex(5)

            calculaAposentadoria = CalculosAposentadoria(self.processoModelo, self.clienteAtual, db=self.db, dib=datetime(year=2020, month=6, day=15))
        else:
            if wdgFuturo == MomentoEntrevista.cadastro:
                self.telaAtual = MomentoEntrevista.cadastro
                self.pbProxEtapa.setText('Próxima etapa')
                self.stackedWidget.setCurrentIndex(0)

    def atualizaEtapa(self, etapa: EtapaEntrevista, completo: bool):
        if etapa == EtapaEntrevista.infoPessoais:
            self.lbInfoPessoais.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa1.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))
            self.frProg1.setStyleSheet(infoPontinhosCabecalho(etapa, completo=completo))
        elif etapa == EtapaEntrevista.infoProcessual:
            self.lbInfoProcessuais.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa2.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))
            self.frProg2.setStyleSheet(infoPontinhosCabecalho(etapa, completo=completo))
        elif etapa == EtapaEntrevista.detalhamento:
            self.lbInfoDetalhamento.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa3.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))
            self.frProg3.setStyleSheet(infoPontinhosCabecalho(etapa, completo=completo))
        elif etapa == EtapaEntrevista.documentacao:
            self.lbInfoFinalizacao.setStyleSheet(infoLabelCabecalho(etapa, completo=completo))
            self.frEtapa4.setStyleSheet(infoIconeCabecalho(etapa, completo=completo))

    def atualizaInfoLateral(self, *args, **kwargs):
        estadoEntrevista: dict = args[0]
        self.frInfo1Icon.setStyleSheet(estadoInfoFinalizado('pessoais', estadoEntrevista['pessoais']))
        self.frInfo2Icon.setStyleSheet(estadoInfoFinalizado('residenciais', estadoEntrevista['residenciais']))
        self.frInfo3Icon.setStyleSheet(estadoInfoFinalizado('profissionais', estadoEntrevista['profissionais']))
        self.frInfo4Icon.setStyleSheet(estadoInfoFinalizado('bancarias', estadoEntrevista['bancarias']))

    def atualizaCliente(self, *args):
        self.clienteAtual: Cliente = args[0]

    def calculaDer(self) -> datetime:
        if self.processoModelo.natureza == NaturezaProcesso.administrativo.value:
            if self.processoModelo.tipoProcesso == TipoProcesso.Concessao.value:
                return datetime.now()

    def calculaDib(self) -> datetime:
        pass

    def showPopupAlerta(self, mensagem, titulo='Atenção!'):
        dialogPopup = QMessageBox()
        dialogPopup.setWindowTitle(titulo)
        dialogPopup.setText(mensagem)
        dialogPopup.setIcon(QMessageBox.Warning)
        dialogPopup.setStandardButtons(QMessageBox.Ok)

        close = dialogPopup.exec_()
        
    def loading(self, value: int):
        self.pbarProgresso.show()
        valor: int = value + self.pbarProgresso.value()
        self.pbarProgresso.setValue(valor)

        if valor >= 100:
            self.timer.start(500)
            
    def escondeLoading(self):
        self.pbarProgresso.hide()
        self.pbarProgresso.setValue(0)
        self.timer.stop()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.sinais.sAtualizaListaClientes.emit()

    def atualizaClientes(self):
        self.parent.atualizaTabClientes()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = EntrevistaController()
    ui.show()
    sys.exit(app.exec_())
