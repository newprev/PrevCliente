from PyQt5.QtWidgets import QWidget, QFrame, QCheckBox

from Telas.efeitos import Efeitos
from Telas.pgImpressaoDocs import Ui_wdgImpressaoDocs
from heart.dashboard.entrevista.geracaoDocumentos.docEntrevista import DocEntrevista
from heart.sinaisCustomizados import Sinais

from modelos.clienteORM import Cliente
from modelos.processosORM import Processos

from Daos.daoProcessos import DaoProcessos
from Daos.daoCliente import DaoCliente

from newPrevEnums import TipoProcesso, NaturezaProcesso, TipoBeneficio


class GerarDocsPage(QWidget, Ui_wdgImpressaoDocs):

    def __init__(self,  cliente: Cliente, processo: Processos, parent=None, db=None):
        super(GerarDocsPage, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.clienteAtual: Cliente = Cliente()
        # self.daoCliente = DaoCliente(db=db)
        self.processo = processo
        self.cliente = cliente

        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.frames = [
            self.frContratoHon, self.frProcuracao,
            self.frDocsComprob, self.frDecHipo,
            self.frDecPensao, self.frOutro4,
            self.frOutro5, self.frOutro6
        ]
        self.abilitandoEfeitoClique()

        self.frContratoHonInfo.hide()
        self.frProcuracaoInfo.hide()
        self.frDocsComprobInfo.hide()
        self.frDecHipoInfo.hide()
        self.frDecPensaoInfo.hide()

        self.doc: DocEntrevista = None

        self.avaliaCheckBoxes()

    def avaliaCheckBoxes(self):
        if self.processo is not None:
            if self.processo.tipoBeneficio == TipoBeneficio.Aposentadoria.value:
                self.cbProcuracao.setChecked(True)
                self.efeitos.shadowCards([self.frProcuracao])

    def atualizaInformacoes(self, processo: Processos, cliente: Cliente):
        self.processo = processo
        self.cliente = cliente

        self.doc = DocEntrevista(processo, cliente)

    def gerarDocumentosSelecionados(self):
        self.doc.criaRequerimentoAdm()

        if self.cbProcuracao.isChecked():
            self.doc.gerarProcuracao()

        if self.cbContratoHon.isChecked():
            self.doc.criaContratoHonorarios()

        if self.cbDecHipo.isChecked():
            self.doc.criaDeclaracaoHipo()

        if self.cbDecPensao.isChecked():
            self.doc.criaDecPensao()

        if self.cbDocsComprob.isChecked():
            self.doc.criaDocumentosComprobatorios()

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
