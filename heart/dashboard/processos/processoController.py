from PyQt5.QtWidgets import QMainWindow
from Design.pyUi.processoPg import Ui_mwProcessoPage

from heart.buscaClientePage import BuscaClientePage
from modelos.clienteORM import Cliente
from modelos.processosORM import Processos
from modelos.advogadoORM import Advogados
from modelos.escritoriosORM import Escritorios
from cache.cacheEscritorio import CacheEscritorio
from cache.cachingLogin import CacheLogin
from util.helpers import mascaraCPF

from util.popUps import popUpOkAlerta


class ProcessosController(QMainWindow, Ui_mwProcessoPage):
    clienteAtual: Cliente
    processoAtual: Processos
    advogadoAtual: Advogados
    escritorioAtual: Escritorios

    def __init__(self, cliente: Cliente = None, processo: Processos = None, parent=None):
        super(ProcessosController, self).__init__(parent=parent)
        self.setupUi(self)

        self.clienteAtual: Cliente = cliente
        self.processoAtual: Processos = processo

        self.carregaEscritorio()
        self.carregaAdvogado()

        self.pbBuscaCliente.clicked.connect(self.abreBuscaCliente)

        if self.clienteAtual is None and self.processoAtual is None:
            self.atualizaInfoNaTela()
        elif self.clienteAtual is None and self.processoAtual is not None:
            self.clienteAtual = Cliente.get_by_id(self.processoAtual.clienteId)
            self.atualizaInfoNaTela()
        elif self.clienteAtual is not None and self.processoAtual is None:
            print('Sei lá...')
        else:
            popUpOkAlerta(
                'Algum erro aconteceu ao tentar abrir a tela de processos. Entre em contato com o suporte.',
                erro='init <ProcessosController>',
                funcao=self.close,
            )

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

    def carregarInfoCliente(self, clientId: int = 0):
        if clientId != 0:
            self.clienteAtual =Cliente.get_by_id(clientId)
            self.atualizaInfoNaTela()

    def atualizaInfoNaTela(self):
        if self.clienteAtual is not None:
            # Info cliente
            self.lbNomeCompleto.setText(self.clienteAtual.nomeCliente.replace(' ', '') + ' ' + self.clienteAtual.sobrenomeCliente.lstrip())
            self.lbCPF.setText(mascaraCPF(self.clienteAtual.cpfCliente))
            self.lbEmail.setText(self.clienteAtual.email)

        # Info advogado e escritório
        self.lbNomeEscritorio.setText(self.escritorioAtual.nomeEscritorio)
        self.lbNumOab.setText(self.advogadoAtual.numeroOAB)
        self.lbNomeAdv.setText(self.advogadoAtual.nomeUsuario + ' ' + self.advogadoAtual.sobrenomeUsuario)


