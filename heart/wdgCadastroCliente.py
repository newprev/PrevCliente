from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtCore import Qt
import sqlite3
import peewee

from datetime import datetime
from dateutil.relativedelta import relativedelta

from Design.pyUi.wdgCadastroCliente import Ui_wdgCadastroCliente
from Design.CustomWidgets.newToast import QToaster

from heart.localStyleSheet.cadastroCliente import etapaCadatro

from cache.cacheEscritorio import CacheEscritorio
from systemLog.logs import logPrioridade

from modelos.clienteORM import Cliente
from modelos.escritoriosORM import Escritorios
from modelos.telefonesORM import Telefones
from modelos.itemContribuicao import ItemContribuicao
from modelos.clienteProfissao import ClienteProfissao
from modelos.clienteInfoBanco import ClienteInfoBanco

from repositorios.integracaoRepositorio import IntegracaoRepository
from util.enums.newPrevEnums import TipoEdicao

from util.helpers.dateHelper import strToDate, calculaIdade
from util.enums.dashboardEnums import TelaAtual, Navegacao, EtapaCadastraCliente
from util.enums.telefoneEnums import TipoTelefone, TelefonePesoal
from util.helpers.helpers import mascaraCPF, mascaraRG, mascaraTelCel, mascaraCep, mascaraNit, estCivil, getEscolaridade, getEstados, getEstadoBySigla, unmaskAll
from util.popUps import popUpOkAlerta, popUpSimCancela


