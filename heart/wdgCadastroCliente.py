from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtCore import Qt

from Design.pyUi.wdgCadastroCliente import Ui_wdgCadastroCliente
from Design.CustomWidgets.newToast import QToaster
from heart.localStyleSheet.cadastroCliente import etapaCadatro

from modelos.clienteORM import Cliente
from modelos.telefonesORM import Telefones
from modelos.itemContribuicao import ItemContribuicao
from repositorios.integracaoRepositorio import IntegracaoRepository

from util.dateHelper import strToDate
from util.enums.dashboardEnums import TelaAtual, Navegacao, EtapaCadastraCliente
from util.helpers import mascaraCPF, mascaraRG, mascaraTelCel, mascaraCep, mascaraNit, estCivil, getEscolaridade, getEstados, getEstadoBySigla
from util.popUps import popUpOkAlerta


class NewCadastraCliente(QWidget, Ui_wdgCadastroCliente):
    clienteAtual: Cliente
    etapaAtual: EtapaCadastraCliente
    editando: bool = False

    def __init__(self, parent=None):
        super(NewCadastraCliente, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent

        self.leRg.editingFinished.connect(lambda: self.leRg.setText(mascaraRG(self.leRg.text())))
        self.leCpf.editingFinished.connect(lambda: self.leCpf.setText(mascaraCPF(self.leCpf.text())))
        self.leTelefone1.editingFinished.connect(lambda: self.leTelefone1.setText(mascaraTelCel(self.leTelefone1.text())))
        self.leCep.editingFinished.connect(lambda: self.leCep.setText(mascaraCep(self.leCep.text())))

        self.leCep.editingFinished.connect(lambda: self.carregaInfoTela('cep'))
        self.leEndereco.textEdited.connect(lambda: self.carregaInfoTela('endereco'))
        self.leCidade.textEdited.connect(lambda: self.carregaInfoTela('cidade'))
        self.leBairro.textEdited.connect(lambda: self.carregaInfoTela('bairro'))
        self.leComplemento.textEdited.connect(lambda: self.carregaInfoTela('complemento'))
        self.leTelefone1.textEdited.connect(lambda: self.carregaInfoTela('telefone1'))
        self.leTelefone2.textEdited.connect(lambda: self.carregaInfoTela('telefone2'))
        self.leCarteiraProf.textEdited.connect(lambda: self.carregaInfoTela('cartProf'))
        self.leProfissao.textEdited.connect(lambda: self.carregaInfoTela('profissao'))
        self.leNomeCliente.textEdited.connect(lambda: self.carregaInfoTela('nomeCliente'))
        self.leRg.textEdited.connect(lambda: self.carregaInfoTela('rg'))
        self.leNumero.textEdited.connect(lambda: self.carregaInfoTela('leNumero'))
        self.leIdade.textEdited.connect(lambda: self.carregaInfoTela('idade'))
        self.leCpf.textEdited.connect(lambda: self.carregaInfoTela('cpf'))
        self.leNomeDaMae.textEdited.connect(lambda: self.carregaInfoTela('nomeMae'))
        self.leEmail.textEdited.connect(lambda: self.carregaInfoTela('email'))
        self.leNomeBanco.textEdited.connect(lambda: self.carregaInfoTela('leNomeBanco'))
        self.leConta.textEdited.connect(lambda: self.carregaInfoTela('leNumeroConta'))
        self.leNumeroAgencia.textEdited.connect(lambda: self.carregaInfoTela('leNumeroAgencia'))
        self.leSenhaInss.textEdited.connect(lambda: self.carregaInfoTela('leSenhaINSS'))
        self.lePix.textEdited.connect(lambda: self.carregaInfoTela('lePix'))
        self.rbFeminino.clicked.connect(lambda: self.carregaInfoTela('rbFeminino'))
        self.rbMasculino.clicked.connect(lambda: self.carregaInfoTela('rbMasculino'))

        self.dtNascimento.dateChanged.connect(lambda: self.carregaInfoTela('dataNascimento'))

        self.cbxEstadoCivil.activated.connect(lambda: self.carregaInfoTela('estCivil'))
        self.cbxEscolaridade.activated.connect(lambda: self.carregaInfoTela('cbxEscolaridade'))

        self.pbVoltar.clicked.connect(lambda: self.avaliaNavegacao(Navegacao.anterior))
        self.pbSalvarDados.clicked.connect(self.avaliaSalvaDados)
        self.pbBuscaCep.clicked.connect(self.buscaCep)
        self.cbMostraPix.stateChanged.connect(lambda: self.avaliaMostraSenhas('pix'))
        self.cbMostraMeuInss.stateChanged.connect(lambda: self.avaliaMostraSenhas('meuInss'))

        self.trocaEtapa(EtapaCadastraCliente.pessoal)

    def avaliaNavegacao(self, tipo: Navegacao):
        if tipo == Navegacao.anterior:
            if self.etapaAtual == EtapaCadastraCliente.pessoal:
                # TODO: PERGUNTAR PARA O ADVOGADO SE DESEJA SALVAR OU DESCARTAR ALTERAÇÕES
                self.dashboard.trocaTela(TelaAtual.Cliente)
            elif self.etapaAtual == EtapaCadastraCliente.profissional:
                self.trocaEtapa(EtapaCadastraCliente.pessoal, sucesso=False)
            elif self.etapaAtual == EtapaCadastraCliente.bancarias:
                self.trocaEtapa(EtapaCadastraCliente.profissional, sucesso=False)

        elif tipo == Navegacao.proximo:
            pass

    def avaliaSalvaDados(self):
        if self.etapaAtual == EtapaCadastraCliente.pessoal:
            if self.leNomeCliente.text() == '' or self.leNomeCliente.text().isnumeric():
                return False
            self.trocaEtapa(EtapaCadastraCliente.profissional)

        elif self.etapaAtual == EtapaCadastraCliente.profissional:
            self.trocaEtapa(EtapaCadastraCliente.bancarias)

        elif self.etapaAtual == EtapaCadastraCliente.bancarias:
            if not self.leNumeroAgencia.text().isnumeric():
                return False
            self.trocaEtapa(EtapaCadastraCliente.finaliza)

        self.clienteAtual.save()
        self.editando = False
        return True

    def avaliaMostraSenhas(self, info: str):
        if info == 'pix':
            if self.cbMostraPix.isChecked():
                self.lePix.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.lePix.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            if self.cbMostraMeuInss.isChecked():
                self.leSenhaInss.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.leSenhaInss.setEchoMode(QLineEdit.EchoMode.Password)


    def buscaCep(self):
        integracaoRepository = IntegracaoRepository()
        dictCep: dict = integracaoRepository.getCep(self.leCep.text().replace('-', ''))
        if 'logradouro' in dictCep.keys():
            self.leEndereco.setText(dictCep['logradouro'])
            self.clienteAtual.endereco = dictCep['logradouro']

            self.leComplemento.setText(dictCep['complemento'])
            self.clienteAtual.complemento = dictCep['complemento']

            self.leBairro.setText(dictCep['bairro'])
            self.clienteAtual.bairro = dictCep['bairro']

            self.leCidade.setText(dictCep['localidade'])
            self.clienteAtual.cidade = dictCep['localidade']

            self.cbxEstado.setCurrentText(getEstadoBySigla(dictCep['uf']))
            self.clienteAtual.estado = getEstadoBySigla(dictCep['uf'])
        elif 'erro' in dictCep.keys():
            self.showPopupAlerta(dictCep['erro'])

    def carregaInfoTela(self, info, *args):
        self.editando = True

        if info == 'cep':
            self.clienteAtual.cep = self.leCep.text().replace('-', '')

        elif info == 'endereco':
            self.clienteAtual.endereco = self.leEndereco.text()

        elif info == 'leNomeBanco':
            self.clienteAtual.nomeBanco = self.leNomeBanco.text()

        elif info == 'leNumeroConta':
            self.clienteAtual.numeroConta = self.leConta.text()

        elif info == 'leNumeroAgencia':
            self.clienteAtual.agenciaBanco = self.leNumeroAgencia.text()

        elif info == 'leSenhaINSS':
            self.clienteAtual.senhaINSS = self.leSenhaInss.text()

        elif info == 'cidade':
            self.clienteAtual.cidade = self.leCidade.text()

        elif info == 'bairro':
            self.clienteAtual.bairro = self.leBairro.text()

        elif info == 'estado':
            self.clienteAtual.estado = self.cbxEstado.currentText()

        elif info == 'cbxEscolaridade':
            self.clienteAtual.grauEscolaridade = self.cbxEscolaridade.currentText()

        elif info == 'complemento':
            self.clienteAtual.complemento = self.leComplemento.text()

        elif info == 'nit':
            self.clienteAtual.nit = self.leNit.text()

        elif info == 'cartProf':
            self.clienteAtual.numCartProf = self.leCarteiraProf.text()

        elif info == 'profissao':
            self.clienteAtual.profissao = self.leProfissao.text()

        elif info == 'cdCliente':
            if self.leCdCliente.text() != '':
                self.clienteAtual.clienteId = int(self.leCdCliente.text())

        elif info == 'sbCliente':
            if self.sbCdCliente.text() != '':
                self.buscaProxCliente()

        elif info == 'nomeCliente':
            index: int = self.leNomeCliente.text().find(' ')
            self.clienteAtual.nomeCliente = self.leNomeCliente[:index]
            self.clienteAtual.sobrenomeCliente = self.leNomeCliente.text()[index + 1:]

        elif info == 'rg':
            self.clienteAtual.rgCliente = self.leRg.text()

        elif info == 'dataNascimento':
            # self.cliente.dataNascimento = self.dtNascimento.date().toPyDate().strftime('%Y-%m-%d %H:%M')
            self.clienteAtual.dataNascimento = self.dtNascimento.date().toPyDate().strftime('%Y-%m-%d')

        elif info == 'idade':
            self.clienteAtual.idade = self.leIdade.text()

        elif info == 'cpf':
            self.clienteAtual.cpfCliente = self.leCpf.text()

        elif info == 'nomeMae':
            self.clienteAtual.nomeMae = self.leNomeDaMae.text()

        elif info == 'estCivil':
            self.clienteAtual.estadoCivil = self.cbxEstadoCivil.currentText()

        elif info == 'email':
            self.clienteAtual.email = self.leEmail.text()

        elif info == 'telefone1':
            if self.clienteAtual.telefoneId is None:
                self.clienteAtual.telefoneId = Telefones()
            self.clienteAtual.telefoneId.numero = self.leTelefone1.text()

        elif info == 'telefone2':
            if self.clienteAtual.telefoneId is None:
                telefoneSecundario = Telefones(
                    numero=self.leTelefone2.text(),
                ).save()

        elif info == 'rbMasculino' or info == 'rbFeminino':
            if self.rbMasculino.isChecked():
                self.clienteAtual.genero = 'M'
            else:
                self.clienteAtual.genero = 'F'

        elif info == 'leNumero':
            if self.leNumero.text() != '':
                self.clienteAtual.numero = int(self.leNumero.text())

        elif info == 'lePix':
            self.clienteAtual.pixCliente = self.lePix.text()

    def carregaClienteNaTela(self, cliente: Cliente, cadastro: bool = False):
        try:
            self.leCpf.setText(mascaraCPF(cliente.cpfCliente))
            self.dtNascimento.setDate(strToDate(cliente.dataNascimento))
            self.leIdade.setText(f'{cliente.idade}')
            self.leNomeDaMae.setText(cliente.nomeMae)
            self.leNomeCliente.setText(cliente.nomeCliente + ' ' + cliente.sobrenomeCliente)
            self.leCdCliente.setText(str(cliente.clienteId))

            if cliente.rgCliente not in [None, 'None']:
                self.leRg.setText(mascaraRG(cliente.rgCliente))

            if cliente.numero not in [None, 'None']:
                self.leNumero.setText(str(cliente.numero))

            if cliente.telefoneId is not None:
                self.leTelefone1.setText(mascaraTelCel(cliente.telefoneId.numero))

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
                self.leCarteiraProf.setText(str(cliente.numCartProf))

            if cliente.profissao not in [None, 'None']:
                self.leProfissao.setText(cliente.profissao)

            if cliente.numeroConta not in [None, 'None']:
                self.leConta.setText(cliente.numeroConta)

            if cliente.nomeBanco not in [None, 'None']:
                self.leNomeBanco.setText(cliente.nomeBanco)

            if cliente.pixCliente not in [None, 'None']:
                self.lePix.setText(cliente.pixCliente)

            if cliente.agenciaBanco not in [None, 'None']:
                self.leNumeroAgencia.setText(cliente.agenciaBanco)

            if cliente.grauEscolaridade not in [None, 'None']:
                self.cbxEscolaridade.setCurrentText(cliente.grauEscolaridade)

            if cliente.senhaINSS not in [None, 'None']:
                self.leSenhaInss.setText(cliente.senhaINSS)

            if cliente.genero == 'M':
                self.rbMasculino.setChecked(True)
            else:
                self.rbFeminino.setChecked(True)

        except Exception as err:
            print(f"carregaClienteNaTela <NewCadastraCliente>: {err=}")
            popUpOkAlerta("Não foi possível carregar as informações do cliente na tela. Tente novamente.", erro=str(err))
            self.dashboard.trocaTela(TelaAtual.Cliente)
            if cadastro:
                self.deletaCliente(cliente.clienteId)

        self.clienteAtual = cliente
        return True

    def carregaComboBoxes(self):
        self.cbxEstadoCivil.addItems(estCivil)
        self.cbxEscolaridade.addItems(getEscolaridade().keys())
        self.cbxEstado.addItems(getEstados().keys())
        self.cbxEstado.setCurrentIndex(24)

    def deletaCliente(self, clienteId: int):
        Cliente.delete_by_id(clienteId)
        ItemContribuicao.delete_by_id(clienteId)
        Telefones.delete_by_id(clienteId)

    def iniciaTela(self):
        self.carregaComboBoxes()
        self.limpaTudo()
        self.trocaEtapa(EtapaCadastraCliente.pessoal)
        self.clienteAtual = Cliente()

    def limpaTudo(self):
        self.leNomeCliente.clear()
        self.leRg.clear()
        self.leIdade.clear()
        self.leCpf.clear()
        self.leNomeDaMae.clear()
        self.leEmail.clear()
        self.leTelefone1.clear()
        self.leTelefone2.clear()
        self.leCep.clear()
        self.leEndereco.clear()
        self.leCidade.clear()
        self.leBairro.clear()
        self.leComplemento.clear()
        self.leNit.clear()
        self.leCarteiraProf.clear()
        self.leProfissao.clear()
        self.leNomeBanco.clear()
        self.leNumeroAgencia.clear()
        self.leConta.clear()
        self.leSenhaInss.clear()
        self.leNumero.clear()
        self.lePix.clear()
        self.leCdCliente.clear()
        self.editando = False

        self.cbxEstado.setCurrentIndex(24)

    def trocaEtapa(self, etapa: EtapaCadastraCliente, sucesso: bool = True):
        self.etapaAtual = etapa

        if etapa == EtapaCadastraCliente.finaliza:
            self.frQuartaEtapa.setStyleSheet(etapaCadatro(etapa, sucesso=sucesso))

            toasty = QToaster()
            toasty.showMessage(self, "Cliente salvo com sucesso!", corner=Qt.BottomLeftCorner)
            self.dashboard.trocaTela(TelaAtual.Cliente)
            self.dashboard.recarregaListaClientes()
        else:
            self.stkCliente.setCurrentIndex(etapa.value)

            if etapa == EtapaCadastraCliente.profissional:
                self.frSegundaEtapa.setStyleSheet(etapaCadatro(etapa, sucesso=sucesso))
            elif etapa == EtapaCadastraCliente.bancarias:
                self.frTerceiraEtapa.setStyleSheet(etapaCadatro(etapa, sucesso=sucesso))
            else:
                self.frSegundaEtapa.setStyleSheet(etapaCadatro(EtapaCadastraCliente.profissional, sucesso=False))
                self.frTerceiraEtapa.setStyleSheet(etapaCadatro(EtapaCadastraCliente.bancarias, sucesso=False))
