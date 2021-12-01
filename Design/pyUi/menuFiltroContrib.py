# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/menuFiltroContrib.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwFiltrosContribuicoes(object):
    def setupUi(self, mwFiltrosContribuicoes):
        mwFiltrosContribuicoes.setObjectName("mwFiltrosContribuicoes")
        mwFiltrosContribuicoes.resize(281, 468)
        mwFiltrosContribuicoes.setStyleSheet("/*------------------------------------ Frame ------------------------------------*/\n"
"#frMenu {\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: lightgrey;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"#frSeparador {\n"
"    background-color: lightgrey;\n"
"}\n"
"\n"
"#frBusca {\n"
"    border-radius: 4px;\n"
"    border: 1px solid lightgrey;\n"
"}\n"
"\n"
"/*------------------------------------ Label ------------------------------------*/\n"
"#lbTitulo {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    font-weight: 300;\n"
"}\n"
"\n"
"#lbData, #lbIndicadores {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#lbInfoDe, #lbInfoAte {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#lbInfoBusca {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"/*------------------------------------ Line Edit ------------------------------------*/\n"
"\n"
"#leBusca {\n"
"    border: 0px solid transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(mwFiltrosContribuicoes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frMenu = QtWidgets.QFrame(self.centralwidget)
        self.frMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMenu.setObjectName("frMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frMenu)
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 0)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbTitulo = QtWidgets.QLabel(self.frMenu)
        self.lbTitulo.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lbTitulo.setObjectName("lbTitulo")
        self.verticalLayout_2.addWidget(self.lbTitulo)
        self.frSeparador = QtWidgets.QFrame(self.frMenu)
        self.frSeparador.setMinimumSize(QtCore.QSize(0, 2))
        self.frSeparador.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frSeparador.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSeparador.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSeparador.setObjectName("frSeparador")
        self.verticalLayout_2.addWidget(self.frSeparador, 0, QtCore.Qt.AlignTop)
        self.frSeparador1 = QtWidgets.QFrame(self.frMenu)
        self.frSeparador1.setMinimumSize(QtCore.QSize(0, 2))
        self.frSeparador1.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frSeparador1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSeparador1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSeparador1.setObjectName("frSeparador1")
        self.verticalLayout_2.addWidget(self.frSeparador1)
        self.lbData = QtWidgets.QLabel(self.frMenu)
        self.lbData.setObjectName("lbData")
        self.verticalLayout_2.addWidget(self.lbData, 0, QtCore.Qt.AlignTop)
        self.frData = QtWidgets.QFrame(self.frMenu)
        self.frData.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frData.setObjectName("frData")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frData)
        self.gridLayout_2.setContentsMargins(12, -1, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbInfoDe = QtWidgets.QLabel(self.frData)
        self.lbInfoDe.setObjectName("lbInfoDe")
        self.gridLayout_2.addWidget(self.lbInfoDe, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.dtDe = QtWidgets.QDateEdit(self.frData)
        self.dtDe.setCalendarPopup(True)
        self.dtDe.setObjectName("dtDe")
        self.gridLayout_2.addWidget(self.dtDe, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.lbInfoAte = QtWidgets.QLabel(self.frData)
        self.lbInfoAte.setObjectName("lbInfoAte")
        self.gridLayout_2.addWidget(self.lbInfoAte, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.dtAte = QtWidgets.QDateEdit(self.frData)
        self.dtAte.setCalendarPopup(True)
        self.dtAte.setObjectName("dtAte")
        self.gridLayout_2.addWidget(self.dtAte, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.frData, 0, QtCore.Qt.AlignTop)
        self.frSeparador2 = QtWidgets.QFrame(self.frMenu)
        self.frSeparador2.setMinimumSize(QtCore.QSize(0, 2))
        self.frSeparador2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frSeparador2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frSeparador2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSeparador2.setObjectName("frSeparador2")
        self.verticalLayout_2.addWidget(self.frSeparador2)
        self.lbIndicadores = QtWidgets.QLabel(self.frMenu)
        self.lbIndicadores.setObjectName("lbIndicadores")
        self.verticalLayout_2.addWidget(self.lbIndicadores)
        self.frBusca = QtWidgets.QFrame(self.frMenu)
        self.frBusca.setMinimumSize(QtCore.QSize(0, 30))
        self.frBusca.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frBusca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBusca.setObjectName("frBusca")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frBusca)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbInfoBusca = QtWidgets.QLabel(self.frBusca)
        self.lbInfoBusca.setObjectName("lbInfoBusca")
        self.horizontalLayout.addWidget(self.lbInfoBusca, 0, QtCore.Qt.AlignLeft)
        self.leBusca = QtWidgets.QLineEdit(self.frBusca)
        self.leBusca.setInputMask("")
        self.leBusca.setMaxLength(30)
        self.leBusca.setObjectName("leBusca")
        self.horizontalLayout.addWidget(self.leBusca)
        self.verticalLayout_2.addWidget(self.frBusca)
        self.scrollArea = QtWidgets.QScrollArea(self.frMenu)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 261, 212))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vlIndicadores = QtWidgets.QVBoxLayout()
        self.vlIndicadores.setContentsMargins(-1, -1, -1, 4)
        self.vlIndicadores.setObjectName("vlIndicadores")
        self.verticalLayout.addLayout(self.vlIndicadores)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.frIndicadores = QtWidgets.QFrame(self.frMenu)
        self.frIndicadores.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frIndicadores.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frIndicadores.setObjectName("frIndicadores")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frIndicadores)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.frIndicadores)
        self.gridLayout.addWidget(self.frMenu, 0, 0, 1, 1)
        mwFiltrosContribuicoes.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwFiltrosContribuicoes)
        QtCore.QMetaObject.connectSlotsByName(mwFiltrosContribuicoes)

    def retranslateUi(self, mwFiltrosContribuicoes):
        _translate = QtCore.QCoreApplication.translate
        mwFiltrosContribuicoes.setWindowTitle(_translate("mwFiltrosContribuicoes", "MainWindow"))
        self.lbTitulo.setText(_translate("mwFiltrosContribuicoes", "Filtros"))
        self.lbData.setText(_translate("mwFiltrosContribuicoes", "Data"))
        self.lbInfoDe.setText(_translate("mwFiltrosContribuicoes", "De:"))
        self.lbInfoAte.setText(_translate("mwFiltrosContribuicoes", "Até:"))
        self.lbIndicadores.setText(_translate("mwFiltrosContribuicoes", "Indicadores"))
        self.lbInfoBusca.setText(_translate("mwFiltrosContribuicoes", "Busca:"))
        self.leBusca.setPlaceholderText(_translate("mwFiltrosContribuicoes", "Indicador"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwFiltrosContribuicoes = QtWidgets.QMainWindow()
    ui = Ui_mwFiltrosContribuicoes()
    ui.setupUi(mwFiltrosContribuicoes)
    mwFiltrosContribuicoes.show()
    sys.exit(app.exec_())
