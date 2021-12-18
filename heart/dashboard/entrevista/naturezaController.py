import datetime

from PyQt5.QtWidgets import QWidget
from Design.pyUi.pgNatureza import Ui_wdgNatureza

import util.popUps
from sinaisCustomizados import Sinais
from modelos.processosORM import Processos
from modelos.clienteORM import Cliente
from modelos.advogadoORM import Advogados
from util.enums.newPrevEnums import MomentoEntrevista
from util.enums.processoEnums import NaturezaProcesso
from .localStyleSheet.central import checkNatureza
from Design.pyUi.efeitos import Efeitos


class NaturezaController(QWidget, Ui_wdgNatureza):
    processoAtivo: Processos
    clienteAtivo: Cliente
    advogadoAtivo: Advogados

    def __init__(self, advogadoModelo: Advogados, processoModelo: Processos, parent=None):
        super(NaturezaController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.iniciaParametrosTela(advogadoModelo, processoModelo)

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)

        self.gbAdmnistrativo.clicked.connect(lambda: self.salvaNaturezaProcesso(NaturezaProcesso.administrativo))
        self.gbJudicial.clicked.connect(lambda: self.salvaNaturezaProcesso(NaturezaProcesso.judicial))

        # self.efeitos.shadowCards([self.pbJudicial, self.pbAdministrativo])

    def iniciaParametrosTela(self, advogadoModelo: Advogados, processoModelo: Processos):
        if advogadoModelo is None or processoModelo is None:
            util.popUps.popUpOkAlerta("Não foi possível carregar alguma das informações para prosseguir.", erro='[naturezaController] - iniciaParametrosTela')

        else:
            self.advogadoAtivo = advogadoModelo
            self.processoAtivo = processoModelo
            # self.processoAtivo.advogadoId = advogadoModelo
            # self.processoAtivo.dataUltAlt = datetime.datetime.now()
            # self.processoAtivo.save()
            # self.processoAtivo.processoId = self.processoAtivo.save()
            self.ativaNatureza(NaturezaProcesso.administrativo, ativa=True)

    def ativaNatureza(self, naturezaEscolhida: NaturezaProcesso, ativa: bool):

        if naturezaEscolhida == NaturezaProcesso.administrativo:
            if ativa:
                self.gbAdmnistrativo.setChecked(True)
                self.gbJudicial.setChecked(False)
                styleAdm = checkNatureza(NaturezaProcesso.administrativo, True)
                styleJud = checkNatureza(NaturezaProcesso.judicial, False)
            else:
                self.gbAdmnistrativo.setChecked(False)
                self.gbJudicial.setChecked(True)
                styleAdm = checkNatureza(NaturezaProcesso.administrativo, False)
                styleJud = checkNatureza(NaturezaProcesso.judicial, True)
        else:
            if ativa:
                self.gbAdmnistrativo.setChecked(False)
                self.gbJudicial.setChecked(True)
                styleAdm = checkNatureza(NaturezaProcesso.administrativo, False)
                styleJud = checkNatureza(NaturezaProcesso.judicial, True)
            else:
                self.gbAdmnistrativo.setChecked(True)
                self.gbJudicial.setChecked(False)
                styleAdm = checkNatureza(NaturezaProcesso.administrativo, True)
                styleJud = checkNatureza(NaturezaProcesso.judicial, False)

        self.gbAdmnistrativo.setStyleSheet(styleAdm)
        self.gbJudicial.setStyleSheet(styleJud)

    def emiteTrocaTela(self, momento: MomentoEntrevista, tela: NaturezaProcesso):
        """
        QtCore.pyqtSignal([MomentoEntrevista, NaturezaProcesso] name='tela')
        :cvar
        """

        self.sinais.sTrocaTelaEntrevista.emit([momento, tela])

    def salvaNaturezaProcesso(self, naturezaEscolhida):
        if naturezaEscolhida == NaturezaProcesso.administrativo:
            self.ativaNatureza(NaturezaProcesso.administrativo, ativa=self.gbAdmnistrativo.isChecked())
        else:
            self.ativaNatureza(NaturezaProcesso.judicial, ativa=self.gbJudicial.isChecked())

        self.processoAtivo.dataUltAlt = datetime.datetime.now()
        if self.gbAdmnistrativo.isChecked():
            self.processoAtivo.natureza = NaturezaProcesso.administrativo.value
        else:
            self.processoAtivo.natureza = NaturezaProcesso.judicial.value
        self.processoAtivo.save()

    def atualizaClienteAtual(self, clienteAtual: Cliente):
        self.clienteAtivo = clienteAtual
        self.processoAtivo.clienteId = clienteAtual

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])

