from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from typing import List

from sinaisCustomizados import Sinais
from Design.pyUi.buscaProcessos import Ui_mwBuscaProcessos
from Design.pyUi.efeitos import Efeitos
from util.helpers import mascaraTelCel, strTipoProcesso, strTipoBeneficio, dataUSAtoBR
from modelos.clienteORM import Cliente
from modelos.telefonesORM import Telefones
from modelos.processosORM import Processos
from util.popUps import popUpOkAlerta


class BuscaProcessosPage(QMainWindow, Ui_mwBuscaProcessos):
    clienteAtual: Cliente
    listaProcessos: List[Processos]
    processoIdSelecionado: int

    def __init__(self, cliente: Cliente, parent=None):
        super(BuscaProcessosPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.clienteAtual = cliente
        self.listaProcessos = []
        self.parent = parent
        self.efeitos = Efeitos()
        self.efeitos.shadowCards([self.frInfoCliente],
            radius=8,
            offset=(0, 6),
            color=(63, 63, 63, 90),
        )
        self.sinais = Sinais()

        self.tblListaProcessos.hideColumn(0)
        self.atualizaInfoTela()
        self.pbSeleciona.clicked.connect(self.avaliaSelecao)
        self.sinais.sEnviaProcesso.connect(self.enviaProcesso)
        self.tblListaProcessos.doubleClicked.connect(self.processoSelecionado)

    def atualizaInfoTela(self):
        if self.clienteAtual is None:
            popUpOkAlerta(
                'Algum erro aconteceu ao tentar abrir a tela de busca de processos. Entre em contato com o suporte.',
                erro='atualizaInfoTela <BuscaProcessosPage>',
                funcao=self.close,
            )
        else:
            self.listaProcessos = Processos.select().where(Processos.clienteId == self.clienteAtual.clienteId)
            telefone: Telefones = Telefones.select().where(Telefones.clienteId == self.clienteAtual).limit(1).get()
            self.lbNomeCompleto.setText(self.clienteAtual.nomeCliente.strip() + ' ' + self.clienteAtual.sobrenomeCliente.strip())
            self.lbEmail.setText(self.clienteAtual.email)
            self.lbTelefone.setText(mascaraTelCel(telefone.numero))

            self.atualizaTabela(self.listaProcessos)

    def atualizaTabela(self, listaProcessos: List[Processos] = None):
        if listaProcessos is None:
            listaAtual = self.listaProcessos
        else:
            listaAtual = listaProcessos

        self.tblListaProcessos.setRowCount(0)

        for linha, processo in enumerate(listaAtual):
            self.tblListaProcessos.insertRow(linha)

            # 0 - Código do processo - processoId<inativo>
            processoIdItem = QTableWidgetItem(str(processo.processoId))
            processoIdItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
            processoIdItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblListaProcessos.setItem(linha, 0, processoIdItem)

            # 1 - Tipo do processo - tipoProcesso<ativo>
            tipoProcessoItem = QTableWidgetItem(strTipoProcesso(processo.tipoProcesso))
            tipoProcessoItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
            tipoProcessoItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblListaProcessos.setItem(linha, 1, tipoProcessoItem)

            # 2 - Tipo do processo - tipoBenefício<ativo>
            tipoBeneficioItem = QTableWidgetItem(strTipoBeneficio(processo.tipoBeneficio, processo.subTipoApos))
            tipoBeneficioItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
            tipoBeneficioItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblListaProcessos.setItem(linha, 2, tipoBeneficioItem)

            # 3 - DER - der<ativo>
            derItem = QTableWidgetItem(dataUSAtoBR(processo.der, comDias=True))
            derItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
            derItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblListaProcessos.setItem(linha, 3, derItem)

            # 4 - Última atualização - der<ativo>
            dataUltAltItem = QTableWidgetItem(dataUSAtoBR(processo.dataUltAlt, comDias=True))
            dataUltAltItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
            dataUltAltItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tblListaProcessos.setItem(linha, 4, dataUltAltItem)

        self.tblListaProcessos.resizeColumnsToContents()

    def processoSelecionado(self, *args):
        self.processoIdSelecionado = int(self.tblListaProcessos.item(args[0].row(), 0).text())
        self.sinais.sEnviaProcesso.emit()

    def avaliaSelecao(self):
        linhaSelecionada: bool = False
        for linha in range(self.tblListaProcessos.rowCount()):
            if self.tblListaProcessos.item(linha, 0).isSelected():
                self.processoIdSelecionado = self.tblListaProcessos.item(linha, 0).text()
                linhaSelecionada = True
                break

        if linhaSelecionada:
            self.sinais.sEnviaProcesso.emit()

    def enviaProcesso(self):
        self.parent.recebeProcesso(self.processoIdSelecionado)
        self.close()



