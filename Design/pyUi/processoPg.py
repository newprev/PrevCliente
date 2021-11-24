# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/processoPg.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwProcessoPage(object):
    def setupUi(self, mwProcessoPage):
        mwProcessoPage.setObjectName("mwProcessoPage")
        mwProcessoPage.resize(1280, 917)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mwProcessoPage.sizePolicy().hasHeightForWidth())
        mwProcessoPage.setSizePolicy(sizePolicy)
        mwProcessoPage.setMinimumSize(QtCore.QSize(1280, 670))
        mwProcessoPage.setStyleSheet("/*-------------------------------------- QWidget --------------------------------------*/\n"
"#wdgCentral{\n"
"    background-color: lightgrey;\n"
"}\n"
"\n"
"\n"
"/*-------------------------------------- Frames --------------------------------------*/\n"
"#frTopBackground {\n"
"    background-color: #048ba8;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#frBottomBackground {\n"
"/*    background-color: rgb(241, 241, 241);*/\n"
"    background-color: lightgrey;\n"
"}\n"
"\n"
"#frBottom {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#frNaturezaRight, #frTipoBeneRight, \n"
"#frTipoProcRight, #frTiposAtiv {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.443182, x2:0, y2:0.5, stop:0 rgba(66, 120, 178, 255), stop:1 rgba(39, 86, 135, 255));\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/*-------------------------------------- Labels --------------------------------------*/\n"
"\n"
"#lbTopTitulo {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#lbTopSubtitulo {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#lbInfoPessoais {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"\n"
"    color: rgb(32, 74, 135);\n"
"}\n"
"\n"
"/*-------------------------------------- QFrame --------------------------------------*/\n"
"#stkMain, #pgSemCliente {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/*-------------------------------------- Push Buttons ------------------------------*/\n"
"#pbProxEtapa {\n"
"/*    background-color: qlineargradient(spread:pad, x1:0.913, y1:0.096, x2:0.005, y2:1, stop:0 rgba(86, 178, 169, 255), stop:1 rgba(21, 135, 133, 255));*/\n"
"    background-color: #0E7C7B;\n"
"    border-radius: 10px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#pbProxEtapa:hover {\n"
"/*    background-color: qlineargradient(spread:pad, x1:0.913, y1:0.096, x2:0.005, y2:1, stop:0 rgba(86, 178, 169, 255), stop:1 rgba(51, 165, 163, 255));*/\n"
"    background-color: transparent;\n"
"    border-radius: 11px;\n"
"    border-color: rgb(2, 104, 104);\n"
"    border-style: groove;\n"
"    border-width: 2px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"\n"
"    color: rgb(2, 104, 104);\n"
"}\n"
"\n"
"#pbVoltaEtapa {\n"
"/*    background-color: qlineargradient(spread:pad, x1:0.877204, y1:0.193, x2:0.301, y2:0.773, stop:0 rgba(167, 66, 146, 255), stop:1 rgba(131, 52, 169, 255));*/\n"
"    background-color: rgb(131, 52, 169);\n"
"    border-radius: 10px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#pbVoltaEtapa:hover {\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.469, y1:0, x2:0.464, y2:1, stop:0 rgba(102, 70, 147, 255), stop:1 rgba(127, 52, 169, 255));*/\n"
"    background-color: rgb(167, 66, 146);\n"
"    border-radius: 10px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}")
        self.wdgCentral = QtWidgets.QWidget(mwProcessoPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdgCentral.sizePolicy().hasHeightForWidth())
        self.wdgCentral.setSizePolicy(sizePolicy)
        self.wdgCentral.setStyleSheet("")
        self.wdgCentral.setObjectName("wdgCentral")
        self.gridLayout = QtWidgets.QGridLayout(self.wdgCentral)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frBottomBackground = QtWidgets.QFrame(self.wdgCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frBottomBackground.sizePolicy().hasHeightForWidth())
        self.frBottomBackground.setSizePolicy(sizePolicy)
        self.frBottomBackground.setMinimumSize(QtCore.QSize(800, 550))
        self.frBottomBackground.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frBottomBackground.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBottomBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBottomBackground.setObjectName("frBottomBackground")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frBottomBackground)
        self.verticalLayout_3.setContentsMargins(0, 8, 0, 8)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stkMain = QtWidgets.QStackedWidget(self.frBottomBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stkMain.sizePolicy().hasHeightForWidth())
        self.stkMain.setSizePolicy(sizePolicy)
        self.stkMain.setMinimumSize(QtCore.QSize(750, 300))
        self.stkMain.setMaximumSize(QtCore.QSize(16777215, 16755515))
        self.stkMain.setObjectName("stkMain")
        self.pgSemCliente = QtWidgets.QWidget()
        self.pgSemCliente.setStyleSheet("/*-------------------------------------- Push Button --------------------------------------*/\n"
"#pbBuscaCliente {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"#pbBuscaCliente:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(51, 126, 251);\n"
"    background-color: rgb(52, 93, 114);\n"
"}\n"
"\n"
"/*-------------------------------------- Label --------------------------------------*/\n"
"#lbInfoCentralCliente {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 20px;\n"
"\n"
"    color: grey;\n"
"}")
        self.pgSemCliente.setObjectName("pgSemCliente")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.pgSemCliente)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.pgSemCliente)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(300, 200))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbInfoCentralCliente = QtWidgets.QLabel(self.frame_3)
        self.lbInfoCentralCliente.setTextFormat(QtCore.Qt.AutoText)
        self.lbInfoCentralCliente.setScaledContents(False)
        self.lbInfoCentralCliente.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbInfoCentralCliente.setWordWrap(True)
        self.lbInfoCentralCliente.setObjectName("lbInfoCentralCliente")
        self.verticalLayout_7.addWidget(self.lbInfoCentralCliente, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pbBuscaCliente = QtWidgets.QPushButton(self.frame_3)
        self.pbBuscaCliente.setMinimumSize(QtCore.QSize(0, 40))
        self.pbBuscaCliente.setObjectName("pbBuscaCliente")
        self.verticalLayout_7.addWidget(self.pbBuscaCliente)
        self.verticalLayout_4.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.frame_2)
        self.stkMain.addWidget(self.pgSemCliente)
        self.pgSemProcesso = QtWidgets.QWidget()
        self.pgSemProcesso.setStyleSheet("/*-------------------------------------- Push Button --------------------------------------*/\n"
"#pbBuscaProcesso {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"#pbBuscaProcesso:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(51, 126, 251);\n"
"    background-color: rgb(52, 93, 114);\n"
"}\n"
"\n"
"/*-------------------------------------- Label --------------------------------------*/\n"
"#lbInfoCentralProcesso {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 20px;\n"
"\n"
"    color: grey;\n"
"}")
        self.pgSemProcesso.setObjectName("pgSemProcesso")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.pgSemProcesso)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_4 = QtWidgets.QFrame(self.pgSemProcesso)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(300, 200))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lbInfoCentralProcesso = QtWidgets.QLabel(self.frame_5)
        self.lbInfoCentralProcesso.setTextFormat(QtCore.Qt.AutoText)
        self.lbInfoCentralProcesso.setScaledContents(False)
        self.lbInfoCentralProcesso.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbInfoCentralProcesso.setWordWrap(True)
        self.lbInfoCentralProcesso.setObjectName("lbInfoCentralProcesso")
        self.verticalLayout_9.addWidget(self.lbInfoCentralProcesso, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pbBuscaProcesso = QtWidgets.QPushButton(self.frame_5)
        self.pbBuscaProcesso.setMinimumSize(QtCore.QSize(0, 40))
        self.pbBuscaProcesso.setObjectName("pbBuscaProcesso")
        self.verticalLayout_9.addWidget(self.pbBuscaProcesso)
        self.verticalLayout_8.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.stkMain.addWidget(self.pgSemProcesso)
        self.verticalLayout_3.addWidget(self.stkMain)
        self.frBottom = QtWidgets.QFrame(self.frBottomBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frBottom.sizePolicy().hasHeightForWidth())
        self.frBottom.setSizePolicy(sizePolicy)
        self.frBottom.setMinimumSize(QtCore.QSize(0, 50))
        self.frBottom.setMaximumSize(QtCore.QSize(13216548, 131654))
        self.frBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frBottom.setLineWidth(6)
        self.frBottom.setMidLineWidth(0)
        self.frBottom.setObjectName("frBottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frBottom)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pbarProgresso = QtWidgets.QProgressBar(self.frBottom)
        self.pbarProgresso.setMinimumSize(QtCore.QSize(350, 10))
        self.pbarProgresso.setMaximumSize(QtCore.QSize(220, 10))
        self.pbarProgresso.setProperty("value", 24)
        self.pbarProgresso.setTextVisible(False)
        self.pbarProgresso.setInvertedAppearance(False)
        self.pbarProgresso.setObjectName("pbarProgresso")
        self.horizontalLayout_2.addWidget(self.pbarProgresso)
        self.verticalLayout_3.addWidget(self.frBottom, 0, QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.frBottomBackground, 2, 1, 1, 1)
        self.frTopBackground = QtWidgets.QFrame(self.wdgCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frTopBackground.sizePolicy().hasHeightForWidth())
        self.frTopBackground.setSizePolicy(sizePolicy)
        self.frTopBackground.setMinimumSize(QtCore.QSize(0, 150))
        self.frTopBackground.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frTopBackground.setStyleSheet("/*--------------------------------------- Frames ---------------------------------------*/\n"
"#frFirulaCliente {\n"
"    background-color: #048ba8;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#frFirulaProcesso {\n"
"    background-color: rgb(220, 147, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#frInfoCliente, #frInfoProcesso {\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"/*--------------------------------------- Labels ---------------------------------------*/\n"
"#lbNomeCompleto, #lbCPF, #lbEmail,\n"
"#lbInfoCpf, #lbInfoEmail, #lbInfoNumProc,\n"
"#lbInfoSituacao, #lbTpProcesso, #lbSituacao,\n"
"#lbNumProc {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 18px;\n"
"\n"
"    color: rgb(52, 52, 52);\n"
"}\n"
"\n"
"/*--------------------------------------- Push Button ---------------------------------------*/\n"
"#pbFecharCliente, #pbFecharProcesso {\n"
"    background-color: transparent;\n"
"    background-image: url(:/infoCards/entrevista-uncheck.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#pbFecharCliente:hover, #pbFecharProcesso:hover {\n"
"    background-color: rgba(2, 48, 57, 30);\n"
"    background-image: url(:/infoCards/entrevista-uncheck.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"\n"
"    border-radius: 10px;\n"
"}")
        self.frTopBackground.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTopBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTopBackground.setObjectName("frTopBackground")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frTopBackground)
        self.verticalLayout_2.setContentsMargins(16, 0, 16, 8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frTitulos = QtWidgets.QFrame(self.frTopBackground)
        self.frTitulos.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frTitulos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTitulos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTitulos.setObjectName("frTitulos")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frTitulos)
        self.verticalLayout_5.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbTopTitulo = QtWidgets.QLabel(self.frTitulos)
        self.lbTopTitulo.setObjectName("lbTopTitulo")
        self.verticalLayout_5.addWidget(self.lbTopTitulo)
        self.lbTopSubtitulo = QtWidgets.QLabel(self.frTitulos)
        self.lbTopSubtitulo.setObjectName("lbTopSubtitulo")
        self.verticalLayout_5.addWidget(self.lbTopSubtitulo, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frTitulos)
        self.frOrganizadorTop = QtWidgets.QFrame(self.frTopBackground)
        self.frOrganizadorTop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frOrganizadorTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frOrganizadorTop.setObjectName("frOrganizadorTop")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frOrganizadorTop)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frInfoCliente = QtWidgets.QFrame(self.frOrganizadorTop)
        self.frInfoCliente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoCliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoCliente.setObjectName("frInfoCliente")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frInfoCliente)
        self.gridLayout_2.setContentsMargins(-1, -1, 16, -1)
        self.gridLayout_2.setHorizontalSpacing(16)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbInfoCpf = QtWidgets.QLabel(self.frInfoCliente)
        self.lbInfoCpf.setObjectName("lbInfoCpf")
        self.gridLayout_2.addWidget(self.lbInfoCpf, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.lbInfoEmail = QtWidgets.QLabel(self.frInfoCliente)
        self.lbInfoEmail.setObjectName("lbInfoEmail")
        self.gridLayout_2.addWidget(self.lbInfoEmail, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.lbEmail = QtWidgets.QLabel(self.frInfoCliente)
        self.lbEmail.setObjectName("lbEmail")
        self.gridLayout_2.addWidget(self.lbEmail, 2, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.lbCPF = QtWidgets.QLabel(self.frInfoCliente)
        self.lbCPF.setObjectName("lbCPF")
        self.gridLayout_2.addWidget(self.lbCPF, 1, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.frFirulaCliente = QtWidgets.QFrame(self.frInfoCliente)
        self.frFirulaCliente.setMinimumSize(QtCore.QSize(10, 0))
        self.frFirulaCliente.setMaximumSize(QtCore.QSize(10, 16777215))
        self.frFirulaCliente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frFirulaCliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFirulaCliente.setObjectName("frFirulaCliente")
        self.gridLayout_2.addWidget(self.frFirulaCliente, 0, 0, 3, 1)
        self.lbNomeCompleto = QtWidgets.QLabel(self.frInfoCliente)
        self.lbNomeCompleto.setObjectName("lbNomeCompleto")
        self.gridLayout_2.addWidget(self.lbNomeCompleto, 0, 2, 1, 2)
        self.pbFecharCliente = QtWidgets.QPushButton(self.frInfoCliente)
        self.pbFecharCliente.setMinimumSize(QtCore.QSize(20, 20))
        self.pbFecharCliente.setMaximumSize(QtCore.QSize(20, 20))
        self.pbFecharCliente.setText("")
        self.pbFecharCliente.setObjectName("pbFecharCliente")
        self.gridLayout_2.addWidget(self.pbFecharCliente, 0, 4, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.frInfoCliente, 0, QtCore.Qt.AlignLeft)
        self.frInfoProcesso = QtWidgets.QFrame(self.frOrganizadorTop)
        self.frInfoProcesso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoProcesso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoProcesso.setObjectName("frInfoProcesso")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frInfoProcesso)
        self.gridLayout_3.setContentsMargins(-1, -1, 16, -1)
        self.gridLayout_3.setHorizontalSpacing(16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbInfoSituacao = QtWidgets.QLabel(self.frInfoProcesso)
        self.lbInfoSituacao.setObjectName("lbInfoSituacao")
        self.gridLayout_3.addWidget(self.lbInfoSituacao, 2, 1, 1, 1)
        self.lbNumProc = QtWidgets.QLabel(self.frInfoProcesso)
        self.lbNumProc.setObjectName("lbNumProc")
        self.gridLayout_3.addWidget(self.lbNumProc, 1, 2, 1, 1)
        self.lbInfoNumProc = QtWidgets.QLabel(self.frInfoProcesso)
        self.lbInfoNumProc.setObjectName("lbInfoNumProc")
        self.gridLayout_3.addWidget(self.lbInfoNumProc, 1, 1, 1, 1)
        self.lbSituacao = QtWidgets.QLabel(self.frInfoProcesso)
        self.lbSituacao.setObjectName("lbSituacao")
        self.gridLayout_3.addWidget(self.lbSituacao, 2, 2, 1, 1)
        self.lbTpProcesso = QtWidgets.QLabel(self.frInfoProcesso)
        self.lbTpProcesso.setObjectName("lbTpProcesso")
        self.gridLayout_3.addWidget(self.lbTpProcesso, 0, 1, 1, 1)
        self.frFirulaProcesso = QtWidgets.QFrame(self.frInfoProcesso)
        self.frFirulaProcesso.setMinimumSize(QtCore.QSize(10, 0))
        self.frFirulaProcesso.setMaximumSize(QtCore.QSize(10, 16777215))
        self.frFirulaProcesso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frFirulaProcesso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFirulaProcesso.setObjectName("frFirulaProcesso")
        self.gridLayout_3.addWidget(self.frFirulaProcesso, 0, 0, 3, 1)
        self.pbFecharProcesso = QtWidgets.QPushButton(self.frInfoProcesso)
        self.pbFecharProcesso.setMinimumSize(QtCore.QSize(20, 20))
        self.pbFecharProcesso.setMaximumSize(QtCore.QSize(20, 20))
        self.pbFecharProcesso.setText("")
        self.pbFecharProcesso.setObjectName("pbFecharProcesso")
        self.gridLayout_3.addWidget(self.pbFecharProcesso, 0, 3, 1, 1)
        self.horizontalLayout_7.addWidget(self.frInfoProcesso, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frOrganizadorTop)
        self.gridLayout.addWidget(self.frTopBackground, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.frGuia = QtWidgets.QFrame(self.wdgCentral)
        self.frGuia.setMinimumSize(QtCore.QSize(0, 0))
        self.frGuia.setStyleSheet("/*----------------------------------------------- Labels -----------------------------------------------*/\n"
"#lbTituloGuia{\n"
"    font-family: \"Ubuntu\";\n"
"    font-size: 20px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#lbNomeAdv, #lbNumOab, #lbNomeEscritorio {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"\n"
"    color: lightgrey;\n"
"}\n"
"\n"
"#lbInfoGeraDocs, #lbInfoGeral, #lbInfoAposentadoria {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"/*----------------------------------------------- Frames -----------------------------------------------*/\n"
"#frProcessoIcone{\n"
"    background-image: url(:/menuIcone/processo.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#frEspacador1{\n"
"    background-color: rgba(230, 230, 230, 100);\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"#frGuia {\n"
"    background-color: #3a405a;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#frInfoAdv {\n"
"/*    background-color: #3a405a;*/\n"
"    border-style: groove;\n"
"    border-width: 2px 0px 0px 0px;\n"
"    border-color: grey;\n"
"}\n"
"\n"
"#frGeral, #frAposentadorias, #frProcuracao {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*----------------------------------------------- Push Buttons -----------------------------------------------*/\n"
"#pbGeral, #pbAposentadorias, #pbProcuracao, \n"
"#pbDocsComp, #pbHipo {\n"
"    background-color: rgba(0,0,0,0);\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    border: 0px;\n"
"    color: lightgrey;\n"
"}\n"
"\n"
"#pbGeral:hover, #pbAposentadorias:hover, #pbProcuracao:hover, \n"
"#pbDocsComp:hover, #pbHipo:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: lightgrey;\n"
"\n"
"    background-color: rgba(142, 157, 220, 200);\n"
"    border-radius: 4px 4px 4px 4px;\n"
"    border-width: 0px 0px 0px 2px;\n"
"    border-color: transparent transparent transparent white;\n"
"    border-style: solid solid solid solid;\n"
"}")
        self.frGuia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frGuia.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frGuia.setObjectName("frGuia")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frGuia)
        self.verticalLayout.setContentsMargins(-1, 24, -1, -1)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.frGuia)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frProcessoIcone = QtWidgets.QFrame(self.frame)
        self.frProcessoIcone.setMinimumSize(QtCore.QSize(32, 32))
        self.frProcessoIcone.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frProcessoIcone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProcessoIcone.setObjectName("frProcessoIcone")
        self.horizontalLayout_3.addWidget(self.frProcessoIcone)
        self.lbTituloGuia = QtWidgets.QLabel(self.frame)
        self.lbTituloGuia.setObjectName("lbTituloGuia")
        self.horizontalLayout_3.addWidget(self.lbTituloGuia)
        self.verticalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.frEspacador1 = QtWidgets.QFrame(self.frGuia)
        self.frEspacador1.setMinimumSize(QtCore.QSize(0, 2))
        self.frEspacador1.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frEspacador1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEspacador1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEspacador1.setObjectName("frEspacador1")
        self.verticalLayout.addWidget(self.frEspacador1, 0, QtCore.Qt.AlignTop)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.lbInfoGeral = QtWidgets.QLabel(self.frGuia)
        self.lbInfoGeral.setObjectName("lbInfoGeral")
        self.verticalLayout.addWidget(self.lbInfoGeral)
        self.frGeral = QtWidgets.QFrame(self.frGuia)
        self.frGeral.setMinimumSize(QtCore.QSize(0, 28))
        self.frGeral.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frGeral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frGeral.setObjectName("frGeral")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frGeral)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbGeral = QtWidgets.QPushButton(self.frGeral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbGeral.sizePolicy().hasHeightForWidth())
        self.pbGeral.setSizePolicy(sizePolicy)
        self.pbGeral.setMinimumSize(QtCore.QSize(0, 24))
        self.pbGeral.setObjectName("pbGeral")
        self.horizontalLayout.addWidget(self.pbGeral)
        self.verticalLayout.addWidget(self.frGeral)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.frEspacador1_3 = QtWidgets.QFrame(self.frGuia)
        self.frEspacador1_3.setMinimumSize(QtCore.QSize(0, 2))
        self.frEspacador1_3.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frEspacador1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEspacador1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEspacador1_3.setObjectName("frEspacador1_3")
        self.verticalLayout.addWidget(self.frEspacador1_3)
        self.lbInfoAposentadoria = QtWidgets.QLabel(self.frGuia)
        self.lbInfoAposentadoria.setObjectName("lbInfoAposentadoria")
        self.verticalLayout.addWidget(self.lbInfoAposentadoria)
        self.frAposentadorias = QtWidgets.QFrame(self.frGuia)
        self.frAposentadorias.setMinimumSize(QtCore.QSize(0, 28))
        self.frAposentadorias.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAposentadorias.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAposentadorias.setObjectName("frAposentadorias")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frAposentadorias)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbAposentadorias = QtWidgets.QPushButton(self.frAposentadorias)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAposentadorias.sizePolicy().hasHeightForWidth())
        self.pbAposentadorias.setSizePolicy(sizePolicy)
        self.pbAposentadorias.setMinimumSize(QtCore.QSize(0, 24))
        self.pbAposentadorias.setObjectName("pbAposentadorias")
        self.horizontalLayout_4.addWidget(self.pbAposentadorias)
        self.verticalLayout.addWidget(self.frAposentadorias)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.frEspacador1_2 = QtWidgets.QFrame(self.frGuia)
        self.frEspacador1_2.setMinimumSize(QtCore.QSize(0, 2))
        self.frEspacador1_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frEspacador1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEspacador1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEspacador1_2.setObjectName("frEspacador1_2")
        self.verticalLayout.addWidget(self.frEspacador1_2)
        self.lbInfoGeraDocs = QtWidgets.QLabel(self.frGuia)
        self.lbInfoGeraDocs.setObjectName("lbInfoGeraDocs")
        self.verticalLayout.addWidget(self.lbInfoGeraDocs)
        self.frProcuracao = QtWidgets.QFrame(self.frGuia)
        self.frProcuracao.setMinimumSize(QtCore.QSize(0, 28))
        self.frProcuracao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frProcuracao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProcuracao.setObjectName("frProcuracao")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frProcuracao)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pbProcuracao = QtWidgets.QPushButton(self.frProcuracao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbProcuracao.sizePolicy().hasHeightForWidth())
        self.pbProcuracao.setSizePolicy(sizePolicy)
        self.pbProcuracao.setMinimumSize(QtCore.QSize(0, 24))
        self.pbProcuracao.setObjectName("pbProcuracao")
        self.horizontalLayout_5.addWidget(self.pbProcuracao)
        self.verticalLayout.addWidget(self.frProcuracao)
        self.pbDocsComp = QtWidgets.QPushButton(self.frGuia)
        self.pbDocsComp.setMinimumSize(QtCore.QSize(0, 24))
        self.pbDocsComp.setObjectName("pbDocsComp")
        self.verticalLayout.addWidget(self.pbDocsComp)
        self.pbHipo = QtWidgets.QPushButton(self.frGuia)
        self.pbHipo.setMinimumSize(QtCore.QSize(0, 24))
        self.pbHipo.setObjectName("pbHipo")
        self.verticalLayout.addWidget(self.pbHipo)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.frInfoAdv = QtWidgets.QFrame(self.frGuia)
        self.frInfoAdv.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoAdv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoAdv.setObjectName("frInfoAdv")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frInfoAdv)
        self.verticalLayout_6.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbNomeEscritorio = QtWidgets.QLabel(self.frInfoAdv)
        self.lbNomeEscritorio.setObjectName("lbNomeEscritorio")
        self.verticalLayout_6.addWidget(self.lbNomeEscritorio)
        self.lbNomeAdv = QtWidgets.QLabel(self.frInfoAdv)
        self.lbNomeAdv.setObjectName("lbNomeAdv")
        self.verticalLayout_6.addWidget(self.lbNomeAdv)
        self.lbNumOab = QtWidgets.QLabel(self.frInfoAdv)
        self.lbNumOab.setObjectName("lbNumOab")
        self.verticalLayout_6.addWidget(self.lbNumOab)
        self.verticalLayout.addWidget(self.frInfoAdv)
        self.gridLayout.addWidget(self.frGuia, 0, 0, 3, 1)
        self.frBottomBackground.raise_()
        self.frGuia.raise_()
        self.frTopBackground.raise_()
        mwProcessoPage.setCentralWidget(self.wdgCentral)

        self.retranslateUi(mwProcessoPage)
        QtCore.QMetaObject.connectSlotsByName(mwProcessoPage)

    def retranslateUi(self, mwProcessoPage):
        _translate = QtCore.QCoreApplication.translate
        mwProcessoPage.setWindowTitle(_translate("mwProcessoPage", "MainWindow"))
        self.lbInfoCentralCliente.setText(_translate("mwProcessoPage", "Para ter acesso às informações processuais, busque um cliente que já tenha iniciado um processo clicando no botão abaixo."))
        self.pbBuscaCliente.setText(_translate("mwProcessoPage", "Buscar cliente"))
        self.lbInfoCentralProcesso.setText(_translate("mwProcessoPage", "O cliente atual possui mais de um processo iniciado. Selecione o processo que deseja se informar clicando no botão abaixo."))
        self.pbBuscaProcesso.setText(_translate("mwProcessoPage", "Buscar processo"))
        self.lbTopTitulo.setText(_translate("mwProcessoPage", "Informações processuais"))
        self.lbTopSubtitulo.setText(_translate("mwProcessoPage", "Encontre todas as informações do(s) processo(s) dos seus clientes"))
        self.lbInfoCpf.setText(_translate("mwProcessoPage", "CPF:"))
        self.lbInfoEmail.setText(_translate("mwProcessoPage", "E-mail:"))
        self.lbEmail.setText(_translate("mwProcessoPage", "-"))
        self.lbCPF.setText(_translate("mwProcessoPage", "-"))
        self.lbNomeCompleto.setText(_translate("mwProcessoPage", "-"))
        self.lbInfoSituacao.setText(_translate("mwProcessoPage", "Situação:"))
        self.lbNumProc.setText(_translate("mwProcessoPage", "-"))
        self.lbInfoNumProc.setText(_translate("mwProcessoPage", "Nº do processo:"))
        self.lbSituacao.setText(_translate("mwProcessoPage", "-"))
        self.lbTpProcesso.setText(_translate("mwProcessoPage", "Tipo do processo"))
        self.lbTituloGuia.setWhatsThis(_translate("mwProcessoPage", "<html><head/><body><p><br/></p></body></html>"))
        self.lbTituloGuia.setText(_translate("mwProcessoPage", "Processos"))
        self.lbInfoGeral.setText(_translate("mwProcessoPage", "Geral"))
        self.pbGeral.setText(_translate("mwProcessoPage", "Geral"))
        self.lbInfoAposentadoria.setText(_translate("mwProcessoPage", "Aposentadoria"))
        self.pbAposentadorias.setText(_translate("mwProcessoPage", "Aposentadorias"))
        self.lbInfoGeraDocs.setText(_translate("mwProcessoPage", "Gerar documentos"))
        self.pbProcuracao.setText(_translate("mwProcessoPage", "Procuração"))
        self.pbDocsComp.setText(_translate("mwProcessoPage", "Doc. Comprobatórios"))
        self.pbHipo.setText(_translate("mwProcessoPage", "Dec. Hipossuficiência"))
        self.lbNomeEscritorio.setText(_translate("mwProcessoPage", "Nome do escritório"))
        self.lbNomeAdv.setText(_translate("mwProcessoPage", "Nome Advogado"))
        self.lbNumOab.setText(_translate("mwProcessoPage", "Numero OAB"))
import Resources.processoPage


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwProcessoPage = QtWidgets.QMainWindow()
    ui = Ui_mwProcessoPage()
    ui.setupUi(mwProcessoPage)
    mwProcessoPage.show()
    sys.exit(app.exec_())
