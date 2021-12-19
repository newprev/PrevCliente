from Design.pyUi.newDashboard import Ui_newDashboard
from PyQt5.QtWidgets import QMainWindow


class NewDashboard(QMainWindow, Ui_newDashboard):

    def __init__(self, parent=None):
        super(NewDashboard, self).__init__(parent=parent)
        self.setupUi(self)
