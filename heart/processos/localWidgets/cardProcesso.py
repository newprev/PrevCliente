from PyQt5.QtWidgets import QWidget
from Design.pyUi.processoCard import Ui_wdgProcessoCard

from modelos.processosORM import Processos
from util.helpers.helpers import strNatureza, strTipoBeneficio, strTipoProcesso


class CardProcesso(QWidget, Ui_wdgProcessoCard):

    def __init__(self, processo: Processos, parent=None):
        super(CardProcesso, self).__init__(parent=parent)
        self.setupUi(self)

        self.lbNumProcesso.setText(f"{processo.numeroProcesso}")
        self.lbNatureza.setText(strNatureza(processo.natureza))
        self.lbTpBeneficio.setText(strTipoBeneficio(processo.tipoBeneficio, processo.regraAposentadoria))
        self.lbTpProcesso.setText(strTipoProcesso(processo.tipoProcesso))
