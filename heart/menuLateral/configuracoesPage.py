from PyQt5.QtWidgets import QWidget, QMessageBox

from Design.pyUi.configuracoesPage import Ui_wdgTabConfiguracoes
from Design.CustomWidgets.newCheckBox import NewCheckBox
from cache.cachingLogin import CacheLogin
from modelos.advogadoORM import Advogados
from modelos.configGeraisORM import ConfigGerais


class ConfiguracoesPage(QWidget, Ui_wdgTabConfiguracoes):
    advogado: Advogados
    configGerais: ConfigGerais

    def __init__(self, parent=None):
        super(ConfiguracoesPage, self).__init__(parent=parent)
        self.setupUi(self)

        self.carregaConfiguracoes()

        self.cbIniciaAutomatico = NewCheckBox(width=40)
        self.hlInicioAutomatico.addWidget(self.cbIniciaAutomatico)
        self.cbIniciaAutomatico.stateChanged.connect(self.atualizaIniciaAuto)

        self.atualizaTela()

    def atualizaIniciaAuto(self):
        self.configGerais.iniciaAuto = self.cbIniciaAutomatico.isChecked()
        self.configGerais.save()

    def atualizaTela(self):
        self.cbIniciaAutomatico.setChecked(self.configGerais.iniciaAuto)

    def carregaConfiguracoes(self):
        try:
            self.advogado = CacheLogin().carregarCache()
            self.configGerais = ConfigGerais.get(ConfigGerais.advogadoId == self.advogado.advogadoId)
        except ConfigGerais.DoesNotExist:
            print('Problema!')
            self.popUpOkAlerta('Não foi possível carregar as configurações. Entre em contato com o suporte')
            self.desabilitarTudo()
        except Exception as err:
            print(f'Deu um super problema ({type(err)}): {err}')

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
