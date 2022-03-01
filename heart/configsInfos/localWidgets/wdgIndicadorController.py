from PyQt5.QtWidgets import QWidget

from Design.efeitos import Efeitos
from Design.pyUi.wdgIndicador import Ui_wdgIndicador
from sinaisCustomizados import Sinais
from modelos.indicadoresORM import Indicadores


class WdgIndicadorController(QWidget, Ui_wdgIndicador):

    def __init__(self, indicador: Indicadores, mostraCb=True, parent=None):
        super(WdgIndicadorController, self).__init__(parent=parent)
        self.setupUi(self)
        self.cbIndicador.setText(indicador.indicadorId.upper())
        self.parent = parent
        self.indicador = indicador
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sEnviaIndicadores.connect(self.enviaIndicador)
        self.cbIndicador.clicked.connect(self.avaliaEnvioIndicador)

    def enviaIndicador(self):
        if self.cbIndicador.isChecked():
            self.efeitos.shadowCards([self], radius=10, color=(63, 63, 63, 100))
        else:
            self.efeitos.desativarSombra([self])
        self.parent.recebeIndicador(self.indicador.indicadorId, self.cbIndicador.isChecked())

    def avaliaEnvioIndicador(self):
        self.sinais.sEnviaIndicadores.emit([])
