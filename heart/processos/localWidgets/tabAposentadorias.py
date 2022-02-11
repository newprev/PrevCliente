from PyQt5.QtWidgets import QWidget
from Design.pyUi.tabAposentadorias import Ui_wdgTabAposentadorias
from typing import List, Tuple

from modelos.aposentadoriaORM import Aposentadoria
from modelos.clienteORM import Cliente

from heart.processos.localWidgets.cardAposentadoria import CardAposentadoria

from Design.pyUi.efeitos import Efeitos

from util.helpers import calculaCoordenadas


class TabAposentariasController(QWidget, Ui_wdgTabAposentadorias):
    listaTemDireito: List[Aposentadoria]
    listaNaoTemDireito: List[Aposentadoria]
    clienteAtual: Cliente
    aposentadoriaEscolhida: Aposentadoria

    def __init__(self, clienteEnviado: Cliente = None, aposTemDireito: List[Aposentadoria] = None, aposNaoTemDireito: List[Aposentadoria] = None,  parent=None):
        super(TabAposentariasController, self).__init__(parent=parent)
        self.setupUi(self)

        self.clienteAtual = clienteEnviado
        self.listaTemDireito = aposTemDireito
        self.listaNaoTemDireito = aposNaoTemDireito

        self.iniciaGrids()

    def recebeProcessoId(self, processoId: int, clienteId: int):
        self.listaTemDireito = Aposentadoria.select().where(
            Aposentadoria.clienteId == clienteId,
            Aposentadoria.processoId == processoId,
            Aposentadoria.possuiDireito == True
        ).order_by(
            Aposentadoria.idadeCliente,
            Aposentadoria.valorBeneficio
        )

        self.listaNaoTemDireito = Aposentadoria.select().where(
            Aposentadoria.clienteId == clienteId,
            Aposentadoria.processoId == processoId,
            Aposentadoria.possuiDireito == False
        )
        self.atualizaGrids()

    def iniciaGrids(self):
        self.limpaLayout()
        if self.listaTemDireito is None or self.listaNaoTemDireito is None:
            return False
        elif len(self.listaTemDireito) > 0 or len(self.listaNaoTemDireito) > 0:
            self.atualizaGrids()

    def atualizaGrids(self):
        # Atualiza grid do tab "Tem direito"
        coordenadas: List[Tuple] = calculaCoordenadas(len(self.listaTemDireito), 2)
        efeitos = Efeitos()
        for numItem, apos in enumerate(self.listaTemDireito):
            aposentadoriaSelecionada = numItem == 0
            card = CardAposentadoria(apos, parent=self, aposSelecionada=aposentadoriaSelecionada)
            if aposentadoriaSelecionada:
                self.aposentadoriaEscolhida = apos
                efeitos.shadowCards([card], color=(41, 45, 64, 180), offset=(5, 7))
            else:
                efeitos.shadowCards([card], color=(82, 85, 90, 100))
            self.glTemDireito.addWidget(card, coordenadas[numItem][0], coordenadas[numItem][1])

        # Atualiza grid do tab "Nao tem direito"
        coordenadas = calculaCoordenadas(len(self.listaNaoTemDireito), 2)
        for numItem, apos in enumerate(self.listaNaoTemDireito):
            card = CardAposentadoria(apos, parent=self)
            efeitos.shadowCards([card])
            self.glNaoTemDireito.addWidget(card, coordenadas[numItem][0], coordenadas[numItem][1])

    def limpaLayout(self):
        for index in reversed(range(self.glNaoTemDireito.count())):
            self.glNaoTemDireito.takeAt(index).widget().setParent(None)

        for index in reversed(range(self.glTemDireito.count())):
            self.glTemDireito.takeAt(index).widget().setParent(None)
