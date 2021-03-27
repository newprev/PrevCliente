from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox

from Daos.daoCliente import DaoCliente
from Telas.tabCliente import Ui_wdgTabCliente
from heart.dashboard.localStyleSheet.filtros import ativaFiltro, estiloBotoesFiltro, estiloLabelFiltro
from helpers import estCivil, getEstados, unmaskAll, calculaIdadeFromString, getEstadoBySigla, mascaraRG, mascaraCPF, \
    mascaraTelCel
from modelos.clienteModelo import ClienteModelo
from modelos.cnisModelo import CNISModelo
from repositorios.clienteRepositorio import ClienteRepository


class TabCliente(Ui_wdgTabCliente, QWidget):

    def __init__(self, db=None, parent=None):
        super(TabCliente, self).__init__(parent)
        self.setupUi(self)
        self.cliente = ClienteModelo()
        self.db = db
        self.parent = parent

        self.cnisClienteAtual = None
        self.daoCliente = DaoCliente(db=db)

        self.tblClientes.resizeColumnsToContents()

        self.frBuscaNome.hide()
        self.frBuscaEmail.hide()
        self.frBuscaTelefone.hide()
        self.frBuscaRgcpf.hide()
        self.leCdCliente.setDisabled(True)

        self.carregaFiltroAZ()
        self.carregaComboBoxes()

        self.pbAtualizar.clicked.connect(self.trataAtualizaCliente)
        self.pbBuscaCep.clicked.connect(self.buscaCep)
        self.pbArrowNome.clicked.connect(lambda: self.ativaDesativaFiltro('Nome'))
        self.pbArrowTelefone.clicked.connect(lambda: self.ativaDesativaFiltro('Telefone'))
        self.pbArrowRgcpf.clicked.connect(lambda: self.ativaDesativaFiltro('Rgcpf'))
        self.pbArrowEmail.clicked.connect(lambda: self.ativaDesativaFiltro('Email'))
        self.cbClienteAntigo.clicked.connect(self.atualizaStatusCliente)

        self.leCep.editingFinished.connect(lambda: self.carregaInfoTela('cep'))
        self.leRg.editingFinished.connect(lambda: self.leRg.setText(mascaraRG(self.leRg.text())))
        self.leCpf.editingFinished.connect(lambda: self.leCpf.setText(mascaraCPF(self.leCpf.text())))
        self.leTelefone.editingFinished.connect(lambda: self.leTelefone.setText(mascaraTelCel(self.leTelefone.text())))
        self.leEndereco.textEdited.connect(lambda: self.carregaInfoTela('endereco'))
        self.leCidade.textEdited.connect(lambda: self.carregaInfoTela('cidade'))
        self.leBairro.textEdited.connect(lambda: self.carregaInfoTela('bairro'))
        self.leComplemento.textEdited.connect(lambda: self.carregaInfoTela('complemento'))
        self.leTelefone.textEdited.connect(lambda: self.carregaInfoTela('telefone'))
        self.leCartProf.textEdited.connect(lambda: self.carregaInfoTela('cartProf'))
        self.leProfissao.textEdited.connect(lambda: self.carregaInfoTela('profissao'))
        self.leCdCliente.textEdited.connect(lambda: self.carregaInfoTela('cdCliente'))
        self.lePrimeiroNome.textEdited.connect(lambda: self.carregaInfoTela('nomeCliente'))
        self.leSobrenome.textEdited.connect(lambda: self.carregaInfoTela('sobrenomeCliente'))
        self.leRg.textEdited.connect(lambda: self.carregaInfoTela('rg'))
        self.leDataNascimento.textEdited.connect(lambda: self.carregaInfoTela('dataNascimento'))
        self.leIdade.textEdited.connect(lambda: self.carregaInfoTela('idade'))
        self.leCpf.textEdited.connect(lambda: self.carregaInfoTela('cpf'))
        self.leNomeMae.textEdited.connect(lambda: self.carregaInfoTela('nomeMae'))
        self.cbxEstCivil.activated.connect(lambda: self.carregaInfoTela('estCivil'))
        self.leEmail.textEdited.connect(lambda: self.carregaInfoTela('email'))

        self.pbCarregaCnis.clicked.connect(self.carregaCnis)

        self.cliente.estadoCivil = self.cbxEstCivil.currentText()

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

            self.leDataNascimento.setText(infoPessoais['dataNascimento'])
            self.cliente.dataNascimento = infoPessoais['dataNascimento']

            self.cliente.idade = calculaIdadeFromString(infoPessoais['dataNascimento'])
            self.leIdade.setText(f'{self.cliente.idade}')

            self.leNit.setText(infoPessoais['nit'])
            self.cliente.nit = unmaskAll(infoPessoais['nit'])

            self.leNomeMae.setText(infoPessoais['nomeMae'].title())
            self.cliente.nomeMae = infoPessoais['nomeMae'].title()

            self.lePrimeiroNome.setText(infoPessoais['nomeCompleto'].split(' ')[0].title())
            self.cliente.nomeCliente = infoPessoais['nomeCompleto'].split(' ')[0].title()

            self.leSobrenome.setText(' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]).title())
            self.cliente.sobrenomeCliente = ' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]).title()

        self.cliente.clienteId = self.daoCliente.cadastroClienteComCnis(self.cliente, self.cnisClienteAtual.getAllDict())
        self.leCdCliente.setText(f"{self.cliente.clienteId}")


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

    def carregaInfoTela(self, info, *args):
        if info == 'cep':
            self.cliente.cep = self.leCep.text()

        elif info == 'endereco':
            self.cliente.endereco = self.leEndereco.text()

        elif info == 'cidade':
            self.cliente.cidade = self.leCidade.text()

        elif info == 'bairro':
            self.cliente.bairro = self.leBairro.text()

        elif info == 'estado':
            self.cliente.estado = self.cbxEstado.currentText()

        elif info == 'complemento':
            self.cliente.complemento = self.leComplemento.text()

        elif info == 'nit':
            self.cliente.nit = self.leNit.text()

        elif info == 'cartProf':
            self.cliente.numCartProf = self.leCartProf.text()

        elif info == 'profissao':
            self.cliente.profissao = self.leProfissao.text()

        elif info == 'cdCliente':
            self.cliente.clienteId = self.leCdCliente.text()

        elif info == 'nomeCliente':
            self.cliente.nomeCliente = self.lePrimeiroNome.text()

        elif info == 'sobrenomeCliente':
            self.cliente.sobrenomeCliente = self.leSobrenome.text()

        elif info == 'rg':
            self.cliente.rgCliente = self.leRg.text()

        elif info == 'dataNascimento':
            self.cliente.dataNascimento = self.leDataNascimento.text()

        elif info == 'idade':
            self.cliente.idade = self.leIdade.text()

        elif info == 'cpf':
            self.cliente.cpfCliente = self.leCpf.text()

        elif info == 'nomeMae':
            self.cliente.nomeMae = self.leNomeMae.text()

        elif info == 'estCivil':
            self.cliente.estadoCivil = self.cbxEstCivil.currentText()

        elif info == 'email':
            self.cliente.email = self.leEmail.text()

        elif info == 'telefone':
            self.cliente.telefone = self.leTelefone.text()

    def buscaCep(self):
        clienteRepository = ClienteRepository()
        dictCep: dict = clienteRepository.getCep(self.leCep.text())
        if 'logradouro' in dictCep.keys():
            self.leEndereco.setText(dictCep['logradouro'])
            self.cliente.endereco = dictCep['logradouro']

            self.leComplemento.setText(dictCep['complemento'])
            self.cliente.complemento = dictCep['complemento']

            self.leBairro.setText(dictCep['bairro'])
            self.cliente.bairro = dictCep['bairro']

            self.leCidade.setText(dictCep['localidade'])
            self.cliente.cidade = dictCep['localidade']

            self.cbxEstado.setCurrentText(getEstadoBySigla(dictCep['uf']))
            self.cliente.estado = getEstadoBySigla(dictCep['uf'])
        elif 'erro' in dictCep.keys():
            self.showPopupAlerta(dictCep['erro'])

    def carregaComboBoxes(self):
        self.cbxEstCivil.addItems(estCivil)
        self.cbxEstado.addItems(getEstados().keys())
        self.cbxEstado.setCurrentIndex(24)

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

    def trataAtualizaCliente(self):
        if self.verificaCodCliente():
            self.daoCliente.atualizaCliente(self.cliente)

    def verificaCodCliente(self) -> bool:
        if self.leCdCliente.text() is not None and self.leCdCliente.text() != "":
            return True
        else:
            return False

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

    def showPopupAlerta(self, mensagem, titulo='Atenção!'):
        dialogPopup = QMessageBox()
        dialogPopup.setWindowTitle(titulo)
        dialogPopup.setText(mensagem)
        dialogPopup.setIcon(QMessageBox.Warning)
        dialogPopup.setStandardButtons(QMessageBox.Ok)

        close = dialogPopup.exec_()
