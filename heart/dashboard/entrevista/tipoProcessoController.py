from PyQt5.QtWidgets import QWidget
from Telas.pgTipoProcesso import Ui_wdgTipoProcesso
from heart.sinaisCustomizados import Sinais
from newPrevEnums import TelasEntrevista
from Telas.efeitos import Efeitos


class TipoProcessoController(QWidget, Ui_wdgTipoProcesso):

    def __init__(self, parent=None, db=None):
        super(TipoProcessoController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sTrocaTelaEntrevista.connect(self.trocaTela)
        self.pbConcessao.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoBeneficio))
        self.pbRecursoOrdinario.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoBeneficio))
        self.pbRevisao.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoBeneficio))
        self.pbRecursoEspecial.clicked.connect(lambda: self.emiteTrocaTela(TelasEntrevista.tipoBeneficio))

        self.efeitos.shadowCards([self.pbConcessao, self.pbRecursoOrdinario, self.pbRevisao, self.pbRecursoEspecial])

    def emiteTrocaTela(self, tela: TelasEntrevista):
        self.sinais.sTrocaTelaEntrevista.emit(tela)

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])