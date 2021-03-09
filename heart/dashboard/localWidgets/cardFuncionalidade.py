from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from Telas.buttonFuncionalidade import Ui_wdgFuncionalidade
from heart.dashboard.localStyleSheet.cardsFuncionalidade import inicializaCard


class CardFuncionalidade(QWidget, Ui_wdgFuncionalidade):

    def __init__(self, tipo: str = None):
        super(CardFuncionalidade, self).__init__()
        self.setupUi(self)

        self.carregaTipoFuncionalidade(tipo)

    def carregaTipoFuncionalidade(self, tipo: str):
        self.pbFuncionalidade.setStyleSheet(inicializaCard(tipo))

        if tipo is None:
            tipo = ''

        if tipo.upper() == 'CLIENTE':
            self.pbFuncionalidade.setText('Cliente')
        elif tipo.upper() == 'ENTREVISTA':
            self.pbFuncionalidade.setText('Entrevista')
        else:
            self.pbFuncionalidade.setText('Func')