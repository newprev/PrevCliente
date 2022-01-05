from typing import Union

from PyQt5.QtWidgets import QWidget
from Design.pyUi.wdgMenuButton import Ui_wdgMenuButton
from heart.informacoesTelas.expSobrevidaTela import ExpSobrevidaTela
from heart.informacoesTelas.indicadoresTela import IndicadoresController
from heart.informacoesTelas.tetosPrevidenciariosTela import TetosPrevidenciarios
from sinaisCustomizados import Sinais
from util.enums.configEnums import TipoConfiguracao

from util.enums.dashboardEnums import TelaPosicao, Icone, TextoBotao
from util.enums.ferramentasEInfoEnums import FerramentasEInfo


class NewMenuButton(QWidget, Ui_wdgMenuButton):
    tipoBotao: Union[TelaPosicao, FerramentasEInfo, TipoConfiguracao]

    def __init__(self, dashboard=None, parent=None):
        super(NewMenuButton, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent
        self.dashboard = dashboard
        self.sinais = Sinais()

        self.pbFuncionalidade.clicked.connect(self.verificaFluxo)
        self.sinais.sTrocaWidgetCentral.connect(self.enviaTrocaTela)

    def setupInicial(self, tela: TelaPosicao = None, ferramenta: FerramentasEInfo = None, configuracoes: TipoConfiguracao = None):
        if tela is not None:
            self.tipoBotao = tela

            if tela == TelaPosicao.Cliente:
                icone = Icone.cliente.value
                texto = TextoBotao.cliente.value
            elif tela == TelaPosicao.Resumo:
                icone = Icone.resumo.value
                texto = TextoBotao.resumo.value
            elif tela == TelaPosicao.Processo:
                icone = Icone.processos.value
                texto = TextoBotao.processos.value
            elif tela == TelaPosicao.Entrevista:
                icone = Icone.entrevista.value
                texto = TextoBotao.entrevista.value

        elif ferramenta is not None:
            self.tipoBotao = ferramenta

            if ferramenta == FerramentasEInfo.indicadores:
                icone = Icone.indicadores.value
                texto = TextoBotao.indicadores.value
            elif ferramenta == FerramentasEInfo.ipca:
                icone = Icone.ipca.value
                texto = TextoBotao.ipca.value
            elif ferramenta == FerramentasEInfo.tetos:
                icone = Icone.tetos.value
                texto = TextoBotao.tetos.value
            elif ferramenta == FerramentasEInfo.expSobrevida:
                icone = Icone.expSobrevida.value
                texto = TextoBotao.expSobrevida.value

        elif configuracoes is not None:
            self.tipoBotao = configuracoes

            if configuracoes == TipoConfiguracao.sistema:
                icone = Icone.configSistema.value
                texto = TextoBotao.configSistema.value

        style = f"""
            #pbFuncionalidade {{
            background-color: #DDDEDF;
            border-radius: 15px;

            background-image: {icone};
            background-repeat: no-repeat;
            background-position: center;
        }}
        
            #pbFuncionalidade:hover {{
            background-color: #F2F2F2;
            border-radius: 15px;

            background-image: {icone};
            background-repeat: no-repeat;
            background-position: center;
        }}
"""

        self.pbFuncionalidade.setStyleSheet(style)
        self.lbNomeFuncionalidade.setText(texto)

    def enviaTrocaTela(self):
        self.dashboard.trocaTela(self.tipoBotao)

    def verificaFluxo(self):
        if isinstance(self.tipoBotao, TelaPosicao):
            self.sinais.sTrocaWidgetCentral.emit()

        elif isinstance(self.tipoBotao, FerramentasEInfo):
            if self.tipoBotao == FerramentasEInfo.indicadores:
                IndicadoresController(parent=self).show()
            elif self.tipoBotao == FerramentasEInfo.tetos:
                TetosPrevidenciarios(parent=self).show()
            elif self.tipoBotao == FerramentasEInfo.expSobrevida:
                ExpSobrevidaTela(parent=self).show()
