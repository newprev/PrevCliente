from PyQt5.QtWidgets import QWidget

from Design.pyUi.pgInformacoesGerais import Ui_wdgInfoGerais
from heart.informacoesTelas.indicadoresTela import IndicadoresController
from heart.informacoesTelas.tetosPrevidenciáriosTela import TetosPrevidenciarios
from heart.informacoesTelas.expSobrevidaTela import ExpSobrevidaTela


class InformacoesGerais(QWidget, Ui_wdgInfoGerais):
    def __init__(self, parent=None):
        super(InformacoesGerais, self).__init__(parent=parent)
        self.setupUi(self)

        self.pbIndicadores.clicked.connect(self.abrirIndicadoresCnis)
        self.pbTetosPrev.clicked.connect(self.abrirTetosPrev)
        self.pbExpSobrevida.clicked.connect(self.abrirExpSobrevida)

    def abrirIndicadoresCnis(self):
        IndicadoresController(parent=self).show()

    def abrirTetosPrev(self):
        TetosPrevidenciarios(parent=self).show()

    def abrirExpSobrevida(self):
        ExpSobrevidaTela(parent=self).show()

