from PyQt5.QtWidgets import QWidget
from Design.pyUi.pgInformacoesGerais import Ui_wdgInfoGerais


class InformacoesGerais(QWidget, Ui_wdgInfoGerais):
    def __init__(self, parent=None):
        super(InformacoesGerais, self).__init__(parent=parent)
        self.setupUi(self)

