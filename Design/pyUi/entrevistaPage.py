# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrevistaPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwEntrevistaPage(object):
    def setupUi(self, mwEntrevistaPage):
        mwEntrevistaPage.setObjectName("mwEntrevistaPage")
        mwEntrevistaPage.resize(1280, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mwEntrevistaPage.sizePolicy().hasHeightForWidth())
        mwEntrevistaPage.setSizePolicy(sizePolicy)
        mwEntrevistaPage.setMinimumSize(QtCore.QSize(1280, 670))
        mwEntrevistaPage.setStyleSheet("/*-------------------------------------- Frames --------------------------------------*/\n"
"#frTopBackground{\n"
"/*    background-color: qlineargradient(spread:pad, x1:1, y1:0.483, x2:0, y2:0.539773, stop:0 rgba(39, 86, 135, 255), stop:1 rgba(62, 141, 225, 204));*/\n"
"    background-color: #048ba8;\n"
"}\n"
"\n"
"#frBottomBackground{\n"
"/*    background-color: rgb(241, 241, 241);*/\n"
"    background-color: lightgrey;\n"
"}\n"
"\n"
"#frBarProgress{\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#frBottom {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#frEtapa1 {\n"
"    background-image: url(:/Etapa1/n1-blue.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#frEtapa2 {\n"
"    background-image: url(:/Etapa2/n1-grey.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#frEtapa3 {\n"
"    background-image: url(:/Etapa3/n3-grey.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#frEtapa4 {\n"
"    background-image: url(:/Etapa4/n4-grey.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#frProg1, #frProg2, #frProg3 {\n"
"    background-image: url(:/dots/d3-grey.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: top;\n"
"}\n"
"\n"
"#frProg1 {\n"
"    background-image: url(:/dots/d3-blue.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: top;\n"
"}\n"
"\n"
"#frNaturezaRight, #frTipoBeneRight, \n"
"#frTipoProcRight, #frTiposAtiv {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.443182, x2:0, y2:0.5, stop:0 rgba(66, 120, 178, 255), stop:1 rgba(39, 86, 135, 255));\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#frInfo1Icon, #frInfo2Icon,\n"
"#frInfo3Icon, #frInfo4Icon  {\n"
"    background-image: url(:/dots/d3-white.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#frGuia {\n"
"    background-color: #3a405a;\n"
"    border-style: groove;\n"
"    border-width: 0px 1px 0px 0px;\n"
"    border-color: lightgrey;\n"
"}\n"
"\n"
"#frInfoAdv {\n"
"/*    background-color: #3a405a;*/\n"
"    border-style: groove;\n"
"    border-width: 2px 0px 0px 0px;\n"
"    border-color: grey;\n"
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
"#lbInfoProcessuais, #lbInfoDetalhamento, #lbInfoFinalizacao {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"\n"
"    color: grey;\n"
"}\n"
"\n"
"#lbInfo1, #lbInfo2, \n"
"#lbInfo3, #lbInfo4 {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"/*-------------------------------------- QFrame --------------------------------------*/\n"
"#stackedWidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(mwEntrevistaPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frGuia = QtWidgets.QFrame(self.centralwidget)
        self.frGuia.setMinimumSize(QtCore.QSize(0, 0))
        self.frGuia.setStyleSheet("/*----------------------------------------------- Labels -----------------------------------------------*/\n"
"#lbTituloGuia{\n"
"    font-family: \"Ubuntu\";\n"
"    font-size: 16px;\n"
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
"/*----------------------------------------------- Frames -----------------------------------------------*/\n"
"#frEntrevistaIcone{\n"
"    background-image: url(:/Guia/entrevista.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"/*----------------------------------------------- Group Box -----------------------------------------------*/\n"
"#gbNatureza::title, #gbBeneficio::title, \n"
"#gbTipo::title, #gbQuestionario::title {\n"
"    border-width: 0px 0px 1px 0px;\n"
"    border-color: white;\n"
"    border-style: solid;    \n"
"    subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QGroupBox{\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    border: 0px solid transparent;\n"
"    background-color: transparent;\n"
"    margin-top: 3ex;\n"
"\n"
"    color: white;    \n"
"}\n"
"\n"
"/*----------------------------------------------- Push Buttons -----------------------------------------------*/\n"
"#pbConfSimulacao {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(78, 86, 121);\n"
"    \n"
"    background-image: url(:/Simulacao/simulacao.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#pbConfSimulacao:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(48, 53, 75);\n"
"    \n"
"    background-image: url(:/Simulacao/simulacao.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"\n"
"    color: white;\n"
"}")
        self.frGuia.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frGuia.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frGuia.setObjectName("frGuia")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frGuia)
        self.verticalLayout.setSpacing(36)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frGuia)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(4)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frEntrevistaIcone = QtWidgets.QFrame(self.frame_2)
        self.frEntrevistaIcone.setMinimumSize(QtCore.QSize(32, 32))
        self.frEntrevistaIcone.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEntrevistaIcone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEntrevistaIcone.setObjectName("frEntrevistaIcone")
        self.horizontalLayout_20.addWidget(self.frEntrevistaIcone)
        self.lbTituloGuia = QtWidgets.QLabel(self.frame_2)
        self.lbTituloGuia.setObjectName("lbTituloGuia")
        self.horizontalLayout_20.addWidget(self.lbTituloGuia)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.gbNatureza = QtWidgets.QGroupBox(self.frGuia)
        self.gbNatureza.setObjectName("gbNatureza")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.gbNatureza)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.vlNatureza = QtWidgets.QVBoxLayout()
        self.vlNatureza.setObjectName("vlNatureza")
        self.verticalLayout_11.addLayout(self.vlNatureza)
        self.verticalLayout.addWidget(self.gbNatureza)
        self.gbTipo = QtWidgets.QGroupBox(self.frGuia)
        self.gbTipo.setObjectName("gbTipo")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.gbTipo)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.vlTipo = QtWidgets.QVBoxLayout()
        self.vlTipo.setObjectName("vlTipo")
        self.verticalLayout_10.addLayout(self.vlTipo)
        self.verticalLayout.addWidget(self.gbTipo)
        self.gbBeneficio = QtWidgets.QGroupBox(self.frGuia)
        self.gbBeneficio.setObjectName("gbBeneficio")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.gbBeneficio)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.vlBeneficio = QtWidgets.QVBoxLayout()
        self.vlBeneficio.setObjectName("vlBeneficio")
        self.verticalLayout_9.addLayout(self.vlBeneficio)
        self.verticalLayout.addWidget(self.gbBeneficio)
        self.gbQuestionario = QtWidgets.QGroupBox(self.frGuia)
        self.gbQuestionario.setObjectName("gbQuestionario")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.gbQuestionario)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.vlQuestionario = QtWidgets.QVBoxLayout()
        self.vlQuestionario.setObjectName("vlQuestionario")
        self.verticalLayout_7.addLayout(self.vlQuestionario)
        self.verticalLayout.addWidget(self.gbQuestionario)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pbConfSimulacao = QtWidgets.QPushButton(self.frGuia)
        self.pbConfSimulacao.setMinimumSize(QtCore.QSize(0, 38))
        self.pbConfSimulacao.setObjectName("pbConfSimulacao")
        self.verticalLayout.addWidget(self.pbConfSimulacao)
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
        self.gridLayout.addWidget(self.frGuia, 0, 0, 2, 1)
        self.frTopBackground = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frTopBackground.sizePolicy().hasHeightForWidth())
        self.frTopBackground.setSizePolicy(sizePolicy)
        self.frTopBackground.setMinimumSize(QtCore.QSize(0, 120))
        self.frTopBackground.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frTopBackground.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTopBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTopBackground.setObjectName("frTopBackground")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frTopBackground)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_15 = QtWidgets.QFrame(self.frTopBackground)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbTopTitulo = QtWidgets.QLabel(self.frame_15)
        self.lbTopTitulo.setObjectName("lbTopTitulo")
        self.verticalLayout_5.addWidget(self.lbTopTitulo)
        self.lbTopSubtitulo = QtWidgets.QLabel(self.frame_15)
        self.lbTopSubtitulo.setObjectName("lbTopSubtitulo")
        self.verticalLayout_5.addWidget(self.lbTopSubtitulo)
        self.verticalLayout_4.addWidget(self.frame_15)
        self.frBarProgress = QtWidgets.QFrame(self.frTopBackground)
        self.frBarProgress.setMinimumSize(QtCore.QSize(930, 50))
        self.frBarProgress.setMaximumSize(QtCore.QSize(930, 50))
        self.frBarProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBarProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBarProgress.setObjectName("frBarProgress")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frBarProgress)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frProgressPessoais = QtWidgets.QFrame(self.frBarProgress)
        self.frProgressPessoais.setMinimumSize(QtCore.QSize(130, 42))
        self.frProgressPessoais.setMaximumSize(QtCore.QSize(130, 42))
        self.frProgressPessoais.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frProgressPessoais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProgressPessoais.setObjectName("frProgressPessoais")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frProgressPessoais)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frEtapa1 = QtWidgets.QFrame(self.frProgressPessoais)
        self.frEtapa1.setMinimumSize(QtCore.QSize(40, 42))
        self.frEtapa1.setMaximumSize(QtCore.QSize(40, 42))
        self.frEtapa1.setSizeIncrement(QtCore.QSize(0, 0))
        self.frEtapa1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEtapa1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEtapa1.setObjectName("frEtapa1")
        self.horizontalLayout_2.addWidget(self.frEtapa1)
        self.frInfo1 = QtWidgets.QFrame(self.frProgressPessoais)
        self.frInfo1.setMinimumSize(QtCore.QSize(0, 42))
        self.frInfo1.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frInfo1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo1.setObjectName("frInfo1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frInfo1)
        self.verticalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbInfoPessoais = QtWidgets.QLabel(self.frInfo1)
        self.lbInfoPessoais.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfoPessoais.setObjectName("lbInfoPessoais")
        self.verticalLayout_2.addWidget(self.lbInfoPessoais)
        self.horizontalLayout_2.addWidget(self.frInfo1)
        self.horizontalLayout.addWidget(self.frProgressPessoais)
        self.frProg1 = QtWidgets.QFrame(self.frBarProgress)
        self.frProg1.setMinimumSize(QtCore.QSize(45, 10))
        self.frProg1.setMaximumSize(QtCore.QSize(45, 10))
        self.frProg1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frProg1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProg1.setObjectName("frProg1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frProg1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout.addWidget(self.frProg1)
        self.frProgressProcesso = QtWidgets.QFrame(self.frBarProgress)
        self.frProgressProcesso.setMinimumSize(QtCore.QSize(130, 42))
        self.frProgressProcesso.setMaximumSize(QtCore.QSize(130, 42))
        self.frProgressProcesso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frProgressProcesso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProgressProcesso.setObjectName("frProgressProcesso")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frProgressProcesso)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frEtapa2 = QtWidgets.QFrame(self.frProgressProcesso)
        self.frEtapa2.setMinimumSize(QtCore.QSize(40, 42))
        self.frEtapa2.setMaximumSize(QtCore.QSize(40, 42))
        self.frEtapa2.setSizeIncrement(QtCore.QSize(0, 0))
        self.frEtapa2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEtapa2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEtapa2.setObjectName("frEtapa2")
        self.horizontalLayout_3.addWidget(self.frEtapa2)
        self.frInfo1_2 = QtWidgets.QFrame(self.frProgressProcesso)
        self.frInfo1_2.setMinimumSize(QtCore.QSize(0, 42))
        self.frInfo1_2.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frInfo1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo1_2.setObjectName("frInfo1_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frInfo1_2)
        self.horizontalLayout_7.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbInfoProcessuais = QtWidgets.QLabel(self.frInfo1_2)
        self.lbInfoProcessuais.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfoProcessuais.setObjectName("lbInfoProcessuais")
        self.horizontalLayout_7.addWidget(self.lbInfoProcessuais)
        self.horizontalLayout_3.addWidget(self.frInfo1_2)
        self.horizontalLayout.addWidget(self.frProgressProcesso)
        self.frProg2 = QtWidgets.QFrame(self.frBarProgress)
        self.frProg2.setMinimumSize(QtCore.QSize(45, 10))
        self.frProg2.setMaximumSize(QtCore.QSize(45, 10))
        self.frProg2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frProg2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProg2.setObjectName("frProg2")
        self.horizontalLayout.addWidget(self.frProg2)
        self.frame_3 = QtWidgets.QFrame(self.frBarProgress)
        self.frame_3.setMinimumSize(QtCore.QSize(130, 42))
        self.frame_3.setMaximumSize(QtCore.QSize(130, 42))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frEtapa3 = QtWidgets.QFrame(self.frame_3)
        self.frEtapa3.setMinimumSize(QtCore.QSize(40, 42))
        self.frEtapa3.setMaximumSize(QtCore.QSize(40, 42))
        self.frEtapa3.setSizeIncrement(QtCore.QSize(0, 0))
        self.frEtapa3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEtapa3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEtapa3.setObjectName("frEtapa3")
        self.horizontalLayout_4.addWidget(self.frEtapa3)
        self.frInfo1_3 = QtWidgets.QFrame(self.frame_3)
        self.frInfo1_3.setMinimumSize(QtCore.QSize(0, 42))
        self.frInfo1_3.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frInfo1_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo1_3.setObjectName("frInfo1_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frInfo1_3)
        self.horizontalLayout_8.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbInfoDetalhamento = QtWidgets.QLabel(self.frInfo1_3)
        self.lbInfoDetalhamento.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfoDetalhamento.setObjectName("lbInfoDetalhamento")
        self.horizontalLayout_8.addWidget(self.lbInfoDetalhamento)
        self.horizontalLayout_4.addWidget(self.frInfo1_3)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frProg3 = QtWidgets.QFrame(self.frBarProgress)
        self.frProg3.setMinimumSize(QtCore.QSize(45, 10))
        self.frProg3.setMaximumSize(QtCore.QSize(45, 10))
        self.frProg3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frProg3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProg3.setObjectName("frProg3")
        self.horizontalLayout.addWidget(self.frProg3)
        self.frame_4 = QtWidgets.QFrame(self.frBarProgress)
        self.frame_4.setMinimumSize(QtCore.QSize(140, 42))
        self.frame_4.setMaximumSize(QtCore.QSize(140, 42))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frEtapa4 = QtWidgets.QFrame(self.frame_4)
        self.frEtapa4.setMinimumSize(QtCore.QSize(40, 42))
        self.frEtapa4.setMaximumSize(QtCore.QSize(40, 42))
        self.frEtapa4.setSizeIncrement(QtCore.QSize(0, 0))
        self.frEtapa4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEtapa4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEtapa4.setObjectName("frEtapa4")
        self.horizontalLayout_5.addWidget(self.frEtapa4)
        self.frInfo1_4 = QtWidgets.QFrame(self.frame_4)
        self.frInfo1_4.setMinimumSize(QtCore.QSize(0, 42))
        self.frInfo1_4.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frInfo1_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo1_4.setObjectName("frInfo1_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frInfo1_4)
        self.horizontalLayout_9.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbInfoFinalizacao = QtWidgets.QLabel(self.frInfo1_4)
        self.lbInfoFinalizacao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfoFinalizacao.setObjectName("lbInfoFinalizacao")
        self.horizontalLayout_9.addWidget(self.lbInfoFinalizacao)
        self.horizontalLayout_5.addWidget(self.frInfo1_4)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_4.addWidget(self.frBarProgress, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frTopBackground, 0, 1, 1, 1)
        self.frBottomBackground = QtWidgets.QFrame(self.centralwidget)
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
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frBottomBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(750, 430))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16755515))
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout_3.addWidget(self.stackedWidget)
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
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frBottom)
        self.horizontalLayout_10.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame = QtWidgets.QFrame(self.frBottom)
        self.frame.setMaximumSize(QtCore.QSize(230, 12))
        self.frame.setSizeIncrement(QtCore.QSize(230, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_10.addWidget(self.frame)
        self.pbVoltaEtapa = QtWidgets.QPushButton(self.frBottom)
        self.pbVoltaEtapa.setMinimumSize(QtCore.QSize(150, 32))
        self.pbVoltaEtapa.setMaximumSize(QtCore.QSize(230, 32))
        self.pbVoltaEtapa.setObjectName("pbVoltaEtapa")
        self.horizontalLayout_10.addWidget(self.pbVoltaEtapa)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.pbarProgresso = QtWidgets.QProgressBar(self.frBottom)
        self.pbarProgresso.setMinimumSize(QtCore.QSize(350, 10))
        self.pbarProgresso.setMaximumSize(QtCore.QSize(220, 10))
        self.pbarProgresso.setProperty("value", 24)
        self.pbarProgresso.setTextVisible(False)
        self.pbarProgresso.setInvertedAppearance(False)
        self.pbarProgresso.setObjectName("pbarProgresso")
        self.horizontalLayout_10.addWidget(self.pbarProgresso)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.pbProxEtapa = QtWidgets.QPushButton(self.frBottom)
        self.pbProxEtapa.setMinimumSize(QtCore.QSize(150, 32))
        self.pbProxEtapa.setMaximumSize(QtCore.QSize(230, 32))
        self.pbProxEtapa.setObjectName("pbProxEtapa")
        self.horizontalLayout_10.addWidget(self.pbProxEtapa)
        self.verticalLayout_3.addWidget(self.frBottom)
        self.gridLayout.addWidget(self.frBottomBackground, 1, 1, 1, 1)
        self.frBottomBackground.raise_()
        self.frTopBackground.raise_()
        self.frGuia.raise_()
        mwEntrevistaPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwEntrevistaPage)
        QtCore.QMetaObject.connectSlotsByName(mwEntrevistaPage)

    def retranslateUi(self, mwEntrevistaPage):
        _translate = QtCore.QCoreApplication.translate
        mwEntrevistaPage.setWindowTitle(_translate("mwEntrevistaPage", "MainWindow"))
        self.lbTituloGuia.setWhatsThis(_translate("mwEntrevistaPage", "<html><head/><body><p><br/></p></body></html>"))
        self.lbTituloGuia.setText(_translate("mwEntrevistaPage", "ETAPAS ENTREVISTA"))
        self.gbNatureza.setTitle(_translate("mwEntrevistaPage", "NATUREZA DO PROCESSO"))
        self.gbTipo.setTitle(_translate("mwEntrevistaPage", "TIPO DO PROCESSO"))
        self.gbBeneficio.setTitle(_translate("mwEntrevistaPage", "TIPO DO BENEFÍCIO"))
        self.gbQuestionario.setTitle(_translate("mwEntrevistaPage", "QUESTIONÁRIO"))
        self.pbConfSimulacao.setText(_translate("mwEntrevistaPage", "Simulação"))
        self.lbNomeEscritorio.setText(_translate("mwEntrevistaPage", "Nome do escritório"))
        self.lbNomeAdv.setText(_translate("mwEntrevistaPage", "Nome Advogado"))
        self.lbNumOab.setText(_translate("mwEntrevistaPage", "Numero OAB"))
        self.lbTopTitulo.setText(_translate("mwEntrevistaPage", "Entrevista Inicial"))
        self.lbTopSubtitulo.setText(_translate("mwEntrevistaPage", "Uma entrevista bem feita é determinante para o sucesso do processo."))
        self.lbInfoPessoais.setText(_translate("mwEntrevistaPage", "Informações \n"
"Pessoais"))
        self.lbInfoProcessuais.setText(_translate("mwEntrevistaPage", "Informações \n"
"Processuais"))
        self.lbInfoDetalhamento.setText(_translate("mwEntrevistaPage", "Detalhamento \n"
"do Processo"))
        self.lbInfoFinalizacao.setText(_translate("mwEntrevistaPage", "Documentação\n"
"e\n"
"Finalização"))
        self.pbVoltaEtapa.setText(_translate("mwEntrevistaPage", "Etapa anterior"))
        self.pbProxEtapa.setText(_translate("mwEntrevistaPage", "Próxima etapa"))
import Resources.entrevistaPage


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwEntrevistaPage = QtWidgets.QMainWindow()
    ui = Ui_mwEntrevistaPage()
    ui.setupUi(mwEntrevistaPage)
    mwEntrevistaPage.show()
    sys.exit(app.exec_())
