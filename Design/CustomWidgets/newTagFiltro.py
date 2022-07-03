import datetime

from PyQt5.QtWidgets import QWidget

from typing import Union
from util.helpers.dateHelper import mascaraData

from Design.CustomWidgets.styleSheets.tagStyles import tipoTagFiltro, textTagFiltro
from Design.pyUi.wdgTagFiltro import Ui_wdgTagFiltro

from sinaisCustomizados import Sinais

from util.enums.newPrevEnums import TipoFiltro


class NewTagFiltro(QWidget, Ui_wdgTagFiltro):
    def __init__(self, filtro: Union[str, datetime.datetime], tipoFiltro: TipoFiltro, dataInicio: bool = False, parent=None):
        super(NewTagFiltro, self).__init__(parent=parent)
        self.setupUi(self)
        self.sinais = Sinais()
        self.parent = parent
        self.sinais.sExcluiFiltro.connect(self.enviaFiltroExcluido)
        self.tipoFiltro: TipoFiltro = tipoFiltro
        self.dataInicio: bool = dataInicio

        self.defineLabel(filtro, tipoFiltro)
        self.pbExcluir.clicked.connect(self.sinais.sExcluiFiltro.emit)
        self.frMain.setStyleSheet(tipoTagFiltro(tipoFiltro))
        self.lbFiltro.setStyleSheet(textTagFiltro(tipoFiltro))

    def enviaFiltroExcluido(self):
        if self.tipoFiltro == TipoFiltro.data:
            self.parent.excluiuFiltro(self.lbFiltro.text(), TipoFiltro.data)
        else:
            self.parent.excluiuFiltro(self.lbFiltro.text(), TipoFiltro.indicador)

        self.close()

    def defineLabel(self, filtro: Union[str, datetime.datetime], tipo: TipoFiltro):
        if tipo == TipoFiltro.data:
            if self.dataInicio:
                self.lbFiltro.setText(f"De: {mascaraData(filtro)}")
            else:
                self.lbFiltro.setText(f"Até: {mascaraData(filtro)}")
        else:
            self.lbFiltro.setText(filtro)

