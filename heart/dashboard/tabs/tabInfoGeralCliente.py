from PyQt5.QtWidgets import QWidget, QWidgetItem
from typing import List

from Design.pyUi.wdgInfoGeralCliente import Ui_wdgInfoGeralCliente
from modelos.clienteORM import Cliente
from modelos.telefonesORM import Telefones
from util.dateHelper import mascaraData, calculaIdadeAutomatica
from Design.CustomWidgets.newCheckBox import NewCheckBox
from heart.dashboard.tabs.localWidgets.wdgTelefone import WdgTelefone

from util.helpers import mascaraRG, mascaraCPF, mascaraCep
from util.enums.newPrevEnums import GeneroCliente
from util.ferramentas.layout import limpaLayout


class TabInfoGeralCliente(Ui_wdgInfoGeralCliente, QWidget):
    clienteModel: Cliente = None
    listaTelefones: List[Telefones] = []
    ncbProfessor: NewCheckBox

    def __init__(self, parent=None):
        super(TabInfoGeralCliente, self).__init__(parent=parent)
        self.setupUi(self)
        self.ncbProfessor = NewCheckBox()
        self.hlProfessor.addWidget(self.ncbProfessor)

    def buscaCliente(self, clienteId: int = 0, modeloCliente: Cliente = None):
        if modeloCliente is not None:
            self.clienteModel = modeloCliente
        else:
            self.clienteModel = Cliente.get_by_id(clienteId)

        self.listaTelefones = Telefones.select().where(Telefones.clienteId == clienteId).order_by(Telefones.ativo.desc())
        self.carregaClienteNaTela()

    def carregaClienteNaTela(self):
        # Cabeçalho
        self.lbCdCliente.setText(str(self.clienteModel.clienteId))
        self.lbNomeCliente.setText(self.clienteModel.nomeCliente + self.clienteModel.sobrenomeCliente)

        # Informações pessoais
        self.lbNome.setText(self.clienteModel.nomeCliente)
        self.lbSobrenome.setText(self.clienteModel.sobrenomeCliente)
        self.lbRg.setText(mascaraRG(self.clienteModel.rgCliente))
        self.lbCpf.setText(mascaraCPF(self.clienteModel.cpfCliente))
        self.lbNomeMae.setText(self.clienteModel.nomeMae)
        self.lbSexo.setText(GeneroCliente(self.clienteModel.genero).name.title())
        self.lbDtNascimento.setText(mascaraData(self.clienteModel.dataNascimento))
        self.lbIdade.setText(calculaIdadeAutomatica(self.clienteModel.dataNascimento))
        self.lbEmail.setText(self.clienteModel.email)
        self.lbEstadoCivil.setText(self.clienteModel.estadoCivil)
        self.lbEscolaridade.setText(self.clienteModel.grauEscolaridade)

        # Informações residenciais
        self.lbCep.setText(mascaraCep(self.clienteModel.cep))
        self.lbNumero.setText(str(self.clienteModel.numero))
        self.lbEndereco.setText(self.clienteModel.endereco)
        self.lbCidade.setText(self.clienteModel.cidade)
        self.lbBairro.setText(self.clienteModel.bairro)
        self.lbEstado.setText(self.clienteModel.estado)
        self.lbComplemento.setText(self.clienteModel.complemento)

        # Informações profissionais
        self.lbNit.setText(str(self.clienteModel.nit))
        self.lbCarteira.setText(str(self.clienteModel.numCarteiraProf) if self.clienteModel.numCarteiraProf is not None else '')
        self.lbProfissao.setText(self.clienteModel.profissao)
        self.ncbProfessor.setDisabled(True)
        self.ncbProfessor.setChecked(self.clienteModel.professor)

        # Informações cadastrais
        self.lbDtCadastro.setText(mascaraData(self.clienteModel.dataCadastro))
        self.lbUltAlt.setText(mascaraData(self.clienteModel.dataUltAlt))

        # Informações de contato
        self.carregaTelefones()

    def carregaTelefones(self):
        telefonesWdg = [WdgTelefone(telefone, parent=self.scaInfoContatos) for telefone in self.listaTelefones]
        telefoneItens = [QWidgetItem(telefone) for telefone in telefonesWdg]
        linha: int = 0
        coluna: int = 0

        for row, tel in enumerate(telefoneItens):
            if row % 2 == 0:
                linha += 1
                coluna = 0
            else:
                coluna += 1
            self.grdTelefones.addItem(tel, linha, coluna)

    def limpaTudo(self):
        # Cabeçalho
        self.lbCdCliente.setText('')
        self.lbNomeCliente.setText('')

        # Informações pessoais
        self.lbNome.setText('')
        self.lbSobrenome.setText('')
        self.lbRg.setText('')
        self.lbCpf.setText('')
        self.lbNomeMae.setText('')
        self.lbSexo.setText('')
        self.lbDtNascimento.setText('')
        self.lbIdade.setText('')
        self.lbEmail.setText('')
        self.lbEstadoCivil.setText('')
        self.lbEscolaridade.setText('')

        # Informações residenciais
        self.lbCep.setText('')
        self.lbNumero.setText('')
        self.lbEndereco.setText('')
        self.lbCidade.setText('')
        self.lbBairro.setText('')
        self.lbEstado.setText('')
        self.lbComplemento.setText('')

        # Informações profissionais
        self.lbNit.setText('')
        self.lbCarteira.setText('')
        self.lbProfissao.setText('')
        self.ncbProfessor.setDisabled(False)
        self.ncbProfessor.setChecked(False)

        limpaLayout(self.grdTelefones)

        self.tabInfoCliente.setCurrentIndex(0)
