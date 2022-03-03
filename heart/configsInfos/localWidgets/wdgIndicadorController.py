from PyQt5.QtWidgets import QWidget

from Design.efeitos import Efeitos
from Design.pyUi.wdgCheckInfo import Ui_wdgCheckInfo
from sinaisCustomizados import Sinais
from modelos.indicadoresORM import Indicadores


class WdgIndicadorController(QWidget, Ui_wdgCheckInfo):

    def __init__(self, indicador: Indicadores, mostraCb=True, parent=None):
        super(WdgIndicadorController, self).__init__(parent=parent)
        self.setupUi(self)
        self.cbInfo.setText(indicador.indicadorId.upper())
        self.parent = parent
        self.indicador = indicador
        self.sinais = Sinais()
        self.efeitos = Efeitos()

        self.sinais.sEnviaIndicadores.connect(self.enviaIndicador)
        self.cbInfo.clicked.connect(self.avaliaEnvioIndicador)

    def enviaIndicador(self):
        if self.cbInfo.isChecked():
            self.efeitos.shadowCards([self], radius=10, color=(63, 63, 63, 100))
        else:
            self.efeitos.desativarSombra([self])
        self.parent.recebeIndicador(self.indicador.indicadorId, self.cbInfo.isChecked())

    def avaliaEnvioIndicador(self):
        self.sinais.sEnviaIndicadores.emit([])
