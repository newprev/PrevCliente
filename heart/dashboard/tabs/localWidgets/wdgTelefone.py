import datetime

from PyQt5.QtWidgets import QGroupBox

from Design.pyUi.wdgTelefone import Ui_gboxTelefone
from Design.CustomWidgets.newCheckBox import NewCheckBox
from modelos.telefonesORM import Telefones
from ..localStyleSheet.telefoneWdg import *

from util.helpers import mascaraTelCel
from util.enums.telefoneEnums import *


class WdgTelefone(QGroupBox, Ui_gboxTelefone):
    telefoneModel: Telefones
    ncbAtivo: NewCheckBox

    def __init__(self, telefone: Telefones, parent=None):
        super(WdgTelefone, self).__init__(parent=parent)
        self.setupUi(self)
        self.telefoneModel = telefone
        self.ncbAtivo = NewCheckBox()
        self.hlAtivo.addWidget(self.ncbAtivo)

        self.ncbAtivo.clicked.connect(self.alterouAtivo)

        self.carregaTelNaTela()

    def carregaTelNaTela(self):
        self.lbNumero.setText(mascaraTelCel(self.telefoneModel.numero))
        self.ncbAtivo.setChecked(self.telefoneModel.ativo)
        self.frTipo.setStyleSheet(tipoTelefone(self.telefoneModel.tipoTelefone))
        self.frPessoal.setStyleSheet(telefonePessoal(self.telefoneModel.pessoalRecado))
        self.setStyleSheet(self.styleSheet() + telefonePrincipal(self.telefoneModel.principal))
        self.lbTipo.setText(TipoTelefone(self.telefoneModel.tipoTelefone).name)
        self.lbPessoal.setText(TelefonePesoal(self.telefoneModel.pessoalRecado).name)
        self.setTitle('Principal' if self.telefoneModel.principal else 'Secundário')

    def alterouAtivo(self):
        self.telefoneModel.ativo = self.ncbAtivo.isChecked()
        self.telefoneModel.dataUltAlt = datetime.date.today()
        self.telefoneModel.save()
