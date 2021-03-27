from PyQt5.QtWidgets import QMainWindow

from Daos.daoCalculos import DaoCalculos
from Telas.insereContrib import Ui_mwInsereContrib
from heart.localStyleSheet.insereContribuicao import habilita
from helpers import dictIndicadores, dictEspecies, mascaraNit
from modelos.clienteModelo import ClienteModelo


class InsereContribuicaoPage(QMainWindow, Ui_mwInsereContrib):

    def __init__(self, parent=None, db=None, cliente: ClienteModelo=None):
        super(InsereContribuicaoPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.tabCalculos = parent
        self.daoCalculos = DaoCalculos(db=db)
        self.db = db
        self.cliente = cliente

        self.lbNomeCompleto.setText(f"{self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}")
        self.lbNit.setText(mascaraNit(self.cliente.nit))
        self.rbBeneficio.setChecked(True)
        self.rbContribuicao.clicked.connect(self.atualizaFoco)
        self.rbRemuneracao.clicked.connect(self.atualizaFoco)
        self.rbBeneficio.clicked.connect(self.atualizaFoco)

        self.atualizaFoco()
        self.carregaQtdsRemCont()
        self.carregaComboBoxes()


    def carregaComboBoxes(self):
        self.cbxIndicadores.addItems(dictIndicadores.keys())
        self.cbxEspecie.addItems(dictEspecies.keys())

    def carregaQtdsRemCont(self):
        qtdRemuneracoes = self.daoCalculos.contaRemuneracoes(self.cliente.clienteId)[0]
        qtdContribuicoes = self.daoCalculos.contaContribuicoes(self.cliente.clienteId)[0]

        self.lbQtdCont.setText(str(qtdContribuicoes))
        self.lbQtdRem.setText(str(qtdRemuneracoes))

    def atualizaFoco(self):
        if self.rbBeneficio.isChecked():
            self.frInfoBeneficio.setStyleSheet(habilita('beneficio', True))
            self.frInfoRemCont.setStyleSheet(habilita('remCont', False))
            self.dtCompetencia.setDisabled(True)
            self.dtFimContRem.setDisabled(True)
            self.leRemuneracao.setDisabled(True)
            self.cbxIndicadores.setDisabled(True)

            self.lbNb.setDisabled(False)
            self.cbxSituacao.setDisabled(False)
            self.cbxEspecie.setDisabled(False)
            self.dtInicio.setDisabled(False)
            self.dtFim.setDisabled(False)
        else:
            if self.rbContribuicao.isChecked():
                self.lbInfoDataFim.setText('Data de Pagamento')
                self.dtFimContRem.setDisabled(False)
            else:
                self.lbInfoDataFim.setText('Data Fim')
                self.dtFimContRem.setDisabled(True)

            self.frInfoBeneficio.setStyleSheet(habilita('beneficio', False))
            self.frInfoRemCont.setStyleSheet(habilita('remCont', True))
            self.dtCompetencia.setDisabled(False)
            self.dtFimContRem.setDisabled(False)
            self.leRemuneracao.setDisabled(False)
            self.cbxIndicadores.setDisabled(False)

            self.lbNb.setDisabled(True)
            self.cbxSituacao.setDisabled(True)
            self.cbxEspecie.setDisabled(True)
            self.dtInicio.setDisabled(True)
            self.dtFim.setDisabled(True)