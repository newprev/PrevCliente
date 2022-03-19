import os
import datetime

from typing import List

from PyQt5.QtCore import QObject, QEvent, Qt, QSize
from PyQt5.QtGui import QFont, QKeyEvent, QCursor, QIcon
from PyQt5.QtWidgets import QFrame, QTableWidgetItem, QPushButton

from Design.pyUi.newListaClientes import Ui_wdgListaClientes
from Design.CustomWidgets.newPopupCNIS import NewPopupCNIS
from Design.CustomWidgets.newFiltroClientes import NewFiltroClientes
from Design.CustomWidgets.newToast import QToaster
from Design.CustomWidgets.newMenuOpcoes import NewMenuOpcoes
from Design.efeitos import Efeitos

from heart.newDashboard.localStyleSheet.localStyleSheet import btnOpcoesStyle, styleTooltip

from modelos.vinculoORM import CnisVinculos
from modelos.clienteORM import Cliente
from modelos.cnisModelo import CNISModelo
from modelos.escritoriosORM import Escritorios
from modelos.itemContribuicao import ItemContribuicao
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from modelos.advogadoORM import Advogados
from modelos.clienteProfissao import ClienteProfissao

from sinaisCustomizados import Sinais
from util.helpers.dateHelper import strToDate, atividadesConcorrentes, atividadeSecundaria
from util.enums.dashboardEnums import TelaAtual

from util.helpers.helpers import mascaraTelCel, unmaskAll, calculaIdadeFromString
from util.popUps import popUpOkAlerta, popUpSimCancela
from util.enums.cadastroEnums import Status


