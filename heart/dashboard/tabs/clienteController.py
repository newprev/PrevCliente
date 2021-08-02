from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox, QTableWidgetItem, QTabBar

from Daos.daoCliente import DaoCliente
from Daos.daoTelAfins import DaoTelAfins
from Daos.daoProcessos import DaoProcessos

from Telas.tabCliente import Ui_wdgTabCliente

from heart.dashboard.localStyleSheet.filtros import ativaFiltro, estiloBotoesFiltro, estiloLabelFiltro
from heart.sinaisCustomizados import Sinais
from heart.telAfinsController import TelAfinsController

from modelos.clienteModelo import ClienteModelo
from modelos.cnisModelo import CNISModelo
from modelos.processosModelo import ProcessosModelo
from modelos.modelsORM import Cliente

from helpers import *

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
        self.carregandoCliente = False

        self.cnisClienteAtual = None
        self.daoCliente = DaoCliente(db=db)
        self.daoTelAfins = DaoTelAfins(db=db)
        self.daoProcessos = DaoProcessos(db=db)

        self.tblClientes.resizeColumnsToContents()
        self.tblClientes.doubleClicked.connect(self.editarCliente)
        self.tblClientes.hideColumn(0)

        self.tabMain.currentChanged.connect(self.trocaDeAba)

        self.frBuscaNome.hide()
        self.frBuscaEmail.hide()
        self.frBuscaTelefone.hide()
        self.frBuscaRgcpf.hide()
        self.sbCdCliente.setDisabled(True)

        self.carregaFiltroAZ()
        self.carregaComboBoxes()

        self.pbAtualizar.clicked.connect(self.trataAtualizaCliente)
        self.pbBuscaCep.clicked.connect(self.buscaCep)
        self.pbArrowNome.clicked.connect(lambda: self.ativaDesativaFiltro('Nome'))
        self.pbArrowTelefone.clicked.connect(lambda: self.ativaDesativaFiltro('Telefone'))
        self.pbArrowRgcpf.clicked.connect(lambda: self.ativaDesativaFiltro('Rgcpf'))
        self.pbArrowEmail.clicked.connect(lambda: self.ativaDesativaFiltro('Email'))
        self.pbCarregaCnis.clicked.connect(self.carregaCnis)
        self.pbMaisTelefones.clicked.connect(self.abrirPgMaisTelefones)
        self.pbLimpar.clicked.connect(self.limpaTudo)
        self.pbLimparFiltro.clicked.connect(self.limpaFiltros)
        self.pbFiltrar.clicked.connect(self.efetivarFiltro)

        self.cbClienteAntigo.clicked.connect(self.atualizaStatusCliente)

        self.leRg.editingFinished.connect(lambda: self.leRg.setText(mascaraRG(self.leRg.text())))
        self.leCpf.editingFinished.connect(lambda: self.leCpf.setText(mascaraCPF(self.leCpf.text())))
        self.leTelefone.editingFinished.connect(lambda: self.leTelefone.setText(mascaraTelCel(self.leTelefone.text())))
        self.leCep.editingFinished.connect(lambda: self.leCep.setText(mascaraCep(self.leCep.text())))

        self.sbCdCliente.editingFinished.connect(self.buscaCliente)
        self.sbCdCliente.valueChanged.connect(lambda: self.carregaInfoTela('sbCliente'))

        self.leCep.editingFinished.connect(lambda: self.carregaInfoTela('cep'))
        self.leEndereco.textEdited.connect(lambda: self.carregaInfoTela('endereco'))
        self.leCidade.textEdited.connect(lambda: self.carregaInfoTela('cidade'))
        self.leBairro.textEdited.connect(lambda: self.carregaInfoTela('bairro'))
        self.leComplemento.textEdited.connect(lambda: self.carregaInfoTela('complemento'))
        self.leTelefone.textEdited.connect(lambda: self.carregaInfoTela('telefone'))
        self.leCartProf.textEdited.connect(lambda: self.carregaInfoTela('cartProf'))
        self.leProfissao.textEdited.connect(lambda: self.carregaInfoTela('profissao'))
        self.lePrimeiroNome.textEdited.connect(lambda: self.carregaInfoTela('nomeCliente'))
        self.leSobrenome.textEdited.connect(lambda: self.carregaInfoTela('sobrenomeCliente'))
        self.leRg.textEdited.connect(lambda: self.carregaInfoTela('rg'))
        self.leNumero.textEdited.connect(lambda: self.carregaInfoTela('leNumero'))
        self.leIdade.textEdited.connect(lambda: self.carregaInfoTela('idade'))
        self.leCpf.textEdited.connect(lambda: self.carregaInfoTela('cpf'))
        self.leNomeMae.textEdited.connect(lambda: self.carregaInfoTela('nomeMae'))
        self.leEmail.textEdited.connect(lambda: self.carregaInfoTela('email'))
        self.leNomeBanco.textEdited.connect(lambda: self.carregaInfoTela('leNomeBanco'))
        self.leNumeroConta.textEdited.connect(lambda: self.carregaInfoTela('leNumeroConta'))
        self.leNumeroAgencia.textEdited.connect(lambda: self.carregaInfoTela('leNumeroAgencia'))
        self.leSenhaINSS.textEdited.connect(lambda: self.carregaInfoTela('leSenhaINSS'))
        self.lePix.textEdited.connect(lambda: self.carregaInfoTela('lePix'))
        self.rbFeminino.clicked.connect(lambda: self.carregaInfoTela('rbFeminino'))
        self.rbMasculino.clicked.connect(lambda: self.carregaInfoTela('rbMasculino'))

        self.dtNascimento.dateChanged.connect(lambda: self.carregaInfoTela('dataNascimento'))

        self.cbxEstCivil.activated.connect(lambda: self.carregaInfoTela('estCivil'))
        self.cbxEscolaridade.activated.connect(lambda: self.carregaInfoTela('cbxEscolaridade'))

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
            self.sbCdCliente.setDisabled(False)
        else:
            self.sbCdCliente.setDisabled(True)

    def atualizaTblClientes(self, clientes: list = None):
        if clientes is None:
            clientesModels: list = self.daoCliente.buscaTodos(returnModel=True)
        else:
            clientesModels = []

        self.tblClientes.setRowCount(0)
        for numLinha, cliente in enumerate(clientesModels):
            self.tblClientes.insertRow(numLinha)
            processo: ProcessosModelo = self.daoProcessos.buscaProcessoPorCliente(cliente, limit=1)[0]

            cdClienteItem = QTableWidgetItem(str(cliente.clienteId))
            cdClienteItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 0, cdClienteItem)

            nomeCompletoItem = QTableWidgetItem(f"{cliente.nomeCliente} {cliente.sobrenomeCliente}")
            nomeCompletoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 1, nomeCompletoItem)

            emailItem = QTableWidgetItem(f"{cliente.email}")
            emailItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 2, emailItem)

            telefoneItem = QTableWidgetItem(f"{mascaraTelCel(cliente.telefone.numero)}")
            telefoneItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 3, telefoneItem)

            cidadeItem = QTableWidgetItem(f"{cliente.cidade}")
            cidadeItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 4, cidadeItem)

            tipoProcessoItem = QTableWidgetItem(strTipoBeneficio(processo.tipoBeneficio, processo.subTipoApos))
            tipoProcessoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 5, tipoProcessoItem)

        self.tblClientes.resizeColumnsToContents()

    def abrirPgMaisTelefones(self):
        pgMaisTelefones = TelAfinsController(self.cliente, db=self.db, parent=self)
        pgMaisTelefones.show()

    def buscaCliente(self):
        if self.sbCdCliente.text() != '':
            cdCliente: int = int(self.sbCdCliente.text())
            self.limpaTudo()
            self.sbCdCliente.setValue(cdCliente)
            self.verificaDados()
            self.cliente = self.daoCliente.buscaClienteById(cdCliente, returnInstance=True)
            if not self.cliente:
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
        self.dtNascimento.setDate(cliente.dataNascimento.date())
        self.leIdade.setText(f'{cliente.idade}')
        self.leNomeMae.setText(cliente.nomeMae)
        self.lePrimeiroNome.setText(cliente.nomeCliente)
        self.leSobrenome.setText(cliente.sobrenomeCliente)
        self.sbCdCliente.setValue(self.cliente.clienteId)

        if cliente.rgCliente not in [None, 'None']:
            self.leRg.setText(mascaraRG(cliente.rgCliente))

        if cliente.numero not in [None, 'None']:
            self.leNumero.setText(str(cliente.numero))

        if cliente.telefone not in [None, 'None']:
            self.leTelefone.setText(mascaraTelCel(cliente.telefone.numero))

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

        if cliente.pixCliente not in [None, 'None']:
            self.lePix.setText(cliente.pixCliente)

        if cliente.agenciaBanco not in [None, 'None']:
            self.leNumeroAgencia.setText(cliente.agenciaBanco)

        if cliente.grauEscolaridade not in [None, 'None']:
            self.cbxEscolaridade.setCurrentText(cliente.grauEscolaridade)

        if cliente.senhaINSS not in [None, 'None']:
            self.leSenhaINSS.setText(cliente.senhaINSS)

        if cliente.genero == 'M':
            self.rbMasculino.setChecked(True)
        else:
            self.rbFeminino.setChecked(True)

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
            if self.sbCdCliente.text() != '' and not self.carregandoCliente:
                self.buscaProxCliente()

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
            self.cliente.telefone.numero = self.leTelefone.text()

        elif info == 'rbMasculino' or info == 'rbFeminino':
            if self.rbMasculino.isChecked():
                self.cliente.genero = 'M'
            else:
                self.cliente.genero = 'F'

        elif info == 'leNumero':
            if self.leNumero.text() != '':
                self.cliente.numero = int(self.leNumero.text())

        elif info == 'lePix':
            self.cliente.pixCliente = self.lePix.text()

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

    def buscaProxCliente(self):
        self.carregandoCliente = True
        if self.sbCdCliente.text() != '':
            clienteId = int(self.sbCdCliente.text())

            self.limpaTudo()
            self.verificaDados()
            self.cliente = self.daoCliente.buscaProxCliente(clienteId)
            cliente = Cliente.select().where(Cliente.clienteId == clienteId).dicts().get()

            print('\n---------------------------------------')
            print(cliente)
            print('---------------------------------------\n')

            if not self.cliente:
                self.cliente = ClienteModelo()
                self.limpaTudo()
            else:
                self.carregaClienteNaTela(self.cliente)
                if self.entrevista:
                    self.sinais.sEnviaCliente.emit()
        self.carregandoCliente = False

    def carregaComboBoxes(self):
        self.cbxEstCivil.addItems(estCivil)
        self.cbxEscolaridade.addItems(getEscolaridade().keys())
        self.cbxEstado.addItems(getEstados().keys())
        self.cbxEstado.setCurrentIndex(24)
        tiposBeneficios: list = [strTipoBeneFacilitado(beneficio) for beneficio in TipoBeneficio]
        tiposBeneficios.sort()
        for tipoBeneficio in tiposBeneficios:
            self.cbxTpBeneficio.addItem(tipoBeneficio)

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
            self.avaliaTelefone()
            self.daoCliente.atualizaCliente(self.cliente)

    def avaliaTelefone(self):
        self.cliente.telefone.clienteId = self.cliente.clienteId
        self.cliente.telefone.tipoTelefone = 'W'
        self.cliente.telefone.pessoalRecado = 'P'

    def verificaCodCliente(self) -> bool:
        cdClienteNotNone = self.sbCdCliente.text() is not None
        cdClienteStrVazio = self.sbCdCliente.text() != ""
        cdClienteNotZero = self.sbCdCliente.text() != 0 and self.sbCdCliente.text() != "0"

        return cdClienteNotZero and cdClienteNotNone and cdClienteStrVazio

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
                button.clicked.connect(lambda state, i=i: self.filtroAZ(i))
                self.hlFlitroAlfabetico.addWidget(button)

    def filtroAZ(self, estado):
        listAlfabeto = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        letraFiltro: str = listAlfabeto[estado]
        self.limpaFiltros()
        for linha in range(self.tblClientes.rowCount()):
            primeiraLetraNomeCliente: str = self.tblClientes.item(linha, 1).text()[0].upper()
            if primeiraLetraNomeCliente != letraFiltro:
                self.tblClientes.hideRow(linha)

    def limpaTudo(self):
        # self.cliente = ClienteModelo()
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
        self.lePix.clear()

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

    def efetivarFiltro(self):
        if self.leBuscaNome.text() != '':
            nomeBuscado: str = self.leBuscaNome.text().lower()
            for linha in range(self.tblClientes.rowCount()):
                nomeCliente: str = self.tblClientes.item(linha, 1).text().lower()
                if nomeCliente.find(nomeBuscado) == -1:
                    self.tblClientes.hideRow(linha)

        if self.leBuscaEmail.text() != '':
            emailBuscado: str = self.leBuscaEmail.text().lower()
            for linha in range(self.tblClientes.rowCount()):
                emailCliente: str = self.tblClientes.item(linha, 2).text().lower()
                if emailCliente.find(emailBuscado) == -1:
                    self.tblClientes.hideRow(linha)

        if self.leBuscaTelefone.text() != '':
            telefoneBuscado: str = self.leBuscaTelefone.text()
            for linha in range(self.tblClientes.rowCount()):
                telefoneCliente: str = self.tblClientes.item(linha, 3).text()
                if telefoneCliente.find(telefoneBuscado) == -1:
                    self.tblClientes.hideRow(linha)

        if self.cbxTpBeneficio.currentText() != '':
            beneficioBuscado: str = self.cbxTpBeneficio.currentText().lower()
            for linha in range(self.tblClientes.rowCount()):
                beneficioCliente: str = self.tblClientes.item(linha, 5).text().lower()
                if beneficioCliente.find(beneficioBuscado) == -1:
                    self.tblClientes.hideRow(linha)

    def limpaFiltros(self):
        self.leBuscaNome.clear()
        self.leBuscaEmail.clear()
        self.leBuscaTelefone.clear()
        self.leBuscaRgcpf.clear()
        for linha in range(self.tblClientes.rowCount()):
            self.tblClientes.showRow(linha)

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
