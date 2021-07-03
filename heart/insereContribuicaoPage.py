from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Daos.daoCalculos import DaoCalculos
from Daos.daoFerramentas import DaoFerramentas
from Telas.insereContrib import Ui_mwInsereContrib
from heart.localStyleSheet.insereContribuicao import habilita
from heart.informacoesTelas.indicadoresTela import IndicadoresController
from helpers import dictIndicadores, dictEspecies, mascaraNit, strToFloat, situacaoBeneficio, strToDatetime
from modelos.beneficiosModelo import BeneficiosModelo
from modelos.clienteModelo import ClienteModelo
from modelos.contribuicoesModelo import ContribuicoesModelo
from modelos.remuneracaoModelo import RemuneracoesModelo
from newPrevEnums import TipoContribuicao, TamanhoData


class InsereContribuicaoPage(QMainWindow, Ui_mwInsereContrib):

    def __init__(self, parent=None, db=None, cliente: ClienteModelo=None, contribuicaoId: int = 0, tipo: TipoContribuicao = TipoContribuicao.contribuicao):
        super(InsereContribuicaoPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.tabCalculos = parent
        self.daoCalculos = DaoCalculos(db=db)
        self.daoFerramentas = DaoFerramentas(db=db)
        self.db = db
        self.cliente = cliente
        self.remuneracao = RemuneracoesModelo()
        self.contribuicao = ContribuicoesModelo()
        self.beneficio = BeneficiosModelo()
        self.listaConvMon: list
        self.indicadoresPg = IndicadoresController(parent=self, db=db)

        self.lbNomeCompleto.setText(f"{self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}")
        self.lbNit.setText(mascaraNit(int(self.cliente.nit)))

        self.rbBeneficio.setChecked(True)
        self.rbContribuicao.clicked.connect(self.atualizaFoco)
        # self.rbRemuneracao.clicked.connect(self.atualizaFoco)
        self.rbBeneficio.clicked.connect(self.atualizaFoco)

        self.pbarSistema.hide()
        self.pbarSistema.setValue(0)
        self.pbConfirmar.clicked.connect(self.trataInsereInfo)
        self.pbCancelar.clicked.connect(self.sairAtividade)
        self.pbInfoIndicadores.clicked.connect(self.openInfoIndicadores)

        self.dtCompetencia.dateChanged.connect(lambda: self.getInfo(info='dtCompetencia'))
        self.dtFim.dateChanged.connect(lambda: self.getInfo(info='dtFim'))
        self.dtInicio.dateChanged.connect(lambda: self.getInfo(info='dtInicio'))
        self.dtFimContRem.dateChanged.connect(lambda: self.getInfo(info='dtFimContRem'))

        self.cbxIndicadores.currentTextChanged.connect(lambda: self.getInfo(info='cbxIndicadores'))
        self.cbxSituacao.currentTextChanged.connect(lambda: self.getInfo(info='cbxSituacao'))
        self.cbxEspecie.currentTextChanged.connect(lambda: self.getInfo(info='cbxEspecie'))

        self.leRemuneracao.textChanged.connect(lambda: self.getInfo(info='leRemuneracao'))
        self.leNb.textChanged.connect(lambda: self.getInfo(info='leNb'))

        self.listaConvMon = self.carregaConvMons()

        self.atualizaFoco()
        self.carregaQtdsRemCont()
        self.carregaComboBoxes()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.escondeLoading)

        if tipo == TipoContribuicao.beneficio:
            self.rbBeneficio.setChecked(True)
            self.atualizaFoco()
        elif tipo == TipoContribuicao.contribuicao:
            self.rbContribuicao.setChecked(True)
            self.atualizaFoco()
        elif tipo == TipoContribuicao.remuneracao:
            self.rbRemuneracao.setChecked(True)
            self.atualizaFoco()

        if contribuicaoId != 0:
            self.buscaContribuicao(contribuicaoId, tipo)

    def buscaContribuicao(self, contribuicaoId: int, tipo: TipoContribuicao):

        if tipo == TipoContribuicao.contribuicao:
            contribuicao: ContribuicoesModelo = self.daoCalculos.buscaContribuicaoPorId(contribuicaoId)
            self.mostraInfoTela(contribuicao, TipoContribuicao.contribuicao)

        elif tipo == TipoContribuicao.remuneracao:
            contribuicao: RemuneracoesModelo = self.daoCalculos.buscaRemuneracaoPorId(contribuicaoId)
            self.mostraInfoTela(contribuicao, TipoContribuicao.remuneracao)

        elif tipo == TipoContribuicao.beneficio:
            contribuicao: BeneficiosModelo = self.daoCalculos.buscaBeneficioPorId(contribuicaoId)
            self.mostraInfoTela(contribuicao, TipoContribuicao.beneficio)

    def mostraInfoTela(self, contribuicao, tipoContribuicao: TipoContribuicao):
        if tipoContribuicao == TipoContribuicao.contribuicao:
            self.leRemuneracao.setText(f'{contribuicao.contribuicao}')
            self.cbxIndicadores.setCurrentText(f'{contribuicao.indicadores}')
            self.dtCompetencia.setDate(strToDatetime(contribuicao.competencia))
            self.dtFimContRem.setDate(strToDatetime(contribuicao.dataPagamento))
            self.cbxIndicadores.setCurrentText(contribuicao.indicadores)
            self.defineSinalMonetario(contribuicao)

        elif tipoContribuicao == TipoContribuicao.remuneracao:
            self.leRemuneracao.setText(f'{contribuicao.remuneracao}')
            self.cbxIndicadores.setCurrentText(contribuicao.indicadores)
            self.dtCompetencia.setDate(strToDatetime(contribuicao.competencia))
            self.defineSinalMonetario(contribuicao)

        elif tipoContribuicao == TipoContribuicao.beneficio:
            especie: str = dictEspecies[contribuicao.especie[:3].strip()]
            if strToDatetime(contribuicao.dataFim, TamanhoData.gg) == datetime.min:
                dataFim: datetime = datetime.now()
            else:
                dataFim: datetime = strToDatetime(contribuicao.dataFim, TamanhoData.gg)

            self.leNb.setText(str(contribuicao.nb))
            self.cbxSituacao.setCurrentText(contribuicao.situacao.title())
            self.cbxEspecie.setCurrentText(especie)
            self.dtInicio.setDate(strToDatetime(contribuicao.dataInicio, TamanhoData.gg))
            self.dtFim.setDate(dataFim)

    def defineSinalMonetario(self, contribuicao):
        if isinstance(contribuicao, ContribuicoesModelo) or isinstance(contribuicao, RemuneracoesModelo):
            competencia: datetime = strToDatetime(contribuicao.competencia, TamanhoData.gg)
            for moeda in self.listaConvMon:
                if moeda.dataInicial <= competencia <= moeda.dataFinal:
                    self.cbxSinal.setCurrentText(moeda.sinal)
                    break

    def carregaConvMons(self) -> list:
        return self.daoFerramentas.getAllMoedas(retornaModelos=True)

    def carregaComboBoxes(self):
        listaSinaisMonetarios: set = {moeda.sinal for moeda in self.listaConvMon}
        self.cbxSinal.addItems(listaSinaisMonetarios)
        self.cbxIndicadores.addItems(dictIndicadores.keys())
        self.cbxEspecie.addItems(sorted(dictEspecies.values()))
        self.cbxSituacao.addItems(sorted(situacaoBeneficio))

    def carregaQtdsRemCont(self):
        qtdRemuneracoes = self.daoCalculos.contaRemuneracoes(self.cliente.clienteId)[0]
        qtdContribuicoes = self.daoCalculos.contaContribuicoes(self.cliente.clienteId)[0]

        # self.lbQtdCont.setText(str(qtdContribuicoes))
        self.lbQtdRem.setText(str(qtdRemuneracoes))

    def atualizaFoco(self):
        self.limpaTudo()
        if self.rbBeneficio.isChecked():
            self.frInfoBeneficio.setStyleSheet(habilita('beneficio', True))
            self.frInfoRemCont.setStyleSheet(habilita('remCont', False))
            self.dtCompetencia.setDisabled(True)
            self.dtFimContRem.setDisabled(True)
            self.leRemuneracao.setDisabled(True)
            self.cbxIndicadores.setDisabled(True)

            self.leNb.setDisabled(False)
            self.cbxSituacao.setDisabled(False)
            self.cbxEspecie.setDisabled(False)
            self.dtInicio.setDisabled(False)
            self.dtFim.setDisabled(False)
        else:
            if self.rbContribuicao.isChecked():
                self.lbInfoDataFim.setText('Data de Pagamento')
                # self.lbRemCont.setText('Contribuição')
                self.dtFimContRem.setDisabled(False)
            else:
                self.lbInfoDataFim.setText('Data Fim')
                self.lbRemCont.setText('Remuneração')
                self.dtFimContRem.setDisabled(True)

            self.frInfoBeneficio.setStyleSheet(habilita('beneficio', False))
            self.frInfoRemCont.setStyleSheet(habilita('remCont', True))
            self.dtCompetencia.setDisabled(False)
            self.dtFimContRem.setDisabled(False)
            self.leRemuneracao.setDisabled(False)
            self.cbxIndicadores.setDisabled(False)

            self.leNb.setDisabled(True)
            self.cbxSituacao.setDisabled(True)
            self.cbxEspecie.setDisabled(True)
            self.dtInicio.setDisabled(True)
            self.dtFim.setDisabled(True)

    def getInfo(self, info: str = None):
        if info == 'dtCompetencia':
            if self.rbContribuicao.isChecked():
                self.contribuicao.competencia = self.dtCompetencia.date().toPyDate().strftime('%Y-%m-%d %H:%M')
            else:
                self.remuneracao.competencia = self.dtCompetencia.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'dtFim':
            self.beneficio.dataFim = self.dtFim.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'dtInicio':
            self.beneficio.dataInicio = self.dtInicio.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'dtFimContRem':
            if self.rbContribuicao.isChecked():
                self.contribuicao.dataPagamento = self.dtFimContRem.date().toPyDate().strftime('%Y-%m-%d %H:%M')
            else:
                self.remuneracao.dataFim = self.dtFimContRem.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'leRemuneracao':
            if self.rbContribuicao.isChecked():
                self.contribuicao.contribuicao = strToFloat(self.leRemuneracao.text())
            else:
                self.remuneracao.remuneracao = strToFloat(self.leRemuneracao.text())

        elif info == 'cbxIndicadores':
            if self.rbContribuicao.isChecked():
                self.contribuicao.indicadores = self.cbxIndicadores.currentText()
            else:
                self.remuneracao.indicadores = self.cbxIndicadores.currentText()

        elif info == 'leNb':
            if self.leNb.text() != '':
                self.beneficio.nb = int(self.leNb.text())

        elif info == 'cbxSituacao':
            self.beneficio.situacao = self.cbxSituacao.currentText()

        elif info == 'cbxEspecie':
            self.beneficio.especie = self.cbxEspecie.currentText()

    def trataInsereInfo(self):
        if self.rbBeneficio.isChecked():
            if self.leNb.text() != '' and self.cbxSituacao.currentText() not in (-1, 0):
                self.loading(40)
                self.beneficio.clienteId = self.cliente.clienteId
                self.loading(20)
                self.beneficio.dadoOrigem = 'MANUAL'
                self.loading(20)
                self.beneficio.seq = 0
                self.loading(20)
                self.daoCalculos.insereBeneficio(self.beneficio)
                self.mensagemSistema('Benefício inserido com sucesso!')
        elif self.rbContribuicao.isChecked():
            if self.leRemuneracao.text() != '':
                self.loading(40)
                self.contribuicao.clienteId = self.cliente.clienteId
                self.loading(20)
                self.contribuicao.dadoOrigem = 'MANUAL'
                self.loading(20)
                self.contribuicao.seq = 0
                self.loading(20)
                self.daoCalculos.insereContribuicao(self.contribuicao)
                self.mensagemSistema('Contribuição inserida com sucesso!')
        else:
            if self.leRemuneracao.text() != '':
                self.loading(40)
                self.remuneracao.clienteId = self.cliente.clienteId
                self.loading(20)
                self.remuneracao.dadoOrigem = 'MANUAL'
                self.loading(20)
                self.remuneracao.seq = 0
                self.loading(20)
                self.daoCalculos.insereRemuneracao(self.remuneracao)
                self.mensagemSistema('Remuneração inserida com sucesso!')

    def sairAtividade(self):
        remuneracao: bool = self.leRemuneracao.text() == ''
        nb: bool = self.leNb.text() == ''
        situacao: bool = self.cbxSituacao.currentIndex() in (-1, 0)

        if remuneracao and nb and situacao:
            self.close()
        else:
            self.popUpSimCancela('Você tem informações sem serem salvas. Deseja sair?', funcao=self.close)

    def limpaTudo(self):
        self.leRemuneracao.clear()
        self.leNb.clear()
        self.cbxSituacao.setCurrentIndex(0)
        self.cbxEspecie.setCurrentIndex(0)
        self.cbxIndicadores.setCurrentIndex(0)

    def loading(self, adicionaTempo):
        if self.pbarSistema.isHidden():
            self.pbarSistema.show()

        valorAtual = self.pbarSistema.value()
        valorAtual += adicionaTempo

        self.pbarSistema.setValue(valorAtual)

        if self.pbarSistema.value() >= 100:
            self.pbarSistema.setValue(100)
            self.timer.start(3000)

    def escondeLoading(self):
        self.pbarSistema.hide()
        self.lbInfoSistema.setText('')
        self.lbInfoSistema.hide()
        self.pbarSistema.setValue(0)
        self.timer.stop()
        self.limpaTudo()

    def openInfoIndicadores(self):
        self.indicadoresPg.show()

    def mensagemSistema(self, mensagem: str):
        self.lbInfoSistema.setText(mensagem)
        self.lbInfoSistema.show()

    def popUpSimCancela(self, mensagem, titulo: str = 'Atenção!', funcao=None):
        pop = QMessageBox()
        pop.setWindowTitle(titulo)
        pop.setText(mensagem)
        pop.setIcon(QMessageBox.Warning)
        pop.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        pop.setDefaultButton(QMessageBox.Cancel)

        x = pop.exec_()
        if x == QMessageBox.Yes:
            funcao()
        elif x == QMessageBox.Cancel:
            return False
        else:
            raise Warning(f'Ocorreu um erro inesperado')