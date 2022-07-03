from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QPoint, pyqtProperty, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QComboBox, QLineEdit, QVBoxLayout
from typing import List

from Design.CustomWidgets.styleSheets.modalEntrevista import estiloPorTipo
from Design.efeitos import Efeitos
from Design.pyUi.wdgModalEntrevista import Ui_mwModalEntrevista
from modelos.Auxiliares.tipoInfo import InformacaoModel
from sinaisCustomizados import Sinais

from util.enums.entrevistaEnums import CategoriaQuiz
from util.popUps import popUpSimCancela


class ModalEntrevistaController(QMainWindow, Ui_mwModalEntrevista):

    def __init__(self, categQuiz: CategoriaQuiz = None, listaQuiz: List[InformacaoModel] = None, parent=None, dashboard=None):
        super(ModalEntrevistaController, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent
        self.dashboard = dashboard
        self.sinais = Sinais()
        self.sinais.sFecharJanela.connect(self.enviaSaindo)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.editando = False
        Efeitos().shadowCards([self.frMain], radius=4, color=(63, 63, 63, 90), offset=(7, 0))

        if map(lambda item: item is None, [categQuiz, listaQuiz]):
            self.iniciaInfo(categQuiz, listaQuiz)
        else:
            print("É... Agora entrou aqui...")

        # frConteudo é um frame do NewDashboard
        self.animacaoEntrada(self.dashboard.frConteudo)

        self.pbFechar.clicked.connect(self.avaliaSair)

    def avaliaSair(self):
        if self.editando:
            popUpSimCancela(
                "Deseja fechar essa tela de configuração sem salvar? Caso prossiga perderá suas alterações.",
                funcaoSim=self.sair,
                funcaoCancela=self.salvarAlteracoes
            )
        else:
            self.sair()

    def animacaoEntrada(self, parent):
        tamanhoParent = parent.geometry()
        xFinal = parent.mapToGlobal(QPoint(0, 0)).x()
        yFinal = parent.mapToGlobal(QPoint(0, 0)).y()

        self.aGeometry = QPropertyAnimation(self, b"geometry")
        self.aGeometry.setDuration(120)
        self.aGeometry.setEasingCurve(QEasingCurve.InSine)
        self.aGeometry.setStartValue(QRect(50, yFinal - 20, tamanhoParent.width() / 3, tamanhoParent.height() + 22))
        self.aGeometry.setEndValue(QRect(xFinal, yFinal - 20, tamanhoParent.width() / 3, tamanhoParent.height() + 22))

        self.aOpacity = QPropertyAnimation(self, b"opacity")
        self.aOpacity.setEasingCurve(QEasingCurve.InSine)
        self.aOpacity.setDuration(70)
        self.aOpacity.setStartValue(0.0)
        self.aOpacity.setEndValue(1)

        self.aGeometry.start()
        self.aOpacity.start()

    def enviaSaindo(self):
        self.parent.habilitaBlur(False)

    def iniciaInfo(self, categInfo: CategoriaQuiz, listaPerguntas: list):
        self.lbInfoPerguntas.setText("Confirme as informações abaixo")

        if categInfo == CategoriaQuiz.insalubridade:
            self.iniciaInsalubridade(listaPerguntas)
        elif categInfo == CategoriaQuiz.deficiencia:
            self.iniciaDeficiencia()
        elif categInfo == CategoriaQuiz.servicoMilitar:
            self.iniciaServMilitar()
        elif categInfo == CategoriaQuiz.trabalhoRural:
            self.iniciaTrabalhoRural()
        elif categInfo == CategoriaQuiz.alteracaoManual:
            self.iniciaAltManual()
        elif categInfo == CategoriaQuiz.outros:
            self.iniciaOutros()
        else:
            return False

    # QLabel, QCheckBox, QComboBox, QLineEdit
    def iniciaOutros(self):
        self.lbInfo.setText(f"{'Outras situações que precisam de atenção': ^60}")

    def iniciaAltManual(self):
        self.lbInfo.setText(f"{'Alteração do CNIS manualmente': ^60}")

    def iniciaTrabalhoRural(self):
        self.lbInfo.setText(f"{'Possui labor em ambiente rural?': ^60}")

    def iniciaServMilitar(self):
        self.lbInfo.setText(f"{'Possui tempo de serviço militar?': ^60}")

    def iniciaDeficiencia(self):
        self.lbInfo.setText(f"{'Existe labor em condição de deficiente?': ^60}")

    def iniciaInsalubridade(self, listaPerguntas: List[InformacaoModel]):
        self.lbInfo.setText(f"{'Existe labor em condições insalubres/especiais?': ^60}")
        vlPerguntas = QVBoxLayout(self)
        vlPerguntas.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        for item in listaPerguntas:
            if isinstance(item.tipoInfo, QCheckBox):
                cbItem = QCheckBox(item.descricao)
                cbItem.setStyleSheet(estiloPorTipo(item.tipoInfo, nivel=item.nivel))
                vlPerguntas.addWidget(cbItem)

        self.scaPerguntas.setLayout(vlPerguntas)

    def sair(self):
        self.sinais.sFecharJanela.emit()
        self.close()

    def salvarAlteracoes(self):
        self.sinais.sFecharJanela.emit()
        self.close()
        
    def windowOpacity(self):
        return super().windowOpacity()

    def setWindowOpacity(self, opacity):
        super().setWindowOpacity(opacity)

    opacity = pyqtProperty(float, windowOpacity, setWindowOpacity)