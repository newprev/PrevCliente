import datetime
from logging import Logger
from typing import List

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QGridLayout

from Design.pyUi.newEntrevistaPrincipal import Ui_wdgEntrevistaPrincipal
from Design.CustomWidgets.newCardPadrao import NewCardPadrao
from Design.CustomWidgets.newToast import QToaster
from Design.CustomWidgets.wdgCheckInfoController import WdgCheckInfo
from Design.CustomWidgets.newModalEntrevista import ModalEntrevistaController
from Design.CustomWidgets.newCardAposentadoria import NewCardAposentadoria
from Design.efeitos import Efeitos

from beneficios.aposentadoria import CalculosAposentadoria
from heart.dashboard.entrevista.localStyleSheet.lateral import iconeInfoCliente
from heart.newEntrevista.localWidgets.pgConfigSimulacao import PgConfigSimulacao
from modelos.Auxiliares.tipoInfo import InformacaoModel
from modelos.incidenteProcessual import IncidenteProcessual
from systemLog.logs import NewLogging
from util.enums.aposentadoriaEnums import ContribSimulacao, IndiceReajuste
from util.helpers.layoutHelpers import limpaLayout

from .localStyleSheet.principal import styleEtapaEntrevista

from modelos.escritoriosORM import Escritorios
from modelos.processosORM import Processos
from modelos.tipoBeneficioORM import TipoBeneficioModel
from modelos.clienteORM import Cliente
from modelos.advogadoORM import Advogados
from modelos.aposentadoriaORM import Aposentadoria

from cache.cachingLogin import CacheLogin

from sinaisCustomizados import Sinais

from util.helpers.dateHelper import calculaIdade, mascaraData, strToDate
from util.enums.dashboardEnums import TelaPosicao
from util.enums.entrevistaEnums import EtapaEntrevista, CategoriaQuiz
from util.enums.processoEnums import NaturezaProcesso, TipoBeneficioEnum, TipoProcesso, SituacaoProcesso
from util.helpers.helpers import strTipoBeneFacilitado, strTipoProcesso, mascaraCPF
from util.popUps import popUpSimCancela, popUpOkAlerta


