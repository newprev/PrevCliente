from typing import List

from PyQt5.QtWidgets import QWidget
from Design.pyUi.newEntrevistaPrincipal import Ui_wdgEntrevistaPrincipal

from modelos.escritoriosORM import Escritorios
from modelos.processosORM import Processos
from modelos.tipoBeneficioORM import TipoBeneficioModel

from Design.CustomWidgets.newCardPadrao import NewCardPadrao
from sinaisCustomizados import Sinais
from util.enums.dashboardEnums import TelaPosicao
from util.enums.entrevistaEnums import EtapaEntrevista
from util.enums.processoEnums import NaturezaProcesso, TipoBeneficioEnum
from util.helpers import strTipoBeneFacilitado
from util.popUps import popUpSimCancela


class NewEntrevistaPrincipal(QWidget, Ui_wdgEntrevistaPrincipal):
    escritorio: Escritorios
    processoAtual: Processos
    etapaAtual: EtapaEntrevista
    listaBeneficios: List[TipoBeneficioModel]

    def __init__(self, escritorioAtual: Escritorios, parent=None):
        super(NewEntrevistaPrincipal, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent
        self.escritorio = escritorioAtual
        self.etapaAtual = EtapaEntrevista.naturezaProcesso
        self.sinais = Sinais()
        self.sinais.sTrocaWidgetCentral.connect(self.voltarDashboard)
        self.processoAtual = Processos()
        self.listaBeneficios = []

        self.carregaTiposBeneficio()
        self.iniciaNatureza()
        self.iniciaBeneficio()
        self.iniciaHistorico()

        self.pbVoltar.clicked.connect(self.avaliarVoltar)

    def avaliarVoltar(self):
        if self.etapaAtual == EtapaEntrevista.naturezaProcesso:
            popUpSimCancela('Deseja deixar a entrevista?\nTodas as informações serão perdidas.', funcao=self.sairEntrevista)
        elif self.etapaAtual == EtapaEntrevista.tipoBeneficio:
            self.frTpBeneficioHist.hide()
            self.lbTpBeneEscolhido.setText('')
            self.trocaEtapa(EtapaEntrevista.naturezaProcesso)

    def atualizaDescricaoNatureza(self, tipo: NaturezaProcesso):
        if tipo == NaturezaProcesso.administrativo:
            self.lbTituloNatureza.setText('ADMINISTRATIVO')
            self.lbDescNatureza.setText("""
            O processo administrativo consiste na sequência de atividades realizadas pela Administração Pública com o objetivo final de dar efeito a algo previsto em lei. O processo administrativo é regulado pela Lei nº 9.784/99, chamada de Lei de Processo Administrativo (LPA).
            O processo administrativo são as atividades da Administração Pública que tem como objetivo alcançar fins específicos previstos em lei.
            Sem o processo administrativo, as ações do Estado não seriam regulares, uniformes e baseados em princípios legais que as dão sustentação.
            Dessa forma, pode-se afirmar que o processo administrativo é um dos principais fundamentos para que o Estado aja conforme a lei e que aplique os seus esforços para consolidar as mesmas.""")
        else:
            self.lbTituloNatureza.setText('JUDICIAL')
            self.lbDescNatureza.setText("""
            De maneira geral, um processo jurídico é o pedido do autor (pessoa física ou jurídica) para a resolução de um conflito. Para isso, ele bate às portas do Poder Judiciário a espera que o Estado, na figura de um juiz, decida sobre a suposta violação de direitos. Podemos também definir o processo judicial como o instrumento legal que pretende eliminar conflitos entre os sujeitos envolvidos, através da aplicação da lei em relação aos fatos apresentados neste processo.
            Cabe destacar, desde logo, que uma ação judicial é diferente de um processo administrativo ou até de um processo criminal. O processo administrativo é um procedimento interno, normalmente desenvolvido dentro de órgãos ligados ao Poder Executivo e são julgado por Tribunais Administrativos. Já o processo criminal, é um processo judicial que discute a responsabilidade penal de um ato através de uma acusação e tem um rito diferente do cível.""")

    def atualizaDescricaoBeneficio(self, tipo: TipoBeneficioEnum):
        beneficio: TipoBeneficioModel = self.listaBeneficios[tipo.value]

        self.lbTituloTpBeneficio.setText(strTipoBeneFacilitado(tipo).upper())
        self.lbDescTpBeneficio.setText(beneficio.descricao)

    def atualizaTipoBeneficio(self, tipo: TipoBeneficioEnum):
        self.lbTpBeneEscolhido.setText(strTipoBeneFacilitado(tipo))
        self.frTpBeneficioHist.show()
        self.processoAtual.tipoBeneficioEnum = tipo.value

    def atualizaNaturezaProcesso(self, natureza: NaturezaProcesso):
        if natureza == NaturezaProcesso.administrativo:
            self.lbNaturezaEscolhida.setText("Administrativo")
        else:
            self.lbNaturezaEscolhida.setText("Judicial")

        self.processoAtual.natureza = natureza.value
        self.trocaEtapa(EtapaEntrevista.tipoBeneficio)
        self.clearFocus()

    def carregaTiposBeneficio(self):
        self.listaBeneficios = TipoBeneficioModel.select()

    def iniciaBeneficio(self):
        pbAposentadoria = NewCardPadrao(
            TipoBeneficioEnum.Aposentadoria,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.Aposentadoria),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.Aposentadoria),
        )
        pbAuxDoenca = NewCardPadrao(
            TipoBeneficioEnum.AuxDoenca,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.AuxDoenca),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.AuxDoenca),
        )
        pbAuxAcidente = NewCardPadrao(
            TipoBeneficioEnum.AuxAcidente,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.AuxAcidente),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.AuxAcidente),
        )
        pbAuxReclusao = NewCardPadrao(
            TipoBeneficioEnum.AuxReclusao,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.AuxReclusao),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.AuxReclusao),
        )
        pbBeneIdoso = NewCardPadrao(
            TipoBeneficioEnum.BeneIdoso,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.BeneIdoso),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.BeneIdoso),
        )
        pbBeneDeficiente = NewCardPadrao(
            TipoBeneficioEnum.BeneDeficiencia,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.BeneDeficiencia),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.BeneDeficiencia),
        )
        pbSalMaternidade = NewCardPadrao(
            TipoBeneficioEnum.SalMaternidade,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.SalMaternidade),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.SalMaternidade),
        )
        pbPensaoMorte = NewCardPadrao(
            TipoBeneficioEnum.PensaoMorte,
            parent=self,
            onHover=lambda: self.atualizaDescricaoBeneficio(TipoBeneficioEnum.PensaoMorte),
            onClick=lambda: self.atualizaTipoBeneficio(TipoBeneficioEnum.PensaoMorte),
        )

        self.vlTpBeneficio.addWidget(pbAposentadoria)
        self.vlTpBeneficio.addWidget(pbAuxDoenca)
        self.vlTpBeneficio.addWidget(pbAuxAcidente)
        self.vlTpBeneficio.addWidget(pbAuxReclusao)
        self.vlTpBeneficio.addWidget(pbBeneIdoso)
        self.vlTpBeneficio.addWidget(pbBeneDeficiente)
        self.vlTpBeneficio.addWidget(pbPensaoMorte)
        self.vlTpBeneficio.addWidget(pbSalMaternidade)

    def iniciaHistorico(self):
        self.lbNaturezaEscolhida.setText('')
        self.frTpBeneficioHist.hide()
        self.frTpProcessoHist.hide()
        self.frEntrevistaHist.hide()

    def iniciaNatureza(self):
        self.lbTituloNatureza.setText('')
        self.lbDescNatureza.setText('')

        pbAdm = NewCardPadrao(
            NaturezaProcesso.administrativo,
            parent=self,
            onHover=lambda: self.atualizaDescricaoNatureza(NaturezaProcesso.administrativo),
            onClick=lambda: self.atualizaNaturezaProcesso(NaturezaProcesso.administrativo),
        )
        pbJud = NewCardPadrao(
            NaturezaProcesso.judicial,
            parent=self,
            onHover=lambda: self.atualizaDescricaoNatureza(NaturezaProcesso.judicial),
            onClick=lambda: self.atualizaNaturezaProcesso(NaturezaProcesso.judicial),
        )

        self.vlNaturezas.addWidget(pbAdm)
        self.vlNaturezas.addWidget(pbJud)

    def sairEntrevista(self):
        self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Cliente)

    def trocaEtapa(self, etapaDestino: EtapaEntrevista):
        self.etapaAtual = etapaDestino
        self.stkEntrevista.setCurrentIndex(etapaDestino.value)

    def voltarDashboard(self):
        self.processoAtual.delete().execute()
        self.dashboard.trocaTela(TelaPosicao.Cliente)


if __name__ == '__main__':
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = NewEntrevistaPrincipal()
    w.show()
    sys.exit(app.exec_())
