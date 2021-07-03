from PyQt5.QtWidgets import QMainWindow

from Daos.daoInformacoes import DaoInformacoes
from Telas.pgInfoIndicadores import Ui_mwInfoIndicadores
from modelos.indicadorModelo import IndicadorModelo


class IndicadoresController(QMainWindow, Ui_mwInfoIndicadores):

    def __init__(self, parent=None, db=None):
        super(IndicadoresController, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        self.parent = parent
        self.daoInformacoes = DaoInformacoes(db=db)
        self.indicadores = []

        self.lbSigla.setText('')
        self.lbIndicadorDesc.setText('')

        self.cbxIndicadores.currentIndexChanged.connect(self.alteraIndicador)

        self.carregaIndicadores()
        self.carregaComboBox()

    def carregaComboBox(self):
        listaSiglas = (indicador.sigla for indicador in self.indicadores)
        self.cbxIndicadores.addItems(listaSiglas)

    def carregaIndicadores(self):
        self.indicadores = list(self.daoInformacoes.buscaIndicadores())

    def alteraIndicador(self):
        indicadorAtual: IndicadorModelo = self.returnIndicador(self.cbxIndicadores.currentText())
        self.lbSigla.setText(indicadorAtual.sigla)
        self.lbIndicadorDesc.setText(indicadorAtual.descricao)

    def returnIndicador(self, sigla: str):
        for indicador in self.indicadores:
            if indicador.sigla == sigla:
                return indicador
