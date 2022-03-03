from PyQt5.QtWidgets import QWidget
from Design.pyUi.wdgCheckInfo import Ui_wdgCheckInfo
from modelos.Auxiliares.tipoInfo import InformacaoModel
from sinaisCustomizados import Sinais


class WdgCheckInfo(QWidget, Ui_wdgCheckInfo):
    def __init__(self, infoModel: InformacaoModel, parent=None):
        super(WdgCheckInfo, self).__init__(parent=parent)
        self.setupUi(self)
        self.cbInfo.setText(infoModel.descricao.upper())
        self.parent = parent
        self.infoModel = infoModel
        self.sinais = Sinais()

        self.sinais.sEnviaSinal.connect(self.enviaInfo)
        self.cbInfo.clicked.connect(self.avaliaEnvioIndicador)

    def enviaInfo(self):
        metodoPai = getattr(self.parent, 'recebeInfo', None)
        if callable(metodoPai):
            self.parent.recebeInfo(self.infoModel)
        else:
            print("Não possui método")

    def avaliaEnvioIndicador(self):
        self.sinais.sEnviaSinal.emit()

