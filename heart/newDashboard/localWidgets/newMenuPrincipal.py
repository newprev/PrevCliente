from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFrame

from Design.pyUi.wdgMenuPrincipal import Ui_wdgMenuPrincipal
from Design.CustomWidgets.newMenuButtons import NewMenuButton
from util.enums.configEnums import TipoConfiguracao

from util.enums.dashboardEnums import TelaPosicao
from util.enums.ferramentasEInfoEnums import FerramentasEInfo


class NewMenuPrincipal(QFrame, Ui_wdgMenuPrincipal):

    def __init__(self, parent=None, **kwargs):
        super(NewMenuPrincipal, self).__init__(parent=parent, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.adicionaBotoes()

    def adicionaBotoes(self):
        # Principal
        wdgCliente = NewMenuButton(None)
        wdgEntrevista = NewMenuButton(None)
        wdgProcesso = NewMenuButton(None)
        wdgResumo = NewMenuButton(None)

        wdgCliente.setupInicial(TelaPosicao.Cliente)
        wdgEntrevista.setupInicial(TelaPosicao.Entrevista)
        wdgProcesso.setupInicial(TelaPosicao.Processo)
        wdgResumo.setupInicial(TelaPosicao.Resumo)

        self.glPrincipal.addWidget(wdgCliente, 0, 0)
        self.glPrincipal.addWidget(wdgEntrevista, 0, 1)
        self.glPrincipal.addWidget(wdgProcesso, 1, 0)
        self.glPrincipal.addWidget(wdgResumo, 1, 1)

        # Ferramentas
        wdgFIndicadores = NewMenuButton(None)
        wdgFTetosPrev = NewMenuButton(None)
        wdgFExpSobrevida = NewMenuButton(None)

        wdgFIndicadores.setupInicial(ferramenta=FerramentasEInfo.indicadores)
        wdgFTetosPrev.setupInicial(ferramenta=FerramentasEInfo.tetos)
        wdgFExpSobrevida.setupInicial(ferramenta=FerramentasEInfo.expSobrevida)

        self.glFerramentas.addWidget(wdgFIndicadores, 0, 0)
        self.glFerramentas.addWidget(wdgFTetosPrev, 0, 1)
        self.glFerramentas.addWidget(wdgFExpSobrevida, 1, 0)

        # Configurações
        wdgConfiguracoes = NewMenuButton(None)

        wdgConfiguracoes.setupInicial(configuracoes=TipoConfiguracao.sistema)

        self.glConfiguracoes.addWidget(wdgConfiguracoes)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        geo = self.geometry()
        parentRect = self.parent.rect()
        geo.moveTopLeft(parentRect.topRight() - self.rect().topRight() + QtCore.QPoint(-20, 20))

        self.setGeometry(geo)
        self.show()

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.close()
