from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox, QTableWidgetItem, QTabBar

from Daos.daoCliente import DaoCliente
from Telas.tabCliente import Ui_wdgTabCliente
from heart.dashboard.localStyleSheet.filtros import ativaFiltro, estiloBotoesFiltro, estiloLabelFiltro
from heart.sinaisCustomizados import Sinais
from helpers import estCivil, getEstados, unmaskAll, calculaIdadeFromString, getEstadoBySigla, mascaraRG, mascaraCPF, \
    mascaraTelCel, mascaraCep, strToDatetime, mascaraNit, getEscolaridade
from modelos.clienteModelo import ClienteModelo
from modelos.cnisModelo import CNISModelo
from newPrevEnums import TamanhoData
from repositorios.integracaoRepositorio import IntegracaoRepository


class TabCliente(Ui_wdgTabCliente, QWidget):

    def __init__(self, db=None, parent=None, entrevista=False):
        super(TabCliente, self).__init__(parent)
        self.setupUi(self)
        self.cliente = ClienteModelo()
        self.db = db
        self.sinais = Sinais()
        self.entrevistaPg = parent
        self.entrevista = entrevista

        self.cnisClienteAtual = None
        self.daoCliente = DaoCliente(db=db)

        self.tblClientes.resizeColumnsToContents()
        self.tblClientes.doubleClicked.connect(self.editarCliente)
        self.tabMain.currentChanged.connect(self.trocaDeAba)

        self.frBuscaNome.hide()
        self.frBuscaEmail.hide()
        self.frBuscaTelefone.hide()
        self.frBuscaRgcpf.hide()
        # self.leCdCliente.setDisabled(True)
        self.sbCdCliente.setDisabled(True)

        self.carregaFiltroAZ()
        self.carregaComboBoxes()
        self.tblClientes.hideColumn(0)

        self.pbAtualizar.clicked.connect(self.trataAtualizaCliente)
        self.pbBuscaCep.clicked.connect(self.buscaCep)
        self.pbArrowNome.clicked.connect(lambda: self.ativaDesativaFiltro('Nome'))
        self.pbArrowTelefone.clicked.connect(lambda: self.ativaDesativaFiltro('Telefone'))
        self.pbArrowRgcpf.clicked.connect(lambda: self.ativaDesativaFiltro('Rgcpf'))
        self.pbArrowEmail.clicked.connect(lambda: self.ativaDesativaFiltro('Email'))
        self.cbClienteAntigo.clicked.connect(self.atualizaStatusCliente)

        self.leRg.editingFinished.connect(lambda: self.leRg.setText(mascaraRG(self.leRg.text())))
        self.leCpf.editingFinished.connect(lambda: self.leCpf.setText(mascaraCPF(self.leCpf.text())))
        self.leTelefone.editingFinished.connect(lambda: self.leTelefone.setText(mascaraTelCel(self.leTelefone.text())))
        self.leCep.editingFinished.connect(lambda: self.leCep.setText(mascaraCep(self.leCep.text())))
        # self.leCdCliente.editingFinished.connect(self.buscaCliente)
        self.sbCdCliente.editingFinished.connect(self.buscaCliente)

        self.leCep.editingFinished.connect(lambda: self.carregaInfoTela('cep'))
        self.leEndereco.textEdited.connect(lambda: self.carregaInfoTela('endereco'))
        self.leCidade.textEdited.connect(lambda: self.carregaInfoTela('cidade'))
        self.leBairro.textEdited.connect(lambda: self.carregaInfoTela('bairro'))
        self.leComplemento.textEdited.connect(lambda: self.carregaInfoTela('complemento'))
        self.leTelefone.textEdited.connect(lambda: self.carregaInfoTela('telefone'))
        self.leCartProf.textEdited.connect(lambda: self.carregaInfoTela('cartProf'))
        self.leProfissao.textEdited.connect(lambda: self.carregaInfoTela('profissao'))
        self.sbCdCliente.valueChanged.connect(lambda: self.carregaInfoTela('sbCliente'))
        self.lePrimeiroNome.textEdited.connect(lambda: self.carregaInfoTela('nomeCliente'))
        self.leSobrenome.textEdited.connect(lambda: self.carregaInfoTela('sobrenomeCliente'))
        self.leRg.textEdited.connect(lambda: self.carregaInfoTela('rg'))
        self.leNumero.textEdited.connect(lambda: self.carregaInfoTela('leNumero'))
        self.dtNascimento.dateChanged.connect(lambda: self.carregaInfoTela('dataNascimento'))
        self.leIdade.textEdited.connect(lambda: self.carregaInfoTela('idade'))
        self.leCpf.textEdited.connect(lambda: self.carregaInfoTela('cpf'))
        self.leNomeMae.textEdited.connect(lambda: self.carregaInfoTela('nomeMae'))
        self.cbxEstCivil.activated.connect(lambda: self.carregaInfoTela('estCivil'))
        self.cbxEscolaridade.activated.connect(lambda: self.carregaInfoTela('cbxEscolaridade'))
        self.leEmail.textEdited.connect(lambda: self.carregaInfoTela('email'))
        self.leNomeBanco.textEdited.connect(lambda: self.carregaInfoTela('leNomeBanco'))
        self.leNumeroConta.textEdited.connect(lambda: self.carregaInfoTela('leNumeroConta'))
        self.leNumeroAgencia.textEdited.connect(lambda: self.carregaInfoTela('leNumeroAgencia'))
        self.leSenhaINSS.textEdited.connect(lambda: self.carregaInfoTela('leSenhaINSS'))

        self.pbCarregaCnis.clicked.connect(self.carregaCnis)

        self.cliente.estadoCivil = self.cbxEstCivil.currentText()

        if entrevista:
            self.entrevistaPg = parent
            self.tabMain.setCurrentIndex(1)
            self.findChild(QTabBar).hide()
            self.sinais.sTrocaInfoLateral.connect(self.atualizaEntrevista)
            self.sinais.sEnviaCliente.connect(self.enviaClienteParaEntrevista)
        else:
            self.atualizaTblClientes()

    def atualizaStatusCliente(self):
        if self.cbClienteAntigo.isChecked():
            # self.leCdCliente.setDisabled(False)
            self.sbCdCliente.setDisabled(False)
        else:
            # self.leCdCliente.setDisabled(True)
            self.sbCdCliente.setDisabled(True)

    def atualizaTblClientes(self, clientes: list = None):
        if clientes is None:
            clientesModels: list = self.daoCliente.buscaTodos(returnModel=True)
        else:
            clientesModels = []

        self.tblClientes.setRowCount(0)
        for numLinha, cliente in enumerate(clientesModels):
            self.tblClientes.insertRow(numLinha)

            cdClienteItem = QTableWidgetItem(str(cliente.clienteId))
            cdClienteItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 0, cdClienteItem)

            nomeCompletoItem = QTableWidgetItem(f"{cliente.nomeCliente} {cliente.sobrenomeCliente}")
            nomeCompletoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 1, nomeCompletoItem)

            emailItem = QTableWidgetItem(f"{cliente.email}")
            emailItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 2, emailItem)

            telefoneItem = QTableWidgetItem(f"{mascaraTelCel(cliente.telefone)}")
            telefoneItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 3, telefoneItem)

            cidadeItem = QTableWidgetItem(f"{cliente.cidade}")
            cidadeItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 4, cidadeItem)

            tipoProcessoItem = QTableWidgetItem('Aposentadoria por tempo de serviço')
            tipoProcessoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 5, tipoProcessoItem)

        self.tblClientes.resizeColumnsToContents()

    def buscaCliente(self):
        if self.sbCdCliente.text() != '':
            cdCliente: int = int(self.sbCdCliente.text())
            self.limpaTudo()
            self.sbCdCliente.setValue(cdCliente)
            self.verificaDados()
            self.cliente = self.daoCliente.buscaClienteById(cdCliente, returnInstance=True)
            if self.cliente is None:
                self.cliente = ClienteModelo()
                self.limpaTudo()
            else:
                self.carregaClienteNaTela(self.cliente)
                if self.entrevista:
                    self.sinais.sEnviaCliente.emit()

    def enviaClienteParaEntrevista(self):
        self.entrevistaPg.atualizaCliente(self.cliente)

    def carregaCnis(self):
        self.cnisClienteAtual = CNISModelo()
        self.cliente.pathCnis = self.cnisClienteAtual.buscaPath()
        if self.cliente.pathCnis is None:
            return False
        infoPessoais: dict = self.cnisClienteAtual.getInfoPessoais()

        if infoPessoais is not None:

            self.cliente.cpfCliente = unmaskAll(infoPessoais['cpf'])
            self.cliente.dataNascimento = strToDatetime(infoPessoais['dataNascimento'])
            self.cliente.idade = calculaIdadeFromString(infoPessoais['dataNascimento'])
            self.cliente.nit = unmaskAll(infoPessoais['nit'])
            self.cliente.nomeMae = infoPessoais['nomeMae'].title()
            self.cliente.nomeCliente = infoPessoais['nomeCompleto'].split(' ')[0].title()
            self.cliente.sobrenomeCliente = ' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]).title()

            if not self.buscaClienteJaCadastrado():
                self.cliente.clienteId = self.daoCliente.cadastroClienteComCnis(self.cliente, self.cnisClienteAtual.getAllDict())

        self.limpaTudo()
        self.carregaClienteNaTela(cliente=self.cliente)
        if self.cliente.numero is None:
            self.cliente.numero = 0

    def buscaClienteJaCadastrado(self) -> bool:
        cliente: ClienteModelo = self.daoCliente.buscaClienteByNit(self.cliente.nit)
        if cliente:
            self.cliente = cliente
            return True
        else:
            return False

    def carregaClienteNaTela(self, cliente: ClienteModelo):

        self.leCpf.setText(mascaraCPF(cliente.cpfCliente))
        self.dtNascimento.setDate(strToDatetime(cliente.dataNascimento))
        self.leIdade.setText(f'{cliente.idade}')
        self.leNomeMae.setText(cliente.nomeMae)
        self.lePrimeiroNome.setText(cliente.nomeCliente)
        self.leSobrenome.setText(cliente.sobrenomeCliente)
        # self.leCdCliente.setText(str(self.cliente.clienteId))
        self.sbCdCliente.setValue(self.cliente.clienteId)

        if cliente.rgCliente not in [None, 'None']:
            self.leRg.setText(mascaraRG(cliente.rgCliente))

        if cliente.numero not in [None, 'None']:
            self.leNumero.setText(str(cliente.numero))

        if cliente.telefone not in [None, 'None']:
            self.leTelefone.setText(mascaraTelCel(cliente.telefone))

        if cliente.email not in [None, 'None']:
            self.leEmail.setText(cliente.email)

        if cliente.cep not in [None, 'None']:
            self.leCep.setText(mascaraCep(cliente.cep))

        if cliente.endereco not in [None, 'None']:
            self.leEndereco.setText(cliente.endereco)

        if cliente.cidade not in [None, 'None']:
            self.leCidade.setText(cliente.cidade)

        if cliente.bairro not in [None, 'None']:
            self.leBairro.setText(cliente.bairro)

        if cliente.estado not in [None, 'None']:
            self.cbxEstado.setCurrentText(cliente.estado)

        if cliente.complemento not in [None, 'None']:
            self.leComplemento.setText(cliente.complemento)

        if cliente.nit not in [None, 'None']:
            self.leNit.setText(mascaraNit(int(cliente.nit)))

        if cliente.numCartProf not in [None, 'None']:
            self.leCartProf.setText(str(cliente.numCartProf))

        if cliente.profissao not in [None, 'None']:
            self.leProfissao.setText(cliente.profissao)

        if cliente.numeroConta not in [None, 'None']:
            self.leNumeroConta.setText(cliente.numeroConta)

        if cliente.nomeBanco not in [None, 'None']:
            self.leNomeBanco.setText(cliente.nomeBanco)

        if cliente.agenciaBanco not in [None, 'None']:
            self.leNumeroAgencia.setText(cliente.agenciaBanco)

        if cliente.grauEscolaridade not in [None, 'None']:
            self.cbxEscolaridade.setCurrentText(cliente.grauEscolaridade)

        if cliente.senhaINSS not in [None, 'None']:
            self.leSenhaINSS.setText(cliente.senhaINSS)

    def carregaInfoTela(self, info, *args):
        if info == 'cep':
            self.cliente.cep = self.leCep.text().replace('-', '')

        elif info == 'endereco':
            self.cliente.endereco = self.leEndereco.text()

        elif info == 'leNomeBanco':
            self.cliente.nomeBanco = self.leNomeBanco.text()

        elif info == 'leNumeroConta':
            self.cliente.numeroConta = self.leNumeroConta.text()

        elif info == 'leNumeroAgencia':
            self.cliente.agenciaBanco = self.leNumeroAgencia.text()

        elif info == 'leSenhaINSS':
            self.cliente.senhaINSS = self.leSenhaINSS.text()

        elif info == 'cidade':
            self.cliente.cidade = self.leCidade.text()

        elif info == 'bairro':
            self.cliente.bairro = self.leBairro.text()

        elif info == 'estado':
            self.cliente.estado = self.cbxEstado.currentText()

        elif info == 'cbxEscolaridade':
            self.cliente.grauEscolaridade = self.cbxEscolaridade.currentText()

        elif info == 'complemento':
            self.cliente.complemento = self.leComplemento.text()

        elif info == 'nit':
            self.cliente.nit = self.leNit.text()

        elif info == 'cartProf':
            self.cliente.numCartProf = self.leCartProf.text()

        elif info == 'profissao':
            self.cliente.profissao = self.leProfissao.text()

        elif info == 'cdCliente':
            if self.leCdCliente.text() != '':
                self.cliente.clienteId = int(self.leCdCliente.text())

        elif info == 'sbCliente':
            if self.sbCdCliente.text() != '':
                self.cliente.clienteId = int(self.sbCdCliente.text())
                self.buscaCliente()

        elif info == 'nomeCliente':
            self.cliente.nomeCliente = self.lePrimeiroNome.text()

        elif info == 'sobrenomeCliente':
            self.cliente.sobrenomeCliente = self.leSobrenome.text()

        elif info == 'rg':
            self.cliente.rgCliente = self.leRg.text()

        elif info == 'dataNascimento':
            self.cliente.dataNascimento = self.dtNascimento.date().toPyDate().strftime('%Y-%m-%d %H:%M')

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

        elif info == 'leNumero':
            if self.leNumero.text() != '':
                self.cliente.numero = int(self.leNumero.text())

        if self.entrevista:
            estadoEntrevista: dict = {
                'pessoais': self.avaliaInfoPessoalCompleta(),
                'residenciais': self.avaliaInfoResidencialCompleta(),
                'profissionais': self.avaliaInfoProfissionalCompleta(),
                'bancarias': self.avaliaInfoBancariaCompleta()
            }
            self.sinais.sTrocaInfoLateral.emit(estadoEntrevista)

    def buscaCep(self):
        integracaoRepository = IntegracaoRepository()
        dictCep: dict = integracaoRepository.getCep(self.leCep.text().replace('-', ''))
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
        self.cbxEscolaridade.addItems(getEscolaridade().keys())
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
        if self.sbCdCliente.text() is not None and self.sbCdCliente.text() != "":
            return True
        else:
            return False

    def carregaFiltroAZ(self):
        listAlfabeto = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        pbStrStyleSheet = estiloBotoesFiltro()
        lbStyleSheet = estiloLabelFiltro()

        for i in range(0, len(listAlfabeto)):

            if i == 0 or i == len(listAlfabeto) - 1:
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

    def limpaTudo(self):
        # self.leCdCliente.clear()
        # self.sbCdCliente.clear()
        self.lePrimeiroNome.clear()
        self.leSobrenome.clear()
        self.leRg.clear()
        self.leIdade.clear()
        self.leCpf.clear()
        self.leNomeMae.clear()
        self.leEmail.clear()
        self.leTelefone.clear()
        self.leCep.clear()
        self.leEndereco.clear()
        self.leCidade.clear()
        self.leBairro.clear()
        self.leComplemento.clear()
        self.leNit.clear()
        self.leCartProf.clear()
        self.leProfissao.clear()
        self.leNomeBanco.clear()
        self.leNumeroAgencia.clear()
        self.leNumeroConta.clear()
        self.leSenhaINSS.clear()
        self.leNumero.clear()

        self.cbxEstado.setCurrentIndex(24)

    def editarCliente(self, *args):
        numLinha: int = args[0].row()
        clienteId = int(self.tblClientes.item(numLinha, 0).text())
        self.sbCdCliente.setValue(clienteId)

        self.buscaCliente()
        self.tabMain.setCurrentIndex(1)

    def trocaDeAba(self, *args):
        abaAtual: int = int(args[0])

        if abaAtual == 0:
            self.atualizaTblClientes()
            self.limpaTudo()

    def showPopupAlerta(self, mensagem, titulo='Atenção!'):
        dialogPopup = QMessageBox()
        dialogPopup.setWindowTitle(titulo)
        dialogPopup.setText(mensagem)
        dialogPopup.setIcon(QMessageBox.Warning)
        dialogPopup.setStandardButtons(QMessageBox.Ok)

        close = dialogPopup.exec_()

    def atualizaEntrevista(self, *args, **kwargs):
        self.entrevistaPg.atualizaInfoLateral(args[0])

    def verificaDados(self):
        if self.cliente.estado is None or self.cliente.estado == '':
            self.cliente.estado = self.cbxEstado.currentText()

    def avaliaInfoPessoalCompleta(self) -> bool:
        return self.lePrimeiroNome.text() != '' and \
               self.leSobrenome.text() != '' and \
               self.leRg.text() != '' and \
               self.leIdade.text() != '' and \
               self.leCpf.text() != '' and \
               self.leNomeMae.text() != '' and \
               self.leTelefone.text() != '' and \
               self.leEmail.text() != ''

    def avaliaInfoResidencialCompleta(self) -> bool:
        return self.leCep.text() != '' and \
               self.leEndereco.text() != '' and \
               self.leCidade.text() != '' and \
               self.leNumero.text() != '' and \
               self.leBairro.text() != ''

    def avaliaInfoProfissionalCompleta(self) -> bool:
        return self.leNit.text() != '' and \
               self.leProfissao.text() != ''

    def avaliaInfoBancariaCompleta(self) -> bool:
        return self.leNomeBanco.text() != '' and \
               self.leNumeroAgencia.text() != '' and \
               self.leNumeroConta.text() != '' and \
               self.leSenhaINSS.text() != ''
