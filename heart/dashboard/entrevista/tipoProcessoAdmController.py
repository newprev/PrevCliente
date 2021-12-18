import datetime

from PyQt5.QtWidgets import QWidget
from Design.pyUi.pgTipoProcessoAdm import Ui_wdgTipoProcessoAdm
from sinaisCustomizados import Sinais
from modelos.processosORM import Processos
from util.enums.newPrevEnums import MomentoEntrevista
from Design.pyUi.efeitos import Efeitos
from util.enums.processoEnums import TipoProcesso


class TipoProcessoAdmController(QWidget, Ui_wdgTipoProcessoAdm):
    processoAtivo: Processos

    def __init__(self, parent=None):
        super(TipoProcessoAdmController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)
        self.pbConcessao.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoProcesso, TipoProcesso.Concessao))
        self.pbRecursoOrdinario.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoProcesso, TipoProcesso.RecOrdinario))
        self.pbRevisao.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoProcesso, TipoProcesso.Revisao))
        self.pbRecursoEspecial.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoProcesso, TipoProcesso.RecEspecial))

        self.efeitos.shadowCards([self.pbConcessao, self.pbRecursoOrdinario, self.pbRevisao, self.pbRecursoEspecial])

    def emiteTrocaTela(self, momento: MomentoEntrevista, tipoProcesso: TipoProcesso):
        """
        QtCore.pyqtSignal([MomentoEntrevista, TipoProcesso] name='tela')
        :cvar
        """
        self.processoAtivo.dataUltAlt = datetime.datetime.now()
        self.processoAtivo.tipoProcesso = tipoProcesso.value
        self.processoAtivo.save()
        self.sinais.sTrocaTelaEntrevista.emit([momento, tipoProcesso])

    def atualizaProcesso(self, processoAtual: Processos):
        self.processoAtivo = processoAtual

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])