from PyQt5.QtWidgets import QWidget
from Design.pyUi.wdgCardAposentadoria import Ui_wdgCardAposentadoria

from modelos.aposentadoriaORM import Aposentadoria
from util.helpers import dataUSAtoBR, strTipoAposentadoria, strTipoSimulacao, mascaraDinheiro


class CardAposentadoria(QWidget, Ui_wdgCardAposentadoria):
    aposentadoria: Aposentadoria

    def __init__(self, aposentadoria: Aposentadoria, parent=None):
        super(CardAposentadoria, self).__init__(parent=parent)
        self.setupUi(self)
        self.aposentadoria: Aposentadoria = aposentadoria

        self.carregaInfoNaTela()

    def carregaInfoNaTela(self):
        self.lbIdade.setText(str(self.aposentadoria.idadeCliente) + " anos")
        self.lbDib.setText(dataUSAtoBR(self.aposentadoria.dib, comDias=True))
        self.lbTipoApos.setText(strTipoAposentadoria(self.aposentadoria.tipo))
        self.lbQtdContrib.setText(str(self.aposentadoria.qtdContribuicoes) + '/180')
        self.lbValorBeneficio.setText(mascaraDinheiro(self.aposentadoria.valorBeneficio))
        self.lbTipoSimulacao.setText(strTipoSimulacao(self.aposentadoria.contribSimulacao))
