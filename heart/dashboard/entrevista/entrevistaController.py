from datetime import datetime

import util.popUps
from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio
from connections import ConfigConnection

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Design.pyUi.entrevistaPage import Ui_mwEntrevistaPage

from heart.dashboard.entrevista.naturezaController import NaturezaController
from heart.dashboard.entrevista.tipoProcessoAdmController import TipoProcessoAdmController
from heart.dashboard.entrevista.tipoBeneficioController import TipoBeneficioConcController
from heart.dashboard.entrevista.tipoAtividadeController import TipoAtividadeController
from heart.dashboard.tabs.clienteController import TabCliente
from heart.dashboard.entrevista.localWidgets.pgConfigSimulacao import PgConfigSimulacao
from heart.processos.processoController import ProcessosController
from heart.dashboard.gerarDocsPage import GerarDocsPage
from heart.dashboard.entrevista.localStyleSheet.cabecalho import *
from sinaisCustomizados import Sinais

from modelos.processosORM import Processos
from modelos.clienteORM import Cliente
from modelos.advogadoORM import Advogados
from modelos.escritoriosORM import Escritorios

from Design.CustomWidgets.infoGuiaEntrevista import InfoGuia

from processos.aposentadoria import CalculosAposentadoria
# from compilado.aposentadoria import CalculosAposentadoria

from util.enums.newPrevEnums import *
from util.enums.aposentadoriaEnums import *
from util.enums.processoEnums import NaturezaProcesso, TipoProcesso, TipoBeneficioEnum
from util.popUps import popUpOkAlerta


