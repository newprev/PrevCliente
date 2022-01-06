from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu, QAction

from Design.CustomWidgets.styleSheets.menuOpcoes import estiloMenu
from typing import Callable


class NewMenuOpcoes(QMenu):
    def __init__(self, parent=None, funcArquivar: Callable = None, funcEditar: Callable = None, funcExcluir: Callable = None, funcAtualizar: Callable = None):
        super(NewMenuOpcoes, self).__init__(parent=parent)
        self.carregaEstilo()

        self.funcArquivar = funcArquivar
        self.funcEditar = funcEditar
        self.funcExcluir = funcExcluir
        self.funcAtualizar = funcAtualizar

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)

        self.iniciaLayout()

    def carregaEstilo(self):
        # print(f"{self.dumpObjectTree()=}")
        self.setStyleSheet("#NewMenuOpcoes { background-color: transparent; }")
        self.setStyleSheet(estiloMenu())

    def iniciaLayout(self):
        if self.funcArquivar is not None:
            acaoArquivar = QAction('Arquivar', self)
            acaoArquivar.triggered.connect(lambda: self.funcArquivar())
            self.addAction(acaoArquivar)

        if self.funcExcluir is not None:
            acaoExcluir = QAction('Excluir', self)
            acaoExcluir.triggered.connect(lambda: self.funcExcluir())
            self.addAction(acaoExcluir)

        if self.funcEditar is not None:
            acaoEditar = QAction('Editar', self)
            acaoEditar.triggered.connect(lambda: self.funcEditar())
            self.addAction(acaoEditar)

        if self.funcAtualizar is not None:
            acaoAtualizar = QAction('Atualizar', self)
            acaoAtualizar.triggered.connect(lambda: self.funcAtualizar())
            self.addAction(acaoAtualizar)

