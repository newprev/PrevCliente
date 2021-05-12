from PyQt5.QtWidgets import QWidget
from Telas.wdgAdvogados import Ui_wdgAdv
from modelos.advogadoModelo import AdvogadoModelo
from heart.sinaisCustomizados import Sinais


class WdgAdvController(QWidget, Ui_wdgAdv):

    def __init__(self, advogado: AdvogadoModelo,  parent=None):
        super(WdgAdvController, self).__init__(parent=parent)
        self.setupUi(self)
        self.sinais = Sinais()
        self.loginPage = parent
        self.advogado = advogado

        self.lbNomeAdv.setText(self.advogado.nomeUsuario + self.advogado.sobrenomeUsuario)
        self.lbNumeroOAB.setText(self.advogado.numeroOAB)

        self.pbCadastrar.clicked.connect(self.enviaSinal)
        self.sinais.sTrocaPrimeiroAcesso.connect(self.enviaAdv)

    def enviaSinal(self):
        self.sinais.sTrocaPrimeiroAcesso.emit(self.advogado)

    def enviaAdv(self):
        self.loginPage.trocaPagina(self.advogado)
