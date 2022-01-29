# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/newEntrevistaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgEntrevistaPrincipal(object):
    def setupUi(self, wdgEntrevistaPrincipal):
        wdgEntrevistaPrincipal.setObjectName("wdgEntrevistaPrincipal")
        wdgEntrevistaPrincipal.resize(1148, 568)
        wdgEntrevistaPrincipal.setStyleSheet("#wdgCadastroCliente {\n"
"    background-color: white;\n"
"}\n"
"\n"
"#frCabecalho, #frMiolo, #frRodape {\n"
"    background-color: white;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(wdgEntrevistaPrincipal)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frPrincipal = QtWidgets.QFrame(wdgEntrevistaPrincipal)
        self.frPrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frPrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPrincipal.setObjectName("frPrincipal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frPrincipal)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frCabecalho = QtWidgets.QFrame(self.frPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frCabecalho.sizePolicy().hasHeightForWidth())
        self.frCabecalho.setSizePolicy(sizePolicy)
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 160))
        self.frCabecalho.setStyleSheet("/*------------------------------------------- Frame -------------------------------------------*/\n"
"#frPrimeiraEtapa {\n"
"    border-radius: 8px;\n"
"    background-color: #009E38;\n"
"}\n"
"\n"
"#frSegundaEtapa, #frTerceiraEtapa, \n"
"#frQuartaEtapa, #frQuintaEtapa {\n"
"    border-radius: 8px;\n"
"    background-color: #CFF2DC;\n"
"}\n"
"\n"
"#frSeparador1, #frSeparador2, #frSeparador3, #frSeparador4 {\n"
"    background-color: lightgrey;\n"
"}\n"
"\n"
"/*------------------------------------------- Push Button -------------------------------------------*/\n"
"#pbVoltar {\n"
"    background-image: url(:/voltar/back.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: #F4F5F8;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#pbVoltar:hover {\n"
"    background-image: url(:/voltar/back.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: rgb(228, 233, 248);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"/*------------------------------------------- Label -------------------------------------------*/\n"
"#lbInfoTitulo {\n"
"    font: 16pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"#lbInfoNatureza, #lbInfoTpBeneficio,\n"
"#lbInfoTpProcesso, #lbInfoEntrevista {\n"
"    font: 10pt \"Avenir LT Std\";\n"
"    color: black;\n"
"    padding: 4px;\n"
"}")
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frCabecalho)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frTitulo = QtWidgets.QFrame(self.frCabecalho)
        self.frTitulo.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frTitulo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTitulo.setObjectName("frTitulo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frTitulo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbVoltar = QtWidgets.QPushButton(self.frTitulo)
        self.pbVoltar.setMinimumSize(QtCore.QSize(40, 40))
        self.pbVoltar.setMaximumSize(QtCore.QSize(40, 40))
        self.pbVoltar.setText("")
        self.pbVoltar.setObjectName("pbVoltar")
        self.horizontalLayout.addWidget(self.pbVoltar)
        self.lbInfoTitulo = QtWidgets.QLabel(self.frTitulo)
        self.lbInfoTitulo.setObjectName("lbInfoTitulo")
        self.horizontalLayout.addWidget(self.lbInfoTitulo)
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frMigalhas = QtWidgets.QFrame(self.frTitulo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMigalhas.sizePolicy().hasHeightForWidth())
        self.frMigalhas.setSizePolicy(sizePolicy)
        self.frMigalhas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMigalhas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMigalhas.setObjectName("frMigalhas")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frMigalhas)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frMigalhas)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frPrimeiraEtapa = QtWidgets.QFrame(self.frame)
        self.frPrimeiraEtapa.setMinimumSize(QtCore.QSize(16, 16))
        self.frPrimeiraEtapa.setMaximumSize(QtCore.QSize(16, 16))
        self.frPrimeiraEtapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frPrimeiraEtapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPrimeiraEtapa.setObjectName("frPrimeiraEtapa")
        self.verticalLayout_3.addWidget(self.frPrimeiraEtapa)
        spacerItem1 = QtWidgets.QSpacerItem(16, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frSeparador1 = QtWidgets.QFrame(self.frame_4)
        self.frSeparador1.setMinimumSize(QtCore.QSize(70, 0))
        self.frSeparador1.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frSeparador1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSeparador1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSeparador1.setObjectName("frSeparador1")
        self.verticalLayout_4.addWidget(self.frSeparador1)
        self.lbInfoNatureza = QtWidgets.QLabel(self.frame_4)
        self.lbInfoNatureza.setObjectName("lbInfoNatureza")
        self.verticalLayout_4.addWidget(self.lbInfoNatureza, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frSegundaEtapa = QtWidgets.QFrame(self.frame_3)
        self.frSegundaEtapa.setMinimumSize(QtCore.QSize(16, 16))
        self.frSegundaEtapa.setMaximumSize(QtCore.QSize(16, 16))
        self.frSegundaEtapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSegundaEtapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSegundaEtapa.setObjectName("frSegundaEtapa")
        self.verticalLayout_5.addWidget(self.frSegundaEtapa)
        spacerItem2 = QtWidgets.QSpacerItem(16, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_6 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frSeparador2 = QtWidgets.QFrame(self.frame_6)
        self.frSeparador2.setMinimumSize(QtCore.QSize(70, 0))
        self.frSeparador2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frSeparador2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSeparador2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSeparador2.setObjectName("frSeparador2")
        self.verticalLayout_6.addWidget(self.frSeparador2)
        self.lbInfoTpBeneficio = QtWidgets.QLabel(self.frame_6)
        self.lbInfoTpBeneficio.setObjectName("lbInfoTpBeneficio")
        self.verticalLayout_6.addWidget(self.lbInfoTpBeneficio, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frTerceiraEtapa = QtWidgets.QFrame(self.frame_7)
        self.frTerceiraEtapa.setMinimumSize(QtCore.QSize(16, 16))
        self.frTerceiraEtapa.setMaximumSize(QtCore.QSize(16, 16))
        self.frTerceiraEtapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTerceiraEtapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTerceiraEtapa.setObjectName("frTerceiraEtapa")
        self.verticalLayout_7.addWidget(self.frTerceiraEtapa)
        spacerItem3 = QtWidgets.QSpacerItem(16, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frSeparador3 = QtWidgets.QFrame(self.frame_5)
        self.frSeparador3.setMinimumSize(QtCore.QSize(70, 0))
        self.frSeparador3.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frSeparador3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSeparador3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSeparador3.setObjectName("frSeparador3")
        self.verticalLayout_8.addWidget(self.frSeparador3)
        self.lbInfoTpProcesso = QtWidgets.QLabel(self.frame_5)
        self.lbInfoTpProcesso.setObjectName("lbInfoTpProcesso")
        self.verticalLayout_8.addWidget(self.lbInfoTpProcesso, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frQuartaEtapa = QtWidgets.QFrame(self.frame_8)
        self.frQuartaEtapa.setMinimumSize(QtCore.QSize(16, 16))
        self.frQuartaEtapa.setMaximumSize(QtCore.QSize(16, 16))
        self.frQuartaEtapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frQuartaEtapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frQuartaEtapa.setObjectName("frQuartaEtapa")
        self.verticalLayout_9.addWidget(self.frQuartaEtapa)
        spacerItem4 = QtWidgets.QSpacerItem(16, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_14 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frSeparador4 = QtWidgets.QFrame(self.frame_14)
        self.frSeparador4.setMinimumSize(QtCore.QSize(70, 0))
        self.frSeparador4.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frSeparador4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSeparador4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSeparador4.setObjectName("frSeparador4")
        self.verticalLayout_11.addWidget(self.frSeparador4)
        self.lbInfoEntrevista = QtWidgets.QLabel(self.frame_14)
        self.lbInfoEntrevista.setObjectName("lbInfoEntrevista")
        self.verticalLayout_11.addWidget(self.lbInfoEntrevista)
        self.horizontalLayout_2.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frMigalhas)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frQuintaEtapa = QtWidgets.QFrame(self.frame_15)
        self.frQuintaEtapa.setMinimumSize(QtCore.QSize(16, 16))
        self.frQuintaEtapa.setMaximumSize(QtCore.QSize(16, 16))
        self.frQuintaEtapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frQuintaEtapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frQuintaEtapa.setObjectName("frQuintaEtapa")
        self.verticalLayout_12.addWidget(self.frQuintaEtapa)
        spacerItem5 = QtWidgets.QSpacerItem(16, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.horizontalLayout_2.addWidget(self.frame_15)
        self.horizontalLayout.addWidget(self.frMigalhas)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addWidget(self.frTitulo, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frCabecalho)
        self.frMiolo = QtWidgets.QFrame(self.frPrincipal)
        self.frMiolo.setStyleSheet("/*-------------------------------------------  Stack --------------------------------------------*/\n"
"#stkCliente {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/*-------------------------------------------  Widget --------------------------------------------*/\n"
"#pgNatureza, #pgTpBeneficio, #pgTpProcesso {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/*-------------------------------------------  Label --------------------------------------------*/\n"
"#lbTituloNatureza, #lbTituloTpBeneficio, \n"
"#lbTituloTpProcesso {\n"
"    font: 14pt \"Avenir LT Std\";\n"
"    color: #1F1E29;\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"#lbDescNatureza, #lbDescTpBeneficio, \n"
"#lbDescTpProcesso {\n"
"    font: 11pt \"Avenir LT Std\";\n"
"    color: #1F1E29;\n"
"}\n"
"\n"
"#lbNatureza, #lbInfoPessoais,\n"
"#lbTpBeneficio, #lbTpProcesso {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"#lbNaturezaEscolhida, #lbTpBeneEscolhido, \n"
"#lbTpProcEscolhido {\n"
"    font: 11pt \"Avenir LT Std\";\n"
"    color: black;\n"
"}\n"
"\n"
"#lbInfoNome, #lbInfoCpf,\n"
"#lbInfoDataNascimento {\n"
"    font: 11pt \"Avenir LT Std\";\n"
"    color: black;\n"
"\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"#lbNome, #lbCpf,\n"
"#lbDataNascimento {\n"
"    font: 11pt \"Avenir LT Std\";\n"
"    color: black;\n"
"\n"
"}\n"
"\n"
"/* ------------------------------------ Frames ------------------------------------*/\n"
"#frInfoNatureza, #frInfoPessoais,\n"
"#frInfoTpBeneficio, #frInfoTpProcesso {\n"
"    background-color: #F9F9F9;\n"
"    border: 0px solid none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/*---------------------------- Push Button ----------------------------------*/\n"
"\n"
"\n"
"/*----------------------------  Line Edit ---------------------------------------*/\n"
"\n"
"\n"
"/*------------------------------ Radio Button -------------------------------------*/\n"
"\n"
"\n"
"/*------------------------------ Check Box -------------------------------------*/\n"
"\n"
"\n"
"/*----------------------------- Combo box --------------------------------------*/\n"
"\n"
"\n"
"/*----------------------------- Date Edit --------------------------------------*/\n"
"")
        self.frMiolo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMiolo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMiolo.setObjectName("frMiolo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frMiolo)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frEsquerda = QtWidgets.QFrame(self.frMiolo)
        self.frEsquerda.setMinimumSize(QtCore.QSize(350, 0))
        self.frEsquerda.setStyleSheet("")
        self.frEsquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEsquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEsquerda.setObjectName("frEsquerda")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frEsquerda)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frInfoHistPessoais = QtWidgets.QFrame(self.frEsquerda)
        self.frInfoHistPessoais.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoHistPessoais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoHistPessoais.setObjectName("frInfoHistPessoais")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frInfoHistPessoais)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbInfoDataNascimento = QtWidgets.QLabel(self.frInfoHistPessoais)
        self.lbInfoDataNascimento.setObjectName("lbInfoDataNascimento")
        self.gridLayout_2.addWidget(self.lbInfoDataNascimento, 3, 0, 1, 1)
        self.lbInfoNome = QtWidgets.QLabel(self.frInfoHistPessoais)
        self.lbInfoNome.setObjectName("lbInfoNome")
        self.gridLayout_2.addWidget(self.lbInfoNome, 1, 0, 1, 1)
        self.lbInfoCpf = QtWidgets.QLabel(self.frInfoHistPessoais)
        self.lbInfoCpf.setObjectName("lbInfoCpf")
        self.gridLayout_2.addWidget(self.lbInfoCpf, 2, 0, 1, 1)
        self.lbNome = QtWidgets.QLabel(self.frInfoHistPessoais)
        self.lbNome.setObjectName("lbNome")
        self.gridLayout_2.addWidget(self.lbNome, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.lbCpf = QtWidgets.QLabel(self.frInfoHistPessoais)
        self.lbCpf.setObjectName("lbCpf")
        self.gridLayout_2.addWidget(self.lbCpf, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.lbDataNascimento = QtWidgets.QLabel(self.frInfoHistPessoais)
        self.lbDataNascimento.setObjectName("lbDataNascimento")
        self.gridLayout_2.addWidget(self.lbDataNascimento, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.frInfoPessoais = QtWidgets.QFrame(self.frInfoHistPessoais)
        self.frInfoPessoais.setMinimumSize(QtCore.QSize(250, 0))
        self.frInfoPessoais.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frInfoPessoais.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoPessoais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoPessoais.setObjectName("frInfoPessoais")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frInfoPessoais)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbInfoPessoais = QtWidgets.QLabel(self.frInfoPessoais)
        self.lbInfoPessoais.setObjectName("lbInfoPessoais")
        self.horizontalLayout_6.addWidget(self.lbInfoPessoais)
        self.gridLayout_2.addWidget(self.frInfoPessoais, 0, 0, 1, 2)
        self.verticalLayout_15.addWidget(self.frInfoHistPessoais)
        self.frNaturezaHist = QtWidgets.QFrame(self.frEsquerda)
        self.frNaturezaHist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frNaturezaHist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNaturezaHist.setObjectName("frNaturezaHist")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frNaturezaHist)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frInfoNatureza = QtWidgets.QFrame(self.frNaturezaHist)
        self.frInfoNatureza.setMinimumSize(QtCore.QSize(250, 0))
        self.frInfoNatureza.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frInfoNatureza.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoNatureza.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoNatureza.setObjectName("frInfoNatureza")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frInfoNatureza)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbNatureza = QtWidgets.QLabel(self.frInfoNatureza)
        self.lbNatureza.setObjectName("lbNatureza")
        self.horizontalLayout_5.addWidget(self.lbNatureza)
        self.verticalLayout_14.addWidget(self.frInfoNatureza)
        self.lbNaturezaEscolhida = QtWidgets.QLabel(self.frNaturezaHist)
        self.lbNaturezaEscolhida.setObjectName("lbNaturezaEscolhida")
        self.verticalLayout_14.addWidget(self.lbNaturezaEscolhida, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_15.addWidget(self.frNaturezaHist)
        self.frTpBeneficioHist = QtWidgets.QFrame(self.frEsquerda)
        self.frTpBeneficioHist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTpBeneficioHist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTpBeneficioHist.setObjectName("frTpBeneficioHist")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frTpBeneficioHist)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frInfoTpBeneficio = QtWidgets.QFrame(self.frTpBeneficioHist)
        self.frInfoTpBeneficio.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoTpBeneficio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoTpBeneficio.setObjectName("frInfoTpBeneficio")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frInfoTpBeneficio)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.lbTpBeneficio = QtWidgets.QLabel(self.frInfoTpBeneficio)
        self.lbTpBeneficio.setObjectName("lbTpBeneficio")
        self.verticalLayout_17.addWidget(self.lbTpBeneficio)
        self.verticalLayout_16.addWidget(self.frInfoTpBeneficio)
        self.lbTpBeneEscolhido = QtWidgets.QLabel(self.frTpBeneficioHist)
        self.lbTpBeneEscolhido.setWordWrap(True)
        self.lbTpBeneEscolhido.setObjectName("lbTpBeneEscolhido")
        self.verticalLayout_16.addWidget(self.lbTpBeneEscolhido)
        self.verticalLayout_15.addWidget(self.frTpBeneficioHist)
        self.frTpProcessoHist = QtWidgets.QFrame(self.frEsquerda)
        self.frTpProcessoHist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTpProcessoHist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTpProcessoHist.setObjectName("frTpProcessoHist")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frTpProcessoHist)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frInfoTpProcesso = QtWidgets.QFrame(self.frTpProcessoHist)
        self.frInfoTpProcesso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoTpProcesso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoTpProcesso.setObjectName("frInfoTpProcesso")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frInfoTpProcesso)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lbTpProcesso = QtWidgets.QLabel(self.frInfoTpProcesso)
        self.lbTpProcesso.setObjectName("lbTpProcesso")
        self.verticalLayout_19.addWidget(self.lbTpProcesso)
        self.verticalLayout_18.addWidget(self.frInfoTpProcesso)
        self.lbTpProcEscolhido = QtWidgets.QLabel(self.frTpProcessoHist)
        self.lbTpProcEscolhido.setObjectName("lbTpProcEscolhido")
        self.verticalLayout_18.addWidget(self.lbTpProcEscolhido)
        self.verticalLayout_15.addWidget(self.frTpProcessoHist)
        self.frEntrevistaHist = QtWidgets.QFrame(self.frEsquerda)
        self.frEntrevistaHist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEntrevistaHist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEntrevistaHist.setObjectName("frEntrevistaHist")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frEntrevistaHist)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frInfoEntrevista = QtWidgets.QFrame(self.frEntrevistaHist)
        self.frInfoEntrevista.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoEntrevista.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoEntrevista.setObjectName("frInfoEntrevista")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frInfoEntrevista)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.lbEntrevista = QtWidgets.QLabel(self.frInfoEntrevista)
        self.lbEntrevista.setObjectName("lbEntrevista")
        self.verticalLayout_21.addWidget(self.lbEntrevista)
        self.verticalLayout_20.addWidget(self.frInfoEntrevista)
        self.glQuizEntrevista = QtWidgets.QGridLayout()
        self.glQuizEntrevista.setObjectName("glQuizEntrevista")
        self.verticalLayout_20.addLayout(self.glQuizEntrevista)
        self.verticalLayout_15.addWidget(self.frEntrevistaHist)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem7)
        self.horizontalLayout_4.addWidget(self.frEsquerda)
        self.stkEntrevista = QtWidgets.QStackedWidget(self.frMiolo)
        self.stkEntrevista.setMaximumSize(QtCore.QSize(16548745, 16777215))
        self.stkEntrevista.setObjectName("stkEntrevista")
        self.pgNatureza = QtWidgets.QWidget()
        self.pgNatureza.setObjectName("pgNatureza")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pgNatureza)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frDireita = QtWidgets.QFrame(self.pgNatureza)
        self.frDireita.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frDireita.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frDireita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDireita.setObjectName("frDireita")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frDireita)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem8)
        self.vlNaturezas = QtWidgets.QVBoxLayout()
        self.vlNaturezas.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.vlNaturezas.setSpacing(4)
        self.vlNaturezas.setObjectName("vlNaturezas")
        self.verticalLayout_13.addLayout(self.vlNaturezas)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem9)
        self.lbTituloNatureza = QtWidgets.QLabel(self.frDireita)
        self.lbTituloNatureza.setMinimumSize(QtCore.QSize(0, 20))
        self.lbTituloNatureza.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbTituloNatureza.setObjectName("lbTituloNatureza")
        self.verticalLayout_13.addWidget(self.lbTituloNatureza)
        self.lbDescNatureza = QtWidgets.QLabel(self.frDireita)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbDescNatureza.sizePolicy().hasHeightForWidth())
        self.lbDescNatureza.setSizePolicy(sizePolicy)
        self.lbDescNatureza.setWordWrap(True)
        self.lbDescNatureza.setObjectName("lbDescNatureza")
        self.verticalLayout_13.addWidget(self.lbDescNatureza, 0, QtCore.Qt.AlignTop)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem10)
        self.horizontalLayout_3.addWidget(self.frDireita)
        self.stkEntrevista.addWidget(self.pgNatureza)
        self.pgTpBeneficio = QtWidgets.QWidget()
        self.pgTpBeneficio.setObjectName("pgTpBeneficio")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.pgTpBeneficio)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_7.setHorizontalSpacing(32)
        self.gridLayout_7.setVerticalSpacing(16)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frTpBenePrincipal = QtWidgets.QFrame(self.pgTpBeneficio)
        self.frTpBenePrincipal.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frTpBenePrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTpBenePrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTpBenePrincipal.setObjectName("frTpBenePrincipal")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frTpBenePrincipal)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.vlTpBeneficio = QtWidgets.QVBoxLayout()
        self.vlTpBeneficio.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.vlTpBeneficio.setObjectName("vlTpBeneficio")
        self.verticalLayout_10.addLayout(self.vlTpBeneficio)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem11)
        self.lbTituloTpBeneficio = QtWidgets.QLabel(self.frTpBenePrincipal)
        self.lbTituloTpBeneficio.setMinimumSize(QtCore.QSize(0, 20))
        self.lbTituloTpBeneficio.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbTituloTpBeneficio.setObjectName("lbTituloTpBeneficio")
        self.verticalLayout_10.addWidget(self.lbTituloTpBeneficio)
        self.lbDescTpBeneficio = QtWidgets.QLabel(self.frTpBenePrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbDescTpBeneficio.sizePolicy().hasHeightForWidth())
        self.lbDescTpBeneficio.setSizePolicy(sizePolicy)
        self.lbDescTpBeneficio.setWordWrap(True)
        self.lbDescTpBeneficio.setObjectName("lbDescTpBeneficio")
        self.verticalLayout_10.addWidget(self.lbDescTpBeneficio, 0, QtCore.Qt.AlignTop)
        spacerItem12 = QtWidgets.QSpacerItem(20, 351, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem12)
        self.gridLayout_7.addWidget(self.frTpBenePrincipal, 0, 0, 1, 1)
        self.stkEntrevista.addWidget(self.pgTpBeneficio)
        self.pgTpProcesso = QtWidgets.QWidget()
        self.pgTpProcesso.setObjectName("pgTpProcesso")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.pgTpProcesso)
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_8.setHorizontalSpacing(32)
        self.gridLayout_8.setVerticalSpacing(16)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frTpProcessoPrincipal = QtWidgets.QFrame(self.pgTpProcesso)
        self.frTpProcessoPrincipal.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frTpProcessoPrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTpProcessoPrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTpProcessoPrincipal.setObjectName("frTpProcessoPrincipal")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frTpProcessoPrincipal)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.vlTpProcesso = QtWidgets.QVBoxLayout()
        self.vlTpProcesso.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.vlTpProcesso.setObjectName("vlTpProcesso")
        self.verticalLayout_22.addLayout(self.vlTpProcesso)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem13)
        self.lbTituloTpProcesso = QtWidgets.QLabel(self.frTpProcessoPrincipal)
        self.lbTituloTpProcesso.setMinimumSize(QtCore.QSize(0, 20))
        self.lbTituloTpProcesso.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbTituloTpProcesso.setObjectName("lbTituloTpProcesso")
        self.verticalLayout_22.addWidget(self.lbTituloTpProcesso)
        self.lbDescTpProcesso = QtWidgets.QLabel(self.frTpProcessoPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbDescTpProcesso.sizePolicy().hasHeightForWidth())
        self.lbDescTpProcesso.setSizePolicy(sizePolicy)
        self.lbDescTpProcesso.setWordWrap(True)
        self.lbDescTpProcesso.setObjectName("lbDescTpProcesso")
        self.verticalLayout_22.addWidget(self.lbDescTpProcesso)
        spacerItem14 = QtWidgets.QSpacerItem(20, 351, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem14)
        self.gridLayout_8.addWidget(self.frTpProcessoPrincipal, 0, 0, 1, 1)
        self.stkEntrevista.addWidget(self.pgTpProcesso)
        self.horizontalLayout_4.addWidget(self.stkEntrevista)
        self.verticalLayout.addWidget(self.frMiolo)
        self.gridLayout.addWidget(self.frPrincipal, 0, 0, 1, 1)

        self.retranslateUi(wdgEntrevistaPrincipal)
        self.stkEntrevista.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgEntrevistaPrincipal)

    def retranslateUi(self, wdgEntrevistaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        wdgEntrevistaPrincipal.setWindowTitle(_translate("wdgEntrevistaPrincipal", "Form"))
        self.lbInfoTitulo.setText(_translate("wdgEntrevistaPrincipal", "Entrevista"))
        self.lbInfoNatureza.setText(_translate("wdgEntrevistaPrincipal", "Natureza do processo"))
        self.lbInfoTpBeneficio.setText(_translate("wdgEntrevistaPrincipal", "Tipo do benefício"))
        self.lbInfoTpProcesso.setText(_translate("wdgEntrevistaPrincipal", "Tipo de processo"))
        self.lbInfoEntrevista.setText(_translate("wdgEntrevistaPrincipal", "Entrevista"))
        self.lbInfoDataNascimento.setText(_translate("wdgEntrevistaPrincipal", "Data de nascimento:"))
        self.lbInfoNome.setText(_translate("wdgEntrevistaPrincipal", "Nome completo:"))
        self.lbInfoCpf.setText(_translate("wdgEntrevistaPrincipal", "CPF:"))
        self.lbNome.setText(_translate("wdgEntrevistaPrincipal", "Nome"))
        self.lbCpf.setText(_translate("wdgEntrevistaPrincipal", "cpf"))
        self.lbDataNascimento.setText(_translate("wdgEntrevistaPrincipal", "dataNascimento"))
        self.lbInfoPessoais.setText(_translate("wdgEntrevistaPrincipal", "Informações pessoais"))
        self.lbNatureza.setText(_translate("wdgEntrevistaPrincipal", "Natureza do processo"))
        self.lbNaturezaEscolhida.setText(_translate("wdgEntrevistaPrincipal", "Administrativo"))
        self.lbTpBeneficio.setText(_translate("wdgEntrevistaPrincipal", "Tipo do benefício"))
        self.lbTpBeneEscolhido.setText(_translate("wdgEntrevistaPrincipal", "Aposentadoria"))
        self.lbTpProcesso.setText(_translate("wdgEntrevistaPrincipal", "Tipo de processo"))
        self.lbTpProcEscolhido.setText(_translate("wdgEntrevistaPrincipal", "Concessão"))
        self.lbEntrevista.setText(_translate("wdgEntrevistaPrincipal", "Tipo de processo"))
        self.lbTituloNatureza.setText(_translate("wdgEntrevistaPrincipal", "Titulo Natureza"))
        self.lbDescNatureza.setText(_translate("wdgEntrevistaPrincipal", "Descricao"))
        self.lbTituloTpBeneficio.setText(_translate("wdgEntrevistaPrincipal", "Titulo Beneficio"))
        self.lbDescTpBeneficio.setText(_translate("wdgEntrevistaPrincipal", "Descricao"))
        self.lbTituloTpProcesso.setText(_translate("wdgEntrevistaPrincipal", "Titulo de processo"))
        self.lbDescTpProcesso.setText(_translate("wdgEntrevistaPrincipal", "Descricao"))
import Resources.newEntrevistaPrincipal


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgEntrevistaPrincipal = QtWidgets.QWidget()
    ui = Ui_wdgEntrevistaPrincipal()
    ui.setupUi(wdgEntrevistaPrincipal)
    wdgEntrevistaPrincipal.show()
    sys.exit(app.exec_())
