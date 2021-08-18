from PyQt5.QtWidgets import QWidget

from Telas.efeitos import Efeitos
from Telas.wdgIndicador import Ui_wdgIndicador
from heart.sinaisCustomizados import Sinais
from modelos.indicadorModelo import IndicadorModelo


class WdgIndicadorController(QWidget, Ui_wdgIndicador):

    def __init__(self, indicador: IndicadorModelo, parent=None):
        super(WdgIndicadorController, self).__init__(parent=parent)
        self.setupUi(self)
        self.cbIndicador.setText(indicador.indicadorId)
        self.parent = parent
        self.indicador = indicador
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sEnviaIndicadores.connect(self.enviaIndicador)
        self.cbIndicador.clicked.connect(self.avaliaEnvioIndicador)

    def enviaIndicador(self):
        if self.cbIndicador.isChecked():
            self.efeitos.shadowCards([self])
        else:
            self.efeitos.desativarSombra([self])
        self.parent.recebeIndicador(self.indicador.indicadorId, self.cbIndicador.isChecked())

    def avaliaEnvioIndicador(self):
        self.sinais.sEnviaIndicadores.emit([])
