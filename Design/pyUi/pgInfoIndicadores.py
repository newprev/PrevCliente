# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/pgInfoIndicadores.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwInfoIndicadores(object):
    def setupUi(self, mwInfoIndicadores):
        mwInfoIndicadores.setObjectName("mwInfoIndicadores")
        mwInfoIndicadores.resize(800, 600)
        mwInfoIndicadores.setStyleSheet("/* ----------------------------------------------- Frame ----------------------------------------------- */\n"
"#frMain {\n"
"    border-radius: 8px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"#frDescricao {\n"
"    border-radius: 8px;\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"#frCabecalho {\n"
"    background-color: #3F4E8C;\n"
"    border: 0px solid none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#frBusca {\n"
"    background-color: rgb(244, 244, 244);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* ----------------------------------------------- Label ----------------------------------------------- */\n"
"#lbTitulo {\n"
"    font: 16pt \"Avenir LT Std\";\n"
"    color: white;\n"
"\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"#lbSigla {\n"
"    font: 24pt \"Avenir LT Std\";\n"
"    color: #6F757B;\n"
"}\n"
"\n"
"#lbSubtitulo, #lbSiglaCbx, \n"
"#lbFonte, #lbDescricao {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: #6F757B;\n"
"\n"
"    background-color: white;\n"
"}\n"
"\n"
" #lbDesc {    \n"
"    font: 14pt \"Avenir LT Std\";\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#lbResumo {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    font-weight: 750;\n"
"    \n"
"    background-color: white;\n"
"}\n"
"\n"
"/* ----------------------------------------------- ScrollArea ----------------------------------------------- */\n"
"#scaIndicadores, #scaDescricao, \n"
"#scrollAreaWidgetContents {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/*-------------------------------------------  Scroll Bar --------------------------------------------*/\n"
"QScrollBar:vertical {\n"
"        background-color: #DDDEDF;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #3F4E8C;\n"
"    min-height: 5px;\n"
"    width: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"      border: none;\n"
"      background: none;\n"
"      color: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"/* ----------------------------------------------- Line Edit ----------------------------------------------- */\n"
"#leBusca {\n"
"    border: 0px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: rgb(244, 244, 244);\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"/* --------------------------------------------- Push Button --------------------------------------------- */\n"
"\n"
"#pbEnviar {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: white;\n"
"\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    background-color: #3F4E8C;\n"
"}\n"
"\n"
"#pbFiltro {\n"
"    background-image: url(:/filtro/filtros.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#pbBusca {\n"
"    background-image: url(:/filtro/busca.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: rgb(244, 244, 244);\n"
"    border-radius: 8px;\n"
"}")
        self.wdgMain = QtWidgets.QWidget(mwInfoIndicadores)
        self.wdgMain.setObjectName("wdgMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wdgMain)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frMain = QtWidgets.QFrame(self.wdgMain)
        self.frMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.gridLayout = QtWidgets.QGridLayout(self.frMain)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(14)
        self.gridLayout.setObjectName("gridLayout")
        self.frCabecalho = QtWidgets.QFrame(self.frMain)
        self.frCabecalho.setMinimumSize(QtCore.QSize(0, 60))
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frCabecalho)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbTitulo = QtWidgets.QLabel(self.frCabecalho)
        self.lbTitulo.setObjectName("lbTitulo")
        self.gridLayout_2.addWidget(self.lbTitulo, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frCabecalho, 0, 0, 1, 1)
        self.frConteudo = QtWidgets.QFrame(self.frMain)
        self.frConteudo.setEnabled(True)
        self.frConteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frConteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frConteudo.setObjectName("frConteudo")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frConteudo)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frBusca = QtWidgets.QFrame(self.frConteudo)
        self.frBusca.setMinimumSize(QtCore.QSize(0, 40))
        self.frBusca.setSizeIncrement(QtCore.QSize(0, 0))
        self.frBusca.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBusca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBusca.setObjectName("frBusca")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frBusca)
        self.horizontalLayout.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leBusca = QtWidgets.QLineEdit(self.frBusca)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leBusca.sizePolicy().hasHeightForWidth())
        self.leBusca.setSizePolicy(sizePolicy)
        self.leBusca.setMaxLength(15)
        self.leBusca.setClearButtonEnabled(False)
        self.leBusca.setObjectName("leBusca")
        self.horizontalLayout.addWidget(self.leBusca)
        self.pbBusca = QtWidgets.QPushButton(self.frBusca)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbBusca.sizePolicy().hasHeightForWidth())
        self.pbBusca.setSizePolicy(sizePolicy)
        self.pbBusca.setText("")
        self.pbBusca.setObjectName("pbBusca")
        self.horizontalLayout.addWidget(self.pbBusca)
        self.gridLayout_3.addWidget(self.frBusca, 0, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.frConteudo)
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scaIndicadores = QtWidgets.QWidget()
        self.scaIndicadores.setGeometry(QtCore.QRect(0, 0, 218, 438))
        self.scaIndicadores.setObjectName("scaIndicadores")
        self.scrollArea.setWidget(self.scaIndicadores)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frConteudo)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frDescricao = QtWidgets.QFrame(self.frame_3)
        self.frDescricao.setMinimumSize(QtCore.QSize(480, 420))
        self.frDescricao.setMaximumSize(QtCore.QSize(450, 450))
        self.frDescricao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frDescricao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDescricao.setObjectName("frDescricao")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frDescricao)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbSigla = QtWidgets.QLabel(self.frDescricao)
        self.lbSigla.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbSigla.setText("")
        self.lbSigla.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbSigla.setObjectName("lbSigla")
        self.verticalLayout_3.addWidget(self.lbSigla)
        self.lbResumo = QtWidgets.QLabel(self.frDescricao)
        self.lbResumo.setMaximumSize(QtCore.QSize(16777215, 42))
        self.lbResumo.setText("")
        self.lbResumo.setWordWrap(True)
        self.lbResumo.setObjectName("lbResumo")
        self.verticalLayout_3.addWidget(self.lbResumo)
        self.scaDescricao = QtWidgets.QScrollArea(self.frDescricao)
        self.scaDescricao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scaDescricao.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scaDescricao.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scaDescricao.setWidgetResizable(True)
        self.scaDescricao.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.scaDescricao.setObjectName("scaDescricao")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbDescricao = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbDescricao.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbDescricao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbDescricao.setWordWrap(True)
        self.lbDescricao.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbDescricao.setObjectName("lbDescricao")
        self.verticalLayout_7.addWidget(self.lbDescricao)
        self.scaDescricao.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scaDescricao)
        self.lbFonte = QtWidgets.QLabel(self.frDescricao)
        self.lbFonte.setMaximumSize(QtCore.QSize(16777215, 18))
        self.lbFonte.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbFonte.setOpenExternalLinks(True)
        self.lbFonte.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbFonte.setObjectName("lbFonte")
        self.verticalLayout_3.addWidget(self.lbFonte)
        self.verticalLayout_6.addWidget(self.frDescricao)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.gridLayout_3.addWidget(self.frame_2, 1, 3, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frConteudo)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbFiltro = QtWidgets.QPushButton(self.frame_5)
        self.pbFiltro.setMinimumSize(QtCore.QSize(40, 40))
        self.pbFiltro.setMaximumSize(QtCore.QSize(40, 40))
        self.pbFiltro.setText("")
        self.pbFiltro.setObjectName("pbFiltro")
        self.horizontalLayout_2.addWidget(self.pbFiltro)
        spacerItem = QtWidgets.QSpacerItem(355, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pbEnviar = QtWidgets.QPushButton(self.frame_5)
        self.pbEnviar.setMinimumSize(QtCore.QSize(110, 24))
        self.pbEnviar.setObjectName("pbEnviar")
        self.horizontalLayout_2.addWidget(self.pbEnviar)
        self.gridLayout_3.addWidget(self.frame_5, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frConteudo, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frMain)
        mwInfoIndicadores.setCentralWidget(self.wdgMain)

        self.retranslateUi(mwInfoIndicadores)
        QtCore.QMetaObject.connectSlotsByName(mwInfoIndicadores)

    def retranslateUi(self, mwInfoIndicadores):
        _translate = QtCore.QCoreApplication.translate
        mwInfoIndicadores.setWindowTitle(_translate("mwInfoIndicadores", "MainWindow"))
        self.lbTitulo.setText(_translate("mwInfoIndicadores", "Informações dos indicadores"))
        self.leBusca.setPlaceholderText(_translate("mwInfoIndicadores", "Digite a sigla de algum indicador"))
        self.lbDescricao.setText(_translate("mwInfoIndicadores", "fgfdgf"))
        self.lbFonte.setText(_translate("mwInfoIndicadores", "TextLabel"))
        self.pbEnviar.setText(_translate("mwInfoIndicadores", "Fechar / Enviar"))
import Resources.pgInfoIndicadores


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwInfoIndicadores = QtWidgets.QMainWindow()
    ui = Ui_mwInfoIndicadores()
    ui.setupUi(mwInfoIndicadores)
    mwInfoIndicadores.show()
    sys.exit(app.exec_())
