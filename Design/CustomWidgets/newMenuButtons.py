from PyQt5.QtWidgets import QWidget
from Design.pyUi.wdgMenuButton import Ui_wdgMenuButton
from sinaisCustomizados import Sinais

from util.enums.dashboardEnums import TelaPosicao, Icone, TextoBotao


class NewMenuButton(QWidget, Ui_wdgMenuButton):
    tipoBotao:TelaPosicao

    def __init__(self, dashboard=None, parent=None):
        super(NewMenuButton, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent
        self.dashboard = dashboard
        self.sinais = Sinais()

        self.pbFuncionalidade.clicked.connect(self.emiteSinal)
        self.sinais.sTrocaWidgetCentral.connect(self.enviaTrocaTela)

    def setupInicial(self, tipo: TelaPosicao):
        self.tipoBotao = tipo

        if tipo == TelaPosicao.Cliente:
            icone = Icone.cliente.value
            texto = TextoBotao.cliente.value
        elif tipo == TelaPosicao.Resumo:
            icone = Icone.resumo.value
            texto = TextoBotao.resumo.value
        elif tipo == TelaPosicao.Processo:
            icone = Icone.processos.value
            texto = TextoBotao.processos.value
        elif tipo == TelaPosicao.Entrevista:
            icone = Icone.entrevista.value
            texto = TextoBotao.entrevista.value

        style = f"""
        #pbFuncionalidade {{
        background-color: #DDDEDF;
        border-radius: 15px;
    
        background-image: {icone};
        background-repeat: no-repeat;
        background-position: center;
        }}"""

        self.pbFuncionalidade.setStyleSheet(style)
        self.lbNomeFuncionalidade.setText(texto)

    def enviaTrocaTela(self):
        self.dashboard.trocaTela(self.tipoBotao)

    def emiteSinal(self):
        self.sinais.sTrocaWidgetCentral.emit()
