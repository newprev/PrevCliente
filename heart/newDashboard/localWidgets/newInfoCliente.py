from datetime import date, datetime
import os
import time
from typing import List

from PyQt5.QtCore import Qt, QObject, QEvent
from PyQt5.QtGui import QCursor, QKeyEvent
from dateutil.relativedelta import relativedelta

from PyQt5.QtWidgets import QWidget

from Design.CustomWidgets.newMenuOpcoes import NewMenuOpcoes
from Design.CustomWidgets.newPopupCNIS import NewPopupCNIS
from Design.pyUi.efeitos import Efeitos
from Design.pyUi.wdgInfoCliente import Ui_wdgInfoCliente
from Design.CustomWidgets.newToast import QToaster
from modelos.cabecalhoORM import CnisCabecalhos
from modelos.clienteInfoBanco import ClienteInfoBanco
from modelos.clienteProfissao import ClienteProfissao
from modelos.cnisModelo import CNISModelo
from modelos.itemContribuicao import ItemContribuicao

from sinaisCustomizados import Sinais

from util.dateHelper import mascaraData, calculaIdade, atividadesConcorrentes, strToDate, atividadeSecundaria
from util.enums.dashboardEnums import TelaAtual
from util.popUps import popUpSimCancela, popUpOkAlerta

from util.helpers import mascaraCPF, mascaraRG, mascaraTelCel, mascaraCep, mascaraNit

from modelos.clienteORM import Cliente


