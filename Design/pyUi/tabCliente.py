# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabCliente.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgTabCliente(object):
    def setupUi(self, wdgTabCliente):
        wdgTabCliente.setObjectName("wdgTabCliente")
        wdgTabCliente.resize(901, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdgTabCliente.sizePolicy().hasHeightForWidth())
        wdgTabCliente.setSizePolicy(sizePolicy)
        wdgTabCliente.setMinimumSize(QtCore.QSize(760, 560))
        wdgTabCliente.setMaximumSize(QtCore.QSize(4514434, 16777215))
        wdgTabCliente.setStyleSheet("#wdgTabCliCadastro, \n"
"#tabClientes,\n"
"#tabMain, \n"
"#tabCadastro, \n"
"#tabCalculos {\n"
"    border-radius: 8px;\n"
"    background-color: transparent;\n"
"    padding: 4px;\n"
"    \n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#tabMain::pane {\n"
"    border-top: 2px solid lightgrey;\n"
"    margin-top: -5px;\n"
"}\n"
"\n"
"#tabMain::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"#tabMain > QTabBar::tab {\n"
"    background-color: transparent    ;\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    padding: 8px;\n"
"    min-width: 100px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"#tabMain > QTabBar::tab:selected {\n"
"    background-color: transparent    ;\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 20px;\n"
"    padding: 8px;\n"
"    margin: 2px;\n"
"    color:    rgb(82, 111, 139);\n"
"\n"
"    border-style: solid;\n"
"    border-width: 3px;\n"
"    border-color: transparent transparent rgb(82, 111, 139) transparent;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgTabCliente)
        self.horizontalLayout.setContentsMargins(8, 4, 8, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabMain = QtWidgets.QTabWidget(wdgTabCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabMain.sizePolicy().hasHeightForWidth())
        self.tabMain.setSizePolicy(sizePolicy)
        self.tabMain.setMinimumSize(QtCore.QSize(0, 560))
        self.tabMain.setStyleSheet("")
        self.tabMain.setIconSize(QtCore.QSize(36, 16))
        self.tabMain.setObjectName("tabMain")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setMinimumSize(QtCore.QSize(0, 560))
        self.tabClientes.setStyleSheet("/*-------------------------------- Labels -----------------------------------------*/\n"
"#lbTituloClientes {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"#lbInfoClientes {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;    \n"
"}\n"
"\n"
"#lbTituloFiltro {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 20px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"#lbBuscaNome, \n"
"#lbBuscaEmail, \n"
"#lbBuscaTelefone,\n"
"#lbBuscaTpBeneficio,\n"
"#lbBuscaRgcpf {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"/*-------------------------------- Frames -----------------------------------------*/\n"
"#frFiltrosBusca {\n"
"    background-color: rgb(82, 111, 139);\n"
"    border: 0px solid;\n"
"\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#frUnderlineNome {\n"
"    border-bottom: 1px solid rgb(136, 138, 133);\n"
"}\n"
"\n"
"/*-------------------------------- Tables -----------------------------------------*/\n"
"#tblClientes{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(52, 73, 94);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    min-height: 45px;\n"
"}\n"
"\n"
"/*-------------------------------- Push Buttons --------------------------------*/\n"
"#pbArrowNome, \n"
"#pbArrowEmail, \n"
"#pbArrowTelefone,\n"
"#pbArrowTpProcesso,\n"
"#pbArrowRgcpf {\n"
"    background-image: url(:/arrowDown/arrowDown.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#pbResetar, #pbFiltrar {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"#pbResetar:hover, #pbFiltrar:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid;\n"
"    background-color: rgb(72, 93, 114);\n"
"}\n"
"\n"
"#pbFiltrar {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: rgb(52, 73, 94);\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"#pbFiltrar:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: rgb(52, 73, 94);\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid;\n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"#pbLimparFiltro {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: rgb(52, 73, 94);\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(233, 185, 110);\n"
"}\n"
"\n"
"#pbLimparFiltro:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: rgb(52, 73, 94);\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid;\n"
"    background-color: rgb(238, 238, 236);\n"
"}")
        self.tabClientes.setObjectName("tabClientes")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabClientes)
        self.horizontalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frFiltrosBusca = QtWidgets.QFrame(self.tabClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frFiltrosBusca.sizePolicy().hasHeightForWidth())
        self.frFiltrosBusca.setSizePolicy(sizePolicy)
        self.frFiltrosBusca.setMinimumSize(QtCore.QSize(215, 500))
        self.frFiltrosBusca.setMaximumSize(QtCore.QSize(215, 510))
        self.frFiltrosBusca.setStyleSheet("")
        self.frFiltrosBusca.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frFiltrosBusca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFiltrosBusca.setObjectName("frFiltrosBusca")
        self.lbTituloFiltro = QtWidgets.QLabel(self.frFiltrosBusca)
        self.lbTituloFiltro.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.lbTituloFiltro.setObjectName("lbTituloFiltro")
        self.frUnderlineNome = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frUnderlineNome.setGeometry(QtCore.QRect(0, 60, 211, 21))
        self.frUnderlineNome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frUnderlineNome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frUnderlineNome.setObjectName("frUnderlineNome")
        self.lbBuscaNome = QtWidgets.QLabel(self.frUnderlineNome)
        self.lbBuscaNome.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.lbBuscaNome.setObjectName("lbBuscaNome")
        self.pbArrowNome = QtWidgets.QPushButton(self.frUnderlineNome)
        self.pbArrowNome.setGeometry(QtCore.QRect(180, 0, 31, 21))
        self.pbArrowNome.setText("")
        self.pbArrowNome.setObjectName("pbArrowNome")
        self.frBuscaNome = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frBuscaNome.setGeometry(QtCore.QRect(0, 80, 211, 40))
        self.frBuscaNome.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frBuscaNome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBuscaNome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBuscaNome.setObjectName("frBuscaNome")
        self.leBuscaNome = QtWidgets.QLineEdit(self.frBuscaNome)
        self.leBuscaNome.setGeometry(QtCore.QRect(10, 10, 191, 25))
        self.leBuscaNome.setObjectName("leBuscaNome")
        self.frBuscaEmail = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frBuscaEmail.setGeometry(QtCore.QRect(0, 150, 211, 40))
        self.frBuscaEmail.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frBuscaEmail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBuscaEmail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBuscaEmail.setObjectName("frBuscaEmail")
        self.leBuscaEmail = QtWidgets.QLineEdit(self.frBuscaEmail)
        self.leBuscaEmail.setGeometry(QtCore.QRect(10, 10, 191, 25))
        self.leBuscaEmail.setObjectName("leBuscaEmail")
        self.frUnderlineEmail = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frUnderlineEmail.setGeometry(QtCore.QRect(0, 130, 211, 21))
        self.frUnderlineEmail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frUnderlineEmail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frUnderlineEmail.setObjectName("frUnderlineEmail")
        self.lbBuscaEmail = QtWidgets.QLabel(self.frUnderlineEmail)
        self.lbBuscaEmail.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.lbBuscaEmail.setObjectName("lbBuscaEmail")
        self.pbArrowEmail = QtWidgets.QPushButton(self.frUnderlineEmail)
        self.pbArrowEmail.setGeometry(QtCore.QRect(180, 0, 31, 21))
        self.pbArrowEmail.setText("")
        self.pbArrowEmail.setObjectName("pbArrowEmail")
        self.frBuscaTelefone = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frBuscaTelefone.setGeometry(QtCore.QRect(0, 230, 211, 40))
        self.frBuscaTelefone.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frBuscaTelefone.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBuscaTelefone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBuscaTelefone.setObjectName("frBuscaTelefone")
        self.leBuscaTelefone = QtWidgets.QLineEdit(self.frBuscaTelefone)
        self.leBuscaTelefone.setGeometry(QtCore.QRect(10, 10, 191, 25))
        self.leBuscaTelefone.setObjectName("leBuscaTelefone")
        self.frUnderlineTelefone = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frUnderlineTelefone.setGeometry(QtCore.QRect(0, 210, 211, 21))
        self.frUnderlineTelefone.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frUnderlineTelefone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frUnderlineTelefone.setObjectName("frUnderlineTelefone")
        self.lbBuscaTelefone = QtWidgets.QLabel(self.frUnderlineTelefone)
        self.lbBuscaTelefone.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.lbBuscaTelefone.setObjectName("lbBuscaTelefone")
        self.pbArrowTelefone = QtWidgets.QPushButton(self.frUnderlineTelefone)
        self.pbArrowTelefone.setGeometry(QtCore.QRect(180, 0, 31, 21))
        self.pbArrowTelefone.setText("")
        self.pbArrowTelefone.setObjectName("pbArrowTelefone")
        self.frBuscaRgcpf = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frBuscaRgcpf.setGeometry(QtCore.QRect(0, 310, 211, 40))
        self.frBuscaRgcpf.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frBuscaRgcpf.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBuscaRgcpf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBuscaRgcpf.setObjectName("frBuscaRgcpf")
        self.leBuscaRgcpf = QtWidgets.QLineEdit(self.frBuscaRgcpf)
        self.leBuscaRgcpf.setGeometry(QtCore.QRect(10, 10, 191, 25))
        self.leBuscaRgcpf.setObjectName("leBuscaRgcpf")
        self.frUnderlineRgcpf = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frUnderlineRgcpf.setGeometry(QtCore.QRect(0, 290, 211, 21))
        self.frUnderlineRgcpf.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frUnderlineRgcpf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frUnderlineRgcpf.setObjectName("frUnderlineRgcpf")
        self.lbBuscaRgcpf = QtWidgets.QLabel(self.frUnderlineRgcpf)
        self.lbBuscaRgcpf.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.lbBuscaRgcpf.setObjectName("lbBuscaRgcpf")
        self.pbArrowRgcpf = QtWidgets.QPushButton(self.frUnderlineRgcpf)
        self.pbArrowRgcpf.setGeometry(QtCore.QRect(180, 0, 31, 21))
        self.pbArrowRgcpf.setText("")
        self.pbArrowRgcpf.setObjectName("pbArrowRgcpf")
        self.frUnderlineTpProcesso = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frUnderlineTpProcesso.setGeometry(QtCore.QRect(0, 360, 211, 21))
        self.frUnderlineTpProcesso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frUnderlineTpProcesso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frUnderlineTpProcesso.setObjectName("frUnderlineTpProcesso")
        self.lbBuscaTpBeneficio = QtWidgets.QLabel(self.frUnderlineTpProcesso)
        self.lbBuscaTpBeneficio.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.lbBuscaTpBeneficio.setObjectName("lbBuscaTpBeneficio")
        self.frBuscaTpBeneficio = QtWidgets.QFrame(self.frFiltrosBusca)
        self.frBuscaTpBeneficio.setGeometry(QtCore.QRect(0, 380, 211, 40))
        self.frBuscaTpBeneficio.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frBuscaTpBeneficio.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBuscaTpBeneficio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBuscaTpBeneficio.setObjectName("frBuscaTpBeneficio")
        self.cbxTpBeneficio = QtWidgets.QComboBox(self.frBuscaTpBeneficio)
        self.cbxTpBeneficio.setGeometry(QtCore.QRect(10, 10, 191, 25))
        self.cbxTpBeneficio.setObjectName("cbxTpBeneficio")
        self.pbFiltrar = QtWidgets.QPushButton(self.frFiltrosBusca)
        self.pbFiltrar.setGeometry(QtCore.QRect(120, 440, 83, 25))
        self.pbFiltrar.setObjectName("pbFiltrar")
        self.pbLimparFiltro = QtWidgets.QPushButton(self.frFiltrosBusca)
        self.pbLimparFiltro.setGeometry(QtCore.QRect(120, 470, 83, 25))
        self.pbLimparFiltro.setObjectName("pbLimparFiltro")
        self.lbTituloFiltro.raise_()
        self.frBuscaNome.raise_()
        self.frUnderlineNome.raise_()
        self.frBuscaEmail.raise_()
        self.frUnderlineEmail.raise_()
        self.frBuscaTelefone.raise_()
        self.frUnderlineTelefone.raise_()
        self.frBuscaRgcpf.raise_()
        self.frUnderlineRgcpf.raise_()
        self.frUnderlineTpProcesso.raise_()
        self.frBuscaTpBeneficio.raise_()
        self.pbFiltrar.raise_()
        self.pbLimparFiltro.raise_()
        self.horizontalLayout_2.addWidget(self.frFiltrosBusca, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.tabClientes)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbTituloClientes = QtWidgets.QLabel(self.frame_3)
        self.lbTituloClientes.setObjectName("lbTituloClientes")
        self.verticalLayout_2.addWidget(self.lbTituloClientes)
        self.lbInfoClientes = QtWidgets.QLabel(self.frame_3)
        self.lbInfoClientes.setObjectName("lbInfoClientes")
        self.verticalLayout_2.addWidget(self.lbInfoClientes)
        self.hlFlitroAlfabetico = QtWidgets.QHBoxLayout()
        self.hlFlitroAlfabetico.setObjectName("hlFlitroAlfabetico")
        self.verticalLayout_2.addLayout(self.hlFlitroAlfabetico)
        self.tblClientes = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblClientes.sizePolicy().hasHeightForWidth())
        self.tblClientes.setSizePolicy(sizePolicy)
        self.tblClientes.setMinimumSize(QtCore.QSize(0, 360))
        self.tblClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblClientes.setObjectName("tblClientes")
        self.tblClientes.setColumnCount(6)
        self.tblClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(12)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(12)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(12)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(12)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(12)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(5, item)
        self.tblClientes.horizontalHeader().setCascadingSectionResizes(True)
        self.tblClientes.horizontalHeader().setStretchLastSection(True)
        self.tblClientes.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tblClientes)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.tabMain.addTab(self.tabClientes, "")
        self.tabInformacoes = QtWidgets.QWidget()
        self.tabInformacoes.setObjectName("tabInformacoes")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabInformacoes)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tabInformacoes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tabMain.addTab(self.tabInformacoes, "")
        self.tabCadastro = QtWidgets.QWidget()
        self.tabCadastro.setMaximumSize(QtCore.QSize(1111, 16777215))
        self.tabCadastro.setStyleSheet("/*-------------------------------- Group Box -----------------------------------------*/\n"
"QGroupBox {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    border: 1px solid transparent;\n"
"\n"
"    background-color: white;\n"
"}\n"
"\n"
"QGroupBox QGroupBox {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"\n"
"    background-color: white;\n"
"}\n"
"\n"
"#gbInfoPessoais::title, #gbInfoBancarias::title,\n"
"#gbInfoProfissionais::title, #gbInfoResidenciais::title {\n"
"    subcontrol-position: top left;\n"
"    background-color: #3A405A;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    color: white;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"#gbInfoPessoais, #gbInfoBancarias,\n"
"#gbInfoProfissionais, #gbInfoResidenciais{\n"
"    border: 1px dashed grey;\n"
"}\n"
"\n"
"/*-------------------------------- ScrollArea -----------------------------------------*/\n"
"#scaCadastro, #scrollArea {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*-------------------------------- Labels -----------------------------------------*/\n"
"#lbTitulo{\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"#lbDescricaoTela, \n"
"#lbFrTituloInfoPessoal,\n"
"#lbFrTituloInfoProfissional,\n"
"#lbFrTituloInfoResidencial,\n"
"#lbFrTituloInfoBancarias {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"\n"
"    background-color: white;\n"
"}\n"
"\n"
"#lbInfoCnis {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;    \n"
"}\n"
"\n"
"QFrame > QLabel {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;    \n"
"}\n"
"\n"
"\n"
"\n"
"/*---------------------------------- Frames -----------------------------------*/\n"
"#frInfoPessoais, #frInfoProfissional, \n"
"#frInfoResidencial, #frInfoBancarias {\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(85, 87, 83);\n"
"}\n"
"\n"
"/*---------------------------------- CheckBox -----------------------------------*/\n"
"#cbClienteAntigo {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/*------------------------------- Push Buttons ------------------------------*/\n"
"\n"
"#pbCarregaCnis {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"/*    background-color: rgb(52, 73, 94);*/\n"
"/*    background-color: rgb(92, 53, 102);*/\n"
"    background-color: #048BA8;\n"
"}\n"
"\n"
"#pbCarregaCnis:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(72, 93, 114);\n"
"}\n"
"\n"
"#pbAtualizar {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"#pbAtualizar:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(51, 126, 251);\n"
"    background-color: rgb(52, 93, 114);\n"
"}\n"
"\n"
"#pbLimpar, #pbMaisTelefones {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"#pbLimpar:hover, #pbMaisTelefones:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(51, 126, 251);\n"
"    background-color: rgb(52, 93, 114);\n"
"}\n"
"\n"
"#pbBuscarCliente {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"#pbBuscarCliente:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 1px solid rgb(51, 126, 251);\n"
"    background-color: rgb(52, 93, 114);\n"
"}\n"
"\n"
"#pbBuscaCep{\n"
"    border-radius: 4px;\n"
"    background-image: url(:/buscaCep/search.png);\n"
"    background-color: rgb(52, 73, 94);\n"
"\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#pbBuscaCep:hover {\n"
"    border-radius: 4px;\n"
"    background-image: url(:/buscaCep/search.png);\n"
"    background-color: rgb(52, 93, 114);\n"
"\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"/*------------------------------- Radio Buttons ------------------------------*/\n"
"\n"
"#rbMasculino, #rbFeminino {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;    \n"
"}")
        self.tabCadastro.setObjectName("tabCadastro")
        self.gridLayout = QtWidgets.QGridLayout(self.tabCadastro)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.tabCadastro)
        self.frame.setMinimumSize(QtCore.QSize(740, 0))
        self.frame.setMaximumSize(QtCore.QSize(1085, 540))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbTitulo = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(-1)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setObjectName("lbTitulo")
        self.verticalLayout_6.addWidget(self.lbTitulo)
        self.lbDescricaoTela = QtWidgets.QLabel(self.frame_6)
        self.lbDescricaoTela.setObjectName("lbDescricaoTela")
        self.verticalLayout_6.addWidget(self.lbDescricaoTela)
        self.gridLayout_6.addWidget(self.frame_6, 0, 0, 1, 3)
        self.gbInfoPessoais = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbInfoPessoais.sizePolicy().hasHeightForWidth())
        self.gbInfoPessoais.setSizePolicy(sizePolicy)
        self.gbInfoPessoais.setMinimumSize(QtCore.QSize(320, 350))
        self.gbInfoPessoais.setMaximumSize(QtCore.QSize(16777215, 500))
        self.gbInfoPessoais.setCheckable(False)
        self.gbInfoPessoais.setObjectName("gbInfoPessoais")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gbInfoPessoais)
        self.gridLayout_2.setContentsMargins(16, 26, 4, 4)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setContentsMargins(0, 16, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lePrimeiroNome = QtWidgets.QLineEdit(self.groupBox_6)
        self.lePrimeiroNome.setMaxLength(20)
        self.lePrimeiroNome.setObjectName("lePrimeiroNome")
        self.horizontalLayout_5.addWidget(self.lePrimeiroNome, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_6, 1, 0, 1, 2)
        self.groupBox_12 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_12.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_12.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cbxEstCivil = QtWidgets.QComboBox(self.groupBox_12)
        self.cbxEstCivil.setObjectName("cbxEstCivil")
        self.horizontalLayout_12.addWidget(self.cbxEstCivil, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_12, 6, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_11.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_11.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_11.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.leNomeMae = QtWidgets.QLineEdit(self.groupBox_11)
        self.leNomeMae.setMaxLength(40)
        self.leNomeMae.setObjectName("leNomeMae")
        self.horizontalLayout_11.addWidget(self.leNomeMae, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_11, 5, 3, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sbCdCliente = QtWidgets.QSpinBox(self.groupBox_5)
        self.sbCdCliente.setMaximum(1000)
        self.sbCdCliente.setObjectName("sbCdCliente")
        self.horizontalLayout_4.addWidget(self.sbCdCliente, 0, QtCore.Qt.AlignTop)
        self.hlCheckBox = QtWidgets.QHBoxLayout()
        self.hlCheckBox.setObjectName("hlCheckBox")
        self.horizontalLayout_4.addLayout(self.hlCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame_8 = QtWidgets.QFrame(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rbMasculino = QtWidgets.QRadioButton(self.frame_8)
        self.rbMasculino.setObjectName("rbMasculino")
        self.verticalLayout_4.addWidget(self.rbMasculino, 0, QtCore.Qt.AlignTop)
        self.rbFeminino = QtWidgets.QRadioButton(self.frame_8)
        self.rbFeminino.setObjectName("rbFeminino")
        self.verticalLayout_4.addWidget(self.rbFeminino, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_4.addWidget(self.frame_8, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_5, 0, 0, 1, 5)
        self.groupBox_7 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_6.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leSobrenome = QtWidgets.QLineEdit(self.groupBox_7)
        self.leSobrenome.setMaxLength(30)
        self.leSobrenome.setObjectName("leSobrenome")
        self.horizontalLayout_6.addWidget(self.leSobrenome, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_7, 1, 2, 1, 3)
        self.groupBox_16 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_16.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_16.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_16.setObjectName("groupBox_16")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_15.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.cbxEscolaridade = QtWidgets.QComboBox(self.groupBox_16)
        self.cbxEscolaridade.setObjectName("cbxEscolaridade")
        self.horizontalLayout_15.addWidget(self.cbxEscolaridade, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_16, 7, 3, 1, 2)
        self.pbMaisTelefones = QtWidgets.QPushButton(self.gbInfoPessoais)
        self.pbMaisTelefones.setMinimumSize(QtCore.QSize(0, 24))
        self.pbMaisTelefones.setObjectName("pbMaisTelefones")
        self.gridLayout_2.addWidget(self.pbMaisTelefones, 8, 0, 1, 2, QtCore.Qt.AlignTop)
        self.groupBox_10 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_10.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_10.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.leCpf = QtWidgets.QLineEdit(self.groupBox_10)
        self.leCpf.setMaxLength(14)
        self.leCpf.setFrame(True)
        self.leCpf.setObjectName("leCpf")
        self.horizontalLayout_10.addWidget(self.leCpf, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_10, 5, 0, 1, 3)
        self.frame_10 = QtWidgets.QFrame(self.gbInfoPessoais)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(8)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame_10)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_9.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.leIdade = QtWidgets.QLineEdit(self.groupBox_9)
        self.leIdade.setMaxLength(2)
        self.leIdade.setObjectName("leIdade")
        self.horizontalLayout_9.addWidget(self.leIdade, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_32.addWidget(self.groupBox_9)
        self.groupBox_14 = QtWidgets.QGroupBox(self.frame_10)
        self.groupBox_14.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_8.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.dtNascimento = QtWidgets.QDateEdit(self.groupBox_14)
        self.dtNascimento.setCalendarPopup(True)
        self.dtNascimento.setObjectName("dtNascimento")
        self.horizontalLayout_8.addWidget(self.dtNascimento, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_32.addWidget(self.groupBox_14)
        self.gridLayout_2.addWidget(self.frame_10, 3, 4, 1, 1, QtCore.Qt.AlignTop)
        self.groupBox_13 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_13.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_13.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_13.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.leEmail = QtWidgets.QLineEdit(self.groupBox_13)
        self.leEmail.setMaxLength(40)
        self.leEmail.setObjectName("leEmail")
        self.horizontalLayout_13.addWidget(self.leEmail, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_13, 6, 1, 1, 4)
        self.groupBox_8 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_7.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.leRg = QtWidgets.QLineEdit(self.groupBox_8)
        self.leRg.setMaxLength(12)
        self.leRg.setObjectName("leRg")
        self.horizontalLayout_7.addWidget(self.leRg, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_8, 3, 0, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.gbInfoPessoais)
        self.groupBox_15.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_15.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_15.setObjectName("groupBox_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_14.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.leTelefone = QtWidgets.QLineEdit(self.groupBox_15)
        self.leTelefone.setMaxLength(16)
        self.leTelefone.setObjectName("leTelefone")
        self.horizontalLayout_14.addWidget(self.leTelefone, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_15, 7, 0, 1, 2)
        self.gridLayout_6.addWidget(self.gbInfoPessoais, 1, 0, 2, 1)
        self.gbInfoResidenciais = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbInfoResidenciais.sizePolicy().hasHeightForWidth())
        self.gbInfoResidenciais.setSizePolicy(sizePolicy)
        self.gbInfoResidenciais.setMaximumSize(QtCore.QSize(16777215, 320))
        self.gbInfoResidenciais.setFlat(True)
        self.gbInfoResidenciais.setCheckable(False)
        self.gbInfoResidenciais.setObjectName("gbInfoResidenciais")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbInfoResidenciais)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(16, 26, 4, 4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 1, 1, 1)
        self.groupBox_23 = QtWidgets.QGroupBox(self.gbInfoResidenciais)
        self.groupBox_23.setObjectName("groupBox_23")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.groupBox_23)
        self.horizontalLayout_23.setContentsMargins(0, 12, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.leComplemento = QtWidgets.QLineEdit(self.groupBox_23)
        self.leComplemento.setObjectName("leComplemento")
        self.horizontalLayout_23.addWidget(self.leComplemento)
        self.gridLayout_3.addWidget(self.groupBox_23, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        self.groupBox_19 = QtWidgets.QGroupBox(self.gbInfoResidenciais)
        self.groupBox_19.setObjectName("groupBox_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.groupBox_19)
        self.horizontalLayout_17.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.leEndereco = QtWidgets.QLineEdit(self.groupBox_19)
        self.leEndereco.setObjectName("leEndereco")
        self.horizontalLayout_17.addWidget(self.leEndereco, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.groupBox_19, 2, 0, 1, 1)
        self.groupBox_20 = QtWidgets.QGroupBox(self.gbInfoResidenciais)
        self.groupBox_20.setObjectName("groupBox_20")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_20.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.leCidade = QtWidgets.QLineEdit(self.groupBox_20)
        self.leCidade.setObjectName("leCidade")
        self.horizontalLayout_20.addWidget(self.leCidade, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.groupBox_20, 2, 2, 1, 1)
        self.groupBox_18 = QtWidgets.QGroupBox(self.gbInfoResidenciais)
        self.groupBox_18.setObjectName("groupBox_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_19.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.leNumero = QtWidgets.QLineEdit(self.groupBox_18)
        self.leNumero.setMaxLength(5)
        self.leNumero.setObjectName("leNumero")
        self.horizontalLayout_19.addWidget(self.leNumero, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.groupBox_18, 0, 2, 1, 1)
        self.groupBox_22 = QtWidgets.QGroupBox(self.gbInfoResidenciais)
        self.groupBox_22.setObjectName("groupBox_22")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.groupBox_22)
        self.horizontalLayout_22.setContentsMargins(0, 12, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.cbxEstado = QtWidgets.QComboBox(self.groupBox_22)
        self.cbxEstado.setObjectName("cbxEstado")
        self.horizontalLayout_22.addWidget(self.cbxEstado)
        self.gridLayout_3.addWidget(self.groupBox_22, 3, 2, 1, 1)
        self.groupBox_21 = QtWidgets.QGroupBox(self.gbInfoResidenciais)
        self.groupBox_21.setObjectName("groupBox_21")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_21.setContentsMargins(0, 12, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.leBairro = QtWidgets.QLineEdit(self.groupBox_21)
        self.leBairro.setObjectName("leBairro")
        self.horizontalLayout_21.addWidget(self.leBairro)
        self.gridLayout_3.addWidget(self.groupBox_21, 3, 0, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.gbInfoResidenciais)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setSpacing(8)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.groupBox_17 = QtWidgets.QGroupBox(self.frame_11)
        self.groupBox_17.setObjectName("groupBox_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_18.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_18.setSpacing(8)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.leCep = QtWidgets.QLineEdit(self.groupBox_17)
        self.leCep.setMaxLength(9)
        self.leCep.setObjectName("leCep")
        self.horizontalLayout_18.addWidget(self.leCep, 0, QtCore.Qt.AlignTop)
        self.pbBuscaCep = QtWidgets.QPushButton(self.groupBox_17)
        self.pbBuscaCep.setMinimumSize(QtCore.QSize(0, 24))
        self.pbBuscaCep.setText("")
        self.pbBuscaCep.setObjectName("pbBuscaCep")
        self.horizontalLayout_18.addWidget(self.pbBuscaCep, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_33.addWidget(self.groupBox_17)
        self.gridLayout_3.addWidget(self.frame_11, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.gbInfoResidenciais, 1, 1, 1, 1)
        self.gbInfoBancarias = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbInfoBancarias.sizePolicy().hasHeightForWidth())
        self.gbInfoBancarias.setSizePolicy(sizePolicy)
        self.gbInfoBancarias.setMinimumSize(QtCore.QSize(195, 0))
        self.gbInfoBancarias.setMaximumSize(QtCore.QSize(300, 16777215))
        self.gbInfoBancarias.setObjectName("gbInfoBancarias")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gbInfoBancarias)
        self.gridLayout_5.setContentsMargins(16, 26, 4, 4)
        self.gridLayout_5.setSpacing(4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_24 = QtWidgets.QGroupBox(self.gbInfoBancarias)
        self.groupBox_24.setObjectName("groupBox_24")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_24.setContentsMargins(0, 12, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.leNomeBanco = QtWidgets.QLineEdit(self.groupBox_24)
        self.leNomeBanco.setMinimumSize(QtCore.QSize(50, 0))
        self.leNomeBanco.setMaximumSize(QtCore.QSize(120, 16777215))
        self.leNomeBanco.setMaxLength(40)
        self.leNomeBanco.setObjectName("leNomeBanco")
        self.horizontalLayout_24.addWidget(self.leNomeBanco, 0, QtCore.Qt.AlignLeft)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem3)
        self.gridLayout_5.addWidget(self.groupBox_24, 0, 0, 1, 2)
        self.groupBox_25 = QtWidgets.QGroupBox(self.gbInfoBancarias)
        self.groupBox_25.setObjectName("groupBox_25")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_25.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.leNumeroAgencia = QtWidgets.QLineEdit(self.groupBox_25)
        self.leNumeroAgencia.setMinimumSize(QtCore.QSize(50, 0))
        self.leNumeroAgencia.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leNumeroAgencia.setMaxLength(5)
        self.leNumeroAgencia.setObjectName("leNumeroAgencia")
        self.horizontalLayout_25.addWidget(self.leNumeroAgencia)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem4)
        self.gridLayout_5.addWidget(self.groupBox_25, 1, 0, 1, 1)
        self.groupBox_26 = QtWidgets.QGroupBox(self.gbInfoBancarias)
        self.groupBox_26.setObjectName("groupBox_26")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.groupBox_26)
        self.horizontalLayout_26.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.leNumeroConta = QtWidgets.QLineEdit(self.groupBox_26)
        self.leNumeroConta.setMinimumSize(QtCore.QSize(50, 0))
        self.leNumeroConta.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leNumeroConta.setMaxLength(5)
        self.leNumeroConta.setObjectName("leNumeroConta")
        self.horizontalLayout_26.addWidget(self.leNumeroConta, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_5.addWidget(self.groupBox_26, 1, 1, 1, 1)
        self.groupBox_27 = QtWidgets.QGroupBox(self.gbInfoBancarias)
        self.groupBox_27.setObjectName("groupBox_27")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.groupBox_27)
        self.horizontalLayout_27.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.lePix = QtWidgets.QLineEdit(self.groupBox_27)
        self.lePix.setMinimumSize(QtCore.QSize(50, 0))
        self.lePix.setMaxLength(40)
        self.lePix.setObjectName("lePix")
        self.horizontalLayout_27.addWidget(self.lePix)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem5)
        self.gridLayout_5.addWidget(self.groupBox_27, 2, 0, 1, 2)
        self.groupBox_28 = QtWidgets.QGroupBox(self.gbInfoBancarias)
        self.groupBox_28.setObjectName("groupBox_28")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.groupBox_28)
        self.horizontalLayout_28.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.leSenhaINSS = QtWidgets.QLineEdit(self.groupBox_28)
        self.leSenhaINSS.setMaxLength(60)
        self.leSenhaINSS.setObjectName("leSenhaINSS")
        self.horizontalLayout_28.addWidget(self.leSenhaINSS)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem6)
        self.gridLayout_5.addWidget(self.groupBox_28, 3, 0, 1, 2)
        self.gridLayout_6.addWidget(self.gbInfoBancarias, 1, 2, 1, 1)
        self.gbInfoProfissionais = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbInfoProfissionais.sizePolicy().hasHeightForWidth())
        self.gbInfoProfissionais.setSizePolicy(sizePolicy)
        self.gbInfoProfissionais.setMaximumSize(QtCore.QSize(16777215, 170))
        self.gbInfoProfissionais.setObjectName("gbInfoProfissionais")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gbInfoProfissionais)
        self.gridLayout_4.setContentsMargins(4, 26, 4, 4)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_29 = QtWidgets.QGroupBox(self.gbInfoProfissionais)
        self.groupBox_29.setObjectName("groupBox_29")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.groupBox_29)
        self.horizontalLayout_29.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.leNit = QtWidgets.QLineEdit(self.groupBox_29)
        self.leNit.setMaxLength(14)
        self.leNit.setObjectName("leNit")
        self.horizontalLayout_29.addWidget(self.leNit)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem7)
        self.gridLayout_4.addWidget(self.groupBox_29, 0, 0, 1, 1)
        self.groupBox_30 = QtWidgets.QGroupBox(self.gbInfoProfissionais)
        self.groupBox_30.setObjectName("groupBox_30")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.groupBox_30)
        self.horizontalLayout_30.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.leCartProf = QtWidgets.QLineEdit(self.groupBox_30)
        self.leCartProf.setObjectName("leCartProf")
        self.horizontalLayout_30.addWidget(self.leCartProf)
        self.gridLayout_4.addWidget(self.groupBox_30, 0, 1, 1, 1)
        self.groupBox_31 = QtWidgets.QGroupBox(self.gbInfoProfissionais)
        self.groupBox_31.setObjectName("groupBox_31")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.groupBox_31)
        self.horizontalLayout_31.setContentsMargins(0, 16, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.leProfissao = QtWidgets.QLineEdit(self.groupBox_31)
        self.leProfissao.setObjectName("leProfissao")
        self.horizontalLayout_31.addWidget(self.leProfissao)
        self.gridLayout_4.addWidget(self.groupBox_31, 1, 0, 1, 2)
        self.gridLayout_6.addWidget(self.gbInfoProfissionais, 2, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pbAtualizar = QtWidgets.QPushButton(self.frame_7)
        self.pbAtualizar.setMinimumSize(QtCore.QSize(0, 24))
        self.pbAtualizar.setObjectName("pbAtualizar")
        self.verticalLayout_5.addWidget(self.pbAtualizar)
        self.pbBuscarCliente = QtWidgets.QPushButton(self.frame_7)
        self.pbBuscarCliente.setMinimumSize(QtCore.QSize(0, 24))
        self.pbBuscarCliente.setObjectName("pbBuscarCliente")
        self.verticalLayout_5.addWidget(self.pbBuscarCliente)
        self.pbLimpar = QtWidgets.QPushButton(self.frame_7)
        self.pbLimpar.setMinimumSize(QtCore.QSize(0, 24))
        self.pbLimpar.setObjectName("pbLimpar")
        self.verticalLayout_5.addWidget(self.pbLimpar)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pbCarregaCnis = QtWidgets.QPushButton(self.frame_9)
        self.pbCarregaCnis.setMinimumSize(QtCore.QSize(70, 60))
        self.pbCarregaCnis.setMaximumSize(QtCore.QSize(70, 60))
        self.pbCarregaCnis.setObjectName("pbCarregaCnis")
        self.horizontalLayout_16.addWidget(self.pbCarregaCnis)
        self.lbInfoCnis = QtWidgets.QLabel(self.frame_9)
        self.lbInfoCnis.setMinimumSize(QtCore.QSize(40, 0))
        self.lbInfoCnis.setMaximumSize(QtCore.QSize(45436, 16777215))
        self.lbInfoCnis.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbInfoCnis.setWordWrap(True)
        self.lbInfoCnis.setObjectName("lbInfoCnis")
        self.horizontalLayout_16.addWidget(self.lbInfoCnis)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.gridLayout_6.addWidget(self.frame_7, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tabMain.addTab(self.tabCadastro, "")
        self.horizontalLayout.addWidget(self.tabMain)

        self.retranslateUi(wdgTabCliente)
        self.tabMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgTabCliente)

    def retranslateUi(self, wdgTabCliente):
        _translate = QtCore.QCoreApplication.translate
        wdgTabCliente.setWindowTitle(_translate("wdgTabCliente", "Form"))
        self.lbTituloFiltro.setText(_translate("wdgTabCliente", "Filtros de busca"))
        self.lbBuscaNome.setText(_translate("wdgTabCliente", "Nome/Sobrenome"))
        self.leBuscaNome.setPlaceholderText(_translate("wdgTabCliente", "Nome ou Sobrenome"))
        self.leBuscaEmail.setPlaceholderText(_translate("wdgTabCliente", "E-mail"))
        self.lbBuscaEmail.setText(_translate("wdgTabCliente", "E-mail"))
        self.leBuscaTelefone.setPlaceholderText(_translate("wdgTabCliente", "Telefone/Celular"))
        self.lbBuscaTelefone.setText(_translate("wdgTabCliente", "Telefone"))
        self.leBuscaRgcpf.setPlaceholderText(_translate("wdgTabCliente", "RG ou CPF"))
        self.lbBuscaRgcpf.setText(_translate("wdgTabCliente", "RG/CPF"))
        self.lbBuscaTpBeneficio.setText(_translate("wdgTabCliente", "Tipo de Benefício"))
        self.pbFiltrar.setText(_translate("wdgTabCliente", "Filtrar"))
        self.pbLimparFiltro.setText(_translate("wdgTabCliente", "Limpar"))
        self.lbTituloClientes.setText(_translate("wdgTabCliente", "Informações de clientes"))
        self.lbInfoClientes.setText(_translate("wdgTabCliente", "Pesquise por toda a sua base de clientes"))
        item = self.tblClientes.horizontalHeaderItem(0)
        item.setText(_translate("wdgTabCliente", "clienteId"))
        item = self.tblClientes.horizontalHeaderItem(1)
        item.setText(_translate("wdgTabCliente", "Nome"))
        item = self.tblClientes.horizontalHeaderItem(2)
        item.setText(_translate("wdgTabCliente", "E-mail"))
        item = self.tblClientes.horizontalHeaderItem(3)
        item.setText(_translate("wdgTabCliente", "Telefone"))
        item = self.tblClientes.horizontalHeaderItem(4)
        item.setText(_translate("wdgTabCliente", "Cidade"))
        item = self.tblClientes.horizontalHeaderItem(5)
        item.setText(_translate("wdgTabCliente", "Tipo de Processo"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabClientes), _translate("wdgTabCliente", "    Clientes    "))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabInformacoes), _translate("wdgTabCliente", "     Informações     "))
        self.lbTitulo.setText(_translate("wdgTabCliente", "<html><head/><body><p>Cadastro de clientes</p></body></html>"))
        self.lbDescricaoTela.setText(_translate("wdgTabCliente", "Para conseguir gerar documentos e gerenciar seus clientes, é importante manter seus dados atualizados."))
        self.gbInfoPessoais.setTitle(_translate("wdgTabCliente", "Informações pessoais"))
        self.groupBox_6.setTitle(_translate("wdgTabCliente", "Primeiro nome"))
        self.lePrimeiroNome.setPlaceholderText(_translate("wdgTabCliente", "Ex: José"))
        self.groupBox_12.setTitle(_translate("wdgTabCliente", "Estado civil"))
        self.groupBox_11.setTitle(_translate("wdgTabCliente", "Nome da mãe"))
        self.leNomeMae.setPlaceholderText(_translate("wdgTabCliente", "Ex: Cleusa da Silva Santos"))
        self.groupBox_5.setTitle(_translate("wdgTabCliente", "Cód Cliente"))
        self.rbMasculino.setText(_translate("wdgTabCliente", "Masculino"))
        self.rbFeminino.setText(_translate("wdgTabCliente", "Feminino"))
        self.groupBox_7.setTitle(_translate("wdgTabCliente", "Sobrenome"))
        self.leSobrenome.setPlaceholderText(_translate("wdgTabCliente", "Ex: da Silva Santos"))
        self.groupBox_16.setTitle(_translate("wdgTabCliente", "Grau de escolaridade"))
        self.pbMaisTelefones.setText(_translate("wdgTabCliente", "Mais telefones"))
        self.groupBox_10.setTitle(_translate("wdgTabCliente", "CPF"))
        self.leCpf.setPlaceholderText(_translate("wdgTabCliente", "254.214.587.99"))
        self.groupBox_9.setTitle(_translate("wdgTabCliente", "Idade"))
        self.leIdade.setPlaceholderText(_translate("wdgTabCliente", "35"))
        self.groupBox_14.setTitle(_translate("wdgTabCliente", "Data de nascimento"))
        self.groupBox_13.setTitle(_translate("wdgTabCliente", "E-mail"))
        self.leEmail.setPlaceholderText(_translate("wdgTabCliente", "cliente@gmail.com"))
        self.groupBox_8.setTitle(_translate("wdgTabCliente", "RG"))
        self.leRg.setPlaceholderText(_translate("wdgTabCliente", "87.452.456-7"))
        self.groupBox_15.setTitle(_translate("wdgTabCliente", "Telefone/Celular"))
        self.leTelefone.setPlaceholderText(_translate("wdgTabCliente", "(11) 9.4578-6541"))
        self.gbInfoResidenciais.setTitle(_translate("wdgTabCliente", "Informações residenciais"))
        self.groupBox_23.setTitle(_translate("wdgTabCliente", "Complemento"))
        self.leComplemento.setPlaceholderText(_translate("wdgTabCliente", "Bloco E, Apto: 504"))
        self.groupBox_19.setTitle(_translate("wdgTabCliente", "Endereço"))
        self.leEndereco.setPlaceholderText(_translate("wdgTabCliente", "Av. Paulista, 1455"))
        self.groupBox_20.setTitle(_translate("wdgTabCliente", "Cidade"))
        self.leCidade.setPlaceholderText(_translate("wdgTabCliente", "São Paulo"))
        self.groupBox_18.setTitle(_translate("wdgTabCliente", "Número"))
        self.leNumero.setPlaceholderText(_translate("wdgTabCliente", "12345"))
        self.groupBox_22.setTitle(_translate("wdgTabCliente", "Estado"))
        self.groupBox_21.setTitle(_translate("wdgTabCliente", "Bairro"))
        self.leBairro.setPlaceholderText(_translate("wdgTabCliente", "Boa Vista"))
        self.groupBox_17.setTitle(_translate("wdgTabCliente", "CEP"))
        self.leCep.setPlaceholderText(_translate("wdgTabCliente", "12345-789"))
        self.gbInfoBancarias.setTitle(_translate("wdgTabCliente", "Informações bancárias"))
        self.groupBox_24.setTitle(_translate("wdgTabCliente", "Nome do banco"))
        self.leNomeBanco.setPlaceholderText(_translate("wdgTabCliente", "Bamerindos"))
        self.groupBox_25.setTitle(_translate("wdgTabCliente", "Agência"))
        self.leNumeroAgencia.setPlaceholderText(_translate("wdgTabCliente", "12345"))
        self.groupBox_26.setTitle(_translate("wdgTabCliente", "Nº conta"))
        self.leNumeroConta.setPlaceholderText(_translate("wdgTabCliente", "12345"))
        self.groupBox_27.setTitle(_translate("wdgTabCliente", "PIX"))
        self.lePix.setPlaceholderText(_translate("wdgTabCliente", "Aa12-#$"))
        self.groupBox_28.setTitle(_translate("wdgTabCliente", "Senha Meu INSS"))
        self.leSenhaINSS.setPlaceholderText(_translate("wdgTabCliente", "Senha"))
        self.gbInfoProfissionais.setTitle(_translate("wdgTabCliente", "Informações profissionais"))
        self.groupBox_29.setTitle(_translate("wdgTabCliente", "NIT"))
        self.leNit.setPlaceholderText(_translate("wdgTabCliente", "123.45678.90-1"))
        self.groupBox_30.setTitle(_translate("wdgTabCliente", "Carteira profissional"))
        self.groupBox_31.setTitle(_translate("wdgTabCliente", "Profissão"))
        self.leProfissao.setPlaceholderText(_translate("wdgTabCliente", "Auxiliar de informática"))
        self.pbAtualizar.setText(_translate("wdgTabCliente", "Atualizar cliente"))
        self.pbBuscarCliente.setText(_translate("wdgTabCliente", "Buscar cliente"))
        self.pbLimpar.setText(_translate("wdgTabCliente", "Limpar"))
        self.pbCarregaCnis.setText(_translate("wdgTabCliente", "Carregar \n"
"CNIS"))
        self.lbInfoCnis.setText(_translate("wdgTabCliente", "Carregar informações a partir do CNIS"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabCadastro), _translate("wdgTabCliente", "    Cadastro    "))
import Resources.tabCliente


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgTabCliente = QtWidgets.QWidget()
    ui = Ui_wdgTabCliente()
    ui.setupUi(wdgTabCliente)
    wdgTabCliente.show()
    sys.exit(app.exec_())
