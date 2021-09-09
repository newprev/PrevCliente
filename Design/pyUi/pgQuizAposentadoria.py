# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pgQuizAposentadoria.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgQuizAposentadoria(object):
    def setupUi(self, wdgQuizAposentadoria):
        wdgQuizAposentadoria.setObjectName("wdgQuizAposentadoria")
        wdgQuizAposentadoria.resize(891, 665)
        wdgQuizAposentadoria.setStyleSheet("/* ------------------------------ Widgets ------------------------------ */\n"
"#wdgNatureza{\n"
"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* ------------------------------ Frames ------------------------------ */\n"
"#frMain{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 246, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#frInfo1, #frInfo2 {\n"
"    background-color: rgb(17, 102, 0);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frInfo3, #frInfo4 {\n"
"    background-color: rgb(27, 113, 10);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frInfo5, #frInfo6 {\n"
"    background-color: rgb(37, 123, 20);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frInfo7, #frInfo8 {\n"
"    background-color: rgb(47, 133, 30);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frInfo9, #frInfo10 {\n"
"    background-color: rgb(57, 143, 40);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frInfo11, #frInfo12 {\n"
"    background-color: rgb(67, 153, 50);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frInfo13, #frInfo14 {\n"
"    background-color: rgb(77, 163, 60);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frInfo15, #frInfo16 {\n"
"    background-color: rgb(87, 173, 70);\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"#frAtiv1, #frAtiv4, #frAtiv7, \n"
"#frAtiv8, #frAtiv9, #frAtiv10  {\n"
"    background-image: url(:/info/information.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"/* ------------------------------ Labels ------------------------------ */\n"
"#lbTituloNatureza, #lbOu {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"\n"
"    color: grey;\n"
"}\n"
"\n"
"/* ------------------------------ CheckBox ------------------------------ */\n"
"#cbAtiv1, #cbAtiv2, #cbAtiv3, \n"
"#cbAtiv4, #cbAtiv5, #cbAtiv6, \n"
"#cbAtiv7, #cbAtiv8, #cbAtiv9, \n"
"#cbAtiv10, #cbAtiv11, #cbAtiv12, \n"
"#cbAtiv13, #cbAtiv14, #cbAtiv15, \n"
"#cbAtiv16 {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#cbAtiv1::indicator , #cbAtiv2::indicator , #cbAtiv3::indicator , \n"
"#cbAtiv4::indicator , #cbAtiv5::indicator , #cbAtiv6::indicator , \n"
"#cbAtiv7::indicator , #cbAtiv8::indicator , #cbAtiv9::indicator , \n"
"#cbAtiv10::indicator , #cbAtiv11::indicator , #cbAtiv12::indicator , \n"
"#cbAtiv13::indicator, #cbAtiv14::indicator, #cbAtiv15::indicator, \n"
"#cbAtiv16::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"/* ------------------------------ Push Buttons ------------------------------ */\n"
"#pbApos, #pbAposDeficiencia, #pbAposEspecial,\n"
"#pbAposRural, #pbAuxReclusao, #pbAuxilioDoenca,\n"
"#pbBeneDeficiencia, #pbBeneIdoso, #pbPensaoMorte,\n"
"#pbSalMaternidade {\n"
"    background-color: rgb(117, 80, 123);\n"
"    border-radius: 16px;\n"
"\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"    color: white;    \n"
"}\n"
"\n"
"#pbApos:hover, #pbApos:hover, #pbAposDeficiencia:hover, #pbAposEspecial:hover,\n"
"#pbAposRural:hover, #pbAuxReclusao:hover, #pbAuxilioDoenca:hover,\n"
"#pbBeneDeficiencia:hover, #pbBeneIdoso:hover, #pbPensaoMorte:hover,\n"
"#pbSalMaternidade:hover {\n"
"    background-color: rgb(115, 210, 22);\n"
"    border-radius: 16px;\n"
"\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"    color: white;    \n"
"}\n"
"\n"
"/* ------------------------------ Scroll Area ------------------------------ */\n"
"#scrollArea, #scrollCentral {\n"
"    background-color: transparent;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(wdgQuizAposentadoria)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frMain = QtWidgets.QFrame(wdgQuizAposentadoria)
        self.frMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.gridLayout = QtWidgets.QGridLayout(self.frMain)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frMain)
        self.frame_2.setMaximumSize(QtCore.QSize(16777214, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbTituloNatureza = QtWidgets.QLabel(self.frame_2)
        self.lbTituloNatureza.setObjectName("lbTituloNatureza")
        self.horizontalLayout.addWidget(self.lbTituloNatureza)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.frMain)
        self.scrollArea.setMinimumSize(QtCore.QSize(830, 500))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollCentral = QtWidgets.QWidget()
        self.scrollCentral.setGeometry(QtCore.QRect(0, 0, 875, 1388))
        self.scrollCentral.setObjectName("scrollCentral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollCentral)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frInfo1 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo1.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo1.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo1.setObjectName("frInfo1")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frInfo1)
        self.horizontalLayout_14.setContentsMargins(16, 4, 32, 4)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.cbAtiv1 = QtWidgets.QCheckBox(self.frInfo1)
        self.cbAtiv1.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv1.setObjectName("cbAtiv1")
        self.horizontalLayout_14.addWidget(self.cbAtiv1)
        self.frAtiv1 = QtWidgets.QFrame(self.frInfo1)
        self.frAtiv1.setMinimumSize(QtCore.QSize(36, 36))
        self.frAtiv1.setMaximumSize(QtCore.QSize(36, 36))
        self.frAtiv1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAtiv1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAtiv1.setObjectName("frAtiv1")
        self.horizontalLayout_14.addWidget(self.frAtiv1)
        self.verticalLayout_2.addWidget(self.frInfo1, 0, QtCore.Qt.AlignHCenter)
        self.frInfo2 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo2.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo2.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo2.setObjectName("frInfo2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frInfo2)
        self.horizontalLayout_3.setContentsMargins(16, 4, 4, 4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbAtiv2 = QtWidgets.QCheckBox(self.frInfo2)
        self.cbAtiv2.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv2.setObjectName("cbAtiv2")
        self.horizontalLayout_3.addWidget(self.cbAtiv2)
        self.verticalLayout_2.addWidget(self.frInfo2, 0, QtCore.Qt.AlignHCenter)
        self.frInfo3 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo3.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo3.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo3.setObjectName("frInfo3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frInfo3)
        self.horizontalLayout_4.setContentsMargins(16, 4, 4, 4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbAtiv3 = QtWidgets.QCheckBox(self.frInfo3)
        self.cbAtiv3.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv3.setObjectName("cbAtiv3")
        self.horizontalLayout_4.addWidget(self.cbAtiv3)
        self.verticalLayout_2.addWidget(self.frInfo3, 0, QtCore.Qt.AlignHCenter)
        self.frInfo4 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo4.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo4.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo4.setObjectName("frInfo4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frInfo4)
        self.horizontalLayout_5.setContentsMargins(16, 4, 32, 4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cbAtiv4 = QtWidgets.QCheckBox(self.frInfo4)
        self.cbAtiv4.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv4.setObjectName("cbAtiv4")
        self.horizontalLayout_5.addWidget(self.cbAtiv4)
        self.frAtiv4 = QtWidgets.QFrame(self.frInfo4)
        self.frAtiv4.setMinimumSize(QtCore.QSize(36, 36))
        self.frAtiv4.setMaximumSize(QtCore.QSize(36, 36))
        self.frAtiv4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAtiv4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAtiv4.setObjectName("frAtiv4")
        self.horizontalLayout_5.addWidget(self.frAtiv4)
        self.verticalLayout_2.addWidget(self.frInfo4, 0, QtCore.Qt.AlignHCenter)
        self.frInfo5 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo5.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo5.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo5.setObjectName("frInfo5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frInfo5)
        self.horizontalLayout_6.setContentsMargins(16, 4, 4, 4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbAtiv5 = QtWidgets.QCheckBox(self.frInfo5)
        self.cbAtiv5.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv5.setObjectName("cbAtiv5")
        self.horizontalLayout_6.addWidget(self.cbAtiv5)
        self.verticalLayout_2.addWidget(self.frInfo5, 0, QtCore.Qt.AlignHCenter)
        self.frInfo6 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo6.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo6.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo6.setObjectName("frInfo6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frInfo6)
        self.horizontalLayout_7.setContentsMargins(16, 4, 4, 4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cbAtiv6 = QtWidgets.QCheckBox(self.frInfo6)
        self.cbAtiv6.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv6.setObjectName("cbAtiv6")
        self.horizontalLayout_7.addWidget(self.cbAtiv6)
        self.verticalLayout_2.addWidget(self.frInfo6, 0, QtCore.Qt.AlignHCenter)
        self.frInfo7 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo7.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo7.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo7.setObjectName("frInfo7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frInfo7)
        self.horizontalLayout_8.setContentsMargins(16, 4, 32, 4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cbAtiv7 = QtWidgets.QCheckBox(self.frInfo7)
        self.cbAtiv7.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv7.setObjectName("cbAtiv7")
        self.horizontalLayout_8.addWidget(self.cbAtiv7)
        self.frAtiv7 = QtWidgets.QFrame(self.frInfo7)
        self.frAtiv7.setMinimumSize(QtCore.QSize(36, 36))
        self.frAtiv7.setMaximumSize(QtCore.QSize(36, 36))
        self.frAtiv7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAtiv7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAtiv7.setObjectName("frAtiv7")
        self.horizontalLayout_8.addWidget(self.frAtiv7)
        self.verticalLayout_2.addWidget(self.frInfo7, 0, QtCore.Qt.AlignHCenter)
        self.frInfo8 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo8.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo8.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo8.setObjectName("frInfo8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frInfo8)
        self.horizontalLayout_9.setContentsMargins(16, 4, 32, 4)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cbAtiv8 = QtWidgets.QCheckBox(self.frInfo8)
        self.cbAtiv8.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv8.setObjectName("cbAtiv8")
        self.horizontalLayout_9.addWidget(self.cbAtiv8)
        self.frAtiv8 = QtWidgets.QFrame(self.frInfo8)
        self.frAtiv8.setMinimumSize(QtCore.QSize(36, 36))
        self.frAtiv8.setMaximumSize(QtCore.QSize(36, 36))
        self.frAtiv8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAtiv8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAtiv8.setObjectName("frAtiv8")
        self.horizontalLayout_9.addWidget(self.frAtiv8)
        self.verticalLayout_2.addWidget(self.frInfo8, 0, QtCore.Qt.AlignHCenter)
        self.frInfo9 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo9.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo9.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo9.setObjectName("frInfo9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frInfo9)
        self.horizontalLayout_10.setContentsMargins(16, 4, 32, 4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cbAtiv9 = QtWidgets.QCheckBox(self.frInfo9)
        self.cbAtiv9.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv9.setObjectName("cbAtiv9")
        self.horizontalLayout_10.addWidget(self.cbAtiv9)
        self.frAtiv9 = QtWidgets.QFrame(self.frInfo9)
        self.frAtiv9.setMinimumSize(QtCore.QSize(36, 36))
        self.frAtiv9.setMaximumSize(QtCore.QSize(36, 36))
        self.frAtiv9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAtiv9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAtiv9.setObjectName("frAtiv9")
        self.horizontalLayout_10.addWidget(self.frAtiv9)
        self.verticalLayout_2.addWidget(self.frInfo9, 0, QtCore.Qt.AlignHCenter)
        self.frInfo10 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo10.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo10.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo10.setObjectName("frInfo10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frInfo10)
        self.horizontalLayout_15.setContentsMargins(16, 4, 32, 4)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.cbAtiv10 = QtWidgets.QCheckBox(self.frInfo10)
        self.cbAtiv10.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv10.setObjectName("cbAtiv10")
        self.horizontalLayout_15.addWidget(self.cbAtiv10)
        self.frAtiv10 = QtWidgets.QFrame(self.frInfo10)
        self.frAtiv10.setMinimumSize(QtCore.QSize(36, 36))
        self.frAtiv10.setMaximumSize(QtCore.QSize(36, 36))
        self.frAtiv10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAtiv10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAtiv10.setObjectName("frAtiv10")
        self.horizontalLayout_15.addWidget(self.frAtiv10)
        self.verticalLayout_2.addWidget(self.frInfo10, 0, QtCore.Qt.AlignHCenter)
        self.frInfo11 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo11.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo11.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfo11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo11.setObjectName("frInfo11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frInfo11)
        self.horizontalLayout_11.setContentsMargins(16, 4, 4, 4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cbAtiv11 = QtWidgets.QCheckBox(self.frInfo11)
        self.cbAtiv11.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv11.setObjectName("cbAtiv11")
        self.horizontalLayout_11.addWidget(self.cbAtiv11)
        self.verticalLayout_2.addWidget(self.frInfo11, 0, QtCore.Qt.AlignHCenter)
        self.frInfo12 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo12.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo12.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo12.setObjectName("frInfo12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frInfo12)
        self.horizontalLayout_12.setContentsMargins(16, 4, 4, 4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cbAtiv12 = QtWidgets.QCheckBox(self.frInfo12)
        self.cbAtiv12.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv12.setObjectName("cbAtiv12")
        self.horizontalLayout_12.addWidget(self.cbAtiv12)
        self.verticalLayout_2.addWidget(self.frInfo12, 0, QtCore.Qt.AlignHCenter)
        self.frInfo13 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo13.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo13.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo13.setObjectName("frInfo13")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frInfo13)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.cbAtiv13 = QtWidgets.QCheckBox(self.frInfo13)
        self.cbAtiv13.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv13.setObjectName("cbAtiv13")
        self.horizontalLayout_17.addWidget(self.cbAtiv13)
        self.verticalLayout_2.addWidget(self.frInfo13, 0, QtCore.Qt.AlignHCenter)
        self.frInfo14 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo14.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo14.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo14.setObjectName("frInfo14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frInfo14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbAtiv14 = QtWidgets.QCheckBox(self.frInfo14)
        self.cbAtiv14.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv14.setObjectName("cbAtiv14")
        self.horizontalLayout_2.addWidget(self.cbAtiv14)
        self.verticalLayout_2.addWidget(self.frInfo14, 0, QtCore.Qt.AlignHCenter)
        self.frInfo15 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo15.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo15.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo15.setObjectName("frInfo15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frInfo15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.cbAtiv15 = QtWidgets.QCheckBox(self.frInfo15)
        self.cbAtiv15.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv15.setObjectName("cbAtiv15")
        self.horizontalLayout_13.addWidget(self.cbAtiv15)
        self.verticalLayout_2.addWidget(self.frInfo15, 0, QtCore.Qt.AlignHCenter)
        self.frInfo16 = QtWidgets.QFrame(self.scrollCentral)
        self.frInfo16.setMinimumSize(QtCore.QSize(800, 80))
        self.frInfo16.setMaximumSize(QtCore.QSize(800, 80))
        self.frInfo16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfo16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfo16.setObjectName("frInfo16")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frInfo16)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.cbAtiv16 = QtWidgets.QCheckBox(self.frInfo16)
        self.cbAtiv16.setMinimumSize(QtCore.QSize(0, 70))
        self.cbAtiv16.setObjectName("cbAtiv16")
        self.horizontalLayout_16.addWidget(self.cbAtiv16)
        self.verticalLayout_2.addWidget(self.frInfo16, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollCentral)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frMain)

        self.retranslateUi(wdgQuizAposentadoria)
        QtCore.QMetaObject.connectSlotsByName(wdgQuizAposentadoria)

    def retranslateUi(self, wdgQuizAposentadoria):
        _translate = QtCore.QCoreApplication.translate
        wdgQuizAposentadoria.setWindowTitle(_translate("wdgQuizAposentadoria", "Form"))
        self.lbTituloNatureza.setText(_translate("wdgQuizAposentadoria", "Questionário aposentadoria"))
        self.cbAtiv1.setText(_translate("wdgQuizAposentadoria", "    Existe labor em condições insalubres/especiais?"))
        self.cbAtiv2.setText(_translate("wdgQuizAposentadoria", "    Existe labor em condição de deficiente?"))
        self.cbAtiv3.setText(_translate("wdgQuizAposentadoria", "    Possui tempo de serviço militar?"))
        self.cbAtiv4.setText(_translate("wdgQuizAposentadoria", "    Possui tempo em regime próprio?"))
        self.cbAtiv5.setText(_translate("wdgQuizAposentadoria", "    Possui tempo rural?"))
        self.cbAtiv6.setText(_translate("wdgQuizAposentadoria", "    Possui tempo como professor do ensino fundamental \n"
"    e médio?"))
        self.cbAtiv7.setText(_translate("wdgQuizAposentadoria", "    Existem contribuições inferiores ao salário mínimo?"))
        self.cbAtiv8.setText(_translate("wdgQuizAposentadoria", "    Existem contribuições realizadas no percentual \n"
"    de 5% (IMEI) ou 5% baixa renda (IREC-FBR)?"))
        self.cbAtiv9.setText(_translate("wdgQuizAposentadoria", "    Existem contribuições realizadas no \n"
"    percentual de 11% (ILEI123 ou IREC-LC123)?"))
        self.cbAtiv10.setText(_translate("wdgQuizAposentadoria", "    Existe algum indicativo no CNIS?"))
        self.cbAtiv11.setText(_translate("wdgQuizAposentadoria", "    Existe algum período laborado que conste \n"
"    no CNIS mas que precisa ser editado?"))
        self.cbAtiv12.setText(_translate("wdgQuizAposentadoria", "    Existe algum período laborado que conste no CNIS mas que \n"
"    o salário de contribuição está incorreto e precisa ser editado?"))
        self.cbAtiv13.setText(_translate("wdgQuizAposentadoria", "    Existe algum período laborado que não conste no CNIS?"))
        self.cbAtiv14.setText(_translate("wdgQuizAposentadoria", "    Já teve alguma ação trabalhista?"))
        self.cbAtiv15.setText(_translate("wdgQuizAposentadoria", "    Já trabalhou como aprendiz em escola \n"
"    técnica SENAI/SENAC?"))
        self.cbAtiv16.setText(_translate("wdgQuizAposentadoria", "    Já trabalhou como seminarista ou ministro de \n"
"    confissão religiosa?"))
import Resources.quizApos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgQuizAposentadoria = QtWidgets.QWidget()
    ui = Ui_wdgQuizAposentadoria()
    ui.setupUi(wdgQuizAposentadoria)
    wdgQuizAposentadoria.show()
    sys.exit(app.exec_())