from PyQt5.QtWidgets import QWidget
from Telas.tabTelAfins import Ui_wdgTelAfins

from modelos.clienteModelo import ClienteModelo


class TelAfinsController(QWidget, Ui_wdgTelAfins):

    def __init__(self, cliente: ClienteModelo, db=None, parent=None):
        super(TelAfinsController, self).__init__(parent)
        self.setupUi(self)
        self.db = db


