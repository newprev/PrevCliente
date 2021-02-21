from PyQt5.QtWidgets import QMainWindow

from Telas.cadastroCliente import Ui_mwCadastroCliente
from helpers import estCivil
from modelos.cnisModelo import CNISModelo


class CadastraClientePage(Ui_mwCadastroCliente, QMainWindow):

    def __init__(self, db=None):
        super(CadastraClientePage, self).__init__()
        self.setupUi(self)
        self.cnisClienteAtual = None

        self.db = db
        self.pbCarregaCnis.clicked.connect(self.carregaCnis)

        self.cbxEstado.addItems(estCivil)

    def carregaCnis(self):
        self.cnisClienteAtual = CNISModelo()
        self.cnisClienteAtual.buscaPath()
        infoPessoais = self.cnisClienteAtual.getInfoPessoais()

        if infoPessoais is not None:
            self.leCpf.setText(infoPessoais['cpf'])
            self.leNis.setText(infoPessoais['nit'])
            self.leNomeMae.setText(infoPessoais['nomeMae'])
            self.lePrimeiroNome.setText(infoPessoais['nomeCompleto'].split(' ')[0])
            self.leSobrenome.setText(' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]))
