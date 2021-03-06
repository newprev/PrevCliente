# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwCadastroCliente(object):
    def setupUi(self, mwCadastroCliente):
        mwCadastroCliente.setObjectName("mwCadastroCliente")
        mwCadastroCliente.resize(1126, 719)
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(True)
        font.setWeight(75)
        mwCadastroCliente.setFont(font)
        mwCadastroCliente.setStyleSheet("#pgCadastro {\n"
"    background-color: #45ADA8;\n"
"}\n"
"\n"
"#lbTitulo {\n"
"    font-family: Ubuntu;\n"
"    color: white;\n"
"\n"
"    font-size: 32px;\n"
"}\n"
"\n"
"#lbSubtitulo {\n"
"    font-family: Ubuntu;\n"
"    color: white;\n"
"\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#lbCnis {\n"
"    font-family: Ubuntu;\n"
"    color: white;\n"
"\n"
"    font-size: 12px;    \n"
"}\n"
"\n"
"#lbQuadroPessoais, #lbQuadroProf, #lbQuadroEndereco {\n"
"    background-color: #45ADA8;\n"
"    margin-left: 3px;\n"
"    color: white;\n"
"    font-family: Ubuntu;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#lbCartProf,  #lbPrimeiroNome,  #lbSobrenome, \n"
"#lbCpg,  #lbRg, #lbEstCivil,  \n"
"#lbNis,  #lbNomeMae,  #lbProf,\n"
"#lbCpf, #lbBairro, #lbCep, \n"
"#lbCidade, #lbComplemento, #lbEndereco, \n"
"#lbEstado {\n"
"    font-family: Ubuntu;\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(mwCadastroCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pgCadastro = QtWidgets.QWidget()
        self.pgCadastro.setStyleSheet("")
        self.pgCadastro.setObjectName("pgCadastro")
        self.lbTitulo = QtWidgets.QLabel(self.pgCadastro)
        self.lbTitulo.setGeometry(QtCore.QRect(20, 10, 311, 51))
        self.lbTitulo.setObjectName("lbTitulo")
        self.lbSubtitulo = QtWidgets.QLabel(self.pgCadastro)
        self.lbSubtitulo.setGeometry(QtCore.QRect(20, 70, 571, 17))
        self.lbSubtitulo.setObjectName("lbSubtitulo")
        self.pbCarregaCnis = QtWidgets.QPushButton(self.pgCadastro)
        self.pbCarregaCnis.setGeometry(QtCore.QRect(990, 60, 111, 25))
        self.pbCarregaCnis.setObjectName("pbCarregaCnis")
        self.lbCnis = QtWidgets.QLabel(self.pgCadastro)
        self.lbCnis.setGeometry(QtCore.QRect(910, 0, 191, 61))
        self.lbCnis.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbCnis.setWordWrap(True)
        self.lbCnis.setObjectName("lbCnis")
        self.frDadosPessoais = QtWidgets.QFrame(self.pgCadastro)
        self.frDadosPessoais.setEnabled(True)
        self.frDadosPessoais.setGeometry(QtCore.QRect(30, 120, 391, 221))
        self.frDadosPessoais.setAcceptDrops(False)
        self.frDadosPessoais.setFrameShape(QtWidgets.QFrame.Panel)
        self.frDadosPessoais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDadosPessoais.setLineWidth(1)
        self.frDadosPessoais.setMidLineWidth(1)
        self.frDadosPessoais.setObjectName("frDadosPessoais")
        self.lbSobrenome = QtWidgets.QLabel(self.frDadosPessoais)
        self.lbSobrenome.setGeometry(QtCore.QRect(200, 20, 161, 17))
        self.lbSobrenome.setObjectName("lbSobrenome")
        self.lbPrimeiroNome = QtWidgets.QLabel(self.frDadosPessoais)
        self.lbPrimeiroNome.setGeometry(QtCore.QRect(20, 20, 161, 17))
        self.lbPrimeiroNome.setObjectName("lbPrimeiroNome")
        self.leNomeMae = QtWidgets.QLineEdit(self.frDadosPessoais)
        self.leNomeMae.setGeometry(QtCore.QRect(200, 170, 161, 25))
        self.leNomeMae.setText("")
        self.leNomeMae.setObjectName("leNomeMae")
        self.lbRg = QtWidgets.QLabel(self.frDadosPessoais)
        self.lbRg.setGeometry(QtCore.QRect(20, 80, 161, 17))
        self.lbRg.setObjectName("lbRg")
        self.leRg = QtWidgets.QLineEdit(self.frDadosPessoais)
        self.leRg.setGeometry(QtCore.QRect(20, 100, 161, 25))
        self.leRg.setText("")
        self.leRg.setObjectName("leRg")
        self.lbCpf = QtWidgets.QLabel(self.frDadosPessoais)
        self.lbCpf.setGeometry(QtCore.QRect(200, 80, 161, 17))
        self.lbCpf.setObjectName("lbCpf")
        self.lbEstCivil = QtWidgets.QLabel(self.frDadosPessoais)
        self.lbEstCivil.setGeometry(QtCore.QRect(20, 150, 161, 17))
        self.lbEstCivil.setObjectName("lbEstCivil")
        self.leSobrenome = QtWidgets.QLineEdit(self.frDadosPessoais)
        self.leSobrenome.setGeometry(QtCore.QRect(200, 40, 161, 25))
        self.leSobrenome.setObjectName("leSobrenome")
        self.lbNomeMae = QtWidgets.QLabel(self.frDadosPessoais)
        self.lbNomeMae.setGeometry(QtCore.QRect(200, 150, 161, 17))
        self.lbNomeMae.setObjectName("lbNomeMae")
        self.lePrimeiroNome = QtWidgets.QLineEdit(self.frDadosPessoais)
        self.lePrimeiroNome.setGeometry(QtCore.QRect(20, 40, 161, 25))
        self.lePrimeiroNome.setObjectName("lePrimeiroNome")
        self.leCpf = QtWidgets.QLineEdit(self.frDadosPessoais)
        self.leCpf.setGeometry(QtCore.QRect(200, 100, 161, 25))
        self.leCpf.setText("")
        self.leCpf.setObjectName("leCpf")
        self.cbxEstCivil = QtWidgets.QComboBox(self.frDadosPessoais)
        self.cbxEstCivil.setGeometry(QtCore.QRect(20, 170, 161, 25))
        self.cbxEstCivil.setObjectName("cbxEstCivil")
        self.lbQuadroPessoais = QtWidgets.QLabel(self.pgCadastro)
        self.lbQuadroPessoais.setGeometry(QtCore.QRect(40, 110, 111, 17))
        self.lbQuadroPessoais.setObjectName("lbQuadroPessoais")
        self.frDadosProf = QtWidgets.QFrame(self.pgCadastro)
        self.frDadosProf.setGeometry(QtCore.QRect(30, 380, 391, 161))
        self.frDadosProf.setFrameShape(QtWidgets.QFrame.Panel)
        self.frDadosProf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDadosProf.setMidLineWidth(1)
        self.frDadosProf.setObjectName("frDadosProf")
        self.lbNis = QtWidgets.QLabel(self.frDadosProf)
        self.lbNis.setGeometry(QtCore.QRect(210, 30, 161, 17))
        self.lbNis.setObjectName("lbNis")
        self.leProf = QtWidgets.QLineEdit(self.frDadosProf)
        self.leProf.setGeometry(QtCore.QRect(10, 110, 161, 25))
        self.leProf.setText("")
        self.leProf.setObjectName("leProf")
        self.lbProf = QtWidgets.QLabel(self.frDadosProf)
        self.lbProf.setGeometry(QtCore.QRect(10, 90, 161, 17))
        self.lbProf.setObjectName("lbProf")
        self.lbCartProf = QtWidgets.QLabel(self.frDadosProf)
        self.lbCartProf.setGeometry(QtCore.QRect(10, 30, 161, 17))
        self.lbCartProf.setObjectName("lbCartProf")
        self.leCartProf = QtWidgets.QLineEdit(self.frDadosProf)
        self.leCartProf.setGeometry(QtCore.QRect(10, 50, 161, 25))
        self.leCartProf.setText("")
        self.leCartProf.setObjectName("leCartProf")
        self.leNis = QtWidgets.QLineEdit(self.frDadosProf)
        self.leNis.setGeometry(QtCore.QRect(210, 50, 161, 25))
        self.leNis.setText("")
        self.leNis.setObjectName("leNis")
        self.lbQuadroProf = QtWidgets.QLabel(self.pgCadastro)
        self.lbQuadroProf.setGeometry(QtCore.QRect(50, 370, 141, 17))
        self.lbQuadroProf.setObjectName("lbQuadroProf")
        self.frDadosProf_2 = QtWidgets.QFrame(self.pgCadastro)
        self.frDadosProf_2.setGeometry(QtCore.QRect(450, 120, 391, 221))
        self.frDadosProf_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frDadosProf_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDadosProf_2.setMidLineWidth(1)
        self.frDadosProf_2.setObjectName("frDadosProf_2")
        self.lbEstado = QtWidgets.QLabel(self.frDadosProf_2)
        self.lbEstado.setGeometry(QtCore.QRect(210, 80, 161, 17))
        self.lbEstado.setObjectName("lbEstado")
        self.leCidade = QtWidgets.QLineEdit(self.frDadosProf_2)
        self.leCidade.setGeometry(QtCore.QRect(10, 100, 161, 25))
        self.leCidade.setText("")
        self.leCidade.setObjectName("leCidade")
        self.lbCidade = QtWidgets.QLabel(self.frDadosProf_2)
        self.lbCidade.setGeometry(QtCore.QRect(10, 80, 161, 17))
        self.lbCidade.setObjectName("lbCidade")
        self.lbEndereco = QtWidgets.QLabel(self.frDadosProf_2)
        self.lbEndereco.setGeometry(QtCore.QRect(210, 20, 161, 17))
        self.lbEndereco.setObjectName("lbEndereco")
        self.leEndereco = QtWidgets.QLineEdit(self.frDadosProf_2)
        self.leEndereco.setGeometry(QtCore.QRect(210, 40, 161, 25))
        self.leEndereco.setText("")
        self.leEndereco.setObjectName("leEndereco")
        self.cbxEstado = QtWidgets.QComboBox(self.frDadosProf_2)
        self.cbxEstado.setGeometry(QtCore.QRect(210, 100, 161, 25))
        self.cbxEstado.setObjectName("cbxEstado")
        self.leCep = QtWidgets.QLineEdit(self.frDadosProf_2)
        self.leCep.setGeometry(QtCore.QRect(10, 40, 161, 25))
        self.leCep.setText("")
        self.leCep.setObjectName("leCep")
        self.lbCep = QtWidgets.QLabel(self.frDadosProf_2)
        self.lbCep.setGeometry(QtCore.QRect(10, 20, 161, 17))
        self.lbCep.setObjectName("lbCep")
        self.leBairro = QtWidgets.QLineEdit(self.frDadosProf_2)
        self.leBairro.setGeometry(QtCore.QRect(10, 160, 161, 25))
        self.leBairro.setText("")
        self.leBairro.setObjectName("leBairro")
        self.lbBairro = QtWidgets.QLabel(self.frDadosProf_2)
        self.lbBairro.setGeometry(QtCore.QRect(10, 140, 161, 17))
        self.lbBairro.setObjectName("lbBairro")
        self.leComplemento = QtWidgets.QLineEdit(self.frDadosProf_2)
        self.leComplemento.setGeometry(QtCore.QRect(210, 160, 161, 25))
        self.leComplemento.setText("")
        self.leComplemento.setObjectName("leComplemento")
        self.lbComplemento = QtWidgets.QLabel(self.frDadosProf_2)
        self.lbComplemento.setGeometry(QtCore.QRect(210, 140, 161, 17))
        self.lbComplemento.setObjectName("lbComplemento")
        self.lbQuadroEndereco = QtWidgets.QLabel(self.pgCadastro)
        self.lbQuadroEndereco.setGeometry(QtCore.QRect(460, 110, 131, 17))
        self.lbQuadroEndereco.setObjectName("lbQuadroEndereco")
        self.frDadosPessoais.raise_()
        self.lbTitulo.raise_()
        self.lbSubtitulo.raise_()
        self.pbCarregaCnis.raise_()
        self.lbCnis.raise_()
        self.lbQuadroPessoais.raise_()
        self.frDadosProf.raise_()
        self.lbQuadroProf.raise_()
        self.frDadosProf_2.raise_()
        self.lbQuadroEndereco.raise_()
        self.stackedWidget.addWidget(self.pgCadastro)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        mwCadastroCliente.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mwCadastroCliente)
        self.statusbar.setObjectName("statusbar")
        mwCadastroCliente.setStatusBar(self.statusbar)

        self.retranslateUi(mwCadastroCliente)
        QtCore.QMetaObject.connectSlotsByName(mwCadastroCliente)

    def retranslateUi(self, mwCadastroCliente):
        _translate = QtCore.QCoreApplication.translate
        mwCadastroCliente.setWindowTitle(_translate("mwCadastroCliente", "MainWindow"))
        self.lbTitulo.setText(_translate("mwCadastroCliente", "Cadastro de clientes"))
        self.lbSubtitulo.setText(_translate("mwCadastroCliente", "Cadastre seus clientes e não perca o controle dos dados e das datas das ações."))
        self.pbCarregaCnis.setText(_translate("mwCadastroCliente", "Carregar CNIS"))
        self.lbCnis.setText(_translate("mwCadastroCliente", "Caso queira carregar as informações principais pelo CNIS"))
        self.lbSobrenome.setText(_translate("mwCadastroCliente", "Sobrenome"))
        self.lbPrimeiroNome.setText(_translate("mwCadastroCliente", "Primeiro nome"))
        self.leNomeMae.setPlaceholderText(_translate("mwCadastroCliente", "Cleusa da Silva"))
        self.lbRg.setText(_translate("mwCadastroCliente", "RG"))
        self.leRg.setPlaceholderText(_translate("mwCadastroCliente", "12.345.678-9"))
        self.lbCpf.setText(_translate("mwCadastroCliente", "CPF"))
        self.lbEstCivil.setText(_translate("mwCadastroCliente", "Estado civil"))
        self.leSobrenome.setPlaceholderText(_translate("mwCadastroCliente", "da Silva Moraes"))
        self.lbNomeMae.setText(_translate("mwCadastroCliente", "Nome da mãe"))
        self.lePrimeiroNome.setPlaceholderText(_translate("mwCadastroCliente", "José"))
        self.leCpf.setPlaceholderText(_translate("mwCadastroCliente", "123.456.789-00"))
        self.lbQuadroPessoais.setText(_translate("mwCadastroCliente", "Dados pessoais"))
        self.lbNis.setText(_translate("mwCadastroCliente", "NIS/NIT"))
        self.lbProf.setText(_translate("mwCadastroCliente", "Profissão"))
        self.lbCartProf.setText(_translate("mwCadastroCliente", "Carteira profissional"))
        self.lbQuadroProf.setText(_translate("mwCadastroCliente", "Dados Profissionais"))
        self.lbEstado.setText(_translate("mwCadastroCliente", "Estado"))
        self.leCidade.setPlaceholderText(_translate("mwCadastroCliente", "São Paulo"))
        self.lbCidade.setText(_translate("mwCadastroCliente", "Cidade"))
        self.lbEndereco.setText(_translate("mwCadastroCliente", "Endereço"))
        self.leEndereco.setPlaceholderText(_translate("mwCadastroCliente", "Av. Paulista, 745"))
        self.leCep.setPlaceholderText(_translate("mwCadastroCliente", "12345-678"))
        self.lbCep.setText(_translate("mwCadastroCliente", "CEP"))
        self.leBairro.setPlaceholderText(_translate("mwCadastroCliente", "Bela Vista"))
        self.lbBairro.setText(_translate("mwCadastroCliente", "Bairro"))
        self.leComplemento.setPlaceholderText(_translate("mwCadastroCliente", "Bloco A, Apto. 65"))
        self.lbComplemento.setText(_translate("mwCadastroCliente", "Complemento"))
        self.lbQuadroEndereco.setText(_translate("mwCadastroCliente", "Dados de moradia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwCadastroCliente = QtWidgets.QMainWindow()
    ui = Ui_mwCadastroCliente()
    ui.setupUi(mwCadastroCliente)
    mwCadastroCliente.show()
    sys.exit(app.exec_())
