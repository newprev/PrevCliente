from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from Telas.tabCliente import Ui_wdgTabCliente
from heart.dashboard.localStyleSheet.filtros import ativaFiltro, estiloBotoesFiltro, estiloLabelFiltro
from helpers import estCivil
from modelos.cnisModelo import CNISModelo


class TabCliente(Ui_wdgTabCliente, QWidget):

    def __init__(self, db=None, parent=None):
        super(TabCliente, self).__init__(parent)
        self.setupUi(self)

        self.cnisClienteAtual = None

        self.frBuscaNome.hide()
        self.frBuscaEmail.hide()
        self.frBuscaTelefone.hide()
        self.frBuscaRgcpf.hide()

        self.carregaFiltroAZ()

        self.pbArrowNome.clicked.connect(lambda: self.ativaDesativaFiltro('Nome'))
        self.pbArrowTelefone.clicked.connect(lambda: self.ativaDesativaFiltro('Telefone'))
        self.pbArrowRgcpf.clicked.connect(lambda: self.ativaDesativaFiltro('Rgcpf'))
        self.pbArrowEmail.clicked.connect(lambda: self.ativaDesativaFiltro('Email'))

        self.db = db
        self.pbCarregaCnis.clicked.connect(self.carregaCnis)

        self.cbxEstCivil.addItems(estCivil)

    def carregaCnis(self):
        self.cnisClienteAtual = CNISModelo()
        self.cnisClienteAtual.buscaPath()
        infoPessoais = self.cnisClienteAtual.getInfoPessoais()

        if infoPessoais is not None:
            self.leCpf.setText(infoPessoais['cpf'])
            self.leNit.setText(infoPessoais['nit'])
            self.leNomeMae.setText(infoPessoais['nomeMae'])
            self.lePrimeiroNome.setText(infoPessoais['nomeCompleto'].split(' ')[0])
            self.leSobrenome.setText(' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]))

        dfCabecalhos = self.cnisClienteAtual.gerarDataframe()
        print(dfCabecalhos[['Seq', 'cdEmp', 'nomeEmp']].head(20))
        print('-------------------------------------------\n')

        dfcabecalhosBeneficio = self.cnisClienteAtual.gerarDataframe(informacao='cabecalhosBeneficio')
        print(dfcabecalhosBeneficio[['Seq', 'NB', 'especie', 'situacao']].head(20))
        print('-------------------------------------------\n')

        dfRemuneracoes = self.cnisClienteAtual.gerarDataframe(informacao='Remuneracoes')
        print(dfRemuneracoes.head(20))
        print('-------------------------------------------\n')

        dfContribuicoes = self.cnisClienteAtual.gerarDataframe(informacao='Contribuicoes')
        print(dfContribuicoes.head(20))
        print('-------------------------------------------\n')

        dfindicadores = self.cnisClienteAtual.gerarDataframe(informacao='indicadores')
        print(dfindicadores.head(20))
        print('-------------------------------------------\n')

    def ativaDesativaFiltro(self, nomeFiltro: str):
        if nomeFiltro.upper() == 'NOME':
            if self.frBuscaNome.isHidden():
                self.pbArrowNome.setStyleSheet(ativaFiltro(False, "pbArrowNome"))
                self.frBuscaNome.show()
            else:
                self.pbArrowNome.setStyleSheet(ativaFiltro(True, "pbArrowNome"))
                self.leBuscaNome.clear()
                self.frBuscaNome.hide()

        elif nomeFiltro.upper() == 'EMAIL':
            if self.frBuscaEmail.isHidden():
                self.pbArrowEmail.setStyleSheet(ativaFiltro(False, "pbArrowEmail"))
                self.frBuscaEmail.show()
            else:
                self.pbArrowEmail.setStyleSheet(ativaFiltro(True, "pbArrowEmail"))
                self.frBuscaEmail.hide()
                self.leBuscaEmail.clear()

        elif nomeFiltro.upper() == 'RGCPF':
            if self.frBuscaRgcpf.isHidden():
                self.pbArrowRgcpf.setStyleSheet(ativaFiltro(False, "pbArrowRgcpf"))
                self.frBuscaRgcpf.show()
            else:
                self.pbArrowRgcpf.setStyleSheet(ativaFiltro(True, "pbArrowRgcpf"))
                self.frBuscaRgcpf.hide()
                self.leBuscaRgcpf.clear()

        elif nomeFiltro.upper() == 'TELEFONE':
            if self.frBuscaTelefone.isHidden():
                self.pbArrowTelefone.setStyleSheet(ativaFiltro(False, "pbArrowTelefone"))
                self.frBuscaTelefone.show()
            else:
                self.pbArrowTelefone.setStyleSheet(ativaFiltro(True, "pbArrowTelefone"))
                self.frBuscaTelefone.hide()
                self.leBuscaTelefone.clear()

    def carregaFiltroAZ(self):
        listAlfabeto = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        pbStrStyleSheet = estiloBotoesFiltro()
        lbStyleSheet = estiloLabelFiltro()

        for i in range(0, len(listAlfabeto)):

            if i == 0 or i == len(listAlfabeto)-1:
                label = QLabel(' ')
                label.setFixedSize(20, 20)
                label.setStyleSheet(lbStyleSheet)
                self.hlFlitroAlfabetico.addWidget(label)
            else:
                button = QPushButton(listAlfabeto[i])
                button.setFixedSize(20, 20)
                button.setStyleSheet(pbStrStyleSheet)
                # button.clicked.connect(lambda state, i=i: self.filtroAZ(i))
                self.hlFlitroAlfabetico.addWidget(button)