class NewInfoCliente(QWidget, Ui_wdgInfoCliente):
    clienteAtual: Cliente
    dadosBancarios: ClienteInfoBanco
    dadosProfissionais: ClienteProfissao
    popupCNIS: NewPopupCNIS
    toasty: QToaster

    def __init__(self, parent=None):
        super(NewInfoCliente, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent
        self.sinais = Sinais()
        self.sinais.sVoltaTela.connect(self.voltarDashboard)
        self.sinais.sEnviaInfo.connect(self.editarInfoCliente)
        self.sinais.sIniciaEntrevista.connect(self.iniciarEntrevista)
        self.sinais.sAbreResumoCnis.connect(self.abreResumo)
        self.toasty = None
        self.popupCNIS = None
        self.limpaTudo()

        self.rbMasculino.setDisabled(True)
        self.rbFeminino.setDisabled(True)
        self.installEventFilter(self)

        self.pbVoltar.clicked.connect(lambda: self.sinais.sVoltaTela.emit())
        self.pbEntrevista.clicked.connect(self.confirmaIniciaEntrevista)
        self.pbResumo.clicked.connect(self.enviaSinalResumoCnis)
        self.iniciarBotoesOpcoes()

    def abreResumo(self):
        self.dashboard.trocaTela(TelaAtual.Resumo, self.clienteAtual)

    def abreMenuInfoOpcoes(self, info: str):

        menu = NewMenuOpcoes(
            parent=self,
            funcEditar=lambda: self.sinais.sEnviaInfo.emit(info),
        )
        menu.exec_(QCursor.pos())
        return True

    def abreMenuCnisOpcoes(self):

        menu = NewMenuOpcoes(
            parent=self,
            funcAtualizar=self.verificaAtualizarCnis,
        )
        menu.exec_(QCursor.pos())
        return True

    def abrirPopupCNIS(self):
        if self.popupCNIS is not None and self.popupCNIS.isVisible():
            self.popupCNIS.close()
            self.popupCNIS.setParent(None)

        self.popupCNIS = NewPopupCNIS(parent=self, dashboard=self.dashboard, esconderBotao=True)
        Efeitos().shadowCards([self.popupCNIS])
        self.popupCNIS.raise_()
        self.popupCNIS.show()

        self.popupCNIS.setFocus()

    def atualizarCnis(self, novoCnis: str):
        try:
            self.clienteAtual.pathCnis = novoCnis

            cnisClienteAtual: CNISModelo = CNISModelo(path=novoCnis)
            cnisClienteAtual.iniciaAvaliacaoCnis()

            infoPessoais: dict = cnisClienteAtual.getInfoPessoais()

            if infoPessoais is not None:
                contribuicoes = cnisClienteAtual.getAllDict(toInsert=True, clienteId=self.clienteAtual.clienteId)
                cabecalho = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalho'])
                cabecalhoBeneficio = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalhoBeneficio'])

                CnisCabecalhos.delete().where(CnisCabecalhos.clienteId==self.clienteAtual.clienteId).execute()
                ItemContribuicao.delete().where(ItemContribuicao.clienteId==self.clienteAtual.clienteId).execute()

                CnisCabecalhos.insert_many(cabecalho).on_conflict_replace().execute()
                CnisCabecalhos.insert_many(cabecalhoBeneficio).on_conflict_replace().execute()

                cnisClienteAtual.insereItensContribuicao(self.clienteAtual)
                self.avaliaAtividadesPrincipais(self.clienteAtual.clienteId)

                self.clienteAtual.dataUltAlt = datetime.now()
                self.clienteAtual.save()

        except Exception as err:
            popUpOkAlerta('Não foi possível salvar o cliente. Tente novamente.', erro=str(err))
            print(f"atualizarCnis <NewInfoCliente>: {err=}")

    def avaliaAtividadesPrincipais(self, clienteId: int):
        listaCabecalhos: List[CnisCabecalhos] = CnisCabecalhos.select().where(CnisCabecalhos.clienteId == clienteId)

        for index, cabecalho in enumerate(listaCabecalhos):
            if index == 0 or listaCabecalhos[index-1].dadoFaltante or listaCabecalhos[index].dadoFaltante:
                continue

            conflitoAtividades = atividadesConcorrentes(
                dataIniAtivA=strToDate(listaCabecalhos[index-1].dataInicio),
                dataFimAtvA=strToDate(listaCabecalhos[index-1].dataFim),
                dataIniAtivB=strToDate(listaCabecalhos[index].dataInicio),
                dataFimAtivB=strToDate(listaCabecalhos[index].dataFim),
            )

            if conflitoAtividades:
                seqSecundarioCalculado = atividadeSecundaria(listaCabecalhos[index-1], listaCabecalhos[index])
                query = ItemContribuicao.update({ItemContribuicao.ativPrimaria: False}).where(
                    ItemContribuicao.clienteId == clienteId,
                    ItemContribuicao.seq == seqSecundarioCalculado,
                    )
                query.execute()

    def avaliaDadosFaltantesNoCNIS(self, cabecalhos: List[dict]) -> List[dict]:
        listaReturn: List[dict] = []

        for cabecalho in cabecalhos:
            faltaDataFim = cabecalho['dataFim'] is None or cabecalho['dataFim'] == ''
            faltaDataInicio = cabecalho['dataInicio'] is None or cabecalho['dataInicio'] == ''

            cabecalho['dadoFaltante'] = faltaDataFim or faltaDataInicio
            listaReturn.append(cabecalho)

        return listaReturn

    def carregaClienteNaTela(self, cliente: Cliente):
        if cliente is not None and cliente.clienteId is not None:
            self.clienteAtual = cliente
            self.dadosBancarios = self.buscaDadosBancarios()
            self.dadosProfissionais = self.buscaDadosProfissionais()

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
            if self.dadosProfissionais is not None:
                self.lbNit.setText(mascaraNit(self.dadosProfissionais.nit))
                self.lbProfissao.setText(self.dadosProfissionais.nomeProfissao)
                self.lbCarteiraProfissional.setText(self.dadosProfissionais.numCaretiraTrabalho)
            else:
                self.lbNit.setText('-')
                self.lbProfissao.setText('-')
                self.lbCarteiraProfissional.setText('-')

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
            self.toasty = QToaster()
            self.toasty.showMessage(self, "Não foi possível carregar as informações do cliente.")

    def confirmaIniciaEntrevista(self):
        popUpSimCancela(
            f"Você deseja iniciar uma nova entrevista com o(a) cliente: \n\n{self.clienteAtual.nomeCliente} {self.clienteAtual.sobrenomeCliente}?",
            titulo="Iniciar entrevista",
            funcao=self.sinais.sIniciaEntrevista.emit,
        )
        return True

    def buscaDadosProfissionais(self):
        try:
            return ClienteProfissao.get_by_id(self.clienteAtual.dadosProfissionais)
        except ClienteProfissao.DoesNotExist as err:
            print(f"buscaDadosProfissionais: {err=}")
            return None

    def buscaDadosBancarios(self):
        try:
            return ClienteInfoBanco.get_by_id(self.clienteAtual.dadosBancarios)
        except ClienteInfoBanco.DoesNotExist as err:
            print(f"buscaDadosBancarios: {err=}")
            return None

    def editarInfoCliente(self, info):
        self.dashboard.recebeCliente(self.clienteAtual, info=info)
        return True

    def enviaSinalResumoCnis(self):
        self.sinais.sAbreResumoCnis.emit()

    def eventFilter(self, a0: QObject, tecla: QEvent) -> bool:
        if isinstance(tecla, QKeyEvent) and self.popupCNIS is not None:
            if self.popupCNIS.isVisible():
                self.popupCNIS.close()

        return super(NewInfoCliente, self).eventFilter(a0, tecla)

    def iniciarEntrevista(self):
        self.dashboard.trocaTela(TelaAtual.Entrevista, self.clienteAtual)

    def iniciarBotoesOpcoes(self):
        # Informações pessoais
        self.pbInfoPessoais.clicked.connect(lambda: self.abreMenuInfoOpcoes('infoPessoais'))

        # Informações residenciais
        self.pbInfoResidenciais.clicked.connect(lambda: self.abreMenuInfoOpcoes('infoResidenciais'))

        # Informações profissionais
        self.pbInfoProfissionais.clicked.connect(lambda: self.abreMenuInfoOpcoes('infoProfissionais'))

        # Atualizar CNIS
        self.pbOpcoesCnis.clicked.connect(self.abreMenuCnisOpcoes)

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

    def recebePathCnis(self, pathCnis:str):
        if os.path.isfile(pathCnis):
            self.atualizarCnis(pathCnis)
            self.carregaClienteNaTela(self.clienteAtual)
            return True
        else:
            popUpOkAlerta("O caminho escolhido está incorreto. Tente novamente.")
            print(f'recebePathCnis <NewInfoCliente>: {os.path.isfile(pathCnis)=}')
            return False

    def toastCarregaCnis(self):
        self.toasty.showMessage(self, "Analisando informações do CNIS...", corner=Qt.BottomLeftCorner)

    def verificaAtualizarCnis(self):
        popUpSimCancela(
            "Atualizar o CNIS excluirá todos as contribuições e benefícios inseridos anteriormente, além das simulações geradas.\nDeseja continuar?",
            titulo="Atualizar arquivo do CNIS",
            funcao=lambda: self.abrirPopupCNIS()
        )
        return True

    def voltarDashboard(self):
        self.limpaTudo()
        self.dashboard.trocaTela(TelaAtual.Cliente)
