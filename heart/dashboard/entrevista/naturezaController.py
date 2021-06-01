from PyQt5.QtWidgets import QWidget
from Telas.pgNatureza import Ui_wdgNatureza
from heart.sinaisCustomizados import Sinais
from newPrevEnums import MomentoEntrevista, NaturezaProcesso
from Telas.efeitos import Efeitos


class NaturezaController(QWidget, Ui_wdgNatureza):

    def __init__(self, parent=None, db=None):
        super(NaturezaController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)
        self.pbAdministrativo.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.naturezaProcesso, NaturezaProcesso.administrativo))
        self.pbJudicial.clicked.connect(lambda: self.emiteTrocaTela(MomentoEntrevista.naturezaProcesso, NaturezaProcesso.judicial))

        self.efeitos.shadowCards([self.pbJudicial, self.pbAdministrativo])

    def emiteTrocaTela(self, momento: MomentoEntrevista, tela: NaturezaProcesso):
        """
        QtCore.pyqtSignal([MomentoEntrevista, NaturezaProcesso] name='tela')
        :cvar
        """
        self.sinais.sTrocaTelaEntrevista.emit([momento, tela])

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])

