from PyQt5.QtWidgets import QWidget, QFrame, QCheckBox
from PyQt5.QtCore import Qt
from Telas.pgQuizAposentadoria import Ui_wdgQuizAposentadoria
from heart.dashboard.tabs.tabCalculos import TabCalculos
from heart.sinaisCustomizados import Sinais
from modelos.clienteORM import Cliente
from Daos.daoCliente import DaoCliente
from util.enums.newPrevEnums import AtivApos
from Telas.efeitos import Efeitos


class TipoAtividadeController(QWidget, Ui_wdgQuizAposentadoria):

    def __init__(self, parent=None, db=None):
        super(TipoAtividadeController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        self.db = db
        self.clienteAtual: Cliente = Cliente()
        self.daoCliente = DaoCliente(db=db)

        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.frames = [
            self.frInfo1, self.frInfo2, self.frInfo3, self.frInfo4,
            self.frInfo5, self.frInfo6, self.frInfo7, self.frInfo8,
            self.frInfo9, self.frInfo10, self.frInfo11, self.frInfo12,
            self.frInfo13
        ]

        self.avisos = [
            self.frAtiv1,
            self.frAtiv4,
            self.frAtiv7,
            self.frAtiv8,
            self.frAtiv9,
            self.frAtiv10,
        ]

        self.cbAtiv11.clicked.connect(lambda: self.apresentarTela(AtivApos(11)))

        self.escondeInfos()
        self.abilitandoEfeitoClique()

    def pegaClienteAtual(self, clienteAtual: Cliente):
        self.clienteAtual = clienteAtual
        self.atualizaInfos()

    def atualizaInfos(self):
        listaIean: list = self.daoCliente.buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['IEAN'])
        listaPrpps: list = self.daoCliente.buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['PRPPS'])
        listaSalMin: list = self.daoCliente.buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['PREC-MENOR-MIN'])
        listaImei_Irec: list = self.daoCliente.buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['IMEI', 'IREC-FBR'])
        listaIle_Irec: list = self.daoCliente.buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['ILEI', 'IREC-LC'])
        listaAny: list = self.daoCliente.buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=[])

        if not len(listaIean) == 0:
            self.frAtiv1.setToolTip('Existe indicativo de trabalho insalubre no CNIS')
            self.atividadeSelecionada(self.frInfo1, self.cbAtiv1)
            self.frAtiv1.show()

        if not len(listaPrpps) == 0:
            self.frAtiv4.setToolTip('Existe indicativo de trabalho em regime próprio no CNIS')
            self.atividadeSelecionada(self.frInfo4, self.cbAtiv4)
            self.frAtiv4.show()

        if not len(listaSalMin) == 0:
            self.frAtiv7.setToolTip('Existe indicativo de contribuição abaixo \ndo salário mínimo no CNIS')
            self.atividadeSelecionada(self.frInfo7, self.cbAtiv7)
            self.frAtiv7.show()

        if not len(listaImei_Irec) == 0:
            self.frAtiv8.setToolTip('Existe indicativo de baixa renda no CNIS')
            self.atividadeSelecionada(self.frInfo8, self.cbAtiv8)
            self.frAtiv8.show()

        if not len(listaIle_Irec) == 0:
            self.frAtiv9.setToolTip('Existe indicativo de contribuição abaixo de 11% no CNIS')
            self.atividadeSelecionada(self.frInfo9, self.cbAtiv9)
            self.frAtiv9.show()

        if not len(listaAny) == 0:
            self.atividadeSelecionada(self.frInfo10, self.cbAtiv10)
            if len(listaAny) == 1:
                self.frAtiv10.setToolTip('Existe indicativo no CNIS')
            else:
                self.frAtiv10.setToolTip('Existem indicativos no CNIS')
            self.frAtiv10.show()

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

    def escondeInfos(self):
        for info in self.avisos:
            info.hide()

    def apresentarTela(self, cbClicada: AtivApos):
        if cbClicada == AtivApos.editarCnisB:
            telaCalculo = TabCalculos(parent=self, db=self.db, origemEntrevista=True)
            telaCalculo.carregarInfoCliente(clienteModel=self.clienteAtual)
            telaCalculo.setWindowFlags(Qt.Tool | Qt.Dialog)
            telaCalculo.show()
