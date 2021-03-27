from pathlib import Path
import re
import fitz

from PyQt5.QtWidgets import QWidget, QFileDialog
from Telas.configuracoesPage import Ui_wdgTabConfiguracoes

class ConfiguracoesPage(QWidget, Ui_wdgTabConfiguracoes):

    def __init__(self, parent=None, db=None):
        super(ConfiguracoesPage, self).__init__(parent=parent)
        self.setupUi(self)

        self.tblTetos.hideColumn(0)

        self.dashboard = parent
        self.db = db
        self.dictTetos = {
            'Ano': [],
            'Mes': [],
            'Valor': []
        }

        self.expRegAno = "[0-9]{4}"
        self.infoAPular = ['Período', 'Mês', 'Valores Correntes', 'Maior Valor-Teto do', 'Salário-de-Benefício']

        self.pbBuscarArq.clicked.connect(self.buscaArquivoTetos)

    def buscaArquivoTetos(self):
        home = str(Path.home())
        pathAux = None

        # Ambiente de desenvolvimento
        pathAux = QFileDialog.getOpenFileName(directory=home, options=QFileDialog.DontUseNativeDialog)

        # Ambiente de produção
        # pathAux = QFileDialog.getOpenFileName(directory=home)

        if pathAux[0] is not None and pathAux[0] != '':
            self.pathCnis = pathAux[0]

        if self.pathCnis is not None and self.pathCnis != '':
            self.extraiTetos(self.pathCnis)
        else:
            return None

    def extraiTetos(self, path: str):
        documento = fitz.open(path)
        qtdPaginas = documento.page_count
        Ano = ''
        Mes = ''

        for pag in range(0, qtdPaginas):
            page = documento.load_page(pag)
            conteudo: str = page.get_text()
            info: list = conteudo.splitlines()

            for index in range(0, len(info)):
                if info[index] not in self.infoAPular:
                    if re.match(self.expRegAno, info[index]) is not None:
                        Ano = info[index].strip()
                    elif info[index].isalpha():
                        Mes = info[index].strip()
                    elif ',' in info[index]:
                        self.dictTetos["Ano"].append(Ano)
                        self.dictTetos["Mes"].append(Mes)
                        self.dictTetos["Valor"].append(info[index].strip())

        for chave, valor in self.dictTetos.items():
            print(f'{chave}({len(valor)}): {valor}')