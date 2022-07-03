from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from math import floor
from typing import List

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from modelos.itemContribuicao import ItemContribuicao
from util.helpers.dateHelper import strToDatetime
from util.helpers.helpers import dictEspecies, mascaraNit, strToFloat, situacaoBeneficio, floatToDinheiro
from util.popUps import popUpOkAlerta

from Design.pyUi.insereContrib import Ui_mwInsereContrib
from heart.localStyleSheet.insereContribuicao import habilita, habilitaBotao
from heart.informacoesTelas.indicadoresTela import IndicadoresController
from modelos.vinculoORM import cnisVinculos
from modelos.clienteORM import Cliente
from modelos.convMonORM import ConvMon
from util.enums.newPrevEnums import TipoContribuicao


class InsereContribuicaoPage(QMainWindow, Ui_mwInsereContrib):

    def __init__(self, parent=None, db=None, cliente: Cliente = None, itemConrtibuicaoId: int = 0, tipo: TipoContribuicao = TipoContribuicao.contribuicao):
        super(InsereContribuicaoPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.tabCalculos = parent
        self.indicadoresContrib = []
        self.db = db
        self.cliente = cliente
        # self.itemContribuicao: CnisBeneficios = CnisBeneficios()
        self.itemContribuicao: ItemContribuicao = ItemContribuicao() 
        self.listaConvMon: list
        self.indicadoresPg = None
        self.tipo = tipo
        self.setAcceptDrops(True)

        self.lbNomeCompleto.setText(f"{self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}")
        self.lbNit.setText(mascaraNit(int(self.cliente.nit)))
        self.lbRepetirAte.hide()

        self.rbBeneficio.setChecked(True)
        self.rbContribuicao.clicked.connect(self.atualizaFoco)
        self.rbBeneficio.clicked.connect(self.atualizaFoco)

        self.cbRepetir.clicked.connect(self.avaliaRepetir)
        self.cbRepetir.setDisabled(True)

        self.pbarSistema.hide()
        self.pbarSistema.setValue(0)
        self.pbConfirmar.clicked.connect(self.trataInsereInfo)
        self.pbCancelar.clicked.connect(self.sairAtividade)
        self.pbInsereIndicadores.clicked.connect(self.openInfoIndicadores)

        self.listaConvMon: List[ConvMon] = ConvMon.select()

        self.atualizaFoco()
        self.carregaQtdsRemCont()
        self.carregaComboBoxes()

        self.cbxSinal.setDisabled(True)

        self.dtCompetencia.dateChanged.connect(lambda: self.getInfo(info='dtCompetencia'))
        self.dtFim.dateChanged.connect(lambda: self.getInfo(info='dtFim'))
        self.dtInicio.dateChanged.connect(lambda: self.getInfo(info='dtInicio'))
        self.dtRepetir.hide()

        self.cbxSituacao.currentTextChanged.connect(lambda: self.getInfo(info='cbxSituacao'))
        self.cbxEspecie.currentTextChanged.connect(lambda: self.getInfo(info='cbxEspecie'))

        self.leSalContribuicao.textChanged.connect(lambda: self.getInfo(info='leSalContribuicao'))
        self.leNb.textChanged.connect(lambda: self.getInfo(info='leNb'))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.escondeLoading)

        if tipo == TipoContribuicao.beneficio:
            self.rbBeneficio.setChecked(True)
            self.atualizaFoco()
        elif tipo == TipoContribuicao.contribuicao or tipo == TipoContribuicao.remuneracao:
            self.rbContribuicao.setChecked(True)
            self.atualizaFoco()
        # elif tipo == TipoContribuicao.remuneracao:
        #     self.rbRemuneracao.setChecked(True)
        #     self.atualizaFoco()

        if itemConrtibuicaoId != 0:
            self.buscaContribuicao(itemConrtibuicaoId, tipo)

    def buscaContribuicao(self, contribuicaoId: int, tipo: TipoContribuicao):

        if tipo == TipoContribuicao.contribuicao:
            contribuicao: ItemContribuicao = ItemContribuicao.get_by_id(contribuicaoId)
            self.itemContribuicao = contribuicao
            self.mostraInfoTela(contribuicao, TipoContribuicao.contribuicao)

        elif tipo == TipoContribuicao.remuneracao:
            contribuicao: ItemContribuicao = ItemContribuicao.get_by_id(contribuicaoId)
            self.itemContribuicao = contribuicao
            self.mostraInfoTela(contribuicao, TipoContribuicao.remuneracao)

        elif tipo == TipoContribuicao.beneficio:
            contribuicao: ItemContribuicao = ItemContribuicao.get_by_id(contribuicaoId)
            self.itemContribuicao = contribuicao
            self.mostraInfoTela(contribuicao, TipoContribuicao.beneficio)

    def mostraInfoTela(self, contribuicao, tipoContribuicao: TipoContribuicao):
        if tipoContribuicao == TipoContribuicao.contribuicao:
            self.leSalContribuicao.setText(floatToDinheiro(contribuicao.contribuicao))
            self.dtCompetencia.setDate(strToDatetime(contribuicao.competencia))
            self.defineSinalMonetario(contribuicao)

        elif tipoContribuicao == TipoContribuicao.remuneracao:
            self.leSalContribuicao.setText(f'{contribuicao.remuneracao}')
            self.dtCompetencia.setDate(strToDatetime(contribuicao.competencia))
            self.defineSinalMonetario(contribuicao)

        elif tipoContribuicao == TipoContribuicao.beneficio:
            cabecalho: cnisVinculos = cnisVinculos.select().where(cnisVinculos.clienteId == self.cliente.clienteId, cnisVinculos.seq == contribuicao.seq).get()
            if strToDatetime(cabecalho.dataFim) == datetime.min:
                dataFim: datetime = datetime.now()
            else:
                dataFim: datetime = strToDatetime(cabecalho.dataFim)

            self.leNb.setText(str(contribuicao.nb))
            self.cbxSituacao.setCurrentText(cabecalho.situacao.title())
            self.cbxEspecie.setCurrentText(cabecalho.especie)
            self.dtInicio.setDate(strToDatetime(cabecalho.dataInicio))
            self.dtFim.setDate(dataFim)

    def defineSinalMonetario(self, contribuicao: ItemContribuicao):
        if contribuicao.tipo in (TipoContribuicao.contribuicao.value, TipoContribuicao.remuneracao.value):
            competencia: datetime = strToDatetime(contribuicao.competencia)

            for moeda in self.listaConvMon:
                dataInicial = strToDatetime(moeda.dataInicial)
                dataFinal = strToDatetime(moeda.dataFinal)
                if dataInicial <= competencia <= dataFinal:
                    self.cbxSinal.setCurrentText(moeda.sinal)
                    break

    def avaliaRepetir(self):
        if self.cbRepetir.isChecked():
            self.dtRepetir.show()
            self.lbRepetirAte.show()
        else:
            self.lbRepetirAte.hide()
            self.dtRepetir.hide()

    def carregaComboBoxes(self):
        listaSinaisMonetarios: set = {moeda.sinal for moeda in self.listaConvMon}
        self.cbxSinal.addItems(listaSinaisMonetarios)
        self.cbxEspecie.addItems(sorted(dictEspecies.values()))
        self.cbxSituacao.addItems(sorted(situacaoBeneficio))

    def carregaQtdsRemCont(self):
        qtdRemuneracoes = ItemContribuicao.select().where(
            ItemContribuicao.clienteId == self.cliente.clienteId,
            ItemContribuicao.tipo == TipoContribuicao.remuneracao.value
        ).count()

        self.lbQtdRem.setText(str(qtdRemuneracoes))

    def atualizaFoco(self):
        self.limpaTudo()
        if self.rbBeneficio.isChecked():
            self.frInfoBeneficio.setStyleSheet(habilita('beneficio', True))
            self.frInfoRemCont.setStyleSheet(habilita('remCont', False))
            self.pbInsereIndicadores.setStyleSheet(habilitaBotao('pbInsereIndicadores', False))
            self.dtCompetencia.setDisabled(True)
            self.leSalContribuicao.setDisabled(True)
            self.dtRepetir.setDisabled(True)
            self.cbRepetir.setDisabled(True)
            # self.cbxSinal.setDisabled(True)
            self.pbInsereIndicadores.setDisabled(True)

            self.leNb.setDisabled(False)
            self.cbxSituacao.setDisabled(False)
            self.cbxEspecie.setDisabled(False)
            self.dtInicio.setDisabled(False)
            self.dtFim.setDisabled(False)
        else:
            self.frInfoBeneficio.setStyleSheet(habilita('beneficio', False))
            self.frInfoRemCont.setStyleSheet(habilita('remCont', True))
            self.pbInsereIndicadores.setStyleSheet(habilitaBotao('pbInsereIndicadores', True))
            self.dtCompetencia.setDisabled(False)
            self.leSalContribuicao.setDisabled(False)
            self.dtRepetir.setDisabled(False)
            self.cbRepetir.setDisabled(False)
            # self.cbxSinal.setDisabled(False)
            self.pbInsereIndicadores.setDisabled(False)

            self.leNb.setDisabled(True)
            self.cbxSituacao.setDisabled(True)
            self.cbxEspecie.setDisabled(True)
            self.dtInicio.setDisabled(True)
            self.dtFim.setDisabled(True)

    def getInfo(self, info: str = None):
        if info == 'dtCompetencia':
            self.itemContribuicao.competencia = self.dtCompetencia.date().toPyDate().strftime('%Y-%m-%d %H:%M')
            for sinal in self.listaConvMon:
                if sinal.moedaCorrenteByData(self.itemContribuicao.competencia):
                    self.cbxSinal.setCurrentText(sinal.sinal)
                    return True

        elif info == 'dtFim':
            self.itemContribuicao.dataFim = self.dtFim.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'dtInicio':
            self.itemContribuicao.dataInicio = self.dtInicio.date().toPyDate().strftime('%Y-%m-%d %H:%M')

        elif info == 'leSalContribuicao':
            if self.rbContribuicao.isChecked():
                self.itemContribuicao.salContribuicao = strToFloat(self.leSalContribuicao.text())
            else:
                self.itemContribuicao.remuneracao = strToFloat(self.leSalContribuicao.text())

        elif info == 'leNb':
            if self.leNb.text() != '':
                self.itemContribuicao.nb = int(self.leNb.text())

        elif info == 'cbxSituacao':
            self.itemContribuicao.situacao = self.cbxSituacao.currentText()

        elif info == 'cbxEspecie':
            self.itemContribuicao.especie = self.cbxEspecie.currentText()

    def trataInsereInfo(self):
        if self.verificaCampos():
            if self.rbBeneficio.isChecked():
                if self.leNb.text() != '' and self.cbxSituacao.currentText() not in (-1, 0):
                    self.loading(40)
                    self.itemContribuicao.clienteId = self.cliente.clienteId
                    self.loading(20)
                    self.itemContribuicao.dadoOrigem = 'MANUAL'
                    self.loading(20)
                    self.itemContribuicao.seq = 0
                    self.loading(20)
                    self.itemContribuicao.dataUltAlt = datetime.now()
                    self.itemContribuicao.save()
                    # self.daoCalculos.insereBeneficio(self.itemContribuicao)
                    self.mensagemSistema('Benefício inserido com sucesso!')

            elif self.rbContribuicao.isChecked():
                if self.leSalContribuicao.text() != '':
                    self.loading(20)
                    self.itemContribuicao.clienteId = self.cliente.clienteId
                    self.loading(20)
                    self.itemContribuicao.dadoOrigem = 'MANUAL'
                    self.loading(20)
                    self.itemContribuicao.seq = 0
                    self.loading(20)
                    if self.cbRepetir.isChecked():
                        if self.dtCompetencia.date().toPyDate() <= self.dtRepetir.date().toPyDate():
                            popUpOkAlerta('A data de repetição é anterior à data da competência inicial.')
                            self.raise_()
                            self.loading(100)
                            return False

                        qtdContribuicoes: int = self.geraContribsRecorrente()
                        self.mensagemSistema(f'{qtdContribuicoes} de contribuições inseridas com sucesso!')
                    else:
                        if self.tipo == TipoContribuicao.remuneracao:
                            self.itemContribuicao.indicadores = self.retornaStrIndicadores()
                            self.itemContribuicao.dataUltAlt = datetime.now()
                            self.itemContribuicao.save()

                        elif self.itemContribuicao.contribuicoesId is not None:
                            if self.itemContribuicao.dataPagamento is None:
                                self.itemContribuicao.dataPagamento = self.itemContribuicao.competencia

                            self.itemContribuicao.indicadores = self.retornaStrIndicadores()
                            self.itemContribuicao.dataUltAlt = datetime.now()
                            self.itemContribuicao.save()

                        elif self.itemContribuicao.contribuicoesId is None:
                            if self.itemContribuicao.dataPagamento is None:
                                self.itemContribuicao.dataPagamento = self.itemContribuicao.competencia

                            self.itemContribuicao.indicadores = self.retornaStrIndicadores()
                            ItemContribuicao.insert(**self.itemContribuicao.toDict()).on_conflict_replace().execute()

                    self.mensagemSistema('Contribuição inserida com sucesso!')

    def geraContribsRecorrente(self) -> int:
        if self.leSalContribuicao.text() == '':
            popUpOkAlerta('O salário de contribuição é inválido. Verifique o valor e tente novamente.')
            self.leSalContribuicao.setFocus()
            return False

        difMeses: int = floor((self.dtRepetir.date().toPyDate() - self.dtCompetencia.date().toPyDate()).days/30)
        qtdContribuicoes: int = 0
        salContribuicao: float = float(self.leSalContribuicao.text().replace(',', '.'))

        for mes in range(0, difMeses+1):
            ItemContribuicao(
                clienteId=self.itemContribuicao.clienteId,
                seq=self.itemContribuicao.seq,
                tipo=TipoContribuicao.contribuicao.value,
                competencia=relativedelta(months=+mes) + self.dtCompetencia.date().toPyDate(),
                contribuicao=salContribuicao*0.2,
                salContribuicao=self.itemContribuicao.salContribuicao,
                dadoOrigem='N',
                geradoAutomaticamente=True,
                indicadores=self.retornaStrIndicadores(),
                dataCadastro=date.today(),
                dataUltAlt=date.today(),
            ).save()
            qtdContribuicoes = mes

        return qtdContribuicoes

    def sairAtividade(self):
        remuneracao: bool = self.leSalContribuicao.text() == ''
        nb: bool = self.leNb.text() == ''
        situacao: bool = self.cbxSituacao.currentIndex() in (-1, 0)

        if remuneracao and nb and situacao:
            self.close()
        else:
            self.popUpSimCancela('Você tem informações sem serem salvas. Deseja sair?', funcao=self.close)

    def verificaCampos(self):

        if self.rbBeneficio.isChecked():
            if self.leNb.text() == '':
                popUpOkAlerta('O campo Número do benefício é obrigatório. \nPreencha-o e tente novamente.')
                self.leNb.setFocus()
                return False

        else:
            if len(self.leSalContribuicao.text()) == 0:
                popUpOkAlerta('O campo Salário de contribuição é obrigatório. \nPreencha-o e tente novamente.')
                self.leSalContribuicao.clear()
                self.leSalContribuicao.setFocus()
                return False

            else:
                try:
                    float(self.leSalContribuicao.text().replace(' ', '').replace(',', '.'))
                    return True
                except ValueError as err:
                    popUpOkAlerta('O campo Salário de contribuição precisa ser um valor monetário. \nPreencha-o e tente novamente.')
                    self.leSalContribuicao.clear()
                    self.leSalContribuicao.setFocus()
                    return False


            # elif self.dtCompetencia.date().toPyDate() > date.today():
            #     popUpOkAlerta('O campo Competência precisa ter uma data anterior a hoje. Tente novamente.')
            #     self.dtCompetencia.setFocus()
            #     return False

        return True

    def limpaTudo(self):
        self.leSalContribuicao.clear()
        self.leNb.clear()
        self.cbxSituacao.setCurrentIndex(0)
        self.cbxEspecie.setCurrentIndex(0)

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
        self.indicadoresPg = IndicadoresController(parent=self, db=self.db)
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

    def recebeIndicadores(self, indicadores: List[str]):
        self.indicadoresContrib = indicadores

    def retornaStrIndicadores(self):
        strIndicadores = ''
        primeiroItem: bool = True
        
        for indicador in self.indicadoresContrib:
            if primeiroItem:
                strIndicadores += indicador
                primeiroItem = False
            else:
                strIndicadores += ', ' + indicador
                
        return strIndicadores

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        print('--------------------------------------------- dropEvent')
        print(f"{a0.source()=}")
        print(f"{a0.type()=}")
        print(f"{a0.mimeData()=}")
        print(f"{a0.possibleActions()=}")
        print(f"{a0.spontaneous()=}")

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        print('--------------------------------------------- dragEnterEvent')
        print(f"{a0.source()=}")
        print(f"{a0.type()=}")
        print(f"{a0.mimeData()=}")
        print(f"{a0.possibleActions()=}")
        print(f"{a0.spontaneous()=}")
