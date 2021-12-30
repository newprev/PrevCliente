from datetime import date, datetime
import os
import time
from dateutil.relativedelta import relativedelta

from PyQt5.QtWidgets import QWidget

from Design.pyUi.wdgInfoCliente import Ui_wdgInfoCliente
from Design.CustomWidgets.newToast import QToaster

from sinaisCustomizados import Sinais

from util.dateHelper import mascaraData, calculaIdade
from util.enums.dashboardEnums import TelaAtual

from util.helpers import mascaraCPF, mascaraRG, mascaraTelCel, mascaraCep, mascaraNit

from modelos.clienteORM import Cliente


class NewInfoCliente(QWidget, Ui_wdgInfoCliente):
    clienteAtual: Cliente
    toasty: QToaster

    def __init__(self, parent=None):
        super(NewInfoCliente, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent
        self.sinais = Sinais()
        self.sinais.sVoltaTela.connect(self.voltarDashboard)
        self.toasty = QToaster()
        self.limpaTudo()

        self.pbVoltar.clicked.connect(lambda: self.sinais.sVoltaTela.emit())

    def carregaClienteNaTela(self, cliente: Cliente):
        if cliente is not None and cliente.clienteId is not None:
            self.clienteAtual = cliente

            # Cabeçalho
            self.lbNomeCliente.setText(f"{cliente.nomeCliente} {cliente.sobrenomeCliente.strip()}")
            self.lbTelefone.setText(mascaraTelCel(cliente.telefoneId.numero) if cliente.telefoneId is not None else "-")
            self.lbEmail.setText(cliente.email)

            # Informações pessoais
            self.lbNomeCompletoInferior.setText(f"{cliente.nomeCliente} {cliente.sobrenomeCliente.strip()}")
            self.lbCpf.setText(mascaraCPF(cliente.cpfCliente))
            self.lbRg.setText(mascaraRG(cliente.rgCliente))
            self.lbDataNascimento.setText(f"{mascaraData(cliente.dataNascimento)} ({calculaIdade(cliente.dataNascimento, date.today()).years} anos)")
            self.lbEscolaridade.setText(cliente.grauEscolaridade)
            self.lbEmailInferior.setText(cliente.email)
            self.lbEstadoCivil.setText(cliente.estadoCivil)
            self.lbNomeMae.setText(cliente.nomeMae)
            self.rbMasculino.setChecked(True)

            # Informações residenciais
            self.lbCidade.setText(cliente.cidade)
            self.lbEstado.setText(cliente.estado)
            self.lbEndereco.setText(cliente.endereco)
            self.lbNumero.setText(str(cliente.numero))
            self.lbCep.setText(mascaraCep(cliente.cep) if cliente.cep is not None else '-')
            self.lbComplemento.setText(cliente.complemento)

            # Informações profissionais
            self.lbNit.setText(mascaraNit(cliente.nit))
            self.lbProfissao.setText(cliente.profissao)
            self.lbCarteiraProfissional.setText(cliente.numCartProf)

            # Informações CNIS
            pathCnis: str = cliente.pathCnis
            if pathCnis is not None:
                indexNomeArquivo = pathCnis.rfind('/') + 1

                secEpoch = int(time.time()) - os.path.getatime(pathCnis)
                ultimaAtualizacaoArquivo: relativedelta = relativedelta(seconds=secEpoch)
                self.lbInfoMetaArquivo.show()

                self.lbInfoNomeArquivo.setText(pathCnis[indexNomeArquivo:])
                if ultimaAtualizacaoArquivo.years != 0:
                    self.lbInfoMetaArquivo.setText(f"{int(ultimaAtualizacaoArquivo.years)} anos atrás")
                elif ultimaAtualizacaoArquivo.months != 0:
                    self.lbInfoMetaArquivo.setText(f"{int(ultimaAtualizacaoArquivo.months)} meses atrás")
                elif ultimaAtualizacaoArquivo.days != 0:
                    self.lbInfoMetaArquivo.setText(f"{int(ultimaAtualizacaoArquivo.days)} dias atrás")
                elif ultimaAtualizacaoArquivo.hours != 0:
                    self.lbInfoMetaArquivo.setText(f"{int(ultimaAtualizacaoArquivo.hours)} horas atrás")
                elif ultimaAtualizacaoArquivo.minutes != 0:
                    self.lbInfoMetaArquivo.setText(f"{int(ultimaAtualizacaoArquivo.minutes)} minutos atrás")
                elif ultimaAtualizacaoArquivo.seconds != 0:
                    self.lbInfoMetaArquivo.setText(f"{int(ultimaAtualizacaoArquivo.seconds)} segundos atrás")
            else:
                self.lbInfoNomeArquivo.setText('CNIS NÃO ENVIADO')
                self.lbInfoMetaArquivo.hide()

        else:
            self.toasty.showMessage(self, "Não foi possível carregar as informações do cliente.")

    def limpaTudo(self):
        self.clienteAtual = None

        # Cabeçalho
        self.lbNomeCliente.setText("Fulano de Tal")
        self.lbTelefone.setText("(11) 9.9999-9999")
        self.lbEmail.setText("fulana.deTal@gmail.com")

        # Informações pessoais
        self.lbNomeCompletoInferior.setText("Fulano de Tal")
        self.lbCpf.setText("999.999.999-99")
        self.lbRg.setText("99.999.999-9")
        self.lbDataNascimento.setText("01/01/1999")
        self.lbEscolaridade.setText("Superior completo")
        self.lbEmailInferior.setText("fulana.deTal@gmail.com")
        self.lbEstadoCivil.setText("Solteiro(a)")
        self.lbNomeMae.setText("Fulana de Tal")
        self.rbMasculino.setChecked(True)

        # Informações residenciais
        self.lbCidade.setText("São Paulo")
        self.lbEstado.setText("São Paulo")
        self.lbEndereco.setText("Av. Paulista")
        self.lbNumero.setText("1254")
        self.lbCep.setText("99999-999")
        self.lbComplemento.setText("Bloco A1 - Apto:601")

        # Informações profissionais
        self.lbNit.setText('99.9999.99')
        self.lbProfissao.setText('Ajudante de obras')
        self.lbCarteiraProfissional.setText('-')

        # Informações CNIS
        self.lbInfoNomeArquivo.setText('fulanoDeTal.pdf')
        self.lbInfoMetaArquivo.setText("10 dias atrás")

    def voltarDashboard(self):
        self.limpaTudo()
        self.dashboard.trocaTela(TelaAtual.Cliente)
