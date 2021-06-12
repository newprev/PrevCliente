from PyQt5.QtWidgets import QWidget
from Telas.pgTipoBeneficioConc import Ui_wdgTipoBeneficioConc
from heart.sinaisCustomizados import Sinais
from newPrevEnums import MomentoEntrevista, TipoBeneficio
from Telas.efeitos import Efeitos


class TipoBeneficioConcController(QWidget, Ui_wdgTipoBeneficioConc):

    def __init__(self, parent=None, db=None):
        super(TipoBeneficioConcController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)
        self.pbAposentadoria.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficio.Aposentadoria))
        self.pbAuxilioDoenca.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficio.AuxDoenca))
        self.pbAuxReclusao.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficio.AuxReclusao))
        self.pbBeneIdoso.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficio.BeneIdoso))
        self.pbBeneDeficiencia.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficio.BeneDeficiencia))
        self.pbPensaoMorte.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficio.PensaoMorte))
        self.pbSalMaternidade.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.tipoBeneficio, TipoBeneficio.SalMaternidade))

        # self.efeitos.shadowCards([self.pbJudicial, self.pbAdministrativo])

    def emiteTrocaTela(self, momento: MomentoEntrevista, tipoBeneficio: TipoBeneficio):
        """
        QtCore.pyqtSignal([MomentoEntrevista, TipoBeneficio] name='tela')
        :cvar
        """
        self.sinais.sTrocaTelaEntrevista.emit([momento, tipoBeneficio])

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])