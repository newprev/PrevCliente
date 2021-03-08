from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from Telas.buttonFuncionalidade import Ui_wdgFuncionalidade


class CardFuncionalidade(QWidget, Ui_wdgFuncionalidade):

    def __init__(self, tipo=None):
        super(CardFuncionalidade, self).__init__()
        self.setupUi(self)

        self.carregaTipoFuncionalidade(tipo)

    def carregaTipoFuncionalidade(self, tipo):
        if tipo == 'cliente':
            self.pbFuncionalidade.setText('Cliente')

        else:
            self.pbFuncionalidade.setText('Func')