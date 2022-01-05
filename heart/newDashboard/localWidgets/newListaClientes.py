import os

from peewee import SqliteDatabase
from typing import List

from PyQt5.QtCore import QObject, QEvent, Qt
from PyQt5.QtGui import QFont, QKeyEvent, QCursor
from PyQt5.QtWidgets import QFrame, QTableWidgetItem, QPushButton

from Design.pyUi.newListaClientes import Ui_wdgListaClientes
from Design.CustomWidgets.newPopupCNIS import NewPopupCNIS
from Design.CustomWidgets.newToast import QToaster
from Design.CustomWidgets.newMenuOpcoes import NewMenuOpcoes
from Design.pyUi.efeitos import Efeitos

from heart.newDashboard.localStyleSheet import btnOpcoesStyle

from modelos.cabecalhoORM import CnisCabecalhos
from modelos.clienteORM import Cliente
from modelos.cnisModelo import CNISModelo
from modelos.escritoriosORM import Escritorios
from modelos.itemContribuicao import ItemContribuicao
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from modelos.advogadoORM import Advogados
from modelos.clienteProfissao import ClienteProfissao

from sinaisCustomizados import Sinais
from util.dateHelper import strToDate, atividadesConcorrentes, atividadeSecundaria

from util.helpers import mascaraTelCel, unmaskAll, calculaIdadeFromString
from util.popUps import popUpOkAlerta


