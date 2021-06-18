# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrevistaPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwEntrevistaPage(object):
    def setupUi(self, mwEntrevistaPage):
        mwEntrevistaPage.setObjectName("mwEntrevistaPage")
        mwEntrevistaPage.resize(1280, 820)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mwEntrevistaPage.sizePolicy().hasHeightForWidth())
        mwEntrevistaPage.setSizePolicy(sizePolicy)
        mwEntrevistaPage.setMinimumSize(QtCore.QSize(1280, 815))
        self.centralwidget = QtWidgets.QWidget(mwEntrevistaPage)
        self.centralwidget.setStyleSheet("/*-------------------------------------- Frames --------------------------------------*/\n"
"#frTopBackground{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.483, x2:0, y2:0.539773, stop:0 rgba(39, 86, 135, 255), stop:1 rgba(62, 141, 225, 204));\n"
"}\n"
"\n"
"#frBottomBackground{\n"
"    background-color: rgb(241, 241, 241);\n"
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
"#frRight {\n"
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
"    border-radius: 5px;\n"
"}\n"
"\n"
"/*-------------------------------------- Push Buttons ------------------------------*/\n"
"#pbProxEtapa {\n"
"    background-color: qlineargradient(spread:pad, x1:0.913, y1:0.096, x2:0.005, y2:1, stop:0 rgba(86, 178, 169, 255), stop:1 rgba(21, 135, 133, 255));\n"
"    border-radius: 16px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#pbProxEtapa:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.913, y1:0.096, x2:0.005, y2:1, stop:0 rgba(86, 178, 169, 255), stop:1 rgba(51, 165, 163, 255));\n"
"    border-radius: 16px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#pbVoltaEtapa {\n"
"    background-color: qlineargradient(spread:pad, x1:0.877204, y1:0.193, x2:0.301, y2:0.773, stop:0 rgba(167, 66, 146, 255), stop:1 rgba(131, 52, 169, 255));\n"
"    border-radius: 16px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#pbVoltaEtapa:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.469, y1:0, x2:0.464, y2:1, stop:0 rgba(102, 70, 147, 255), stop:1 rgba(127, 52, 169, 255));\n"
"    border-radius: 16px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    color: white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frTopBackground = QtWidgets.QFrame(self.centralwidget)
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
        self.verticalLayout.addWidget(self.frTopBackground)
        self.frBottomBackground = QtWidgets.QFrame(self.centralwidget)
        self.frBottomBackground.setMinimumSize(QtCore.QSize(800, 700))
        self.frBottomBackground.setMaximumSize(QtCore.QSize(16777215, 800))
        self.frBottomBackground.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBottomBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBottomBackground.setObjectName("frBottomBackground")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frBottomBackground)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frBottomBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(750, 682))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_18.addWidget(self.stackedWidget)
        self.frRight = QtWidgets.QFrame(self.frBottomBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frRight.sizePolicy().hasHeightForWidth())
        self.frRight.setSizePolicy(sizePolicy)
        self.frRight.setMinimumSize(QtCore.QSize(250, 600))
        self.frRight.setMaximumSize(QtCore.QSize(280, 600))
        self.frRight.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frRight.setObjectName("frRight")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frRight)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frNaturezaRight = QtWidgets.QFrame(self.frRight)
        self.frNaturezaRight.setMinimumSize(QtCore.QSize(210, 40))
        self.frNaturezaRight.setMaximumSize(QtCore.QSize(210, 40))
        self.frNaturezaRight.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frNaturezaRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNaturezaRight.setObjectName("frNaturezaRight")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frNaturezaRight)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frInfo1Icon = QtWidgets.QFrame(self.frNaturezaRight)
        self.frInfo1Icon.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frInfo1Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo1Icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo1Icon.setObjectName("frInfo1Icon")
        self.horizontalLayout_10.addWidget(self.frInfo1Icon)
        self.frame_5 = QtWidgets.QFrame(self.frNaturezaRight)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lbInfo1 = QtWidgets.QLabel(self.frame_5)
        self.lbInfo1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo1.setObjectName("lbInfo1")
        self.horizontalLayout_14.addWidget(self.lbInfo1)
        self.horizontalLayout_10.addWidget(self.frame_5)
        self.verticalLayout_3.addWidget(self.frNaturezaRight, 0, QtCore.Qt.AlignHCenter)
        self.frTipoProcRight = QtWidgets.QFrame(self.frRight)
        self.frTipoProcRight.setMinimumSize(QtCore.QSize(210, 40))
        self.frTipoProcRight.setMaximumSize(QtCore.QSize(210, 40))
        self.frTipoProcRight.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTipoProcRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTipoProcRight.setObjectName("frTipoProcRight")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frTipoProcRight)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frInfo2Icon = QtWidgets.QFrame(self.frTipoProcRight)
        self.frInfo2Icon.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frInfo2Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo2Icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo2Icon.setObjectName("frInfo2Icon")
        self.horizontalLayout_11.addWidget(self.frInfo2Icon)
        self.frame_8 = QtWidgets.QFrame(self.frTipoProcRight)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lbInfo2 = QtWidgets.QLabel(self.frame_8)
        self.lbInfo2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo2.setObjectName("lbInfo2")
        self.horizontalLayout_15.addWidget(self.lbInfo2)
        self.horizontalLayout_11.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.frTipoProcRight, 0, QtCore.Qt.AlignHCenter)
        self.frTipoBeneRight = QtWidgets.QFrame(self.frRight)
        self.frTipoBeneRight.setMinimumSize(QtCore.QSize(210, 40))
        self.frTipoBeneRight.setMaximumSize(QtCore.QSize(210, 40))
        self.frTipoBeneRight.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTipoBeneRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTipoBeneRight.setObjectName("frTipoBeneRight")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frTipoBeneRight)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frInfo3Icon = QtWidgets.QFrame(self.frTipoBeneRight)
        self.frInfo3Icon.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frInfo3Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo3Icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo3Icon.setObjectName("frInfo3Icon")
        self.horizontalLayout_12.addWidget(self.frInfo3Icon)
        self.frame_11 = QtWidgets.QFrame(self.frTipoBeneRight)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lbInfo3 = QtWidgets.QLabel(self.frame_11)
        self.lbInfo3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo3.setObjectName("lbInfo3")
        self.horizontalLayout_16.addWidget(self.lbInfo3)
        self.horizontalLayout_12.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frTipoBeneRight, 0, QtCore.Qt.AlignHCenter)
        self.frTiposAtiv = QtWidgets.QFrame(self.frRight)
        self.frTiposAtiv.setMinimumSize(QtCore.QSize(210, 40))
        self.frTiposAtiv.setMaximumSize(QtCore.QSize(210, 40))
        self.frTiposAtiv.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTiposAtiv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTiposAtiv.setObjectName("frTiposAtiv")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frTiposAtiv)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frInfo4Icon = QtWidgets.QFrame(self.frTiposAtiv)
        self.frInfo4Icon.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frInfo4Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo4Icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo4Icon.setObjectName("frInfo4Icon")
        self.horizontalLayout_13.addWidget(self.frInfo4Icon)
        self.frame_14 = QtWidgets.QFrame(self.frTiposAtiv)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lbInfo4 = QtWidgets.QLabel(self.frame_14)
        self.lbInfo4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo4.setObjectName("lbInfo4")
        self.horizontalLayout_17.addWidget(self.lbInfo4)
        self.horizontalLayout_13.addWidget(self.frame_14)
        self.verticalLayout_3.addWidget(self.frTiposAtiv, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pbProxEtapa = QtWidgets.QPushButton(self.frRight)
        self.pbProxEtapa.setMinimumSize(QtCore.QSize(230, 32))
        self.pbProxEtapa.setMaximumSize(QtCore.QSize(230, 32))
        self.pbProxEtapa.setObjectName("pbProxEtapa")
        self.verticalLayout_3.addWidget(self.pbProxEtapa, 0, QtCore.Qt.AlignHCenter)
        self.pbVoltaEtapa = QtWidgets.QPushButton(self.frRight)
        self.pbVoltaEtapa.setMinimumSize(QtCore.QSize(230, 32))
        self.pbVoltaEtapa.setMaximumSize(QtCore.QSize(230, 32))
        self.pbVoltaEtapa.setObjectName("pbVoltaEtapa")
        self.verticalLayout_3.addWidget(self.pbVoltaEtapa, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.frRight)
        self.frame.setMaximumSize(QtCore.QSize(230, 12))
        self.frame.setSizeIncrement(QtCore.QSize(230, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_19.addItem(spacerItem1)
        self.pbarProgresso = QtWidgets.QProgressBar(self.frame)
        self.pbarProgresso.setMinimumSize(QtCore.QSize(220, 10))
        self.pbarProgresso.setMaximumSize(QtCore.QSize(220, 10))
        self.pbarProgresso.setProperty("value", 24)
        self.pbarProgresso.setTextVisible(False)
        self.pbarProgresso.setInvertedAppearance(False)
        self.pbarProgresso.setObjectName("pbarProgresso")
        self.horizontalLayout_19.addWidget(self.pbarProgresso)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_18.addWidget(self.frRight)
        self.verticalLayout.addWidget(self.frBottomBackground, 0, QtCore.Qt.AlignTop)
        self.frBottomBackground.raise_()
        self.frTopBackground.raise_()
        mwEntrevistaPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwEntrevistaPage)
        QtCore.QMetaObject.connectSlotsByName(mwEntrevistaPage)

    def retranslateUi(self, mwEntrevistaPage):
        _translate = QtCore.QCoreApplication.translate
        mwEntrevistaPage.setWindowTitle(_translate("mwEntrevistaPage", "MainWindow"))
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
        self.lbInfo1.setText(_translate("mwEntrevistaPage", "Natureza do\n"
" Processo"))
        self.lbInfo2.setText(_translate("mwEntrevistaPage", "Tipo do \n"
"Processo"))
        self.lbInfo3.setText(_translate("mwEntrevistaPage", "Tipo do \n"
"Benefício"))
        self.lbInfo4.setText(_translate("mwEntrevistaPage", "Tipos de \n"
"Atividades"))
        self.pbProxEtapa.setText(_translate("mwEntrevistaPage", "Próxima etapa"))
        self.pbVoltaEtapa.setText(_translate("mwEntrevistaPage", "Etapa anterior"))
import Resources.entrevistaPage


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwEntrevistaPage = QtWidgets.QMainWindow()
    ui = Ui_mwEntrevistaPage()
    ui.setupUi(mwEntrevistaPage)
    mwEntrevistaPage.show()
    sys.exit(app.exec_())
