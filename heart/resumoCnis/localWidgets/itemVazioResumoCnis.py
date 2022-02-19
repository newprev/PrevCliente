from PyQt5.QtWidgets import QWidget
from Design.pyUi.itemVazioResumoCNIS import Ui_WdgItemRes


class ItemVazioCnis(QWidget, Ui_WdgItemRes):

    def __init__(self, parent=None):
        super(ItemVazioCnis, self).__init__(parent=parent)
        self.setupUi(self)