class NewCadastraCliente(QWidget, Ui_wdgCadastroCliente):
    clienteAtual: Cliente = None
    escritorioAtual: Escritorios = None
    dadosBancarios: ClienteInfoBanco = None
    dadosProfissionais: ClienteProfissao = None
    etapaAtual: EtapaCadastraCliente
    editando: bool = False

    def __init__(self, parent=None):
        super(NewCadastraCliente, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent

        self.buscaEscritorio()

        self.iniciaCamposPessoais()
        self.leIdade.setDisabled(True)
        self.leCdCliente.setDisabled(True)

        # Definindo ordem do focus
        self.setTabOrder(self.leNomeCliente, self.dtNascimento)
        self.setTabOrder(self.dtNascimento, self.cbxEstadoCivil)
        self.setTabOrder(self.cbxEstadoCivil, self.cbxEscolaridade)
        self.setTabOrder(self.cbxEscolaridade, self.leRg)
        self.setTabOrder(self.leRg, self.leCpf)
        self.setTabOrder(self.leCpf, self.rbMasculino)
        self.setTabOrder(self.rbMasculino, self.leTelefone1)
        self.setTabOrder(self.leTelefone1, self.leTelefone2)
        self.setTabOrder(self.leTelefone2, self.leEmail)
        self.setTabOrder(self.leEmail, self.leNomeDaMae)
        self.setTabOrder(self.leNomeDaMae, self.leCep)
        self.setTabOrder(self.leCep, self.pbBuscaCep)
        self.setTabOrder(self.pbBuscaCep, self.leCidade)
        self.setTabOrder(self.leCidade, self.cbxEstado)
        self.setTabOrder(self.cbxEstado, self.leEndereco)
        self.setTabOrder(self.leEndereco, self.leBairro)
        self.setTabOrder(self.leBairro, self.leComplemento)
        self.setTabOrder(self.leComplemento, self.leNumero)
        self.setTabOrder(self.leNumero, self.pbSalvarDados)

        self.setTabOrder(self.leNit, self.leCarteiraProf)
        self.setTabOrder(self.leCarteiraProf, self.leProfissao)
        self.setTabOrder(self.leProfissao, self.pbSalvarDados)

        self.setTabOrder(self.leNomeBanco, self.leNumeroAgencia)
        self.setTabOrder(self.leNumeroAgencia, self.leConta)
        self.setTabOrder(self.leNumeroAgencia, self.leConta)
        self.setTabOrder(self.leConta, self.lePix)
        self.setTabOrder(self.lePix, self.leSenhaInss)
        self.setTabOrder(self.leSenhaInss, self.pbSalvarDados)

        self.pbVoltar.clicked.connect(lambda: self.avaliaNavegacao(Navegacao.anterior))
        self.pbSalvarDados.clicked.connect(self.avaliaSalvaDados)
        self.cbMostraPix.stateChanged.connect(lambda: self.avaliaMostraSenhas('pix'))
        self.cbMostraMeuInss.stateChanged.connect(lambda: self.avaliaMostraSenhas('meuInss'))

        self.trocaEtapa(EtapaCadastraCliente.pessoal)

    def atualizaIdadeTela(self):
        dataNascimento: datetime.date = self.dtNascimento.date().toPyDate()
        idade: relativedelta = calculaIdade(dataNascimento, datetime.today())
        self.leIdade.setText(f"{idade.years} anos, {idade.months} meses")

    def avaliaNavegacao(self, tipo: Navegacao):
        if tipo == Navegacao.anterior:
            if self.etapaAtual == EtapaCadastraCliente.pessoal:
                self.verificaPerderAlteracoes()
            elif self.etapaAtual == EtapaCadastraCliente.profissional:
                self.trocaEtapa(EtapaCadastraCliente.pessoal, sucesso=False)
            elif self.etapaAtual == EtapaCadastraCliente.bancarias:
                self.trocaEtapa(EtapaCadastraCliente.profissional, sucesso=False)

        elif tipo == Navegacao.proximo:
            pass

    def avaliaInsereTelefone(self):
        if self.leTelefone1.text() == '':
            return True

        try:
            telefone: Telefones = Telefones.select().where(Telefones.clienteId == self.clienteAtual.clienteId, Telefones.principal == True).get()
            telefone.numero = unmaskAll(self.leTelefone1.text())
            telefone.dataUltAlt = datetime.now()
            telefone.save()
        except Telefones.DoesNotExist as err:
            telefone = Telefones(
                clienteId=self.clienteAtual.clienteId,
                principal=True,
                numero=unmaskAll(self.leTelefone1.text()),
                pessoalRecado=TelefonePesoal.Pessoal.value,
                tipoTelefone=TipoTelefone.Whatsapp.value,
                ativo=True
            )
            telefone.save()
        finally:
            self.clienteAtual.telefoneId = telefone.telefoneId
            self.clienteAtual.dataUltAlt = datetime.now()
            self.clienteAtual.save()

            self.leTelefone1.setText(mascaraTelCel(self.leTelefone1.text()))

    def avaliaInsereTelefoneSecundario(self):
        if self.leTelefone2.text() == '':
            return True

        try:
            telefone: Telefones = Telefones.select().where(Telefones.clienteId == self.clienteAtual.clienteId, Telefones.principal == False).get()
            telefone.numero = unmaskAll(self.leTelefone2.text())
            telefone.dataUltAlt = datetime.now()
            telefone.save()
        except Telefones.DoesNotExist as err:
            Telefones(
                clienteId=self.clienteAtual.clienteId,
                principal=False,
                numero=unmaskAll(self.leTelefone2.text()),
                pessoalRecado=TelefonePesoal.Recado.value,
                tipoTelefone=TipoTelefone.Whatsapp.value,
                ativo=True
            ).save()
        finally:
            self.leTelefone2.setText(mascaraTelCel(self.leTelefone2.text()))

    def avaliaSalvaDados(self):
        if self.etapaAtual == EtapaCadastraCliente.pessoal:
            if self.leNomeCliente.text() == '' or self.leNomeCliente.text().isnumeric():
                return False

            self.salvaEtapaPessoal()
            self.trocaEtapa(EtapaCadastraCliente.profissional)
            self.leNit.setFocus()

        elif self.etapaAtual == EtapaCadastraCliente.profissional:
            self.salvaEtapaProfissional()

            if self.clienteAtual.dadosProfissionais is None:
                self.clienteAtual.dadosProfissionais = self.dadosProfissionais.infoId
                self.clienteAtual.dataUltAlt = datetime.now()
                self.clienteAtual.save()

            self.trocaEtapa(EtapaCadastraCliente.bancarias)
            self.leNomeBanco.setFocus()

        elif self.etapaAtual == EtapaCadastraCliente.bancarias:
            if not self.leNumeroAgencia.text().isnumeric():
                return False

            self.salvaEtapaBancaria()

            self.clienteAtual.dadosBancarios = self.dadosBancarios
            self.clienteAtual.dataUltAlt = datetime.now()
            self.clienteAtual.save()

            self.trocaEtapa(EtapaCadastraCliente.finaliza)

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

    def buscaDadosBancarios(self) -> ClienteInfoBanco:
        try:
            infoBanco = None
            infoBanco = ClienteInfoBanco.select().where(
                ClienteInfoBanco.clienteId == self.clienteAtual.clienteId
            ).get()
            return infoBanco
        except ClienteInfoBanco.DoesNotExist as err:
            infoBanco = ClienteInfoBanco(
                clienteId=self.clienteAtual.clienteId
            )
            infoBanco.save()
            print(f"buscaDadosBancarios: {err=}")
        except Exception as err:
            print(f"buscaDadosBancarios: {err=}")
        finally:
            return infoBanco

    def buscaEscritorio(self) -> bool:
        if self.escritorioAtual is None:
            self.escritorioAtual = CacheEscritorio().carregarCache()

            if self.escritorioAtual is None:
                self.escritorioAtual = CacheEscritorio().carregarCacheTemporario()

                if self.escritorioAtual is None:
                    if self.clienteAtual is not None:
                        ClienteInfoBanco.delete().where(ClienteInfoBanco.clienteId == self.clienteAtual.clienteId).execute()
                        ClienteProfissao.delete().where(ClienteProfissao.clienteId == self.clienteAtual.clienteId).execute()
                        self.clienteAtual.delete()
                    popUpOkAlerta("Não foi possível carregar as informações do escritório. Tente novamente.", erro="NewCadastraCliente<buscaEscritorio>")
                    return False

        return True

    def carregaClienteNaTela(self, cliente: Cliente, cadastro: bool = False, tela: str=None):
        try:
            #################################### Info pessoal
            self.clienteAtual = cliente
            if self.clienteAtual.clienteId is None:
                self.leNomeCliente.setFocus()
                return True

            self.leCpf.setText(mascaraCPF(cliente.cpfCliente))
            self.dtNascimento.setDate(strToDate(cliente.dataNascimento))
            self.atualizaIdadeTela()
            self.leNomeDaMae.setText(cliente.nomeMae)
            self.leNomeCliente.setText(cliente.nomeCliente + ' ' + cliente.sobrenomeCliente)
            self.leCdCliente.setText(str(cliente.clienteId))

            telefoneSecundario = self.carregaTelefoneSecundario(cliente.clienteId)
            if telefoneSecundario is not None:
                self.leTelefone2.setText(mascaraTelCel(telefoneSecundario.numero))

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

            if cliente.grauEscolaridade not in [None, 'None']:
                self.cbxEscolaridade.setCurrentText(cliente.grauEscolaridade)

            if cliente.senhaINSS not in [None, 'None']:
                self.leSenhaInss.setText(cliente.senhaINSS)

            if cliente.genero == 'M':
                self.rbMasculino.setChecked(True)
            else:
                self.rbFeminino.setChecked(True)

            #################################### Info profissionais
            self.dadosProfissionais = ClienteProfissao.get_by_id(cliente.dadosProfissionais)

            if self.dadosProfissionais.nit not in [None, 'None']:
                self.leNit.setText(mascaraNit(unmaskAll(self.dadosProfissionais.nit)))

            if self.dadosProfissionais.numCaretiraTrabalho not in [None, 'None']:
                self.leCarteiraProf.setText(str(self.dadosProfissionais.numCaretiraTrabalho))

            if self.dadosProfissionais.nomeProfissao not in [None, 'None']:
                self.leProfissao.setText(self.dadosProfissionais.nomeProfissao)

            #################################### Info bancárias
            self.dadosBancarios = self.buscaDadosBancarios()
            if self.dadosBancarios is None:
                return True

            if self.dadosBancarios.numeroConta not in [None, 'None']:
                self.leConta.setText(self.dadosBancarios.numeroConta)

            if self.dadosBancarios.nomeBanco not in [None, 'None']:
                self.leNomeBanco.setText(self.dadosBancarios.nomeBanco)

            if self.dadosBancarios.chavePix not in [None, 'None']:
                self.lePix.setText(self.dadosBancarios.chavePix)

            if self.dadosBancarios.numeroAgencia not in [None, 'None']:
                self.leNumeroAgencia.setText(self.dadosBancarios.numeroAgencia)

        except Exception as err:
            print(f"carregaClienteNaTela <NewCadastraCliente>: {err=}")
            popUpOkAlerta("Não foi possível carregar as informações do cliente na tela. Tente novamente.", erro=str(err))
            self.dashboard.trocaTela(TelaAtual.Cliente)
            if cadastro:
                self.deletaCliente(cliente.clienteId)

        if tela is not None:
            if tela == 'infoPessoais' or tela == 'infoResidenciais':
                self.trocaEtapa(EtapaCadastraCliente.pessoal)
            elif tela == 'infoProfissionais':
                self.trocaEtapa(EtapaCadastraCliente.profissional)
            else:
                self.trocaEtapa(EtapaCadastraCliente.bancarias)

        return True

    def carregaComboBoxes(self):
        self.cbxEstadoCivil.addItems(estCivil)
        self.cbxEscolaridade.addItems(getEscolaridade().keys())
        self.cbxEstado.addItems(getEstados().keys())
        self.cbxEstado.setCurrentIndex(24)

    def carregaTelefoneSecundario(self, clienteId: int):
        try:
            return Telefones.select(Telefones.numero).where(Telefones.clienteId==clienteId, Telefones.principal==False).get()
        except Telefones.DoesNotExist as err:
            print(f"{err=}")
            return None

    def deletaCliente(self, clienteId: int):
        Cliente.delete_by_id(clienteId)
        ItemContribuicao.delete_by_id(clienteId)
        Telefones.delete_by_id(clienteId)

    def iniciaCamposPessoais(self):
        self.leRg.editingFinished.connect(lambda: self.leRg.setText(mascaraRG(self.leRg.text())))
        self.leCpf.editingFinished.connect(lambda: self.leCpf.setText(mascaraCPF(self.leCpf.text())))
        self.leCep.editingFinished.connect(lambda: self.leCep.setText(mascaraCep(self.leCep.text())))
        self.leTelefone1.editingFinished.connect(lambda: self.leTelefone1.setText(mascaraTelCel(self.leTelefone1.text())))
        self.leTelefone2.editingFinished.connect(lambda: self.leTelefone2.setText(mascaraTelCel(self.leTelefone2.text())))
        self.dtNascimento.dateChanged.connect(self.atualizaIdadeTela)
        self.pbBuscaCep.clicked.connect(self.buscaCep)

    def iniciaTela(self):
        self.limpaTudo()
        self.carregaComboBoxes()
        self.trocaEtapa(EtapaCadastraCliente.pessoal)
        self.clienteAtual = Cliente()

    def insereInfoTela(self, info, *args):
        self.editando = True

        #//////////////////////////////////// Dados pessoais
        if info == 'cep':
            self.clienteAtual.cep = self.leCep.text().replace('-', '')

        elif info == 'endereco':
            self.clienteAtual.endereco = self.leEndereco.text()

        elif info == 'cdCliente':
            if self.leCdCliente.text() != '':
                self.clienteAtual.clienteId = int(self.leCdCliente.text())

        elif info == 'nomeCliente':
            index: int = self.leNomeCliente.text().find(' ')
            self.clienteAtual.nomeCliente = self.leNomeCliente.text()[:index]
            self.clienteAtual.sobrenomeCliente = self.leNomeCliente.text()[index + 1:]

        elif info == 'rg':
            self.clienteAtual.rgCliente = self.leRg.text()

        elif info == 'dataNascimento':
            self.clienteAtual.dataNascimento = self.dtNascimento.date().toPyDate().strftime('%Y-%m-%d')

        elif info == 'cpf':
            self.clienteAtual.cpfCliente = unmaskAll(self.leCpf.text())

        elif info == 'nomeMae':
            self.clienteAtual.nomeMae = self.leNomeDaMae.text()

        elif info == 'estCivil':
            self.clienteAtual.estadoCivil = self.cbxEstadoCivil.currentText()

        elif info == 'email':
            self.clienteAtual.email = self.leEmail.text()

        elif info == 'telefone1':
            if self.clienteAtual.telefoneId is None or self.clienteAtual.telefoneId.telefoneId is None:
                if self.clienteAtual.clienteId is None:
                    self.clienteAtual.save()

                telefone = Telefones(
                    clienteId=self.clienteAtual.clienteId,
                    numero=self.leTelefone1.text(),
                    pessoalRecado='P',
                    tipoTelefone='W'
                ).save()
                self.clienteAtual.telefoneId = telefone

            self.clienteAtual.telefoneId.numero = self.leTelefone1.text()
            self.clienteAtual.telefoneId.dataUltAlt = datetime.now()
            self.clienteAtual.telefoneId.save()

        elif info == 'rbMasculino' or info == 'rbFeminino':
            if self.rbMasculino.isChecked():
                self.clienteAtual.genero = 'M'
            else:
                self.clienteAtual.genero = 'F'

        elif info == 'leNumero':
            if self.leNumero.text() != '' and self.leNumero.text().isnumeric():
                self.clienteAtual.numero = int(self.leNumero.text())

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

        #//////////////////////////////////// Dados bancários
        elif info == 'leNomeBanco':
            if self.dadosBancarios is None:
                self.dadosBancarios = ClienteInfoBanco(
                    clienteId=self.clienteAtual.clienteId,
                    nomeBanco=self.leNomeBanco.text()
                )
                self.dadosBancarios.save()

            self.dadosBancarios.nomeBanco = self.leNomeBanco.text()

        elif info == 'leNumeroConta':
            if self.dadosBancarios is None:
                self.dadosBancarios = ClienteInfoBanco(
                    clienteId=self.clienteAtual.clienteId,
                    nomeBanco=self.leNomeBanco.text()
                )
                self.dadosBancarios.save()

            self.dadosBancarios.numeroConta = self.leConta.text()

        elif info == 'leNumeroAgencia':
            self.dadosBancarios.numeroAgencia = self.leNumeroAgencia.text()

        elif info == 'lePix':
            self.dadosBancarios.chavePix = self.lePix.text()

        #//////////////////////////////////// Dados profissionais
        elif info == 'nit':
            if self.dadosProfissionais is None:
                self.dadosProfissionais = ClienteProfissao(
                    clienteId=self.clienteAtual.clienteId,
                    nit=self.leNit.text()
                )
                # self.dadosProfissionais.save()
                # self.clienteAtual.dadosProfissionais = self.dadosProfissionais.infoId
                # self.clienteAtual.dataUltAlt = datetime.now()
                # self.clienteAtual.save()

            self.dadosProfissionais.nit = self.leNit.text()

        elif info == 'cartProf':
            if self.dadosProfissionais is None:
                self.dadosProfissionais = ClienteProfissao(clienteId=self.clienteAtual.clienteId)
                # self.dadosProfissionais.save()

            self.dadosProfissionais.numCaretiraTrabalho = self.leCarteiraProf.text()

        elif info == 'profissao':
            if self.dadosProfissionais is None:
                self.dadosProfissionais = ClienteProfissao(clienteId=self.clienteAtual.clienteId)
                # self.dadosProfissionais.save()

            self.dadosProfissionais.nomeProfissao = self.leProfissao.text()

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
        self.cbxEstadoCivil.clear()
        self.cbxEscolaridade.clear()

    def sairCadastro(self):
        if self.clienteAtual.clienteId is not None:
            self.deletaCliente(self.clienteAtual.clienteId)
        else:
            self.clienteAtual.delete().execute()

        self.limpaTudo()
        self.dashboard.trocaTela(TelaAtual.Cliente)

    def salvaEtapaBancaria(self):
        if self.dadosBancarios is None:
            self.dadosBancarios = ClienteInfoBanco()

        self.dadosBancarios.estado = self.clienteAtual.estado
        self.dadosBancarios.clienteId = self.clienteAtual.clienteId
        self.insereInfoTela('lePix')
        self.insereInfoTela('leNomeBanco')
        self.insereInfoTela('leNumeroConta')
        self.insereInfoTela('leNumeroAgencia')
        self.insereInfoTela('leSenhaINSS')
        self.dadosBancarios.save()

    def salvaEtapaPessoal(self):
        self.insereInfoTela('nomeCliente')
        self.insereInfoTela('nomeMae')
        self.insereInfoTela('rg')
        self.insereInfoTela('cpf')
        self.insereInfoTela('email')
        self.insereInfoTela('dataNascimento')
        self.insereInfoTela('estCivil')
        self.insereInfoTela('cbxEscolaridade')
        self.insereInfoTela('complemento')
        self.insereInfoTela('cep')
        self.insereInfoTela('endereco')
        self.insereInfoTela('cidade')
        self.insereInfoTela('bairro')
        self.insereInfoTela('leNumero')
        self.insereInfoTela('complemento')

        if self.rbMasculino.isChecked():
            self.insereInfoTela('rbMasculino')
        else:
            self.insereInfoTela('rbFeminino')

        if self.clienteAtual.escritorioId is None:
            self.clienteAtual.escritorioId = self.escritorioAtual.escritorioId

        try:
            self.clienteAtual.save()
        except sqlite3.IntegrityError as err:
            logPrioridade("salvaEtapaPessoal<wdgCadastroCliente>", tipoEdicao=TipoEdicao.insert)
            popUpOkAlerta(
                "Caso queira fazer uma simulação, acesse o menu da calculadora rápida.",
                titulo="Cliente já cadastrado.",
                funcao=self.sairCadastro,
            )
        except peewee.IntegrityError as err:
            logPrioridade("salvaEtapaPessoal<wdgCadastroCliente>", tipoEdicao=TipoEdicao.insert)
            popUpOkAlerta(
                "Caso queira fazer uma simulação, acesse o menu da calculadora rápida.",
                titulo="Cliente já cadastrado.",
                funcao=self.sairCadastro,
            )

        self.avaliaInsereTelefone()
        self.avaliaInsereTelefoneSecundario()

    def salvaEtapaProfissional(self):
        self.insereInfoTela('cartProf')
        self.insereInfoTela('profissao')
        self.insereInfoTela('nit')
        self.dadosProfissionais.save()

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

    def verificaPerderAlteracoes(self):
        popUpSimCancela(
            "Deseja voltar para a tela anterior? Isso apagará suas alterações.",
            funcaoSim=lambda: self.dashboard.trocaTela(TelaAtual.Cliente)
        )
