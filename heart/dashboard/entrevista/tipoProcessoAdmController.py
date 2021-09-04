from PyQt5.QtWidgets import QWidget
from Design.pyUi.pgTipoProcessoAdm import Ui_wdgTipoProcessoAdm
from heart.sinaisCustomizados import Sinais
from util.enums.newPrevEnums import MomentoEntrevista, TipoProcesso
from Design.pyUi.efeitos import Efeitos


class TipoProcessoAdmController(QWidget, Ui_wdgTipoProcessoAdm):

    def __init__(self, parent=None, db=None):
        super(TipoProcessoAdmController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
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
        self.sinais.sTrocaTelaEntrevista.emit([momento, tipoProcesso])

    def trocaTela(self, *args):
        self.entrevistaPage.trocaTelaCentral(args[0])