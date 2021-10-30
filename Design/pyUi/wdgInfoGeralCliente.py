# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wdgInfoGeralCliente.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgInfoGeralCliente(object):
    def setupUi(self, wdgInfoGeralCliente):
        wdgInfoGeralCliente.setObjectName("wdgInfoGeralCliente")
        wdgInfoGeralCliente.resize(1115, 622)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdgInfoGeralCliente.sizePolicy().hasHeightForWidth())
        wdgInfoGeralCliente.setSizePolicy(sizePolicy)
        wdgInfoGeralCliente.setStyleSheet("/*------------------------------------ Frames ------------------------------------*/\n"
"#frTabInfo {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*------------------------------------ Scroll Area ------------------------------------*/\n"
"QScrollArea {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*---------------------------------------- Grid ----------------------------------------\n"
"#scaPessoais, #scaResidencial, #scaProfissional {\n"
"    background-color: rgb(233, 241, 247);\n"
"    border-radius: 10px;\n"
"}*/\n"
"\n"
"/*------------------------------------ Labels ------------------------------------*/\n"
"#lbCdCliente {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#lbNomeCliente {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"/*------------------------------------ Tab ------------------------------------*/\n"
"#tabInfoCliente::pane {\n"
"    border-top: 2px solid lightgrey;\n"
"    margin-top: -5px;\n"
"}\n"
"\n"
"#tabInfoCliente::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"#tabInfoCliente > QTabBar::tab {\n"
"    background-color: transparent    ;\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    padding: 10px 20px 10px 20px;\n"
"    min-width: 101px;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"#tabInfoCliente > QTabBar::tab:selected {\n"
"    background-color: transparent    ;\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 17px;\n"
"    color: rgb(82, 111, 139);\n"
"    padding: 8px;\n"
"    margin: 2px;\n"
"    min-width: 100px;\n"
"\n"
"    border-style: groove;\n"
"    border-width: 3px;\n"
"    border-color: transparent transparent rgb(82, 111, 139) transparent;\n"
"}\n"
"/*\n"
"#tabInfoCliente > QTabBar::tab:last{\n"
"    background-color: transparent    ;\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    padding: 8px;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"#tabInfoCliente > QTabBar::tab:last:selected {\n"
"    background-color: transparent    ;\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 13px;\n"
"    color: rgb(82, 111, 139);\n"
"    padding: 8px;\n"
"    margin: 2px;\n"
"\n"
"    border-style: groove;\n"
"    border-width: 3px;\n"
"    border-color: transparent transparent rgb(82, 111, 139) transparent;\n"
"}*/")
        self.verticalLayout = QtWidgets.QVBoxLayout(wdgInfoGeralCliente)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frMain = QtWidgets.QFrame(wdgInfoGeralCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMain.sizePolicy().hasHeightForWidth())
        self.frMain.setSizePolicy(sizePolicy)
        self.frMain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frMain)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frCabecalho = QtWidgets.QFrame(self.frMain)
        self.frCabecalho.setMinimumSize(QtCore.QSize(0, 90))
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frCabecalho.setStyleSheet("#lbCdCliente {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#lbInfoCdCliente {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    color: rgb(159, 159, 159);\n"
"}")
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frCabecalho)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frCabecalho)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbNomeCliente = QtWidgets.QLabel(self.frame_3)
        self.lbNomeCliente.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbNomeCliente.setObjectName("lbNomeCliente")
        self.verticalLayout_3.addWidget(self.lbNomeCliente)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(16)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.lbInfoCdCliente = QtWidgets.QLabel(self.frame_7)
        self.lbInfoCdCliente.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lbInfoCdCliente.setObjectName("lbInfoCdCliente")
        self.horizontalLayout_32.addWidget(self.lbInfoCdCliente)
        self.lbCdCliente = QtWidgets.QLabel(self.frame_7)
        self.lbCdCliente.setText("")
        self.lbCdCliente.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbCdCliente.setObjectName("lbCdCliente")
        self.horizontalLayout_32.addWidget(self.lbCdCliente)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frCabecalho)
        self.frame_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbInfoNotaCliente = QtWidgets.QLabel(self.frame_4)
        self.lbInfoNotaCliente.setObjectName("lbInfoNotaCliente")
        self.verticalLayout_4.addWidget(self.lbInfoNotaCliente)
        self.lbNotaCliente = QtWidgets.QLabel(self.frame_4)
        self.lbNotaCliente.setObjectName("lbNotaCliente")
        self.verticalLayout_4.addWidget(self.lbNotaCliente)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frCabecalho)
        self.frTabInfo = QtWidgets.QFrame(self.frMain)
        self.frTabInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTabInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTabInfo.setObjectName("frTabInfo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frTabInfo)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabInfoCliente = QtWidgets.QTabWidget(self.frTabInfo)
        self.tabInfoCliente.setStyleSheet("")
        self.tabInfoCliente.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabInfoCliente.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabInfoCliente.setElideMode(QtCore.Qt.ElideRight)
        self.tabInfoCliente.setUsesScrollButtons(False)
        self.tabInfoCliente.setMovable(True)
        self.tabInfoCliente.setTabBarAutoHide(True)
        self.tabInfoCliente.setObjectName("tabInfoCliente")
        self.tabInfoPessoais = QtWidgets.QWidget()
        self.tabInfoPessoais.setStyleSheet("/*---------------------------------------- Frames ----------------------------------------*/\n"
"#scaPessoais > QFrame {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: transparent transparent rgb(227, 227, 227) transparent;\n"
"}\n"
"\n"
"/*---------------------------------------- Labels ----------------------------------------*/\n"
"#lbNome, #lbSobrenome, #lbEscolaridade,\n"
"#lbSexo, #lbRg, #lbNomeMae,\n"
"#lbDtNascimento, #lbIdade, #lbEmail,\n"
"#lbEstadoCivil, #lbCpf {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#lbInfoNome, #lbInfoSobrenome, #lbInfoEscolaridade,\n"
"#lbInfoSexo, #lbInfoRg, #lbInfoNomeMae,\n"
"#lbInfoDtNascimento, #lbInfoIdade, #lbInfoEmail,\n"
"#lbInfoEstadoCivil, #lbInfoCpf {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    color: rgb(159, 159, 159);\n"
"}\n"
"")
        self.tabInfoPessoais.setObjectName("tabInfoPessoais")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabInfoPessoais)
        self.horizontalLayout_3.setContentsMargins(0, 32, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tabInfoPessoais)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scaPessoais = QtWidgets.QWidget()
        self.scaPessoais.setGeometry(QtCore.QRect(0, 0, 1093, 437))
        self.scaPessoais.setObjectName("scaPessoais")
        self.gridLayout = QtWidgets.QGridLayout(self.scaPessoais)
        self.gridLayout.setContentsMargins(16, 8, 16, 8)
        self.gridLayout.setHorizontalSpacing(24)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.frNome = QtWidgets.QFrame(self.scaPessoais)
        self.frNome.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frNome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frNome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNome.setObjectName("frNome")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frNome)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbInfoNome = QtWidgets.QLabel(self.frNome)
        self.lbInfoNome.setObjectName("lbInfoNome")
        self.horizontalLayout_4.addWidget(self.lbInfoNome)
        self.lbNome = QtWidgets.QLabel(self.frNome)
        self.lbNome.setText("")
        self.lbNome.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbNome.setObjectName("lbNome")
        self.horizontalLayout_4.addWidget(self.lbNome)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addWidget(self.frNome, 0, 0, 1, 1)
        self.frRg = QtWidgets.QFrame(self.scaPessoais)
        self.frRg.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frRg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frRg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frRg.setObjectName("frRg")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frRg)
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_6.setSpacing(16)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbInfoRg = QtWidgets.QLabel(self.frRg)
        self.lbInfoRg.setObjectName("lbInfoRg")
        self.horizontalLayout_6.addWidget(self.lbInfoRg)
        self.lbRg = QtWidgets.QLabel(self.frRg)
        self.lbRg.setText("")
        self.lbRg.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbRg.setObjectName("lbRg")
        self.horizontalLayout_6.addWidget(self.lbRg)
        spacerItem1 = QtWidgets.QSpacerItem(452, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frRg, 3, 0, 1, 1)
        self.frEstadoCivil = QtWidgets.QFrame(self.scaPessoais)
        self.frEstadoCivil.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frEstadoCivil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEstadoCivil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEstadoCivil.setObjectName("frEstadoCivil")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frEstadoCivil)
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_11.setSpacing(16)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbInfoEstadoCivil = QtWidgets.QLabel(self.frEstadoCivil)
        self.lbInfoEstadoCivil.setObjectName("lbInfoEstadoCivil")
        self.horizontalLayout_11.addWidget(self.lbInfoEstadoCivil)
        self.lbEstadoCivil = QtWidgets.QLabel(self.frEstadoCivil)
        self.lbEstadoCivil.setText("")
        self.lbEstadoCivil.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbEstadoCivil.setObjectName("lbEstadoCivil")
        self.horizontalLayout_11.addWidget(self.lbEstadoCivil)
        spacerItem2 = QtWidgets.QSpacerItem(370, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.gridLayout.addWidget(self.frEstadoCivil, 5, 1, 1, 1)
        self.frEmail = QtWidgets.QFrame(self.scaPessoais)
        self.frEmail.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frEmail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEmail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEmail.setObjectName("frEmail")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frEmail)
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_10.setSpacing(16)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbInfoEmail = QtWidgets.QLabel(self.frEmail)
        self.lbInfoEmail.setObjectName("lbInfoEmail")
        self.horizontalLayout_10.addWidget(self.lbInfoEmail)
        self.lbEmail = QtWidgets.QLabel(self.frEmail)
        self.lbEmail.setText("")
        self.lbEmail.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbEmail.setObjectName("lbEmail")
        self.horizontalLayout_10.addWidget(self.lbEmail)
        spacerItem3 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frEmail, 5, 0, 1, 1)
        self.frSobrenome = QtWidgets.QFrame(self.scaPessoais)
        self.frSobrenome.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frSobrenome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frSobrenome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSobrenome.setObjectName("frSobrenome")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frSobrenome)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbInfoSobrenome = QtWidgets.QLabel(self.frSobrenome)
        self.lbInfoSobrenome.setObjectName("lbInfoSobrenome")
        self.horizontalLayout_5.addWidget(self.lbInfoSobrenome)
        self.lbSobrenome = QtWidgets.QLabel(self.frSobrenome)
        self.lbSobrenome.setText("")
        self.lbSobrenome.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbSobrenome.setObjectName("lbSobrenome")
        self.horizontalLayout_5.addWidget(self.lbSobrenome)
        spacerItem4 = QtWidgets.QSpacerItem(376, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout.addWidget(self.frSobrenome, 0, 1, 1, 1)
        self.frSexo = QtWidgets.QFrame(self.scaPessoais)
        self.frSexo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frSexo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frSexo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSexo.setObjectName("frSexo")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frSexo)
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_13.setSpacing(16)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lbInfoSexo = QtWidgets.QLabel(self.frSexo)
        self.lbInfoSexo.setObjectName("lbInfoSexo")
        self.horizontalLayout_13.addWidget(self.lbInfoSexo)
        self.lbSexo = QtWidgets.QLabel(self.frSexo)
        self.lbSexo.setText("")
        self.lbSexo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbSexo.setObjectName("lbSexo")
        self.horizontalLayout_13.addWidget(self.lbSexo)
        spacerItem5 = QtWidgets.QSpacerItem(435, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.gridLayout.addWidget(self.frSexo, 1, 1, 1, 1)
        self.frIdade = QtWidgets.QFrame(self.scaPessoais)
        self.frIdade.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frIdade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frIdade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frIdade.setObjectName("frIdade")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frIdade)
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_8.setSpacing(16)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbInfoIdade = QtWidgets.QLabel(self.frIdade)
        self.lbInfoIdade.setObjectName("lbInfoIdade")
        self.horizontalLayout_8.addWidget(self.lbInfoIdade)
        self.lbIdade = QtWidgets.QLabel(self.frIdade)
        self.lbIdade.setText("")
        self.lbIdade.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbIdade.setObjectName("lbIdade")
        self.horizontalLayout_8.addWidget(self.lbIdade)
        spacerItem6 = QtWidgets.QSpacerItem(427, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.gridLayout.addWidget(self.frIdade, 4, 1, 1, 1)
        self.frDtNascimento = QtWidgets.QFrame(self.scaPessoais)
        self.frDtNascimento.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frDtNascimento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frDtNascimento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDtNascimento.setObjectName("frDtNascimento")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frDtNascimento)
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7.setSpacing(16)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbInfoDtNascimento = QtWidgets.QLabel(self.frDtNascimento)
        self.lbInfoDtNascimento.setObjectName("lbInfoDtNascimento")
        self.horizontalLayout_7.addWidget(self.lbInfoDtNascimento)
        self.lbDtNascimento = QtWidgets.QLabel(self.frDtNascimento)
        self.lbDtNascimento.setText("")
        self.lbDtNascimento.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbDtNascimento.setObjectName("lbDtNascimento")
        self.horizontalLayout_7.addWidget(self.lbDtNascimento)
        spacerItem7 = QtWidgets.QSpacerItem(302, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.gridLayout.addWidget(self.frDtNascimento, 4, 0, 1, 1)
        self.frCpf = QtWidgets.QFrame(self.scaPessoais)
        self.frCpf.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCpf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCpf.setObjectName("frCpf")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frCpf)
        self.horizontalLayout_31.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_31.setSpacing(16)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.lbInfoCpf = QtWidgets.QLabel(self.frCpf)
        self.lbInfoCpf.setObjectName("lbInfoCpf")
        self.horizontalLayout_31.addWidget(self.lbInfoCpf)
        self.lbCpf = QtWidgets.QLabel(self.frCpf)
        self.lbCpf.setText("")
        self.lbCpf.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbCpf.setObjectName("lbCpf")
        self.horizontalLayout_31.addWidget(self.lbCpf)
        spacerItem8 = QtWidgets.QSpacerItem(444, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem8)
        self.gridLayout.addWidget(self.frCpf, 3, 1, 1, 1)
        self.frNomeMae = QtWidgets.QFrame(self.scaPessoais)
        self.frNomeMae.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frNomeMae.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNomeMae.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNomeMae.setObjectName("frNomeMae")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frNomeMae)
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_9.setSpacing(16)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbInfoNomeMae = QtWidgets.QLabel(self.frNomeMae)
        self.lbInfoNomeMae.setObjectName("lbInfoNomeMae")
        self.horizontalLayout_9.addWidget(self.lbInfoNomeMae)
        self.lbNomeMae = QtWidgets.QLabel(self.frNomeMae)
        self.lbNomeMae.setText("")
        self.lbNomeMae.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbNomeMae.setObjectName("lbNomeMae")
        self.horizontalLayout_9.addWidget(self.lbNomeMae)
        spacerItem9 = QtWidgets.QSpacerItem(359, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.gridLayout.addWidget(self.frNomeMae, 1, 0, 1, 1)
        self.frEscolaridade = QtWidgets.QFrame(self.scaPessoais)
        self.frEscolaridade.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frEscolaridade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEscolaridade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEscolaridade.setObjectName("frEscolaridade")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frEscolaridade)
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_12.setSpacing(16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lbInfoEscolaridade = QtWidgets.QLabel(self.frEscolaridade)
        self.lbInfoEscolaridade.setObjectName("lbInfoEscolaridade")
        self.horizontalLayout_12.addWidget(self.lbInfoEscolaridade)
        self.lbEscolaridade = QtWidgets.QLabel(self.frEscolaridade)
        self.lbEscolaridade.setText("")
        self.lbEscolaridade.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbEscolaridade.setObjectName("lbEscolaridade")
        self.horizontalLayout_12.addWidget(self.lbEscolaridade)
        spacerItem10 = QtWidgets.QSpacerItem(280, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.gridLayout.addWidget(self.frEscolaridade, 6, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 7, 0, 1, 1)
        self.scrollArea.setWidget(self.scaPessoais)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.tabInfoCliente.addTab(self.tabInfoPessoais, "")
        self.tabInfoResidencial = QtWidgets.QWidget()
        self.tabInfoResidencial.setStyleSheet("/*---------------------------------------- Frames ----------------------------------------*/\n"
"#scaResidencial > QFrame {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: transparent transparent rgb(227, 227, 227) transparent;\n"
"}\n"
"\n"
"/*---------------------------------------- Labels ----------------------------------------*/\n"
"#lbCep, #lbNumero, #lbEndereco,\n"
"#lbCidade, #lbBairro, #lbEstado,\n"
"#lbComplemento {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#lbInfoCep, #lbInfoNumero, #lbInfoEndereco,\n"
"#lbInfoCidade, #lbInfoBairro, #lbInfoEstado,\n"
"#lbInfoComplemento {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    color: rgb(159, 159, 159);\n"
"}\n"
"")
        self.tabInfoResidencial.setObjectName("tabInfoResidencial")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tabInfoResidencial)
        self.horizontalLayout_14.setContentsMargins(0, 32, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame = QtWidgets.QFrame(self.tabInfoResidencial)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scaResidencial = QtWidgets.QWidget()
        self.scaResidencial.setGeometry(QtCore.QRect(0, 0, 1093, 437))
        self.scaResidencial.setObjectName("scaResidencial")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scaResidencial)
        self.gridLayout_2.setContentsMargins(16, 8, 16, 8)
        self.gridLayout_2.setHorizontalSpacing(24)
        self.gridLayout_2.setVerticalSpacing(8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frCidade = QtWidgets.QFrame(self.scaResidencial)
        self.frCidade.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frCidade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCidade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCidade.setObjectName("frCidade")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frCidade)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lbInfoCidade = QtWidgets.QLabel(self.frCidade)
        self.lbInfoCidade.setObjectName("lbInfoCidade")
        self.horizontalLayout_18.addWidget(self.lbInfoCidade)
        self.lbCidade = QtWidgets.QLabel(self.frCidade)
        self.lbCidade.setText("")
        self.lbCidade.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbCidade.setObjectName("lbCidade")
        self.horizontalLayout_18.addWidget(self.lbCidade)
        spacerItem12 = QtWidgets.QSpacerItem(420, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem12)
        self.gridLayout_2.addWidget(self.frCidade, 1, 1, 1, 1)
        self.frEndereco = QtWidgets.QFrame(self.scaResidencial)
        self.frEndereco.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frEndereco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEndereco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEndereco.setObjectName("frEndereco")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frEndereco)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lbInfoEndereco = QtWidgets.QLabel(self.frEndereco)
        self.lbInfoEndereco.setObjectName("lbInfoEndereco")
        self.horizontalLayout_17.addWidget(self.lbInfoEndereco)
        self.lbEndereco = QtWidgets.QLabel(self.frEndereco)
        self.lbEndereco.setText("")
        self.lbEndereco.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbEndereco.setObjectName("lbEndereco")
        self.horizontalLayout_17.addWidget(self.lbEndereco)
        spacerItem13 = QtWidgets.QSpacerItem(395, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem13)
        self.gridLayout_2.addWidget(self.frEndereco, 1, 0, 1, 1)
        self.frNumero = QtWidgets.QFrame(self.scaResidencial)
        self.frNumero.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frNumero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNumero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNumero.setObjectName("frNumero")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frNumero)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lbInfoNumero = QtWidgets.QLabel(self.frNumero)
        self.lbInfoNumero.setObjectName("lbInfoNumero")
        self.horizontalLayout_16.addWidget(self.lbInfoNumero)
        self.lbNumero = QtWidgets.QLabel(self.frNumero)
        self.lbNumero.setText("")
        self.lbNumero.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbNumero.setObjectName("lbNumero")
        self.horizontalLayout_16.addWidget(self.lbNumero)
        spacerItem14 = QtWidgets.QSpacerItem(411, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem14)
        self.gridLayout_2.addWidget(self.frNumero, 0, 1, 1, 1)
        self.frBairro = QtWidgets.QFrame(self.scaResidencial)
        self.frBairro.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frBairro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frBairro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBairro.setObjectName("frBairro")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frBairro)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lbInfoBairro = QtWidgets.QLabel(self.frBairro)
        self.lbInfoBairro.setObjectName("lbInfoBairro")
        self.horizontalLayout_19.addWidget(self.lbInfoBairro)
        self.lbBairro = QtWidgets.QLabel(self.frBairro)
        self.lbBairro.setText("")
        self.lbBairro.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbBairro.setObjectName("lbBairro")
        self.horizontalLayout_19.addWidget(self.lbBairro)
        spacerItem15 = QtWidgets.QSpacerItem(424, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem15)
        self.gridLayout_2.addWidget(self.frBairro, 2, 0, 1, 1)
        self.frEstado = QtWidgets.QFrame(self.scaResidencial)
        self.frEstado.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frEstado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEstado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEstado.setObjectName("frEstado")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frEstado)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lbInfoEstado = QtWidgets.QLabel(self.frEstado)
        self.lbInfoEstado.setObjectName("lbInfoEstado")
        self.horizontalLayout_20.addWidget(self.lbInfoEstado)
        self.lbEstado = QtWidgets.QLabel(self.frEstado)
        self.lbEstado.setText("")
        self.lbEstado.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbEstado.setObjectName("lbEstado")
        self.horizontalLayout_20.addWidget(self.lbEstado)
        spacerItem16 = QtWidgets.QSpacerItem(421, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem16)
        self.gridLayout_2.addWidget(self.frEstado, 2, 1, 1, 1)
        self.frCep = QtWidgets.QFrame(self.scaResidencial)
        self.frCep.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frCep.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCep.setObjectName("frCep")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frCep)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lbInfoCep = QtWidgets.QLabel(self.frCep)
        self.lbInfoCep.setObjectName("lbInfoCep")
        self.horizontalLayout_15.addWidget(self.lbInfoCep)
        self.lbCep = QtWidgets.QLabel(self.frCep)
        self.lbCep.setText("")
        self.lbCep.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbCep.setObjectName("lbCep")
        self.horizontalLayout_15.addWidget(self.lbCep)
        spacerItem17 = QtWidgets.QSpacerItem(449, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem17)
        self.gridLayout_2.addWidget(self.frCep, 0, 0, 1, 1)
        self.frComplemento = QtWidgets.QFrame(self.scaResidencial)
        self.frComplemento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frComplemento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frComplemento.setObjectName("frComplemento")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frComplemento)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbInfoComplemento = QtWidgets.QLabel(self.frComplemento)
        self.lbInfoComplemento.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lbInfoComplemento.setObjectName("lbInfoComplemento")
        self.verticalLayout_6.addWidget(self.lbInfoComplemento)
        self.lbComplemento = QtWidgets.QLabel(self.frComplemento)
        self.lbComplemento.setText("")
        self.lbComplemento.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbComplemento.setObjectName("lbComplemento")
        self.verticalLayout_6.addWidget(self.lbComplemento)
        self.gridLayout_2.addWidget(self.frComplemento, 3, 0, 1, 2)
        self.scrollArea_2.setWidget(self.scaResidencial)
        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.horizontalLayout_14.addWidget(self.frame)
        self.tabInfoCliente.addTab(self.tabInfoResidencial, "")
        self.tabProfissional = QtWidgets.QWidget()
        self.tabProfissional.setStyleSheet("/*---------------------------------------- Frames ----------------------------------------*/\n"
"#scaProfissional > QFrame {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: transparent transparent rgb(227, 227, 227) transparent;\n"
"}\n"
"\n"
"/*---------------------------------------- Labels ----------------------------------------*/\n"
"#lbNit, #lbCarteira, #lbProfissao {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#lbInfoNit, #lbInfoCarteira, #lbInfoProfissao, #lbProfessor {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    color: rgb(159, 159, 159);\n"
"}\n"
"")
        self.tabProfissional.setObjectName("tabProfissional")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.tabProfissional)
        self.horizontalLayout_21.setContentsMargins(0, 32, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_2 = QtWidgets.QFrame(self.tabProfissional)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scaProfissional = QtWidgets.QWidget()
        self.scaProfissional.setGeometry(QtCore.QRect(0, 0, 1093, 437))
        self.scaProfissional.setObjectName("scaProfissional")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scaProfissional)
        self.gridLayout_3.setContentsMargins(16, 8, 16, 8)
        self.gridLayout_3.setHorizontalSpacing(24)
        self.gridLayout_3.setVerticalSpacing(8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frNit = QtWidgets.QFrame(self.scaProfissional)
        self.frNit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frNit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNit.setObjectName("frNit")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frNit)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.lbInfoNit = QtWidgets.QLabel(self.frNit)
        self.lbInfoNit.setObjectName("lbInfoNit")
        self.horizontalLayout_23.addWidget(self.lbInfoNit)
        self.lbNit = QtWidgets.QLabel(self.frNit)
        self.lbNit.setText("")
        self.lbNit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbNit.setObjectName("lbNit")
        self.horizontalLayout_23.addWidget(self.lbNit)
        spacerItem18 = QtWidgets.QSpacerItem(405, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem18)
        self.gridLayout_3.addWidget(self.frNit, 0, 0, 1, 1)
        self.frProfissao = QtWidgets.QFrame(self.scaProfissional)
        self.frProfissao.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frProfissao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frProfissao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProfissao.setObjectName("frProfissao")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frProfissao)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.lbInfoProfissao = QtWidgets.QLabel(self.frProfissao)
        self.lbInfoProfissao.setObjectName("lbInfoProfissao")
        self.horizontalLayout_24.addWidget(self.lbInfoProfissao)
        self.lbProfissao = QtWidgets.QLabel(self.frProfissao)
        self.lbProfissao.setText("")
        self.lbProfissao.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbProfissao.setObjectName("lbProfissao")
        self.horizontalLayout_24.addWidget(self.lbProfissao)
        spacerItem19 = QtWidgets.QSpacerItem(342, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem19)
        self.gridLayout_3.addWidget(self.frProfissao, 1, 0, 1, 1)
        self.frCarteira = QtWidgets.QFrame(self.scaProfissional)
        self.frCarteira.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frCarteira.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCarteira.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCarteira.setObjectName("frCarteira")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frCarteira)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lbInfoCarteira = QtWidgets.QLabel(self.frCarteira)
        self.lbInfoCarteira.setObjectName("lbInfoCarteira")
        self.horizontalLayout_22.addWidget(self.lbInfoCarteira)
        self.lbCarteira = QtWidgets.QLabel(self.frCarteira)
        self.lbCarteira.setText("")
        self.lbCarteira.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbCarteira.setObjectName("lbCarteira")
        self.horizontalLayout_22.addWidget(self.lbCarteira)
        spacerItem20 = QtWidgets.QSpacerItem(345, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem20)
        self.gridLayout_3.addWidget(self.frCarteira, 0, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem21, 2, 0, 1, 1)
        self.frProfessor = QtWidgets.QFrame(self.scaProfissional)
        self.frProfessor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frProfessor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frProfessor.setObjectName("frProfessor")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frProfessor)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.lbProfessor = QtWidgets.QLabel(self.frProfessor)
        self.lbProfessor.setObjectName("lbProfessor")
        self.horizontalLayout_33.addWidget(self.lbProfessor)
        self.hlProfessor = QtWidgets.QHBoxLayout()
        self.hlProfessor.setObjectName("hlProfessor")
        self.horizontalLayout_33.addLayout(self.hlProfessor)
        spacerItem22 = QtWidgets.QSpacerItem(421, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem22)
        self.gridLayout_3.addWidget(self.frProfessor, 1, 1, 1, 1)
        self.scrollArea_3.setWidget(self.scaProfissional)
        self.verticalLayout_7.addWidget(self.scrollArea_3)
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.tabInfoCliente.addTab(self.tabProfissional, "")
        self.tabContatos = QtWidgets.QWidget()
        self.tabContatos.setObjectName("tabContatos")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.tabContatos)
        self.horizontalLayout_29.setContentsMargins(0, 32, 0, 0)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.frame_6 = QtWidgets.QFrame(self.tabContatos)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.frame_6)
        self.scrollArea_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scaInfoContatos = QtWidgets.QWidget()
        self.scaInfoContatos.setGeometry(QtCore.QRect(0, 0, 1075, 419))
        self.scaInfoContatos.setObjectName("scaInfoContatos")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scaInfoContatos)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.grdTelefones = QtWidgets.QGridLayout()
        self.grdTelefones.setObjectName("grdTelefones")
        self.verticalLayout_8.addLayout(self.grdTelefones)
        self.scrollArea_5.setWidget(self.scaInfoContatos)
        self.horizontalLayout_30.addWidget(self.scrollArea_5)
        self.horizontalLayout_29.addWidget(self.frame_6)
        self.tabInfoCliente.addTab(self.tabContatos, "")
        self.tabProcessos = QtWidgets.QWidget()
        self.tabProcessos.setObjectName("tabProcessos")
        self.tabInfoCliente.addTab(self.tabProcessos, "")
        self.tabInfoCadastrais = QtWidgets.QWidget()
        self.tabInfoCadastrais.setStyleSheet("/*---------------------------------------- Frames ----------------------------------------*/\n"
"#scaInfoCadastrais > QFrame {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: transparent transparent rgb(227, 227, 227) transparent;\n"
"}\n"
"\n"
"/*---------------------------------------- Labels ----------------------------------------*/\n"
"#lbDtCadastro, #lbUltAlt {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#lbInfoDtCadastro, #lbInfoUltAlt {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    color: rgb(159, 159, 159);\n"
"}\n"
"")
        self.tabInfoCadastrais.setObjectName("tabInfoCadastrais")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.tabInfoCadastrais)
        self.horizontalLayout_25.setContentsMargins(-1, 32, -1, -1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_5 = QtWidgets.QFrame(self.tabInfoCadastrais)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.frame_5)
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scaInfoCadastrais = QtWidgets.QWidget()
        self.scaInfoCadastrais.setGeometry(QtCore.QRect(0, 0, 1075, 428))
        self.scaInfoCadastrais.setObjectName("scaInfoCadastrais")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scaInfoCadastrais)
        self.gridLayout_4.setContentsMargins(16, 8, 16, 8)
        self.gridLayout_4.setHorizontalSpacing(24)
        self.gridLayout_4.setVerticalSpacing(8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frDtCadastro = QtWidgets.QFrame(self.scaInfoCadastrais)
        self.frDtCadastro.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frDtCadastro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frDtCadastro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDtCadastro.setObjectName("frDtCadastro")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frDtCadastro)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.lbInfoDtCadastro = QtWidgets.QLabel(self.frDtCadastro)
        self.lbInfoDtCadastro.setObjectName("lbInfoDtCadastro")
        self.horizontalLayout_27.addWidget(self.lbInfoDtCadastro)
        self.lbDtCadastro = QtWidgets.QLabel(self.frDtCadastro)
        self.lbDtCadastro.setText("")
        self.lbDtCadastro.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbDtCadastro.setObjectName("lbDtCadastro")
        self.horizontalLayout_27.addWidget(self.lbDtCadastro)
        spacerItem23 = QtWidgets.QSpacerItem(359, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem23)
        self.gridLayout_4.addWidget(self.frDtCadastro, 0, 0, 1, 1)
        self.frUltAlt = QtWidgets.QFrame(self.scaInfoCadastrais)
        self.frUltAlt.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frUltAlt.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frUltAlt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frUltAlt.setObjectName("frUltAlt")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frUltAlt)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.lbInfoUltAlt = QtWidgets.QLabel(self.frUltAlt)
        self.lbInfoUltAlt.setObjectName("lbInfoUltAlt")
        self.horizontalLayout_28.addWidget(self.lbInfoUltAlt)
        self.lbUltAlt = QtWidgets.QLabel(self.frUltAlt)
        self.lbUltAlt.setText("")
        self.lbUltAlt.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbUltAlt.setObjectName("lbUltAlt")
        self.horizontalLayout_28.addWidget(self.lbUltAlt)
        spacerItem24 = QtWidgets.QSpacerItem(320, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem24)
        self.gridLayout_4.addWidget(self.frUltAlt, 0, 1, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem25, 1, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scaInfoCadastrais)
        self.horizontalLayout_26.addWidget(self.scrollArea_4)
        self.horizontalLayout_25.addWidget(self.frame_5)
        self.tabInfoCliente.addTab(self.tabInfoCadastrais, "")
        self.horizontalLayout.addWidget(self.tabInfoCliente)
        self.verticalLayout_2.addWidget(self.frTabInfo)
        self.verticalLayout.addWidget(self.frMain)

        self.retranslateUi(wdgInfoGeralCliente)
        self.tabInfoCliente.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgInfoGeralCliente)

    def retranslateUi(self, wdgInfoGeralCliente):
        _translate = QtCore.QCoreApplication.translate
        wdgInfoGeralCliente.setWindowTitle(_translate("wdgInfoGeralCliente", "Form"))
        self.lbNomeCliente.setText(_translate("wdgInfoGeralCliente", "Nome cliente"))
        self.lbInfoCdCliente.setText(_translate("wdgInfoGeralCliente", "Código do cliente: "))
        self.lbInfoNotaCliente.setText(_translate("wdgInfoGeralCliente", "Nota do cliente"))
        self.lbNotaCliente.setText(_translate("wdgInfoGeralCliente", "nota"))
        self.lbInfoNome.setText(_translate("wdgInfoGeralCliente", "NOME"))
        self.lbInfoRg.setText(_translate("wdgInfoGeralCliente", "RG"))
        self.lbInfoEstadoCivil.setText(_translate("wdgInfoGeralCliente", "ESTADO CIVIL"))
        self.lbInfoEmail.setText(_translate("wdgInfoGeralCliente", "EMAIL"))
        self.lbInfoSobrenome.setText(_translate("wdgInfoGeralCliente", "SOBRENOME"))
        self.lbInfoSexo.setText(_translate("wdgInfoGeralCliente", "SEXO"))
        self.lbInfoIdade.setText(_translate("wdgInfoGeralCliente", "IDADE"))
        self.lbInfoDtNascimento.setText(_translate("wdgInfoGeralCliente", "DATA DE NASCIMENTO"))
        self.lbInfoCpf.setText(_translate("wdgInfoGeralCliente", "CPF"))
        self.lbInfoNomeMae.setText(_translate("wdgInfoGeralCliente", "NOME DA MÃE"))
        self.lbInfoEscolaridade.setText(_translate("wdgInfoGeralCliente", "GRAU DE ESCOLARIDADE"))
        self.tabInfoCliente.setTabText(self.tabInfoCliente.indexOf(self.tabInfoPessoais), _translate("wdgInfoGeralCliente", "Pessoal"))
        self.lbInfoCidade.setText(_translate("wdgInfoGeralCliente", "CIDADE"))
        self.lbInfoEndereco.setText(_translate("wdgInfoGeralCliente", "ENDEREÇO"))
        self.lbInfoNumero.setText(_translate("wdgInfoGeralCliente", "NÚMERO"))
        self.lbInfoBairro.setText(_translate("wdgInfoGeralCliente", "BAIRRO"))
        self.lbInfoEstado.setText(_translate("wdgInfoGeralCliente", "ESTADO"))
        self.lbInfoCep.setText(_translate("wdgInfoGeralCliente", "CEP"))
        self.lbInfoComplemento.setText(_translate("wdgInfoGeralCliente", "COMPLEMENTO"))
        self.tabInfoCliente.setTabText(self.tabInfoCliente.indexOf(self.tabInfoResidencial), _translate("wdgInfoGeralCliente", "Residencial"))
        self.lbInfoNit.setText(_translate("wdgInfoGeralCliente", "NIT"))
        self.lbInfoProfissao.setText(_translate("wdgInfoGeralCliente", "PROFISSÃO"))
        self.lbInfoCarteira.setText(_translate("wdgInfoGeralCliente", "CARTEIRA PROFISSIONAL"))
        self.lbProfessor.setText(_translate("wdgInfoGeralCliente", "PROFESSOR(A)"))
        self.tabInfoCliente.setTabText(self.tabInfoCliente.indexOf(self.tabProfissional), _translate("wdgInfoGeralCliente", "Profissional"))
        self.tabInfoCliente.setTabText(self.tabInfoCliente.indexOf(self.tabContatos), _translate("wdgInfoGeralCliente", "Contatos"))
        self.tabInfoCliente.setTabText(self.tabInfoCliente.indexOf(self.tabProcessos), _translate("wdgInfoGeralCliente", "Processos"))
        self.lbInfoDtCadastro.setText(_translate("wdgInfoGeralCliente", "CLIENTE DESDE"))
        self.lbInfoUltAlt.setText(_translate("wdgInfoGeralCliente", "ÚLTIMA ALTERAÇÃO"))
        self.tabInfoCliente.setTabText(self.tabInfoCliente.indexOf(self.tabInfoCadastrais), _translate("wdgInfoGeralCliente", "              Informações cadastrais              "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgInfoGeralCliente = QtWidgets.QWidget()
    ui = Ui_wdgInfoGeralCliente()
    ui.setupUi(wdgInfoGeralCliente)
    wdgInfoGeralCliente.show()
    sys.exit(app.exec_())