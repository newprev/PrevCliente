from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu, QAction

from Design.CustomWidgets.styleSheets.menuOpcoes import estiloMenu
from typing import Callable


class NewMenuOpcoes(QMenu):
    def __init__(
            self,
            parent=None,
            funcArquivar: Callable = None,
            funcProcessos: Callable = None,
            funcDesarquivar: Callable = None,
            funcEditar: Callable = None,
            funcExcluir: Callable = None,
            funcAtualizar: Callable = None,
            funcEntrevista: Callable = None,
            funcResumoCnis: Callable = None,
    ):
        super(NewMenuOpcoes, self).__init__(parent=parent)
        self.carregaEstilo()

        self.funcArquivar = funcArquivar
        self.funcProcessos = funcProcessos
        self.funcDesarquivar = funcDesarquivar
        self.funcEditar = funcEditar
        self.funcExcluir = funcExcluir
        self.funcAtualizar = funcAtualizar
        self.funcEntrevista = funcEntrevista
        self.funcResumoCnis = funcResumoCnis

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)

        self.iniciaLayout()

    def carregaEstilo(self):
        self.setStyleSheet("#NewMenuOpcoes { background-color: transparent; }")
        self.setStyleSheet(estiloMenu())

    def iniciaLayout(self):
        if self.funcArquivar is not None:
            acaoArquivar = QAction('Arquivar', self)
            acaoArquivar.triggered.connect(lambda: self.funcArquivar())
            self.addAction(acaoArquivar)

        if self.funcProcessos is not None:
            acaoProcesso = QAction('Processos', self)
            acaoProcesso.triggered.connect(lambda: self.funcProcessos())
            self.addAction(acaoProcesso)

        if self.funcDesarquivar is not None:
            acaoDesarquivar = QAction('Desarquivar', self)
            acaoDesarquivar.triggered.connect(lambda: self.funcDesarquivar())
            self.addAction(acaoDesarquivar)

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

        if self.funcEntrevista is not None:
            acaoEntrevista = QAction('Entrevista', self)
            acaoEntrevista.triggered.connect(lambda: self.funcEntrevista())
            self.addAction(acaoEntrevista)

        if self.funcResumoCnis is not None:
            acaoResumoCnis = QAction('Resumo CNIS', self)
            acaoResumoCnis.triggered.connect(lambda: self.funcResumoCnis())
            self.addAction(acaoResumoCnis)