class NewListaClientes(QFrame, Ui_wdgListaClientes):
    popupCNIS: NewPopupCNIS
    toast: QToaster
    menuFiltro: NewFiltroClientes
    filtros: dict

    def __init__(self, escritorio: Escritorios, advogado: Advogados, parent=None):
        super(NewListaClientes, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent
        self.popupCNIS = None
        self.escritorioAtual = escritorio
        self.advogadoAtual = advogado
        self.filtros = None
        self.menuFiltro = None

        self.sinais = Sinais()
        self.sinais.sEnviaClienteParam.connect(self.enviaClienteDashboard)
        self.sinais.sEnviaInfoCliente.connect(self.enviaInfoClienteDashboard)
        self.efeitos = Efeitos()

        self.toast = None

        self.tblClientes.hideColumn(0)
        self.tblClientes.hideColumn(8)
        self.installEventFilter(self)
        self.frInfoCliEncontrados.hide()

        self.pbNovoCliente.clicked.connect(self.abrirPopupCNIS)
        self.pbFiltro.clicked.connect(self.abreMenuFiltro)
        self.pbBusca.clicked.connect(self.avaliaFiltroTexto)
        self.tblClientes.doubleClicked.connect(self.selecionaCliente)
        self.leBusca.editingFinished.connect(self.avaliaFiltroTexto)

        # Tooltips
        self.setStyleSheet(styleTooltip())
        self.pbFiltro.setToolTip('Utilize filtros para pesquisas específicas.')

        self.atualizaTblClientes()

    def abreMenuFiltro(self):
        if self.menuFiltro is None:
            self.menuFiltro = NewFiltroClientes(parent=self, position=QCursor.pos(), filtros=self.filtros)
            Efeitos().shadowCards([self.menuFiltro])
            self.menuFiltro.raise_()
            self.menuFiltro.show()

    def abreMenuOpcoes(self):
        linhaSelecionada: int = self.tblClientes.selectedItems()[0].row()
        clienteId: int = int(self.tblClientes.item(linhaSelecionada, 0).text())

        menu = NewMenuOpcoes(
            parent=self,
            funcEditar=lambda: self.editarCliente(clienteId),
            funcArquivar=lambda: self.avaliaArquivarCliente(clienteId, linhaSelecionada),
            funcEntrevista=lambda: self.confirmaInicioEntrevista(clienteId),
            funcResumoCnis=lambda: self.navegaResumoCnis(clienteId),
        )
        menu.exec_(QCursor.pos())

    def atualizaTblClientes(self, arquivados: bool = False):
        if arquivados:
            clientesModels: list = Cliente.select().order_by(Cliente.nomeCliente)
        else:
            clientesModels: list = Cliente.select().where(Cliente.arquivado==False).order_by(Cliente.nomeCliente)

        self.tblClientes.setRowCount(0)
        self.tblClientes.setIconSize(QSize(8, 8))

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

            # 1 - icone arquivado <Aparente>
            if cliente.arquivado:
                iconItem = QTableWidgetItem()
                icone = QIcon(":/status/pink-circle.png")
                iconItem.setIcon(icone)
                iconItem.setTextAlignment(Qt.AlignRight)
                self.tblClientes.setItem(numLinha, 1, iconItem)
            else:
                iconItem = QTableWidgetItem()
                icone = QIcon(":/status/green-circle.png")
                iconItem.setIcon(icone)
                iconItem.setTextAlignment(Qt.AlignRight)
                self.tblClientes.setItem(numLinha, 1, iconItem)

            # 2 - Nome completo do cliente <Aparente>
            nomeCompletoItem = QTableWidgetItem(f"{cliente.nomeCliente} {cliente.sobrenomeCliente}")
            nomeCompletoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 2, nomeCompletoItem)

            # 3 - E-mail do cliente <Aparente>
            if cliente.email is None:
                emailItem = QTableWidgetItem('')
            else:
                emailItem = QTableWidgetItem(f"{cliente.email}")
            emailItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 3, emailItem)

            # 4 - Contato do cliente <Aparente>
            telefoneItem = QTableWidgetItem(f"{mascaraTelCel(telefone.numero)}")
            telefoneItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 4, telefoneItem)

            # 5 - Cidade de nascimento do cliente <Aparente>
            if cliente.cidade is None:
                cidadeItem = QTableWidgetItem('')
            else:
                cidadeItem = QTableWidgetItem(f"{cliente.cidade}")
            cidadeItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 5, cidadeItem)

            # 6 - Documentos <Aparente>
            docs = QTableWidgetItem('')
            self.tblClientes.setItem(numLinha, 6, docs)

            # 7 - Botão de edição <Aparente>
            pbOpcoes = QPushButton()
            pbOpcoes.clicked.connect(self.abreMenuOpcoes)
            pbOpcoes.setStyleSheet(btnOpcoesStyle())
            pbOpcoes.setMaximumSize(24, 24)
            self.tblClientes.setCellWidget(numLinha, 7, pbOpcoes)

            # 8 - Arquivado <Escondido>
            arquivado = QTableWidgetItem()
            arquivado.setFlags(Qt.ItemFlag.ItemIsUserCheckable)
            arquivado.setCheckState(cliente.arquivado)
            self.tblClientes.setItem(numLinha, 8, arquivado)

        self.tblClientes.resizeColumnsToContents()
        self.pbNovoCliente.setFocus()

    def abrirPopupCNIS(self):
        if self.popupCNIS is not None and self.popupCNIS.isVisible():
            self.popupCNIS.close()
            self.popupCNIS.setParent(None)

        self.popupCNIS = NewPopupCNIS(parent=self, dashboard=self.dashboard)
        Efeitos().shadowCards([self.popupCNIS])
        self.popupCNIS.raise_()
        self.popupCNIS.show()

        self.popupCNIS.setFocus()

    def arquivarCliente(self, clienteId: int):
        try:
            clienteAArquivar: Cliente = Cliente.get_by_id(clienteId)
            clienteAArquivar.arquivado = True
            clienteAArquivar.dataUltAlt = datetime.datetime.now()
            clienteAArquivar.save()
            return True
        except Cliente.DoesNotExist as err:
            print(f"{err=}")
            popUpOkAlerta("Não foi possível arquivar o cliente selecionado. Verifique se os dados estão corretos e tente novamente.", erro=err)
            return False

    def avaliaArquivarCliente(self, clienteId: int, linhaSelecionada: int):
        nomeCliente: str = self.tblClientes.item(linhaSelecionada, 1).text().upper()
        popUpSimCancela(f"Tem certeza que deseja arquivar o(a) cliente {nomeCliente} ?", funcaoSim=lambda: self.arquivarCliente(clienteId))
        self.atualizaTblClientes()
        return True

    def avaliaDadosFaltantesNoCNIS(self, cabecalhos: List[dict]) -> List[dict]:
        listaReturn: List[dict] = []

        for cabecalho in cabecalhos:
            faltaDataFim = cabecalho['dataFim'] is None or cabecalho['dataFim'] == ''
            faltaDataInicio = cabecalho['dataInicio'] is None or cabecalho['dataInicio'] == ''

            cabecalho['dadoFaltante'] = faltaDataFim or faltaDataInicio
            listaReturn.append(cabecalho)

        return listaReturn

    def avaliaFiltrosMenu(self, filtros: dict):
        self.menuFiltro = None
        self.filtros = filtros
        if filtros.keys():
            for chave, valor in filtros.items():

                if chave == 'arquivados':
                    self.atualizaTblClientes(arquivados=valor)
                    self.avaliaFiltroTexto()

    def avaliaFiltroTexto(self):
        strBusca: str = self.leBusca.text().strip()
        qtdLinhas = self.tblClientes.rowCount()
        qtdEncontrados: int = 0

        if strBusca == '':
            self.frInfoCliEncontrados.hide()
            for linha in range(qtdLinhas):
                self.tblClientes.showRow(linha)
            return True

        if len(strBusca) == 1:
            for linha in range(qtdLinhas):
                primeiraLetra = self.tblClientes.item(linha, 1).text()[0]
                if primeiraLetra.upper() == strBusca.upper():
                    qtdEncontrados += 1
                    self.tblClientes.showRow(linha)
                else:
                    self.tblClientes.hideRow(linha)

        else:
            for linha in range(qtdLinhas):
                nomeCompleto: str = self.tblClientes.item(linha, 1).text().upper()
                nomes: List[str] = nomeCompleto.split(' ')
                if strBusca.upper() in nomes:
                    qtdEncontrados += 1
                    self.tblClientes.showRow(linha)
                else:
                    self.tblClientes.hideRow(linha)

        self.lbInfoBusca.setText(f'{qtdEncontrados} clientes encontrados')
        self.frInfoCliEncontrados.show()

    def avaliaAtividadesPrincipais(self, clienteId: int):
        listaCabecalhos: List[CnisVinculos] = CnisVinculos.select().where(CnisVinculos.clienteId == clienteId)

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

    def buscaClienteEdicao(self, cpf: str):
        if cpf is not None and cpf != '':
            try:
                clienteAEditar: Cliente = Cliente.select().where(Cliente.cpfCliente==cpf).get()
                self.enviaClienteDashboard(clienteAEditar)
                return True
            except Cliente.DoesNotExist as err:
                print(f"buscaClienteEdicao: {err=}")
                popUpOkAlerta(f"Houve um erro ao busca cliente já cadastrado com o CPF: {cpf}. Tente novamente.", erro=err)
                return False

    def buscaTelefone(self, clienteAtual: Cliente) -> Telefones:
        try:
            return Telefones.select().where(Telefones.clienteId == clienteAtual.clienteId).get()
        except Telefones.DoesNotExist:
            return None

    def carregaCnis(self, pathCnis: str):
        cnisInseridoComSucesso: bool = False
        try:
            self.cnisClienteAtual: CNISModelo = CNISModelo(path=pathCnis)
            self.cnisClienteAtual.iniciaAvaliacaoCnis()
            infoPessoais: dict = self.cnisClienteAtual.getInfoPessoais()

            clienteCadastrado: Status = self.verificaCadastradoCliente(unmaskAll(infoPessoais['cpf']))

            if infoPessoais is not None and clienteCadastrado != Status.jaCadastrado:
                if clienteCadastrado in [Status.semCabecalho, Status.semContrib]:
                    clienteAtual: Cliente = Cliente.select().where(
                        Cliente.cpfCliente==unmaskAll(infoPessoais['cpf'])
                    ).get()
                else:
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

                    clienteAtual.telefoneId = self.buscaTelefone(clienteAtual)
                    clienteAtual.save()

                contribuicoes = self.cnisClienteAtual.getAllDict(toInsert=True, clienteId=clienteAtual.clienteId)
                cabecalho = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalho'])
                cabecalhoBeneficio = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalhoBeneficio'])

                CnisVinculos.insert_many(cabecalho).on_conflict_replace().execute()
                CnisVinculos.insert_many(cabecalhoBeneficio).on_conflict_replace().execute()

                self.cnisClienteAtual.insereItensContribuicao(clienteAtual)
                cnisInseridoComSucesso = True

            elif infoPessoais is not None:
                popUpSimCancela(
                    f"O(a) cliente {infoPessoais['nomeCompleto'].upper()} já está cadastrado(a). Deseja atualizar suas informações?",
                    titulo="Cliente já cadastrado(a)",
                    funcaoSim=lambda: self.buscaClienteEdicao(unmaskAll(infoPessoais['cpf']))
                )
                return False

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

    def confirmaInicioEntrevista(self, clienteId: int):
        clienteEscolhido: Cliente = Cliente.get_by_id(clienteId)

        popUpSimCancela(
            f"Deseja iniciar uma entrevista com o(a) cliente:\n\n{clienteEscolhido.nomeCliente} {clienteEscolhido.sobrenomeCliente}?",
            titulo="Iniciar entrevista",
            funcaoSim=lambda: self.dashboard.trocaTela(TelaAtual.Entrevista, clienteEscolhido)
        )
        return True

    def editarCliente(self, clienteId: int):
        try:
            clienteSelecionado: Cliente = Cliente.get_by_id(clienteId)
            self.sinais.sEnviaClienteParam.emit(clienteSelecionado)
        except Cliente.DoesNotExist as err:
            popUpOkAlerta(
                "Não foi possível carregar as informações do cliente selecionado. Tente novamente mais tarde.",
                erro=f"editarCliente: {err=}"
            )
            return False

    def enviaClienteDashboard(self, cliente: Cliente):
        self.dashboard.recebeCliente(cliente)

    def enviaInfoClienteDashboard(self, cliente: Cliente):
        self.dashboard.navegaInfoCliente(cliente)

    def eventFilter(self, a0: QObject, tecla: QEvent) -> bool:
        if isinstance(tecla, QKeyEvent) and self.popupCNIS is not None:
            if self.popupCNIS.isVisible():
                self.popupCNIS.close()

        return super(NewListaClientes, self).eventFilter(a0, tecla)

    def navegaResumoCnis(self, clienteId: int):
        clienteEscolhido: Cliente = Cliente.get_by_id(clienteId)
        self.dashboard.trocaTela(TelaAtual.Resumo, clienteEscolhido)

    def selecionaCliente(self, *args, **kwargs):
        linhaSelecionada = args[0].row()

        clienteId = self.tblClientes.item(linhaSelecionada, 0).text()
        clienteSelecionado: Cliente = Cliente.get_by_id(clienteId)

        self.sinais.sEnviaInfoCliente.emit(clienteSelecionado)

    def recebePathCnis(self, path: str):
        if path is None or path == '':
            clienteSemCnis: Cliente = Cliente()
            # clienteSemCnis.save()
            self.sinais.sEnviaClienteParam.emit(clienteSemCnis)
            return True
        elif os.path.isfile(path):
            self.carregaCnis(path)
            return True

        return False

    def toastCarregaCnis(self):
        self.toast = QToaster(None)
        self.toast.showMessage(self, "Analisando informações do CNIS...", corner=Qt.BottomLeftCorner)

    def verificaCadastradoCliente(self, cpf: str) -> Status:
        try:
            cliente: Cliente = Cliente.select().where(Cliente.cpfCliente==cpf).get()
            qtdItens: int = ItemContribuicao.select().where(ItemContribuicao.clienteId==cliente.clienteId).count()
            qtdCabecalhos: int = CnisVinculos.select().where(CnisVinculos.clienteId==cliente.clienteId).count()

            if qtdItens == 0:
                CnisVinculos.select().where(CnisVinculos.clienteId == cliente.clienteId).get()
                return Status.semContrib
            elif qtdCabecalhos == 0:
                ItemContribuicao.delete().where(ItemContribuicao.clienteId == cliente.clienteId).execute()
                return Status.semCabecalho
            return Status.jaCadastrado

        except Cliente.DoesNotExist as err:
            # TODO: ADICIONAR LOG
            print(f"verificaCadastradoCliente: {err=}")
            return Status.naoCadastrado
        except ItemContribuicao.DoesNotExist as err:
            # TODO: ADICIONAR LOG
            print(f"verificaCadastradoCliente: {err=}")
            CnisVinculos.select().where(CnisVinculos.clienteId == cliente.clienteId).get()
            return Status.semContrib
        except CnisVinculos.DoesNotExist as err:
            # TODO: ADICIONAR LOG
            print(f"verificaCadastradoCliente: {err=}")
            ItemContribuicao.delete().where(ItemContribuicao.clienteId==cliente.clienteId).execute()
            return Status.semCabecalho
        except Exception as err:
            # TODO: ADICIONAR LOG
            print(f"verificaClienteJaCadastrado: {err=}")
            return Status.erro


if __name__ == '__main__':
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = NewListaClientes()
    w.show()
    sys.exit(app.exec_())