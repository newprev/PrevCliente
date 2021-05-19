from PyQt5.QtWidgets import QWidget
from Telas.pgNatureza import Ui_wdgNatureza
from heart.sinaisCustomizados import Sinais
from newPrevEnums import TelasEntrevista


class NaturezaController(QWidget, Ui_wdgNatureza):

    def __init__(self, parent=None, db=None):
        super(NaturezaController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.sinais = Sinais()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)
        self.pbAdministrativo.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.administrativo))
        self.pbJudicial.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.judicial))

    def emiteTrocaTela(self, tela: TelasEntrevista):
        self.sinais.sTrocaTelaEntrevista.emit(tela)

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])