class EntrevistaController(QMainWindow, Ui_mwEntrevistaPage):
    aposentadoriaModelo: CalculosAposentadoria = None
    processoModelo: Processos
    advogadoAtual: Advogados
    clienteAtual: Cliente
    infoNatureza: InfoGuia
    infoTipo: InfoGuia
    infoBeneficio: InfoGuia
    infoQuestionario: InfoGuia
    clienteController: TabCliente
    naturezaPg: NaturezaController
    tipoProcessoAdmPg: TipoProcessoAdmController
    tipoBeneficioConcPg: TipoBeneficioConcController
    tipoAtividadePg: TipoAtividadeController
    impressaoDocsPg: GerarDocsPage
    escritorioAtual: Escritorios
    entrevistaParams: dict = {
        'contribSimulacao': ContribSimulacao.ULTI,
        'valorSimulacao': 0.0,
        'porcentagemCont': 11,
        'indiceReajuste': IndiceReajuste.Ipca
    }
    processosController: ProcessosController

    def __init__(self, parent=None):
        super(EntrevistaController, self).__init__(parent)
        self.setupUi(self)
        self.tipoConexao = TiposConexoes.nuvem
        self.dbConnection = ConfigConnection(instanciaBanco=self.tipoConexao)
        self.parent = parent
        self.sinais = Sinais()
        self.telaAtual = MomentoEntrevista.cadastro
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.escondeLoading)

        self.setWindowTitle("Entrevista - [entrevistaController]")

        self.iniciaInfoEntrevista()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTelaCentral)
        self.sinais.sAtualizaListaClientes.connect(self.atualizaClientes)

        self.stackedWidget.addWidget(self.clienteController)  # tela: cadastro - 0
        self.stackedWidget.addWidget(self.naturezaPg)  # tela: naturezaProcesso - 1
        self.stackedWidget.addWidget(self.tipoProcessoAdmPg)  # tela: tiposESubtipos de processos admnistrativos - 2
        self.stackedWidget.addWidget(self.tipoBeneficioConcPg)  # tela: tiposESubtipos de benefícios Concessão -  3
        self.stackedWidget.addWidget(self.tipoAtividadePg)  # tela: tiposESubtipos de atividade Aposentadoria - 4
        self.stackedWidget.addWidget(self.impressaoDocsPg)  # tela: tiposESubtipos de geração de documentos - 5

        self.pbProxEtapa.clicked.connect(lambda: self.avaliaTrocaTela())
        self.pbVoltaEtapa.clicked.connect(lambda: self.avaliaTrocaTela(proxima=False))
        self.pbConfSimulacao.clicked.connect(self.abreTelaConfiguracoes)

        self.pbarProgresso.hide()
        self.frame.show()

        self.buscaAdvogadoAtual()
        self.iniciaInfoGuia()

        self.atualizaEtapa(EtapaEntrevista.infoPessoais, False)
        self.atualizaEtapa(EtapaEntrevista.infoProcessual, False)
        self.atualizaEtapa(EtapaEntrevista.detalhamento, False)
        self.atualizaEtapa(EtapaEntrevista.documentacao, False)

        self.stackedWidget.setCurrentIndex(self.telaAtual.value)

    def iniciaInfoEntrevista(self):
        cacheAdv = CacheLogin()
        cacheEscritorio = CacheEscritorio()
        self.clienteAtual = Cliente()
        self.processoModelo = Processos()

        self.advogadoAtual = cacheAdv.carregarCache()
        if self.advogadoAtual is None:
            self.advogadoAtual = cacheAdv.carregarCacheTemporario()

        if self.advogadoAtual is None:
            util.popUps.popUpOkAlerta('Erro ao carregar informações do advogado atual', erro='[entrevistaController] - iniciaInfoEntrevista')
            return False

        self.escritorioAtual = cacheEscritorio.carregarCache()
        if self.escritorioAtual is None:
            self.escritorioAtual = cacheEscritorio.carregarCacheTemporario()

        if self.advogadoAtual is None:
            util.popUps.popUpOkAlerta('Erro ao carregar informações do advogado atual', erro='[entrevistaController] - iniciaInfoEntrevista')
            return False

        self.clienteController = TabCliente(parent=self, entrevista=True)
        self.naturezaPg = NaturezaController(self.advogadoAtual, self.processoModelo, parent=self)
        self.tipoProcessoAdmPg = TipoProcessoAdmController(parent=self)
        self.tipoBeneficioConcPg = TipoBeneficioConcController(parent=self)
        self.tipoAtividadePg = TipoAtividadeController(parent=self)
        self.impressaoDocsPg = GerarDocsPage(None, None, parent=self)

    def abreTelaConfiguracoes(self):
        pgConfigSimulacao = PgConfigSimulacao(self.entrevistaParams, parent=self)
        pgConfigSimulacao.show()

    def avaliaTrocaTela(self, proxima=True):
        """
        QtCore.pyqtSignal([MomentoEntrevista, Tipo] name='tela')
        :cvar
        """
        self.telaAtual = MomentoEntrevista(self.stackedWidget.currentIndex())

        if not self.clienteAtual:
            self.loading(20)
            self.showPopupAlerta("Para seguir para a próxima estapa da entrevista, é necessário definir um cliente.")
            self.loading(100)
            return False
        if proxima:
            if self.telaAtual == MomentoEntrevista.cadastro:

                self.loading(20)
                self.naturezaPg.atualizaClienteAtual(self.clienteAtual)
                self.processoModelo.advogadoId = self.advogadoAtual
                self.processoModelo.estado = self.escritorioAtual.estado

                self.loading(20)
                self.clienteController.verificaDados()

                self.loading(20)
                self.clienteController.trataAtualizaCliente()

                self.loading(20)
                self.sinais.sTrocaTelaEntrevista.emit([MomentoEntrevista.cadastro, None])
                self.telaAtual = MomentoEntrevista.naturezaProcesso
                self.atualizaEtapa(EtapaEntrevista.infoPessoais, completo=True)
                self.loading(20)

            elif self.telaAtual == MomentoEntrevista.naturezaProcesso:
                self.telaAtual = MomentoEntrevista.tipoProcesso
                self.infoNatureza.atualizaInfo(NaturezaProcesso(self.processoModelo.natureza).name, True)
                self.tipoProcessoAdmPg.atualizaProcesso(self.processoModelo)
                self.sinais.sTrocaTelaEntrevista.emit([MomentoEntrevista.naturezaProcesso, MomentoEntrevista.tipoProcesso])

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
                    self.processoModelo.processosId = Processos(**self.processoModelo.toDict()).save()
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

    def buscaAdvogadoAtual(self):
        cacheAdv = CacheLogin()

        self.advogadoAtual = cacheAdv.carregarCache()
        if self.advogadoAtual is None:
            self.advogadoAtual = cacheAdv.carregarCacheTemporario()
            if self.advogadoAtual is None:
                popUpOkAlerta('O cadastro do advogado atual não pode ser carregado. Informe a equipe técnica.')
                self.close()

    def iniciaInfoGuia(self):
        # Natureza
        self.infoNatureza = InfoGuia('A escolher', False, parent=self.frGuia)
        self.vlNatureza.addWidget(self.infoNatureza)

        # Tipo processo
        self.infoTipo = InfoGuia('A escolher', False, parent=self.frGuia)
        self.vlTipo.addWidget(self.infoTipo)

        # Tipo benefício
        self.infoBeneficio = InfoGuia('A escolher', False, parent=self.frGuia)
        self.vlBeneficio.addWidget(self.infoBeneficio)

        # Tipo benefício
        self.infoQuestionario = InfoGuia('-', False, parent=self.frGuia)
        self.vlQuestionario.addWidget(self.infoQuestionario)

        # Rodapé
        self.lbNomeAdv.setText(self.advogadoAtual.nomeAdvogado + self.advogadoAtual.sobrenomeAdvogado)
        self.lbNumOab.setText(str(self.advogadoAtual.numeroOAB))
        self.lbNomeEscritorio.setText(self.escritorioAtual.nomeFantasia)

    def trocaTelaCentral(self, *args):
        wdgAtual: MomentoEntrevista = MomentoEntrevista(self.stackedWidget.currentIndex())
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

            if wdgFuturo == MomentoEntrevista.tipoProcesso:
                self.stackedWidget.setCurrentIndex(2)
            elif wdgFuturo == NaturezaProcesso.judicial:
                self.processoModelo.natureza = NaturezaProcesso.judicial.value
                # TODO: wdgAtual dos tiposESubtipos de processos judiciais
                pass
            else:
                self.stackedWidget.setCurrentIndex(0)

        # O usuário está na wdgAtual sobre o tipo de processo
        elif wdgAtual == MomentoEntrevista.tipoProcesso:
            self.telaAtual = MomentoEntrevista.tipoProcesso
            self.tipoBeneficioConcPg.atualizaProcesso(self.processoModelo)
            if wdgFuturo == TipoProcesso.Concessao:
                self.processoModelo.tipoProcesso = TipoProcesso.Concessao.value
                self.stackedWidget.setCurrentIndex(3)
                self.infoTipo.atualizaInfo("Concessão", True)
            elif wdgFuturo == TipoProcesso.Revisao:
                self.processoModelo.tipoProcesso = TipoProcesso.Revisao.value
                self.infoTipo.atualizaInfo("Revisão", True)
                # TODO: Tela dos tiposESubtipos de benefícios de revisão
                pass
            elif wdgFuturo == TipoProcesso.RecOrdinario:
                self.processoModelo.tipoProcesso = TipoProcesso.RecOrdinario.value
                self.infoTipo.atualizaInfo("Recurso ordinário", True)
                # TODO: Tela dos tiposESubtipos de benefícios de recurso ordinário
                pass
            elif wdgFuturo == TipoProcesso.RecEspecial:
                self.processoModelo.tipoProcesso = TipoProcesso.RecEspecial.value
                self.infoTipo.atualizaInfo("Recurso especial", True)
                # TODO: Tela dos tiposESubtipos de benefícios de recurso especial
                pass
            else:
                self.stackedWidget.setCurrentIndex(1)

        # O usuário está na wdgAtual sobre o tipo de benefícios
        elif wdgAtual == MomentoEntrevista.tipoBeneficio:
            self.atualizaEtapa(EtapaEntrevista.infoProcessual, completo=True)

            if wdgFuturo is not None:
                self.pbProxEtapa.setText('Concluir')
                self.infoBeneficio.atualizaInfo(wdgFuturo.name, True)

                if wdgFuturo == TipoBeneficioEnum.Aposentadoria:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.Aposentadoria.value
                    self.tipoAtividadePg.pegaClienteAtual(self.clienteAtual)
                    self.stackedWidget.setCurrentIndex(4)
                elif wdgFuturo == TipoBeneficioEnum.AuxDoenca:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.AuxDoenca.value
                    # TODO: wdgAtual dos tiposESubtipos de atividades auxílio doença
                    pass
                elif wdgFuturo == TipoBeneficioEnum.AuxAcidente:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.AposTempoContr.value
                    # TODO: wdgAtual dos tiposESubtipos de atividades aposentadoria por tempo de contribuição
                    pass
                elif wdgFuturo == TipoBeneficioEnum.AuxReclusao:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.AuxReclusao.value
                    # TODO: wdgAtual dos tiposESubtipos de atividades auxílio reclusão
                    pass
                elif wdgFuturo == TipoBeneficioEnum.BeneIdoso:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.BeneIdoso.value
                    # TODO: wdgAtual dos tiposESubtipos de atividades benefício idoso
                    pass
                elif wdgFuturo == TipoBeneficioEnum.BeneDeficiencia:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.BeneDeficiencia.value
                    # TODO: wdgAtual dos tiposESubtipos de atividades benefício deficientes
                    pass
                elif wdgFuturo == TipoBeneficioEnum.PensaoMorte:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.PensaoMorte.value
                    # TODO: wdgAtual dos tiposESubtipos de atividades pensão por morte
                    pass
                elif wdgFuturo == TipoBeneficioEnum.SalMaternidade:
                    self.telaAtual = MomentoEntrevista.tipoAtividade
                    self.processoModelo.tipoBeneficio = TipoBeneficioEnum.SalMaternidade.value
                    # TODO: wdgAtual dos tiposESubtipos de atividades salário maternidade
                    pass
                else:
                    self.stackedWidget.setCurrentIndex(2)

        # O usuário está na wdgAtual sobre o Quiz
        elif wdgAtual == MomentoEntrevista.tipoAtividade:
            self.atualizaEtapa(EtapaEntrevista.detalhamento, completo=True)
            self.telaAtual = MomentoEntrevista.telaGeraDocs
            self.pbProxEtapa.setText('Gerar documentos')
            self.stackedWidget.setCurrentIndex(5)

            calculaAposentadoria = CalculosAposentadoria(self.processoModelo, self.clienteAtual, self.entrevistaParams)
            calculaAposentadoria.salvaAposentadorias()

            ProcessosController(cliente=self.clienteAtual, processo=self.processoModelo, parent=self).showMaximized()
            self.close()

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

    def atualizaCliente(self, *args):
        self.clienteAtual: Cliente = args[0]
        if self.clienteAtual is not None:
            if self.processoModelo.processoId is None:
                self.processoModelo = Processos.create(
                    clienteId=self.clienteAtual,
                    dataUltAlt=datetime.now()
                )
            else:
                self.processoModelo.clienteId = self.clienteAtual
                self.processoModelo.dataUltAlt = datetime.now()
                self.processoModelo.save()

    def calculaDer(self) -> datetime.date:
        if self.processoModelo.natureza == NaturezaProcesso.administrativo.value:
            if self.processoModelo.tipoProcesso == TipoProcesso.Concessao.value:
                return datetime.today()

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
