from PyQt5.QtWidgets import QFrame

from Design.pyUi.infoGuiaEntrevista import Ui_frEtapaEntrevista
from Design.CustomWidgets.styleSheets.entrevistaStyles import iconeEscolhido


class InfoGuia(Ui_frEtapaEntrevista, QFrame):
    def __init__(self, infoTexto: str, infoEscolhida: bool, parent=None):
        super(InfoGuia, self).__init__(parent=parent)
        self.setupUi(self)
        self.atualizaInfo(infoTexto, infoEscolhida)

    def atualizaInfo(self, infoTexto: str, infoEscolhida: bool):
        self.lbInfo.setText(infoTexto.title())
        self.frIcone.setStyleSheet(iconeEscolhido(infoEscolhida))
