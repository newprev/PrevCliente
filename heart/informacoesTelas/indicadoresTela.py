from typing import List

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

from Daos.daoInformacoes import DaoInformacoes
from Telas.pgInfoIndicadores import Ui_mwInfoIndicadores
from heart.sinaisCustomizados import Sinais
from modelos.indicadorModelo import IndicadorModelo
from heart.informacoesTelas.localWidgets.wdgIndicadorController import WdgIndicadorController


class IndicadoresController(QMainWindow, Ui_mwInfoIndicadores):

    def __init__(self, parent=None, db=None):
        super(IndicadoresController, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        self.parent = parent
        self.daoInformacoes = DaoInformacoes(db=db)
        self.indicadores = []
        self.indicadoresNoProcesso: List[str] = []
        self.indicadoresVLayout = QVBoxLayout()
        self.sinais = Sinais()
        self.sinais.sEnviaIndicadores.connect(self.enviaIndicadores)

        self.lbSigla.setText('')
        self.lbDescricao.setText('')

        self.pbEnviar.clicked.connect(lambda: self.close())

        self.carregaIndicadores()
        self.carregaLista()

    def recebeIndicador(self, indicador: str, ativo: bool):
        if ativo:
            if indicador not in self.indicadoresNoProcesso:
                self.alteraIndicador(indicador)
                self.indicadoresNoProcesso.append(indicador)
        else:
            self.indicadoresNoProcesso.remove(indicador)

    def carregaLista(self):
        listaIndicadores = list(self.indicadores)
        for indicador in listaIndicadores:
            wdgIndicador = WdgIndicadorController(indicador, parent=self)
            self.indicadoresVLayout.addWidget(wdgIndicador)

        self.scaIndicadores.setLayout(self.indicadoresVLayout)

    def carregaIndicadores(self):
        self.indicadores = list(self.daoInformacoes.buscaIndicadores())

    def alteraIndicador(self, indicadorId: str):
        indicadorAtual: IndicadorModelo = self.returnIndicador(indicadorId)
        self.lbSigla.setText(indicadorAtual.indicadorId)
        self.lbDescricao.setText(indicadorAtual.descricao)
        self.lbResumo.setText(indicadorAtual.resumo)
        self.lbFonte.setText(f"Fonte: {indicadorAtual.fonte}")

    def returnIndicador(self, indicadorId: str):
        for indicador in self.indicadores:
            if indicador.indicadorId == indicadorId:
                return indicador

    def enviaIndicadores(self):
        self.parent.recebeIndicadores(self.indicadoresNoProcesso)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.sinais.sEnviaIndicadores.emit(self.indicadoresNoProcesso)
