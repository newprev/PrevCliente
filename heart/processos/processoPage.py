from PyQt5.QtWidgets import QWidget
from Design.pyUi.processoPage import Ui_wdgProcessoPage
from heart.buscaClientePage import BuscaClientePage
from util.enums.processoEnums import SituacaoTela


class ProcessoPage(QWidget, Ui_wdgProcessoPage):
    situacaoTela: SituacaoTela = SituacaoTela.clienteFaltante

    def __init__(self, parent=None):
        super(ProcessoPage, self).__init__(parent=parent)
        self.setupUi(self)

        self.pbBuscarCliente.clicked.connect(self.abreTelaBuscaCliente)

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

            self.frInfoGeralProcessos.hide()

        elif situacao == SituacaoTela.processoFaltante:
            self.stkInfoCliente.setCurrentIndex(1)
            self.limpaProcesso()

        else:
            self.stkInfoCliente.setCurrentIndex(1)
            self.frInfoGeralProcessos.show()

    def carregarInfoCliente(self, clienteId: int = 0):
        print(f"Oooooopa! Fucionou bem! ------ {clienteId=}")

    def limpaCliente(self):
        print('limpaCliente')

    def limpaProcesso(self):
        print('limpaProcesso')