class NewListaClientes(QFrame, Ui_wdgListaClientes):
    popupCNIS: NewPopupCNIS
    toast: QToaster

    def __init__(self, escritorio: Escritorios, advogado: Advogados, parent=None):
        super(NewListaClientes, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent
        self.popupCNIS = None
        self.escritorioAtual = escritorio
        self.advogadoAtual = advogado

        self.sinais = Sinais()
        self.sinais.sEnviaClienteParam.connect(self.enviaClienteDashboard)
        self.sinais.sEnviaInfoCliente.connect(self.enviaInfoClienteDashboard)
        self.efeitos = Efeitos()
        self.toast = QToaster(parent=self)

        self.tblClientes.hideColumn(0)
        self.installEventFilter(self)

        self.pbNovoCliente.clicked.connect(self.abrirPopupCNIS)
        self.tblClientes.doubleClicked.connect(self.selecionaCliente)

        self.atualizaTblClientes()

    def abreMenuOpcoes(self, linha: int):
        menu = NewMenuOpcoes(
            parent=self,
            funcEditar=lambda: print(f"abreMenuOpcoes: {linha}"),
            funcArquivar=lambda: print(f"abreMenuOpcoes: {linha}"),
        )
        self.efeitos.shadowCards([menu])
        position = self.mapToGlobal(QCursor.pos())
        menu.move(position.x() - 10, position.y() - 250)
        menu.show()

    def atualizaTblClientes(self, clientes: list = None):
        if clientes is None:
            clientesModels: list = Cliente.select().order_by(Cliente.nomeCliente)
        else:
            clientesModels = []

        self.tblClientes.setRowCount(0)
        for numLinha, cliente in enumerate(clientesModels):
            self.tblClientes.insertRow(numLinha)
            processo: Processos = Processos.get_or_none(Processos.clienteId == cliente.clienteId)
            telefone: Telefones = Telefones.get_or_none(Telefones.clienteId == cliente.clienteId)

            if processo is None:
                processo = Processos()
            if telefone is None:
                telefone = Telefones()

            # 0 - clienteId <Escondida>
            cdClienteItem = QTableWidgetItem(str(cliente.clienteId))
            cdClienteItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 0, cdClienteItem)

            # 1 - Nome completo do cliente <Aparente>
            nomeCompletoItem = QTableWidgetItem(f"{cliente.nomeCliente} {cliente.sobrenomeCliente}")
            nomeCompletoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 1, nomeCompletoItem)

            # 2 - E-mail do cliente <Aparente>
            if cliente.email is None:
                emailItem = QTableWidgetItem('')
            else:
                emailItem = QTableWidgetItem(f"{cliente.email}")
            emailItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 2, emailItem)

            # 3 - Contato do cliente <Aparente>
            telefoneItem = QTableWidgetItem(f"{mascaraTelCel(telefone.numero)}")
            telefoneItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 3, telefoneItem)

            # 4 - Cidade de nascimento do cliente <Aparente>
            if cliente.cidade is None:
                cidadeItem = QTableWidgetItem('')
            else:
                cidadeItem = QTableWidgetItem(f"{cliente.cidade}")
            cidadeItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 4, cidadeItem)

            # tipoProcessoItem = QTableWidgetItem(strTipoBeneficio(processo.tipoBeneficio, processo.subTipoApos))
            # tipoProcessoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            # self.tblClientes.setItem(numLinha, 5, tipoProcessoItem)

            pbOpcoes = QPushButton()
            pbOpcoes.clicked.connect(lambda: self.abreMenuOpcoes(numLinha))
            pbOpcoes.setStyleSheet(btnOpcoesStyle())
            pbOpcoes.setMaximumSize(24, 24)
            self.tblClientes.setCellWidget(numLinha, 6, pbOpcoes)

        self.tblClientes.resizeColumnsToContents()

    def abrirPopupCNIS(self):
        if self.popupCNIS is not None and self.popupCNIS.isVisible():
            self.popupCNIS.close()
            self.popupCNIS.setParent(None)

        self.popupCNIS = NewPopupCNIS(parent=self, dashboard=self.dashboard)
        Efeitos().shadowCards([self.popupCNIS])
        self.popupCNIS.raise_()
        self.popupCNIS.show()

        self.popupCNIS.setFocus()

    def avaliaDadosFaltantesNoCNIS(self, cabecalhos: List[dict]) -> List[dict]:
        listaReturn: List[dict] = []

        for cabecalho in cabecalhos:
            faltaDataFim = cabecalho['dataFim'] is None or cabecalho['dataFim'] == ''
            faltaDataInicio = cabecalho['dataInicio'] is None or cabecalho['dataInicio'] == ''

            cabecalho['dadoFaltante'] = faltaDataFim or faltaDataInicio
            listaReturn.append(cabecalho)

        return listaReturn

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

    def carregaCnis(self, pathCnis: str):
        cnisInseridoComSucesso: bool = False

        self.cnisClienteAtual: CNISModelo = CNISModelo(path=pathCnis)
        self.cnisClienteAtual.iniciaAvaliacaoCnis()
        db: SqliteDatabase = Cliente._meta.database

        # clienteAtual = Cliente()
        try:
            infoPessoais: dict = self.cnisClienteAtual.getInfoPessoais()

            if infoPessoais is not None:
                clienteAtual: Cliente = Cliente(
                    escritorioId=Escritorios.select().where(Escritorios.escritorioId == self.escritorioAtual.escritorioId),
                    cpfCliente=unmaskAll(infoPessoais['cpf']),
                    dataNascimento=strToDate(infoPessoais['dataNascimento']),
                    idade=calculaIdadeFromString(infoPessoais['dataNascimento']),
                    nomeMae=infoPessoais['nomeMae'].title(),
                    nomeCliente=infoPessoais['nomeCompleto'].split(' ')[0].title(),
                    sobrenomeCliente=' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]).title(),
                    pathCnis=pathCnis
                )
                clienteAtual.save()

                # Dados profissionais
                dadosProfissao: ClienteProfissao = ClienteProfissao(
                    clienteId=clienteAtual.clienteId,
                    nit=unmaskAll(infoPessoais['nit'])
                )
                dadosProfissao.save()

                clienteAtual.dadosProfissionais = dadosProfissao

                contribuicoes = self.cnisClienteAtual.getAllDict(toInsert=True, clienteId=clienteAtual.clienteId)
                cabecalho = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalho'])
                cabecalhoBeneficio = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalhoBeneficio'])

                CnisCabecalhos.insert_many(cabecalho).on_conflict_replace().execute()
                CnisCabecalhos.insert_many(cabecalhoBeneficio).on_conflict_replace().execute()

                clienteAtual.telefoneId = self.buscaTelefone(clienteAtual)
                clienteAtual.save()

                self.cnisClienteAtual.insereItensContribuicao(clienteAtual)
                cnisInseridoComSucesso = True

        except Cliente.DoesNotExist:
            self.showPopupAlerta('Erro ao inserir cliente.')
            if clienteAtual is not None:
                clienteAtual.delete()
            return False

        except Exception as err:
            popUpOkAlerta('Não foi possível salvar o cliente. Tente novamente.', erro=str(err))
            print(f'carregaCnis - erro: {err=}')

        if cnisInseridoComSucesso:
            self.avaliaAtividadesPrincipais(clienteAtual.clienteId)

        self.sinais.sEnviaClienteParam.emit(clienteAtual)

    def buscaTelefone(self, clienteAtual: Cliente) -> Telefones:
        try:
            return Telefones.select().where(Telefones.clienteId == clienteAtual.clienteId).get()
        except Telefones.DoesNotExist:
            return None

    def eventFilter(self, a0: QObject, tecla: QEvent) -> bool:
        if isinstance(tecla, QKeyEvent) and self.popupCNIS is not None:
            if self.popupCNIS.isVisible():
                self.popupCNIS.close()

        return super(NewListaClientes, self).eventFilter(a0, tecla)

    def enviaClienteDashboard(self, cliente: Cliente):
        self.dashboard.recebeCliente(cliente)

    def enviaInfoClienteDashboard(self, cliente: Cliente):
        self.dashboard.navegaInfoCliente(cliente)

    def selecionaCliente(self, *args, **kwargs):
        linhaSelecionada = args[0].row()

        clienteId = self.tblClientes.item(linhaSelecionada, 0).text()
        clienteSelecionado: Cliente = Cliente.get_by_id(clienteId)

        self.sinais.sEnviaInfoCliente.emit(clienteSelecionado)

    def recebePathCnis(self, path: str):
        if os.path.isfile(path):
            self.carregaCnis(path)
            return True

    def toastCarregaCnis(self):
        self.toast.showMessage(self, "Analisando informações do CNIS...", corner=Qt.BottomLeftCorner)


if __name__ == '__main__':
    from PyQt5 import QtWidgets, QtGui
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = NewListaClientes()
    w.show()
    sys.exit(app.exec_())