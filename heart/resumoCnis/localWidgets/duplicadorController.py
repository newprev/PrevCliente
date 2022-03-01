from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from Design.pyUi.wdgDuplicador import Ui_mwDuplicador
from Design.efeitos import Efeitos
from sinaisCustomizados import Sinais

from util.popUps import popUpSimCancela, popUpOkAlerta


class DuplicadorController(QMainWindow, Ui_mwDuplicador):
    def __init__(self, salarioContribuicao: int, parent=None):
        super(DuplicadorController, self).__init__(parent=parent)
        self.setupUi(self)
        self.resumoCnis = parent
        self.salContribuicao = salarioContribuicao

        self.sinais = Sinais()
        self.sinais.sEnviaSinal.connect(self.enviaQtdReplicacao)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.efeitos = Efeitos()
        self.efeitos.shadowCards([self.frMain])
        self.efeitos.shadowCards([self.sbQtdMeses], radius=4, color=(63, 63, 63, 90))
        self.sbQtdMeses.setValue(0)
        self.sbQtdMeses.setFocus()

        self.pbFechar.clicked.connect(self.avaliaFecharController)
        self.pbReplicar.clicked.connect(self.sinais.sEnviaSinal.emit)

    def avaliaFecharController(self):
        if self.sbQtdMeses.value() != 0:
            popUpSimCancela(
                "Confirmar sair da janela de replicação?",
                funcaoSim=self.close
            )
        else:
            self.close()

    def enviaQtdReplicacao(self):
        if self.sbQtdMeses.value() != 0:
            self.resumoCnis.replicarInsercao(self.sbQtdMeses.value(), self.salContribuicao)
            self.close()
        else:
            popUpOkAlerta("Informe uma quantidade maior do que 0.", funcao=lambda: self.sbQtdMeses.setFocus())
