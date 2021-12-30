import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFrame, QCheckBox

from Design.DesignSystem.designEnums import FontStyle
from Design.pyUi.menuFiltroContrib_teste import Ui_wdgNewMenu
from util.helpers import dictIndicadores

from sinaisCustomizados import Sinais


class NewSubMenu(QFrame, Ui_wdgNewMenu):
    closed = QtCore.pyqtSignal()
    menuAberto = False
    tabResumos = None

    def __init__(self, parent=None):
        super(NewSubMenu, self).__init__(parent=parent)
        self.setupUi(self)
        self.menuAberto = False
        self.indicadores: dict = dictIndicadores
        self.sinais = Sinais()
        self.alterouDataDe: bool = False
        self.alterouDataAte: bool = False

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.dtDe.setDate(datetime.date.today())
        self.dtAte.setDate(datetime.date.today())

        self.dtDe.dateChanged.connect(lambda: self.alterouData('De'))
        self.dtAte.dateChanged.connect(lambda: self.alterouData('Ate'))

        self.leBusca.textChanged.connect(self.avaliaBusca)
        self.leBusca.setFocus()

    def alterouData(self, tipo: str):
        if tipo == 'De':
            self.alterouDataDe = True
        else:
            self.alterouDataAte = True

    def carregaIndicadores(self):
        if '' in self.indicadores:
            self.indicadores.pop('')

        for chave in self.indicadores.keys():
            self.vlIndicadores.addWidget(QCheckBox(chave, parent=self))

    def enviaParametros(self):
        dateDe: datetime.date = self.dtDe.date().toPyDate().strftime('%Y-%m-%d')
        dateAte: datetime.date = self.dtAte.date().toPyDate().strftime('%Y-%m-%d')
        datas = []
        if self.alterouDataDe:
            datas.append(dateDe)
        else:
            datas.append(None)

        if self.alterouDataAte:
            datas.append(dateAte)
        else:
            datas.append(None)

        indicadoresAEnviar = []
        for index in reversed(range(self.vlIndicadores.count())):
            cbIndicador: QCheckBox = self.vlIndicadores.takeAt(index).widget()
            if cbIndicador.isChecked():
                indicadoresAEnviar.append(cbIndicador.text())

        self.tabResumos.atualizaFiltros(indicadores=indicadoresAEnviar, datas=datas)

    def atualizaSelecao(self, indicadoresSelecionados):
        for index in range(self.vlIndicadores.count()):
            cbIndicador: QCheckBox = self.vlIndicadores.itemAt(index).widget()
            selecionado = cbIndicador.text() in indicadoresSelecionados
            cbIndicador.setChecked(selecionado)

    def avaliaBusca(self, *args):
        filtro = args[0].upper()

        for index in range(self.vlIndicadores.count()):
            cb: QCheckBox = self.vlIndicadores.itemAt(index).widget()
            if filtro in cb.text():
                cb.show()
            else:
                cb.hide()

    def setupInicial(self, **kwargs) -> None:
        self.tabResumos = kwargs['parent']
        self.sinais.sAtualizaParams.connect(self.enviaParametros)
        self.carregaIndicadores()
        self.atualizaSelecao(kwargs['indicadoresSelecionados'])

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        position = self.mapToGlobal(QCursor.pos())
        self.move(position)
        self.menuAberto = True

    def changeEvent(self, a0: QtCore.QEvent) -> None:
        if self.menuAberto and not self.isActiveWindow():
            self.sinais.sAtualizaParams.emit()
            self.close()
