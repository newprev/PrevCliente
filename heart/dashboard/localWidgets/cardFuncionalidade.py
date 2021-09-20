from PyQt5.QtWidgets import QWidget

from Design.pyUi.buttonFuncionalidade import Ui_wdgFuncionalidade
from heart.dashboard.localStyleSheet.cardsFuncionalidade import inicializaCard
from heart.sinaisCustomizados import Sinais
from util.enums.telaEnums import TelaPosicao


class CardFuncionalidade(QWidget, Ui_wdgFuncionalidade):

    def __init__(self, parent=None, tipo: str = None):
        super(CardFuncionalidade, self).__init__(parent=parent)
        self.setupUi(self)
        self.sinais = Sinais()
        self.dashboard = parent
        self.tipo = tipo
        self.pbFuncionalidade.clicked.connect(self.emitirSinal)
        self.sinais.sTrocaWidgetCentral.connect(self.trocaPagina)

        self.carregaTipoFuncionalidade(tipo)

    def carregaTipoFuncionalidade(self, tipo: str):
        self.pbFuncionalidade.setStyleSheet(inicializaCard(tipo))

        if tipo is None:
            tipo = ''

        if tipo.upper() == 'CLIENTE':
            self.pbFuncionalidade.setText('Cliente')
        elif tipo.upper() == 'ENTREVISTA':
            self.pbFuncionalidade.setText('Entrevista')
        elif tipo.upper() == 'CALCULOS':
            self.pbFuncionalidade.setText('Calculos')
        elif tipo.upper() == 'RESUMO':
            self.pbFuncionalidade.setText('Resumo CNIS')
        else:
            self.pbFuncionalidade.setText('Func')

    def emitirSinal(self):
        if self.tipo.upper() == 'CLIENTE':
            self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Cliente)
        elif self.tipo.upper() == 'RESUMO':
            self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Resumo)
        elif self.tipo.upper() == 'ENTREVISTA':
            self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Entrevista)

    def trocaPagina(self, *args, **kwargs):
        self.dashboard.trocarParaPagina(args[0])
