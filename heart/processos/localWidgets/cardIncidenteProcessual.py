from PyQt5.QtWidgets import QWidget
from Design.pyUi.cardIncidenteProcessual import Ui_wdgIncidenteProcessual
from modelos.incidenteProcessual import IncidenteProcessual
from util.helpers.dateHelper import strDataPorExtenso
from util.helpers.helpers import strSituacaoProcessual


class CardIncidenteProcessual(QWidget, Ui_wdgIncidenteProcessual):
    incidenteAtual: IncidenteProcessual

    def __init__(self, incidenteAtual: IncidenteProcessual, parent=None):
        super(CardIncidenteProcessual, self).__init__(parent=parent)
        self.setupUi(self)
        self.incidenteAtual = incidenteAtual

        self.carregaInfo()

    def carregaInfo(self):
        self.lbSeq.setText(str(self.incidenteAtual.seq))
        self.lbAndamento.setText(strSituacaoProcessual(self.incidenteAtual.andamento))
        self.lbDescricao.setText(self.incidenteAtual.descricao)
        self.lbDataIncidente.setText(strDataPorExtenso(self.incidenteAtual.dataIncidente))
