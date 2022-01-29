import datetime

from PyQt5.QtWidgets import QWidget
from Design.pyUi.pgTipoBeneficioConc import Ui_wdgTipoBeneficioConc
from sinaisCustomizados import Sinais
from modelos.processosORM import Processos
from util.enums.newPrevEnums import MomentoEntrevista
from util.enums.processoEnums import TipoBeneficioEnum


class TipoBeneficioConcController(QWidget, Ui_wdgTipoBeneficioConc):
    processoAtivo: Processos

    def __init__(self, parent=None):
        super(TipoBeneficioConcController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        # self.db = db
        self.sinais = Sinais()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)
        self.pbAposentadoria.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficioEnum.Aposentadoria))
        self.pbAuxilioDoenca.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficioEnum.AuxDoenca))
        self.pbAuxReclusao.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficioEnum.AuxReclusao))
        self.pbBeneIdoso.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficioEnum.BeneIdoso))
        self.pbBeneDeficiencia.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficioEnum.BeneDeficiencia))
        self.pbPensaoMorte.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficioEnum.PensaoMorte))
        self.pbSalMaternidade.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficioEnum.SalMaternidade))

        # self.efeitos.shadowCards([self.pbJudicial, self.pbAdministrativo])

    def emiteTrocaTela(self, momento: MomentoEntrevista, tipoBeneficio: TipoBeneficioEnum):
        """
        QtCore.pyqtSignal([MomentoEntrevista, TipoBeneficioEnum] name='tela')
        :cvar
        """
        self.processoAtivo.tipoBeneficio = tipoBeneficio.value
        self.processoAtivo.dataUltAlt = datetime.datetime.now()
        self.processoAtivo.save()
        self.sinais.sTrocaTelaEntrevista.emit([momento, tipoBeneficio])

    def atualizaProcesso(self, processoAtual: Processos):
        self.processoAtivo = processoAtual

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])
