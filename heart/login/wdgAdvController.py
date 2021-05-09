from PyQt5.QtWidgets import QWidget
from Telas.wdgAdvogados import Ui_wdgAdv
from modelos.advogadoModelo import AdvogadoModelo


class WdgAdvController(QWidget, Ui_wdgAdv):

    def __init__(self, advogado: AdvogadoModelo,  parent=None):
        super(WdgAdvController, self).__init__(parent=parent)
        self.setupUi(self)

        self.lbNomeAdv.setText(advogado.nomeUsuario + advogado.sobrenomeUsuario)
        self.lbNumeroOAB.setText(advogado.numeroOAB)
