from PyQt5.QtWidgets import QMainWindow
from Design.pyUi.processoPg import Ui_mwProcessoPage
from typing import List

from heart.buscaClientePage import BuscaClientePage
from heart.buscaProcessoPage import BuscaProcessosPage
from heart.dashboard.processos.localStyleSheet.processo import layoutBotaoGuia
from heart.dashboard.processos.localWidgets.tabAposentadorias import TabAposentariasController

from modelos.clienteORM import Cliente
from modelos.processosORM import Processos
from modelos.advogadoORM import Advogados
from modelos.escritoriosORM import Escritorios
from modelos.aposentadoriaORM import Aposentadoria

from cache.cacheEscritorio import CacheEscritorio
from cache.cachingLogin import CacheLogin

from util.enums.aposentadoriaEnums import TelaAtiva
from util.enums.processoEnums import TipoBeneficio, TipoProcesso, SituacaoProcesso
from util.helpers import mascaraCPF
from util.popUps import popUpOkAlerta


class ProcessosController(QMainWindow, Ui_mwProcessoPage):
    clienteAtual: Cliente
    processoAtual: Processos
    advogadoAtual: Advogados
    escritorioAtual: Escritorios
    telaAtual: TelaAtiva
    listaAposentadorias: List[Aposentadoria]

    def __init__(self, cliente: Cliente = None, processo: Processos = None, parent=None):
        super(ProcessosController, self).__init__(parent=parent)
        self.setupUi(self)

        self.clienteAtual: Cliente = cliente
        self.processoAtual: Processos = processo
        self.tabAposController = TabAposentariasController()
        self.vlAposentadoria.addWidget(self.tabAposController)

        self.carregaEscritorio()
        self.carregaAdvogado()
        self.telaAtual = TelaAtiva(0)

        self.pbBuscaCliente.clicked.connect(self.abreBuscaCliente)
        self.pbBuscaProcesso.clicked.connect(self.abreBuscaProcesso)
        self.pbFecharCliente.clicked.connect(self.fecharCliente)
        self.pbFecharProcesso.clicked.connect(self.fecharProcesso)
        self.pbAposentadorias.clicked.connect(self.avaliaNavegacaoProcesso)

        self.iniciaEstados()

    def avaliaNavegacaoProcesso(self):
        if self.processoAtual is None or self.clienteAtual is None:
            popUpOkAlerta(
                'Para acessar a tela com informações de aposentadorias, é necessário escolher um cliente e determinar um processo utilizando o botão ao centro da tela.',
            )
            self.raise_()
        else:
            self.atualizaInfoNaTela()
            # self.limpaBotoes()
            # self.pbAposentadorias.setStyleSheet(layoutBotaoGuia("pbAposentadorias", selecionado=True))

    def carregaAdvogado(self):
        self.advogadoAtual = CacheLogin().carregarCache()
        if self.advogadoAtual is None:
            self.advogadoAtual = CacheLogin().carregarCacheTemporario()
            if self.advogadoAtual is None:
                popUpOkAlerta('Erro ao carregar informações do advogado. Informe o suporte', erro='init <ProcessosController>', funcao=self.close)

    def carregaEscritorio(self):
        self.escritorioAtual = CacheEscritorio().carregarCache()
        if self.escritorioAtual is None:
            self.escritorioAtual = CacheEscritorio().carregarCacheTemporario()
            if self.escritorioAtual is None:
                popUpOkAlerta('Erro ao carregar informações do escritório. Informe o suporte', erro='init <ProcessosController>', funcao=self.close)

    def abreBuscaCliente(self):
        BuscaClientePage(parent=self).show()

    def abreBuscaProcesso(self):
        BuscaProcessosPage(self.clienteAtual, parent=self).show()

    def carregarInfoCliente(self, clientId: int = 0):
        if clientId != 0:
            self.clienteAtual = Cliente.get_by_id(clientId)
            self.atualizaInfoNaTela()
            if self.multiplosProcessos():
                self.trocaCardCentral(TelaAtiva.BuscaCliente, TelaAtiva.BuscaProcesso)
            else:
                self.processoAtual = Processos.select().where(Processos.clienteId == self.clienteAtual.clienteId).get()
                self.atualizaInfoNaTela()
                self.trocaCardCentral(None, TelaAtiva.Aposentadoria)

    def atualizaInfoNaTela(self):
        # Info cliente
        if self.clienteAtual is not None:
            self.lbNomeCompleto.setText(self.clienteAtual.nomeCliente.replace(' ', '') + ' ' + self.clienteAtual.sobrenomeCliente.lstrip())
            self.lbCPF.setText(mascaraCPF(self.clienteAtual.cpfCliente))
            self.lbEmail.setText(self.clienteAtual.email)
            self.frInfoCliente.show()
        else:
            self.frInfoCliente.hide()

        # Info processo
        if self.processoAtual is not None:
            if self.processoAtual.situacaoId == SituacaoProcesso.aDarEntrada.value:
                situacaoProcesso = 'A dar entrada'
            elif self.processoAtual.situacaoId == SituacaoProcesso.emAndamento.value:
                situacaoProcesso = 'Em andamento'
            elif self.processoAtual.situacaoId == SituacaoProcesso.arquivado.value:
                situacaoProcesso = 'Arquivado'
            elif self.processoAtual.situacaoId == SituacaoProcesso.cancelado.value:
                situacaoProcesso = 'Cancelado'
            elif self.processoAtual.situacaoId == SituacaoProcesso.finalizado.value:
                situacaoProcesso = 'Finalizado'
            else:
                situacaoProcesso = '-'

            self.tabAposController.recebeProcessoId(self.processoAtual.processoId, self.clienteAtual.clienteId)

            self.lbNumProc.setText(self.processoAtual.numeroProcesso if self.processoAtual.numeroProcesso is not None else '-')
            self.lbTpProcesso.setText(self.strTipoProcesso())
            self.lbSituacao.setText(situacaoProcesso)
            self.frInfoProcesso.show()
            self.trocaCardCentral(self.telaAtual, TelaAtiva.Aposentadoria)
        else:
            self.frInfoProcesso.hide()

        # Info advogado e escritório
        self.lbNomeEscritorio.setText(self.escritorioAtual.nomeEscritorio)
        self.lbNumOab.setText(self.advogadoAtual.numeroOAB)
        self.lbNomeAdv.setText(self.advogadoAtual.nomeUsuario + ' ' + self.advogadoAtual.sobrenomeUsuario)

    def multiplosProcessos(self) -> bool:
        qtdProcessos: int = Processos.select().where(Processos.clienteId == self.clienteAtual.clienteId).count()
        return qtdProcessos > 1

    def iniciaEstados(self):
        if self.processoAtual is not None:
            self.trocaCardCentral(None, TelaAtiva.Geral)
            self.frInfoProcesso.show()
            self.atualizaInfoNaTela()
            self.trocaCardCentral(None, TelaAtiva.Aposentadoria)
        elif self.clienteAtual is not None:
            self.trocaCardCentral(None, TelaAtiva.BuscaCliente)
            self.frInfoCliente.show()
        elif self.clienteAtual is None:
            self.trocaCardCentral(None, TelaAtiva.BuscaCliente)
            self.frInfoCliente.hide()
            self.frInfoProcesso.hide()
        else:
            self.trocaCardCentral(None, TelaAtiva.Geral)
            self.frInfoProcesso.hide()
            self.frInfoCliente.hide()

    def trocaCardCentral(self, estadoAtual: TelaAtiva, estadoFuturo: TelaAtiva):
        self.stkMain.setCurrentIndex(estadoFuturo.value)
        self.telaAtual = estadoFuturo
        self.limpaBotoes()

        if estadoFuturo == TelaAtiva.Aposentadoria:
            self.pbAposentadorias.setStyleSheet(layoutBotaoGuia('pbAposentadorias', selecionado=True))
        elif estadoFuturo == TelaAtiva.Geral or estadoFuturo == TelaAtiva.BuscaCliente or estadoFuturo == TelaAtiva.BuscaProcesso:
            self.pbGeral.setStyleSheet(layoutBotaoGuia('pbGeral', selecionado=True))

    def strTipoProcesso(self, prefix: bool = True, sufix: bool = True) -> str:
        strPrefixo: str = ''
        strSufixo: str = ''

        if prefix:
            strPrefixo = TipoProcesso(self.processoAtual.tipoProcesso).name

        if sufix:
            strSufixo = TipoBeneficio(self.processoAtual.tipoBeneficio).name

        if prefix and sufix:
            return strPrefixo + ': ' + strSufixo
        else:
            return strPrefixo + strSufixo

    def fecharCliente(self):
        self.clienteAtual = None
        self.processoAtual = None
        self.atualizaInfoNaTela()
        self.trocaCardCentral(None, TelaAtiva.BuscaCliente)

    def fecharProcesso(self):
        self.processoAtual = None
        self.atualizaInfoNaTela()
        self.trocaCardCentral(None, TelaAtiva.BuscaProcesso)

    def recebeProcesso(self, processoId: int):
        if processoId is not None:
            self.processoAtual = Processos.get_by_id(processoId)
            self.atualizaInfoNaTela()

    def limpaTudo(self):
        # Cliente
        self.clienteAtual = None
        self.lbCPF.setText('-')
        self.lbNomeCompleto.setText('-')
        self.lbEmail.setText('-')

        # Processo
        self.processoAtual = None
        self.lbNumProc.setText('-')
        self.lbTpProcesso.setText('-')
        self.lbSituacao.setText('-')

        # Aposentadoria
        self.tabAposController.limpaLayout()
        self.trocaCardCentral(None, TelaAtiva.BuscaCliente)

    def limpaBotoes(self):
        self.pbAposentadorias.setStyleSheet(layoutBotaoGuia("pbAposentadorias", selecionado=False))
        self.pbGeral.setStyleSheet(layoutBotaoGuia("pbGeral", selecionado=False))
        self.pbProcuracao.setStyleSheet(layoutBotaoGuia("pbProcuracao", selecionado=False))
        self.pbDocsComp.setStyleSheet(layoutBotaoGuia("pbDocsComp", selecionado=False))
