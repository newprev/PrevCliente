from typing import Callable

from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame

from Design.CustomWidgets.styleSheets.newCardPadrao import firulaHover
from Design.pyUi.efeitos import Efeitos
from Design.pyUi.newCardPadrao import Ui_frCardPadrao
from util.enums.processoEnums import NaturezaProcesso, TipoBeneficio
from util.helpers import strTipoBeneFacilitado


class NewCardPadrao(Ui_frCardPadrao, QFrame):
    onHover: Callable
    onClick: Callable

    def __init__(self, tipoCard, parent=None, onHover: Callable = None, onClick: Callable = None):
        super(NewCardPadrao, self).__init__(parent=parent)
        self.setupUi(self)
        self.tipoCard = tipoCard
        self.onHover = onHover
        self.onClick = onClick

        self.iniciaFuncionalidade()

        if onClick is not None:
            self.pbFuncionalidade.clicked.connect(self.onClick)

    def iniciaFuncionalidade(self):
        if isinstance(self.tipoCard, NaturezaProcesso):
            if self.tipoCard == NaturezaProcesso.administrativo:
                self.pbFuncionalidade.setText('ADMINISTRATIVO')
            else:
                self.pbFuncionalidade.setText('JUDICIAL')

        elif isinstance(self.tipoCard, TipoBeneficio):
            self.pbFuncionalidade.setText(strTipoBeneFacilitado(self.tipoCard).upper())

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.frFirula.setStyleSheet(firulaHover(True))
        Efeitos().shadowCards([self], color=(63, 63, 63, 40))

        if self.onHover is not None:
            self.onHover()

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.frFirula.setStyleSheet(firulaHover(False))
        Efeitos().desativarSombra([self])
