from PyQt5.QtWidgets import QWidget
from Telas.pgTipoBeneficio import Ui_wdgTipoBeneficio
from heart.sinaisCustomizados import Sinais
from newPrevEnums import TelasEntrevista
from Telas.efeitos import Efeitos


class TipoBeneficioController(QWidget, Ui_wdgTipoBeneficio):

    def __init__(self, parent=None, db=None):
        super(TipoBeneficioController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)
        self.pbApos.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbAposDeficiencia.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbAposRural.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbAposEspecial.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbAuxilioDoenca.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbAuxReclusao.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbBeneIdoso.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbBeneDeficiencia.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbPensaoMorte.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))
        self.pbSalMaternidade.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoAtividade))

        # self.efeitos.shadowCards([self.pbJudicial, self.pbAdministrativo])

    def emiteTrocaTela(self, tela: TelasEntrevista):
        self.sinais.sTrocaTelaEntrevista.emit(tela)

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])