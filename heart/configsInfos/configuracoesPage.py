import datetime

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Design.pyUi.configuracoesPage import Ui_mwConfiguracoes

from cache.cachingLogin import CacheLogin
from heart.configsInfos.localStyleSheet.configuracoes import configSelecionada
from modelos.advogadoORM import Advogados
from modelos.configGeraisORM import ConfigGerais

from util.popUps import popUpOkAlerta
from util.enums.configEnums import CategoriaConfig


class ConfiguracoesPage(QMainWindow, Ui_mwConfiguracoes):
    advogado: Advogados
    configGerais: ConfigGerais = ConfigGerais()

    def __init__(self, parent=None):
        super(ConfiguracoesPage, self).__init__(parent=parent)
        self.setupUi(self)
        self.cbIniciaAutomatico.setToolTip('Caso tenha marcado para lembrar senha na tela de login e esse parâmetro esteja ativado.\nO programa iniciará sem passar pela tela de login.')

        self.carregaConfiguracoes()
        self.atualizaTela()
        self.trocaCategConfig(CategoriaConfig.geral)

        self.cbIniciaAutomatico.stateChanged.connect(self.atualizaIniciaAuto)
        self.pbSalvar.clicked.connect(self.close)
        self.pbGeral.clicked.connect(lambda: self.trocaCategConfig(CategoriaConfig.geral))
        self.pbBackup.clicked.connect(lambda: self.trocaCategConfig(CategoriaConfig.backup))

    def atualizaIniciaAuto(self):
        if self.configGerais is not None:
            self.configGerais.iniciaAuto = not self.cbIniciaAutomatico.isChecked()
            self.configGerais.dataUltAlt = datetime.datetime.now()
            self.configGerais.save()

    def atualizaTela(self):
        if self.configGerais is not None:
            self.cbIniciaAutomatico.setChecked(self.configGerais.iniciaAuto)
        else:
            self.cbIniciaAutomatico.setChecked(False)

    def carregaConfiguracoes(self):
        cache = CacheLogin()
        try:
            self.advogado = cache.carregarCache()
            if not self.advogado:
                self.advogado = cache.carregarCacheTemporario()
            self.configGerais = ConfigGerais.get(ConfigGerais.advogadoId == self.advogado.advogadoId)
        except ConfigGerais.DoesNotExist as err:
            print('Problema!')
            popUpOkAlerta('Não foi possível carregar as configurações. Entre em contato com o suporte', erro=f"carregaConfiguracoes() \n\n{err}")
            cache.limpaCache()
            cache.limpaTemporarios()
            self.desabilitarTudo()
        except Exception as err:
            print(f'Deu um super problema ({type(err)}): {err}')
            cache.limpaCache()
            cache.limpaTemporarios()

    def desabilitarTudo(self):
        self.cbIniciaAutomatico.setDisabled(True)

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

    def popUpOkAlerta(self, mensagem, titulo: str = 'Atenção!'):
        pop = QMessageBox()
        pop.setWindowTitle(titulo)
        pop.setText(mensagem)
        pop.setIcon(QMessageBox.Warning)
        pop.setStandardButtons(QMessageBox.Ok)

        x = pop.exec_()

    def trocaCategConfig(self, categoria: CategoriaConfig):
        if categoria == CategoriaConfig.geral:
            self.frGeral.setStyleSheet(configSelecionada(categoria))
            self.frBackup.setStyleSheet(configSelecionada(CategoriaConfig.backup, habilita=False))

        else:
            self.frBackup.setStyleSheet(configSelecionada(categoria))
            self.frGeral.setStyleSheet(configSelecionada(CategoriaConfig.geral, habilita=False))

        self.stkPrincipal.setCurrentIndex(categoria.value)


