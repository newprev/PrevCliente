import datetime
from peewee import SqliteDatabase

from PyQt5.QtWidgets import QWidget, QFrame, QCheckBox
from PyQt5.QtCore import Qt
from Design.pyUi.pgQuizAposentadoria import Ui_wdgQuizAposentadoria
from SQLs.itensContribuicao import buscaIndicesByClienteId
from heart.dashboard.tabs.tabResumoCNIS import TabResumoCNIS
from sinaisCustomizados import Sinais
from modelos.clienteORM import Cliente
from Design.efeitos import Efeitos
from util.enums.aposentadoriaEnums import AtivApos


class TipoAtividadeController(QWidget, Ui_wdgQuizAposentadoria):

    def __init__(self, parent=None):
        super(TipoAtividadeController, self).__init__(parent)

        self.setupUi(self)
        self.entrevistaPage = parent
        # self.db = db
        self.db: SqliteDatabase = Cliente._meta.database
        self.clienteAtual: Cliente = Cliente()

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
            self.frAtiv6,
            self.frAtiv7,
            self.frAtiv8,
            self.frAtiv9,
            self.frAtiv10,
        ]

        self.cbAtiv11.clicked.connect(lambda: self.apresentarTela(AtivApos(11)))
        self.cbAtiv6.clicked.connect(self.atualizaProfessor)

        self.escondeInfos()
        self.abilitandoEfeitoClique()

    def pegaClienteAtual(self, clienteAtual: Cliente):
        self.clienteAtual = clienteAtual
        self.atualizaInfos()

    def atualizaInfos(self):
        query = buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['IEAN'])
        listaIean: list = self.db.execute_sql(buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['IEAN'])).fetchall()
        listaPrpps: list = self.db.execute_sql(buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['PRPPS'])).fetchall()
        listaSalMin: list = self.db.execute_sql(buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['PREC-MENOR-MIN'])).fetchall()
        listaImei_Irec: list = self.db.execute_sql(buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['IMEI', 'IREC-FBR'])).fetchall()
        listaIle_Irec: list = self.db.execute_sql(buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=['ILEI', 'IREC-LC'])).fetchall()
        listaAny: list = self.db.execute_sql(buscaIndicesByClienteId(self.clienteAtual.clienteId, indices=[])).fetchall()

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

        if self.clienteAtual.professor:
            self.atividadeSelecionada(self.frInfo6, self.cbAtiv6)
            self.frAtiv6.setToolTip('O(A) cliente trabalhou como professor(a)')
            self.frAtiv6.show()

    def atualizaProfessor(self):
        self.clienteAtual.professor = self.cbAtiv6.isChecked()
        self.clienteAtual.dataUltAlt = datetime.datetime.now()
        self.clienteAtual.save()

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
            telaCalculo = TabResumoCNIS(parent=self, db=self.db, origemEntrevista=True)
            telaCalculo.carregarInfoCliente(clienteModel=self.clienteAtual)
            telaCalculo.setWindowFlags(Qt.Tool | Qt.Dialog)
            telaCalculo.show()
