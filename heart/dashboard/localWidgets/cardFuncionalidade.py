from PyQt5.QtWidgets import QWidget

from Design.pyUi.buttonFuncionalidade import Ui_wdgFuncionalidade
from heart.dashboard.localStyleSheet.cardsFuncionalidade import inicializaCard
from sinaisCustomizados import Sinais
from util.enums.dashboardEnums import TelaPosicao


class CardFuncionalidade(QWidget, Ui_wdgFuncionalidade):

    def __init__(self, parent=None, tipo: TelaPosicao = None):
        super(CardFuncionalidade, self).__init__(parent=parent)
        self.setupUi(self)
        self.sinais = Sinais()
        self.dashboard = parent
        self.tipo: TelaPosicao = tipo
        self.pbFuncionalidade.clicked.connect(self.emitirSinal)
        self.sinais.sTrocaWidgetCentral.connect(self.trocaPagina)

        self.carregaTipoFuncionalidade(tipo)

    def carregaTipoFuncionalidade(self, tipo: TelaPosicao):
        self.pbFuncionalidade.setStyleSheet(inicializaCard(tipo))

        if tipo == TelaPosicao.Cliente:
            self.pbFuncionalidade.setText('Cliente')
        elif tipo == TelaPosicao.Entrevista:
            self.pbFuncionalidade.setText('Entrevista')
        elif tipo == TelaPosicao.Calculos:
            self.pbFuncionalidade.setText('Calculos')
        elif tipo == TelaPosicao.Resumo:
            self.pbFuncionalidade.setText('Resumo CNIS')
        elif tipo == TelaPosicao.Processo:
            self.pbFuncionalidade.setText('Processos')
        else:
            self.pbFuncionalidade.setText('Func')

    def emitirSinal(self):
        if self.tipo == TelaPosicao.Cliente:
            self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Cliente)
        elif self.tipo == TelaPosicao.Resumo:
            self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Resumo)
        elif self.tipo == TelaPosicao.Entrevista:
            self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Entrevista)
        elif self.tipo == TelaPosicao.Processo:
            self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Processo)

    def trocaPagina(self, *args):
        self.dashboard.trocarParaPagina(args[0])
