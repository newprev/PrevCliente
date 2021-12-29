import os
from timeit import Timer

from peewee import SqliteDatabase
from typing import List

from PyQt5.QtCore import QObject, QEvent, Qt
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtWidgets import QFrame, QTableWidgetItem

from Design.pyUi.newListaClientes import Ui_wdgListaClientes
from Design.CustomWidgets.newPopupCNIS import NewPopupCNIS
from Design.CustomWidgets.newToast import QToaster
from Design.pyUi.efeitos import Efeitos

from modelos.cabecalhoORM import CnisCabecalhos

from modelos.clienteORM import Cliente
from modelos.cnisModelo import CNISModelo
from modelos.escritoriosORM import Escritorios
from modelos.itemContribuicao import ItemContribuicao
from modelos.processosORM import Processos
from modelos.telefonesORM import Telefones
from modelos.advogadoORM import Advogados
from sinaisCustomizados import Sinais
from util.dateHelper import strToDate, atividadesConcorrentes, atividadeSecundaria

from util.helpers import mascaraTelCel, strTipoBeneficio, unmaskAll, calculaIdadeFromString
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
        self.toast = QToaster(parent=self)

        self.tblClientes.hideColumn(0)
        self.installEventFilter(self)

        self.pbNovoCliente.clicked.connect(self.abrirPopupCNIS)
        self.tblClientes.doubleClicked.connect(self.selecionaCliente)

        self.atualizaTblClientes()

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

            cdClienteItem = QTableWidgetItem(str(cliente.clienteId))
            cdClienteItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 0, cdClienteItem)

            nomeCompletoItem = QTableWidgetItem(f"{cliente.nomeCliente} {cliente.sobrenomeCliente}")
            nomeCompletoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 1, nomeCompletoItem)

            if cliente.email is None:
                emailItem = QTableWidgetItem('')
            else:
                emailItem = QTableWidgetItem(f"{cliente.email}")
            emailItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 2, emailItem)

            telefoneItem = QTableWidgetItem(f"{mascaraTelCel(telefone.numero)}")
            telefoneItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 3, telefoneItem)

            if cliente.cidade is None:
                cidadeItem = QTableWidgetItem('')
            else:
                cidadeItem = QTableWidgetItem(f"{cliente.cidade}")
            cidadeItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 4, cidadeItem)

            tipoProcessoItem = QTableWidgetItem(strTipoBeneficio(processo.tipoBeneficio, processo.subTipoApos))
            tipoProcessoItem.setFont(QFont('TeX Gyre Adventor', pointSize=12, italic=True, weight=25))
            self.tblClientes.setItem(numLinha, 5, tipoProcessoItem)

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
        
        clienteAtual = Cliente()

        try:
            infoPessoais: dict = self.cnisClienteAtual.getInfoPessoais()

            if infoPessoais is not None:
                clienteAInserir = Cliente()

                clienteAInserir.cpfCliente = unmaskAll(infoPessoais['cpf'])
                clienteAInserir.dataNascimento = strToDate(infoPessoais['dataNascimento'])
                clienteAInserir.idade = calculaIdadeFromString(infoPessoais['dataNascimento'])
                clienteAInserir.nit = unmaskAll(infoPessoais['nit'])
                clienteAInserir.nomeMae = infoPessoais['nomeMae'].title()
                clienteAInserir.nomeCliente = infoPessoais['nomeCompleto'].split(' ')[0].title()
                clienteAInserir.sobrenomeCliente = ' '.join(infoPessoais['nomeCompleto'].split(' ')[1:]).title()
                clienteAInserir.escritorioId = Escritorios.select().where(Escritorios.escritorioId == self.escritorioAtual.escritorioId)

                with db.atomic() as transaction:
                    try:
                        Cliente.insert(**clienteAInserir.toDict()).on_conflict_replace().execute()
                        clienteAtual: Cliente = Cliente.get(Cliente.cpfCliente == clienteAInserir.cpfCliente)
                        clienteAtual.pathCnis = pathCnis

                        contribuicoes = self.cnisClienteAtual.getAllDict(toInsert=True, clienteId=clienteAtual.clienteId)
                        cabecalho = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalho'])
                        cabecalhoBeneficio = self.avaliaDadosFaltantesNoCNIS(contribuicoes['cabecalhoBeneficio'])

                        CnisCabecalhos.insert_many(cabecalho).on_conflict_replace().execute()
                        CnisCabecalhos.insert_many(cabecalhoBeneficio).on_conflict_replace().execute()

                        clienteAtual.telefoneId = Telefones.get_by_id(clienteAtual)
                        transaction.commit()
                        cnisInseridoComSucesso = True
                    except Cliente.DoesNotExist:
                        self.showPopupAlerta('Erro ao inserir cliente.')
                        transaction.rollback()
                        return False
                    except Telefones.DoesNotExist:
                        clienteAtual.telefoneId = Telefones()
                        transaction.commit()
                        cnisInseridoComSucesso = True
                    except Exception as err:
                        erro = f"carregaCnis: ({type(err)}) {err}"
                        transaction.rollback()
                        popUpOkAlerta('Erro ao inserir cliente.', erro=erro)
                        return False

            self.cnisClienteAtual.insereItensContribuicao(clienteAtual)

        except Exception as err:
            popUpOkAlerta('Não foi possível salvar o cliente. Tente novamente.', erro=str(err))
            print(f'carregaCnis - erro: ({type(err)}) {err}')

        if cnisInseridoComSucesso:
            self.avaliaAtividadesPrincipais(clienteAtual.clienteId)

        self.sinais.sEnviaClienteParam.emit(clienteAtual)

    def eventFilter(self, a0: QObject, tecla: QEvent) -> bool:
        if isinstance(tecla, QKeyEvent):
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