class NewEntrevistaPrincipal(QWidget, Ui_wdgEntrevistaPrincipal):
    escritorio: Escritorios
    processoAtual: Processos
    etapaAtual: EtapaEntrevista
    listaBeneficios: List[TipoBeneficioModel]
    clienteAtual: Cliente
    advogadoAtual: Advogados
    toasty: QToaster
    entrevistaParams: dict = {
        'contribSimulacao': ContribSimulacao.ULTI,
        'valorSimulacao': 0.0,
        'porcentagemCont': 11,
        'indiceReajuste': IndiceReajuste.Ipca
    }
    aposentadoriaModel: CalculosAposentadoria
    apiLog: Logger
    salvandoSimulacao: bool = False

    def __init__(self, escritorioAtual: Escritorios = None, cliente: Cliente = None, parent=None):
        super(NewEntrevistaPrincipal, self).__init__(parent=parent)
        self.setupUi(self)
        self.dashboard = parent
        self.escritorio = escritorioAtual
        self.etapaAtual = EtapaEntrevista.naturezaProcesso
        self.toasty = None
        self.sinais = Sinais()
        self.sinais.sTrocaWidgetCentral.connect(self.voltarDashboard)
        self.processoAtual = Processos()
        self.clienteAtual = cliente
        self.listaBeneficios = []
        self.aposentadoriaModel = CalculosAposentadoria(None, None, None)

        self.newLog = NewLogging()
        self.apiLog = self.newLog.buscaLogger()

        self.iniciaQuiz()
        self.buscaAdvogadoAtual()
        self.carregaTiposBeneficio()
        self.iniciaInfoPessoais()
        self.iniciaNatureza()
        self.iniciaBeneficio()
        self.iniciaTpProcesso()
        self.iniciaHistorico()
        self.trocaEtapa(self.etapaAtual)

        self.pbVoltar.clicked.connect(self.avaliarVoltar)
        self.pbFinalizarEntrevista.clicked.connect(self.avaliaFinalizaEntrevista)
        self.pbConfigSimulacao.clicked.connect(self.abreConfig)
        self.pbInfoCliente.clicked.connect(self.avaliaMostraInfoLateral)
        self.pbSalvarSimulacao.clicked.connect(self.salvarSimulacao)
        self.pbCancelarSimulacao.clicked.connect(self.avaliaCancelaSimulacao)

    def abreConfig(self):
        configPage = PgConfigSimulacao(parent=self, entrevistaParams=self.entrevistaParams)
        configPage.raise_()
        configPage.show()

    def atualizaDescricaoBeneficio(self, tipo: TipoBeneficioEnum):
        beneficio: TipoBeneficioModel = self.listaBeneficios[tipo.value]

        self.lbTituloTpBeneficio.setText(strTipoBeneFacilitado(tipo).upper())
        self.lbDescTpBeneficio.setText(beneficio.descricao)

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

    def atualizaDescricaoTpProcesso(self, tipo: TipoProcesso):
        self.lbTituloTpProcesso.setText(strTipoProcesso(tipo))

        if tipo == TipoProcesso.Concessao:
            self.lbDescTpProcesso.setText("A concessão é a permissão para realizar alguma coisa. É a cessão voluntária de algum direito. Em sentido estrito, é a concessão pelo estado de algum serviço público a uma empresa privada")
        elif tipo == TipoProcesso.Revisao:
            self.lbDescTpProcesso.setText("A Revisão de Benefícios tem como objetivo fazer uma reanálise do benefício que está sendo pago por você. Geralmente isso é feito quando você ou o INSS percebe que houve alguma falha na hora de ser concedido o benefício previdenciário.")
        elif tipo == TipoProcesso.RecOrdinario:
            self.lbDescTpProcesso.setText("O recurso INSS é uma maneira de recorrer de uma decisão com a qual não se concorda, solicitando uma revisão da deliberação apresentada. Quando se trata de benefícios previdenciários, o recurso é usado como forma de pedir uma nova avaliação em relação a algum requerimento inicial feito ao INSS.")
        elif tipo == TipoProcesso.RecEspecial:
            self.lbDescTpProcesso.setText("Serviço para discordar do resultado do julgamento de um recurso ordinário (1ª instância). O recurso especial é enviado para a Câmara de Julgamentos (2ª instância). O pedido deve ser feito em até 30 dias após tomar conhecimento do resultado com o qual você discorda. Este pedido é realizado totalmente pela internet, você não precisa ir ao INSS, a não ser quando chamado para alguma comprovação.")

    def atualizaTipoBeneficio(self, tipo: TipoBeneficioEnum):
        self.lbTpBeneEscolhido.setText(strTipoBeneFacilitado(tipo))
        self.frTpBeneficioHist.show()

        self.processoAtual.tipoBeneficio = tipo.value
        self.processoAtual.dataUltAlt = datetime.datetime.now()
        self.processoAtual.save()

        self.trocaEtapa(EtapaEntrevista.tipoProcesso)

    def atualizaTipoProcesso(self, tipo: TipoProcesso):
        self.lbTpProcEscolhido.setText(strTipoProcesso(tipo))
        self.frTpProcessoHist.show()

        self.processoAtual.tipoProcesso = tipo.value
        self.processoAtual.dataUltAlt = datetime.datetime.now()
        self.processoAtual.save()

        self.trocaEtapa(EtapaEntrevista.quizEntrevista)

    def atualizaNaturezaProcesso(self, natureza: NaturezaProcesso):
        if natureza == NaturezaProcesso.administrativo:
            self.lbNaturezaEscolhida.setText("Administrativo")
        else:
            self.lbNaturezaEscolhida.setText("Judicial")

        self.frNaturezaHist.show()

        if self.clienteAtual is not None and self.clienteAtual.clienteId is not None:
            self.processoAtual.clienteId = self.clienteAtual.clienteId

        self.processoAtual.natureza = natureza.value
        self.processoAtual.dataUltAlt = datetime.datetime.now()
        self.processoAtual.advogadoId = self.advogadoAtual.advogadoId
        self.processoAtual.estado = self.escritorio.estado
        self.processoAtual.save()
        self.trocaEtapa(EtapaEntrevista.tipoBeneficio)
        self.clearFocus()

    def avaliaCancelaSimulacao(self):
        popUpSimCancela(
            "Deseja cancelar essa simulação?\nVocê voltará para a tela anterior e poderá alterar as respostas e as configurações da entrevista.",
            titulo="Cancelar simulação",
            funcaoSim=self.cancelarSimulacao,
        )

    def avaliaFinalizaEntrevista(self):
        tipoDoBeneficio = TipoBeneficioEnum(self.processoAtual.tipoBeneficio.tipoId)

        if self.processoAtual.natureza == NaturezaProcesso.administrativo.value:
            if tipoDoBeneficio == TipoBeneficioEnum.Aposentadoria:
                self.aposentadoriaModel = CalculosAposentadoria(processo=self.processoAtual, cliente=self.clienteAtual, entrevistaParams=self.entrevistaParams)
                listaSimulacao = self.aposentadoriaModel.geraSimulacoes()
                self.carregaTelaSimulacao(listaSimulacoes=listaSimulacao)
                self.frEsquerda.hide()
                self.trocaEtapa(EtapaEntrevista.simulacoes)
                self.apiLog.info('Finalizou questionário da entrevista')

            elif tipoDoBeneficio == TipoBeneficioEnum.AuxAcidente:
                self.mensagemToast("Calculo de benefício ainda não implementado..")
            elif tipoDoBeneficio == TipoBeneficioEnum.AuxDoenca:
                self.mensagemToast("Calculo de benefício ainda não implementado..")
            elif tipoDoBeneficio == TipoBeneficioEnum.AuxReclusao:
                self.mensagemToast("Calculo de benefício ainda não implementado..")
            elif tipoDoBeneficio == TipoBeneficioEnum.BeneDeficiencia:
                self.mensagemToast("Calculo de benefício ainda não implementado..")
            elif tipoDoBeneficio == TipoBeneficioEnum.BeneIdoso:
                self.mensagemToast("Calculo de benefício ainda não implementado..")
            elif tipoDoBeneficio == TipoBeneficioEnum.PensaoMorte:
                self.mensagemToast("Calculo de benefício ainda não implementado..")
            elif tipoDoBeneficio == TipoBeneficioEnum.SalMaternidade:
                self.mensagemToast("Calculo de benefício ainda não implementado..")
            else:
                popUpOkAlerta("Tipo do benefício não encontrado. Entre em contato com o suporte.", erro=f"{self.processoAtual.tipoBeneficio=}\n{self.processoAtual.processoId=}")
        else:
            self.mensagemToast("Natureza do processo ainda não implementada...")

    def avaliaMostraInfoLateral(self):
        self.pbInfoCliente.setStyleSheet(iconeInfoCliente(self.frEsquerda.isHidden()))

        if self.frEsquerda.isHidden():
            self.frEsquerda.show()
        else:
            self.frEsquerda.hide()

    def avaliarVoltar(self):
        if self.etapaAtual == EtapaEntrevista.naturezaProcesso:
            popUpSimCancela('Deseja deixar a entrevista?\nTodas as informações serão perdidas.', funcaoSim=self.sairEntrevista)
        elif self.etapaAtual == EtapaEntrevista.tipoBeneficio:
            self.frTpBeneficioHist.hide()
            self.lbTpBeneEscolhido.setText('')
            self.trocaEtapa(EtapaEntrevista.naturezaProcesso)
        elif self.etapaAtual == EtapaEntrevista.tipoProcesso:
            self.frTpProcessoHist.hide()
            self.lbTpProcEscolhido.setText('')
            self.trocaEtapa(EtapaEntrevista.tipoBeneficio)
        elif self.etapaAtual == EtapaEntrevista.quizEntrevista:
            self.trocaEtapa(EtapaEntrevista.tipoProcesso)
        elif self.etapaAtual == EtapaEntrevista.simulacoes:
            self.frEsquerda.show()
            self.trocaEtapa(EtapaEntrevista.quizEntrevista)

    def buscaAdvogadoAtual(self):
        cacheAdvogado = CacheLogin()
        self.advogadoAtual = cacheAdvogado.carregarCache()
        if self.advogadoAtual is None or self.advogadoAtual.advogadoId is None:
            self.advogadoAtual = cacheAdvogado.carregarCacheTemporario()

            if self.advogadoAtual is None or self.advogadoAtual.escritorioId is None:
                popUpOkAlerta("Não foi possível carregar as informações do advogado. Tente fazer o login novamente.")
                cacheAdvogado.limpaCache()
                cacheAdvogado.limpaTemporarios()
                return False

        return True

    def cancelarSimulacao(self):
        self.aposentadoriaModel.limpaTudo()
        self.avaliarVoltar()

    def carregaTelaSimulacao(self, listaSimulacoes: List[Aposentadoria] = []):
        if len(listaSimulacoes) > 0:
            listaAposentadorias: List[Aposentadoria] = listaSimulacoes
        else:
            listaAposentadorias: List[Aposentadoria] = Aposentadoria.select().where(
                Aposentadoria.clienteId == self.clienteAtual.clienteId,
                Aposentadoria.processoId == self.processoAtual.processoId,
            ).order_by(
                Aposentadoria.valorSimulacao.desc(),
                Aposentadoria.valorBeneficio.desc(),
                Aposentadoria.idadeCliente,
            )

        if len(listaAposentadorias) > 0:
            glSimulacoes = QGridLayout(self)
            glSimulacoes.setSpacing(36)
            glSimulacoes.setContentsMargins(16, 16, 16, 16)

            for index, aposentadoria in enumerate(listaAposentadorias):
                self.processoAtual.regraAposentadoria = aposentadoria.tipo
                glSimulacoes.addWidget(NewCardAposentadoria(aposentadoria, parent=self), index//4, index % 4)

            self.scaSimulacoes.setLayout(glSimulacoes)

    def carregaTiposBeneficio(self):
        self.listaBeneficios = TipoBeneficioModel.select()

    def defineCliente(self, cliente: Cliente):
        if cliente is not None and cliente.clienteId is not None:
            self.apiLog.info("Iniciou entrevista")
            self.clienteAtual = cliente
            self.iniciaInfoPessoais()

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

    def habilitaBlur(self, ativar: bool = True):
        efeito = Efeitos()
        efeito.blurWidgets([self.frPrincipal], disable=not ativar)

    def iniciaInfoPessoais(self):
        if self.clienteAtual is not None and self.clienteAtual.clienteId is not None:
            idadeCliente = calculaIdade(self.clienteAtual.dataNascimento, datetime.datetime.today())
            self.lbNome.setText(f"{self.clienteAtual.nomeCliente} {self.clienteAtual.sobrenomeCliente}")
            self.lbCpf.setText(mascaraCPF(self.clienteAtual.cpfCliente))
            self.lbDataNascimento.setText(f"{mascaraData(strToDate(self.clienteAtual.dataNascimento))} ({idadeCliente.years} anos)")
            self.frInfoHistPessoais.show()
        else:
            self.frInfoHistPessoais.hide()

    def iniciaQuiz(self):
        vlQuiz = QVBoxLayout(self)

        infoInsalubre = InformacaoModel('Insalubridade', CategoriaQuiz.insalubridade)
        insalubridade = WdgCheckInfo(infoInsalubre, parent=self)
        vlQuiz.addWidget(insalubridade)

        infoDeficiente = InformacaoModel('Deficiência', CategoriaQuiz.deficiencia)
        deficiencia = WdgCheckInfo(infoDeficiente, parent=self)
        vlQuiz.addWidget(deficiencia)

        infoMilitar = InformacaoModel('Serviço militar', CategoriaQuiz.servicoMilitar)
        ServMilitar = WdgCheckInfo(infoMilitar, parent=self)
        vlQuiz.addWidget(ServMilitar)

        infoRural = InformacaoModel('Trabalho rural', CategoriaQuiz.trabalhoRural)
        trabalhoRural = WdgCheckInfo(infoRural, parent=self)
        vlQuiz.addWidget(trabalhoRural)

        infoManual = InformacaoModel('Alteração manual', CategoriaQuiz.alteracaoManual)
        altManual = WdgCheckInfo(infoManual, parent=self)
        vlQuiz.addWidget(altManual)

        infoOutros = InformacaoModel('Outros', CategoriaQuiz.outros)
        outros = WdgCheckInfo(infoOutros, parent=self)
        vlQuiz.addWidget(outros)

        self.scaQuestionario.setLayout(vlQuiz)

    def iniciaTpProcesso(self):
        pbConcessao = NewCardPadrao(
            TipoProcesso.Concessao,
            parent=self,
            onHover=lambda: self.atualizaDescricaoTpProcesso(TipoProcesso.Concessao),
            onClick=lambda: self.atualizaTipoProcesso(TipoProcesso.Concessao),
        )
        pbRevisao = NewCardPadrao(
            TipoProcesso.Revisao,
            parent=self,
            onHover=lambda: self.atualizaDescricaoTpProcesso(TipoProcesso.Revisao),
            onClick=lambda: self.atualizaTipoProcesso(TipoProcesso.Revisao),
        )
        pbRecOrdinario = NewCardPadrao(
            TipoProcesso.RecOrdinario,
            parent=self,
            onHover=lambda: self.atualizaDescricaoTpProcesso(TipoProcesso.RecOrdinario),
            onClick=lambda: self.atualizaTipoProcesso(TipoProcesso.RecOrdinario),
        )
        pbRecEspecial = NewCardPadrao(
            TipoProcesso.RecEspecial,
            parent=self,
            onHover=lambda: self.atualizaDescricaoTpProcesso(TipoProcesso.RecEspecial),
            onClick=lambda: self.atualizaTipoProcesso(TipoProcesso.RecEspecial),
        )

        self.vlTpProcesso.addWidget(pbConcessao)
        self.vlTpProcesso.addWidget(pbRevisao)
        self.vlTpProcesso.addWidget(pbRecOrdinario)
        self.vlTpProcesso.addWidget(pbRecEspecial)

    def iniciaHistorico(self):
        self.frNaturezaHist.hide()
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

    def mensagemToast(self, mensagem: str):
        if self.toasty is None:
            self.toasty = QToaster(self)
        self.toasty.showMessage(self, mensagem)

    def recebeInfo(self, info: InformacaoModel):
        perguntas=[
            InformacaoModel(
                descricao="Testando questão 1",
                tipoInfo=QCheckBox()
            ),
            InformacaoModel(
                descricao="Testando questão 2",
                tipoInfo=QCheckBox(),
                nivel=1
            ),
            InformacaoModel(
                descricao="Testando questão 3",
                tipoInfo=QCheckBox()
            ),
            InformacaoModel(
                descricao="Testando questão 4",
                tipoInfo=QCheckBox()
            ),
        ]
        modalEntrevista = ModalEntrevistaController(info.tipoInfo, perguntas, parent=self, dashboard=self.dashboard)
        modalEntrevista.show()
        self.habilitaBlur(ativar=True)

    def salvarSimulacao(self):
        # TODO: LIMPAR TUDO
        IncidenteProcessual(
            processoId=self.processoAtual.processoId,
            andamento=SituacaoProcesso.aDarEntrada.value,
            descricao='Processo a iniciar salvo no banco de dados.',
            seq=1,
            codAndamento=0,
            dataIncidente=datetime.datetime.now(),
            dataCadastro=datetime.datetime.now(),
            dataUltAlt=datetime.datetime.now()
        ).save()

        self.salvandoSimulacao = True
        self.aposentadoriaModel.salvaAposentadorias()
        self.aposentadoriaModel.limpaTudo()
        self.voltarDashboard()

    def sairEntrevista(self):
        self.sinais.sTrocaWidgetCentral.emit(TelaPosicao.Cliente)

    def trocaEtapa(self, etapaDestino: EtapaEntrevista):
        self.etapaAtual = etapaDestino
        self.stkEntrevista.setCurrentIndex(etapaDestino.value)
        self.frMigalhas.setStyleSheet(styleEtapaEntrevista(etapaDestino))

    def voltarDashboard(self):
        if not self.salvandoSimulacao:
            self.processoAtual.delete().execute()

        self.dashboard.trocaTela(TelaPosicao.Cliente)


if __name__ == '__main__':
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = NewEntrevistaPrincipal()
    w.show()
    sys.exit(app.exec_())
