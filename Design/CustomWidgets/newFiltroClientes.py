from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, QPropertyAnimation, QEasingCurve, QRect, pyqtProperty
from PyQt5.QtWidgets import QWidget

from Design.pyUi.wdgFiltroClientes import Ui_wdgFiltroClientes
from sinaisCustomizados import Sinais


class NewFiltroClientes(QWidget, Ui_wdgFiltroClientes):
    posicaoBotao: QPoint
    filtros: dict

    def __init__(self, parent=None, position: QPoint = None, filtros: dict = None):
        super(NewFiltroClientes, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.sinais = Sinais()
        self.sinais.sEnviaFiltro.connect(self.enviaFiltro)

        self.posicaoBotao = position
        if filtros is None:
            self.filtros = {'arquivados': False}
        else:
            self.filtros = filtros

        self.iniciaFiltros()

        self.pbOk.clicked.connect(lambda: self.sinais.sEnviaFiltro.emit())
        self.cbArquivados.stateChanged.connect(self.atualizaArquivados)

    def animacaoEntrada(self, position: QPoint):
        self.aGeometry = QPropertyAnimation(self, b"geometry")
        self.aGeometry.setDuration(70)
        self.aGeometry.setEasingCurve(QEasingCurve.InSine)
        self.aGeometry.setStartValue(QRect(position.x(), position.y() + 10, self.width(), self.height()))
        self.aGeometry.setEndValue(QRect(position.x(), position.y(), self.width(), self.height()))

        self.aOpacity = QPropertyAnimation(self, b"opacity")
        self.aOpacity.setEasingCurve(QEasingCurve.InSine)
        self.aOpacity.setDuration(50)
        self.aOpacity.setStartValue(0.0)
        self.aOpacity.setEndValue(1)

        self.aGeometry.start()
        self.aOpacity.start()

    def atualizaArquivados(self):
        self.filtros['arquivados'] = self.cbArquivados.isChecked()

    def enviaFiltro(self):
        self.parent.avaliaFiltrosMenu(self.filtros)
        self.close()

    def iniciaFiltros(self):
        self.cbArquivados.setChecked(self.filtros['arquivados'])

    def showEvent(self, a0: QtCore.QEvent) -> None:
        self.animacaoEntrada(QPoint(400, 30))

    def windowOpacity(self):
        return super().windowOpacity()

    def setWindowOpacity(self, opacity):
        super().setWindowOpacity(opacity)

    opacity = pyqtProperty(float, windowOpacity, setWindowOpacity)

