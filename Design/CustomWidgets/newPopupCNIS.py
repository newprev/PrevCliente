from pathlib import Path
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QFileDialog, QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QRect, pyqtProperty, Qt, QEasingCurve, QUrl

from Design.CustomWidgets.newToast import QToaster
from Design.pyUi.wdgEnviaCNIS import Ui_wdgEnviaCNIS

from sinaisCustomizados import Sinais
from util.popUps import popUpOkAlerta


class NewPopupCNIS(QWidget, Ui_wdgEnviaCNIS):
    foraDaTela: bool = False
    dashboard: QMainWindow
    toast: QToaster

    def __init__(self, dashboard=None, parent=None):
        super(NewPopupCNIS, self).__init__(parent=parent)
        self.setupUi(self)
        self.center()
        self.parent = parent
        self.dashboard = dashboard
        self.sinais = Sinais()
        self.sinais.sEnviaPath.connect(self.enviaPath)
        self.sinais.sAbreToast.connect(self.mostraToast)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAcceptDrops(True)
        self.toast = QToaster()

        self.pbBuscaCNIS.clicked.connect(self.abreBuscaCNIS)

    def abreBuscaCNIS(self):
        home = str(Path.home())

        # Ambiente de produção
        pathAux = QFileDialog.getOpenFileName(directory=home)

        if pathAux[0] is not None and pathAux[0] != '':
            if not pathAux[0].endswith('.pdf'):
                pathEscolhido = pathAux[0]
                formatoDoArquivo = pathEscolhido[pathEscolhido.rfind('.') + 1:]
                popUpOkAlerta(
                    f"O arquivo escolhido tem o formato {formatoDoArquivo.upper()}, mas precisa ser do formato PDF.\nTente buscar novamente.",
                    titulo="Formato do arquivo"
                )
            else:
                self.processaCnis(pathAux[0])

    def animacaoEntrada(self):
        wFinal = (self.dashboard.size().width() - self.rect().width())/2
        hFinal = (self.dashboard.size().height() - self.rect().height())/2 - 70

        self.aGeometry = QPropertyAnimation(self, b"geometry")
        self.aGeometry.setDuration(70)
        self.aGeometry.setEasingCurve(QEasingCurve.InSine)
        self.aGeometry.setStartValue(QRect(wFinal, hFinal + 20, self.width(), self.height()))
        self.aGeometry.setEndValue(QRect(wFinal, hFinal, self.width(), self.height()))

        self.aOpacity = QPropertyAnimation(self, b"opacity")
        self.aOpacity.setEasingCurve(QEasingCurve.InSine)
        self.aOpacity.setDuration(70)
        self.aOpacity.setStartValue(0.0)
        self.aOpacity.setEndValue(1)

        self.aGeometry.start()
        self.aOpacity.start()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def dragEnterEvent(self, evento: QtGui.QDragEnterEvent) -> None:
        if evento.mimeData().hasUrls():
            self.sinais.sAbreToast.emit()
            evento.accept()
        else:
            evento.ignore()

    def dragMoveEvent(self, evento: QtGui.QDragMoveEvent) -> None:
        if evento.mimeData().hasUrls():
            evento.setDropAction(Qt.CopyAction)
            evento.accept()
        else:
            evento.ignore()

    def dropEvent(self, evento: QtGui.QDropEvent) -> None:
        if evento.mimeData().hasUrls():
            evento.setDropAction(Qt.CopyAction)
            evento.accept()

            path: QUrl = evento.mimeData().urls()[0]
            if path.isLocalFile():
                pathCnis = path.toLocalFile()
                self.processaCnis(pathCnis)

    def enviaPath(self, pathCnis: str):
        self.close()
        self.parent.recebePathCnis(pathCnis)

    def mostraToast(self):
        self.parent.toastCarregaCnis()

    def processaCnis(self, path: str):
        if os.path.isfile(path):
            self.sinais.sEnviaPath.emit(path)
            
    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.animacaoEntrada()

    def windowOpacity(self):
        return super().windowOpacity()

    def setWindowOpacity(self, opacity):
        super().setWindowOpacity(opacity)

    opacity = pyqtProperty(float, windowOpacity, setWindowOpacity)

