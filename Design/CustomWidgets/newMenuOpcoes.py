from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QSizePolicy

from Design.pyUi.newMenuOpcoes import Ui_newMenuOpcoes
from typing import Callable


class NewMenuOpcoes(Ui_newMenuOpcoes, QFrame):
    def __init__(self, parent=None, funcArquivar: Callable = None, funcEditar: Callable = None, funcExcluir: Callable = None):
        super(NewMenuOpcoes, self).__init__(parent=parent)
        self.setupUi(self)

        self.funcArquivar = funcArquivar
        self.funcEditar = funcEditar
        self.funcExcluir = funcExcluir

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.iniciaLayout()
        self.atualizaTamanho()

    def atualizaTamanho(self):
        newHeight = 24

        if self.funcExcluir is not None:
            newHeight += 44

        if self.funcEditar is not None:
            newHeight += 44

        if self.funcArquivar is not None:
            newHeight += 44

        self.resize(self.width(), newHeight)

    def iniciaLayout(self):
        if self.funcArquivar is None:
            self.pbArquivar.hide()
            self.pbArquivar.close()
            self.pbArquivar.deleteLater()
        else:
            self.pbArquivar.clicked.connect(lambda: self.funcArquivar())

        if self.funcExcluir is None:
            self.pbExcluir.hide()
            self.pbExcluir.close()
            self.pbExcluir.deleteLater()
        else:
            self.pbExcluir.clicked.connect(lambda: self.funcExcluir())

        if self.funcEditar is None:
            self.pbEditar.hide()
            self.pbEditar.close()
            self.pbEditar.deleteLater()
        else:
            self.pbEditar.clicked.connect(lambda: self.funcEditar())

