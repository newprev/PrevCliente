from PyQt5.QtWidgets import QWidget
from Design.pyUi.itemResumoCNIS import Ui_WdgItemRes
from Design.efeitos import Efeitos
from heart.resumoCnis.localStyleSheet.resumoCnis import backgroundAlerta

from modelos.vinculoORM import CnisVinculos
from modelos.itemContribuicao import ItemContribuicao
from Design.CustomWidgets.newToast import QToaster

from sinaisCustomizados import Sinais
from util.helpers.dateHelper import mascaraData
from util.helpers.helpers import mascaraCNPJ
from util.popUps import popUpSimCancela


class ItemResumoCnis(QWidget, Ui_WdgItemRes):
    vinculoAtual: CnisVinculos
    selecionado: bool = False
    dadoFaltante: bool = False
    insalubridade: bool = False
    toasty: QToaster

    def __init__(self, cabecalhoCnis: CnisVinculos, parent=None):
        super(ItemResumoCnis, self).__init__(parent=parent)
        self.setupUi(self)
        self.resumoPage = parent

        self.vinculoAtual = cabecalhoCnis
        self.efeito = Efeitos()
        self.carregaCabecalho()
        self.sinais = Sinais()
        self.sinais.sAtualizaVinculo.connect(self.enviaCabecalho)
        self.sinais.sDeletaVinculo.connect(self.atualizarCabecalhos)
        self.sinais.sEditaVinculo.connect(self.enviaParaEdicao)
        self.toasty = None

        self.mouseDoubleClickEvent = lambda _: self.cabecalhoselecionado()
        self.pbRemover.clicked.connect(self.avaliaDeletarResumo)
        self.pbEditar.clicked.connect(self.avaliaEnviaParaEdicao)

        self.efeito.shadowCards([self.frEdicao], radius=40, color=(63, 63, 63, 30), offset=(-1, 1))
        self.efeito.shadowCards([self.frDadoFaltante], radius=40, color=(63, 63, 63, 30), offset=(-1, 1))

    def atualizarCabecalhos(self):
        self.resumoPage.atualizarVinculos()

    def avaliaEnviaParaEdicao(self):
        if self.vinculoAtual is not None:
            self.sinais.sEditaVinculo.emit()

    def avaliaDeletarResumo(self):
        nomeVinculo = self.vinculoAtual.nomeEmp if self.vinculoAtual.nb is None else self.vinculoAtual.especie[5:]
        popUpSimCancela(
            f"Realmente deseja deletar o vínculo {nomeVinculo} e todas as suas competências?",
            funcaoSim=self.deletarVinculo
        )

    def carregaCabecalho(self):
        # Nome da empresa ou do benefícios
        if self.vinculoAtual.especie is not None:
            self.lbCdEmp.setText(f"{self.vinculoAtual.seq} - {self.vinculoAtual.especie[5:]}")
            self.lbCNPJouNB.setText(f"Núm. Benefício: {self.vinculoAtual.nb}")
        else:
            self.lbCdEmp.setText(f"{self.vinculoAtual.seq} - {self.vinculoAtual.nomeEmp}")
            self.lbCNPJouNB.setText("CNPJ: " + mascaraCNPJ(self.vinculoAtual.cdEmp))

        # Data de início
        if self.vinculoAtual.dataInicio is not None and len(self.vinculoAtual.dataInicio) > 0:
            self.lbDataInicio.setText(mascaraData(self.vinculoAtual.dataInicio))
        else:
            self.lbDataInicio.setText('')

        # Data de fim
        if self.vinculoAtual.dataFim is not None and len(self.vinculoAtual.dataFim) > 0:
            self.lbDataFim.setText(mascaraData(self.vinculoAtual.dataFim))
        else:
            self.lbDataFim.setText('')

        # Situação do benefício
        if self.vinculoAtual.situacao is not None and len(self.vinculoAtual.situacao) > 0:
            self.lbSituacao.setText(self.vinculoAtual.situacao)
        else:
            self.lbSituacao.setText("")
            self.lbInfoSituacao.setText("")

        # Dado faltante
        if self.vinculoAtual.dadoFaltante:
            if (self.vinculoAtual.dataInicio is None or self.vinculoAtual.dataInicio == '') and (self.vinculoAtual.dataFim is not None and self.vinculoAtual.dataFim != ''):
                self.frFaltaData.setToolTip("A data início deste vículo não foi encontrada. Sem essa informação, não é possível fazer o cálculo do tempo de contribuição.")

            elif (self.vinculoAtual.dataFim is None or self.vinculoAtual.dataFim == '') and (self.vinculoAtual.dataInicio is not None and self.vinculoAtual.dataInicio != ''):
                self.frFaltaData.setToolTip("A data fim deste vículo não foi encontrada. Sem essa informação, não é possível fazer o cálculo do tempo de contribuição.")

            else:
                self.frFaltaData.setToolTip("As datas início e fim deste vículo não foram encontradas. Sem essas informações, não é possível fazer o cálculo do tempo de contribuição.")

            self.frFaltaData.show()
            self.dadoFaltante = True
        else:
            self.frFaltaData.hide()

        # Insalubridade
        qtdInsalubridade = ItemContribuicao.select().where(
            ItemContribuicao.clienteId == self.vinculoAtual.clienteId,
            ItemContribuicao.seq == self.vinculoAtual.seq,
            ItemContribuicao.fatorInsalubridade.is_null(False)
        ).count()

        if qtdInsalubridade > 0:
            self.insalubridade = True
            self.frInsalubridade.show()
            self.frInsalubridade.setToolTip(f'Esse vínculo possui {qtdInsalubridade} competências com labor insalubre.')
        else:
            self.frInsalubridade.hide()

        if not self.vinculoAtual.dadoFaltante and qtdInsalubridade == 0:
            self.frDadoFaltante.hide()
        elif (not self.vinculoAtual.dadoFaltante and qtdInsalubridade > 0) or (self.vinculoAtual.dadoFaltante and qtdInsalubridade == 0):
            self.lineDadoFaltante.hide()

    def cabecalhoselecionado(self):
        self.selecionado = not self.selecionado

        if self.selecionado:
            Efeitos().shadowCards([self])
            self.sinais.sAtualizaVinculo.emit()
        else:
            Efeitos().desativarSombra([self])

    def deletarVinculo(self):
        try:
            qtdeCompetencias: int = ItemContribuicao.select().where(
                ItemContribuicao.clienteId == self.vinculoAtual.clienteId,
                ItemContribuicao.seq == self.vinculoAtual.seq,
            ).count()

            ItemContribuicao.delete().where(
                ItemContribuicao.clienteId == self.vinculoAtual.clienteId,
                ItemContribuicao.seq == self.vinculoAtual.seq,
            ).execute()
            CnisVinculos.delete_by_id(self.vinculoAtual.vinculoId)
            self.sinais.sDeletaVinculo.emit()
            if self.toasty is None:
                self.toasty = QToaster(self)
                self.toasty.showMessage(self, f"O vínculo e {qtdeCompetencias} competências foram excluídas com sucesso.")
        except Exception as err:
            print(f"deletarVinculo: Não foi possível deletar os itens e o resumoCnis:: {err=}")
            if self.toasty is None:
                self.toasty = QToaster(self)
            self.toasty.showMessage(self, f"Houve um erro e não foi possível excluir os itens e o vínculo.")

    def desselecionaCabecalho(self):
        Efeitos().desativarSombra([self])
        self.selecionado = False

    def enviaCabecalho(self):
        self.resumoPage.recebeVinculoSelecionado(self.vinculoAtual)

    def enviaParaEdicao(self):
        self.resumoPage.vinculoParaEdicao(self.vinculoAtual)
