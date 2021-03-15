from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from Daos.daoCliente import DaoCliente
from Telas.tabCliente import Ui_wdgTabCliente
from heart.dashboard.localStyleSheet.filtros import ativaFiltro, estiloBotoesFiltro, estiloLabelFiltro
from helpers import estCivil, getEstados, unmaskAll
from modelos.clienteModelo import ClienteModelo
from modelos.cnisModelo import CNISModelo


class TabCliente(Ui_wdgTabCliente, QWidget):

    def __init__(self, db=None, parent=None):
        super(TabCliente, self).__init__(parent)
        self.setupUi(self)
        self.cliente = ClienteModelo()
        self.db = db
        self.parent = parent

        self.cnisClienteAtual = None
        self.daoCliente = DaoCliente(db=db)

        self.frBuscaNome.hide()
        self.frBuscaEmail.hide()
        self.frBuscaTelefone.hide()
        self.frBuscaRgcpf.hide()
        self.leCdCliente.setDisabled(True)

        self.carregaFiltroAZ()
        self.carregaComboBoxes()

        self.pbArrowNome.clicked.connect(lambda: self.ativaDesativaFiltro('Nome'))
        self.pbArrowTelefone.clicked.connect(lambda: self.ativaDesativaFiltro('Telefone'))
        self.pbArrowRgcpf.clicked.connect(lambda: self.ativaDesativaFiltro('Rgcpf'))
        self.pbArrowEmail.clicked.connect(lambda: self.ativaDesativaFiltro('Email'))
        self.cbClienteAntigo.clicked.connect(self.atualizaStatusCliente)

        self.pbCarregaCnis.clicked.connect(self.carregaCnis)

    def atualizaStatusCliente(self):
        if self.cbClienteAntigo.isChecked():
            self.leCdCliente.setDisabled(False)
        else:
            self.leCdCliente.setDisabled(True)

    def carregaCnis(self):
        self.cnisClienteAtual = CNISModelo()
        self.cliente.pathCnis = self.cnisClienteAtual.buscaPath()
        if self.cliente.pathCnis is None:
            return False
        infoPessoais = self.cnisClienteAtual.getInfoPessoais()

        if infoPessoais is not None:
            self.leCpf.setText(infoPessoais['cpf'])
            self.cliente.cpfCliente = unmaskAll(infoPessoais['cpf'])

            self.leNit.setText(infoPessoais['nit'])
            self.cliente.nit = unmaskAll(infoPessoais['nit'])

            self.leNomeMae.setText(infoPessoais['nomeMae'].title())
            self.cliente.nomeMae = infoPessoais['nomeMae'].title()

            self.lePrimeiroNome.setText(infoPessoais['nomeCompleto'].split(' ')[0].title())
            self.cliente.nomeCliente = infoPessoais['nomeCompleto'].split(' ')[0].title()

            self.leSobrenome.setText(' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]).title())
            self.cliente.sobrenomeCliente = ' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]).title()

        self.daoCliente.cadastroClienteComCnis(self.cliente, self.cnisClienteAtual.getAllDict())


        # dfCabecalhos = self.cnisClienteAtual.gerarDataframe()
        # print(dfCabecalhos[['Seq', 'cdEmp', 'nomeEmp']].head(20))
        # print('-------------------------------------------\n')
        #
        # dfcabecalhosBeneficio = self.cnisClienteAtual.gerarDataframe(informacao='cabecalhosBeneficio')
        # print(dfcabecalhosBeneficio[['Seq', 'NB', 'especie', 'situacao']].head(20))
        # print('-------------------------------------------\n')
        #
        # dfRemuneracoes = self.cnisClienteAtual.gerarDataframe(informacao='Remuneracoes')
        # print(dfRemuneracoes.head(20))
        # print('-------------------------------------------\n')
        #
        # dfContribuicoes = self.cnisClienteAtual.gerarDataframe(informacao='Contribuicoes')
        # print(dfContribuicoes.head(20))
        # print('-------------------------------------------\n')
        #
        # dfindicadores = self.cnisClienteAtual.gerarDataframe(informacao='indicadores')
        # print(dfindicadores.head(20))
        # print('-------------------------------------------\n')

    def carregaComboBoxes(self):
        self.cbxEstCivil.addItems(estCivil)
        self.cbxEstado.addItems(getEstados().keys())

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
