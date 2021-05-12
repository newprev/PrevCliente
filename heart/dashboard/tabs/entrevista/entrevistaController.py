from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTabBar
from Telas.entrevistaPage import Ui_mwEntrevistaPage
from connections import ConfigConnection
from heart.dashboard.tabs.clienteController import TabCliente
from newPrevEnums import TiposConexoes


class EntrevistaController(QMainWindow, Ui_mwEntrevistaPage):

    def __init__(self, parent=None, db=None):
        super(EntrevistaController, self).__init__(parent)
        self.setupUi(self)
        self.tipoConexao = TiposConexoes.nuvem
        self.dbConnection = ConfigConnection(instanciaBanco=self.tipoConexao)
        # self.db = self.dbConnection.getDatabase()
        self.db = db

        self.clienteController = TabCliente(db=self.db, entrevista=True)

        self.stackedWidget.addWidget(self.clienteController)
        # self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())
        # self.stackedWidget.removeWidget(self.stackedWidget.currentWidget())

        self.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = EntrevistaController()
    ui.show()
    sys.exit(app.exec_())
