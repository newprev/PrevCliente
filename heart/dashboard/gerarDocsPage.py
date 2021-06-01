from PyQt5.QtWidgets import QWidget, QFrame, QCheckBox

from Telas.efeitos import Efeitos
from Telas.pgImpressaoDocs import Ui_wdgImpressaoDocs
from heart.dashboard.entrevista.geracaoDocumentos.docEntrevista import DocEntrevista
from heart.sinaisCustomizados import Sinais

from modelos.clienteModelo import ClienteModelo
from modelos.processosModelo import ProcessosModelo

from Daos.daoProcessos import DaoProcessos
from Daos.daoCliente import DaoCliente

from newPrevEnums import TipoProcesso, NaturezaProcesso, TipoBeneficio


class GerarDocsPage(QWidget, Ui_wdgImpressaoDocs):

    def __init__(self,  cliente: ClienteModelo, processo: ProcessosModelo, parent=None, db=None):
        super(GerarDocsPage, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.clienteAtual: ClienteModelo = ClienteModelo()
        self.daoCliente = DaoCliente(db=db)
        self.processo = processo
        self.cliente = cliente

        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.frames = [
            self.frProcuracao, self.frDocsComprob,
            self.frOutro1, self.frOutro2,
            self.frOutro3, self.frOutro4,
            self.frOutro5, self.frOutro6,
        ]
        self.abilitandoEfeitoClique()

        self.frAtiv1.hide()
        self.frAtiv4.hide()
        self.frAtiv7.hide()
        self.frAtiv8.hide()

        self.doc: DocEntrevista = None

        self.avaliaCheckBoxes()

    def avaliaCheckBoxes(self):
        if self.processo is not None:
            if self.processo.tipoBeneficio == TipoBeneficio.Aposentadoria.value:
                self.cbProcuracao.setChecked(True)
                self.efeitos.shadowCards([self.frProcuracao])

    def atualizaInformacoes(self, processo: ProcessosModelo, cliente: ClienteModelo):
        self.processo = processo
        self.cliente = cliente

        self.doc = DocEntrevista(processo, cliente)

    def gerarDocumentosSelecionados(self):
        if self.cbProcuracao.isChecked():
            self.doc.gerarProcuracao()
        if self.cbDocsComprob.isChecked():
            self.doc.gerarDocumentosComprobatorios()

    def atividadeSelecionada(self, frame: QFrame, checkBox: QCheckBox):
        self.efeitos.shadowCards([frame])
        frame.setMinimumSize(815, 82)
        checkBox.setChecked(True)

    def atividadeDesSelecionada(self, frame: QFrame, checkBox: QCheckBox):
        self.efeitos.desativarSombra([frame])
        frame.setMinimumSize(800, 80)
        checkBox.setChecked(False)

    def abilitandoEfeitoClique(self):
        for frame in self.frames:
            cb: QCheckBox = frame.children()[1]
            cb.clicked.connect(lambda state, frame=frame: self.avaliaAtivaDesativa(frame, state))

    def avaliaAtivaDesativa(self, frame: QFrame, state: bool):
        checkBox: QCheckBox = frame.children()[1]
        if state:
            self.atividadeSelecionada(frame, checkBox)
        else:
            self.atividadeDesSelecionada(frame, checkBox)
