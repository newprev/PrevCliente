# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/pgTetosPrevidenciarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwTetosPrev(object):
    def setupUi(self, mwTetosPrev):
        mwTetosPrev.setObjectName("mwTetosPrev")
        mwTetosPrev.resize(529, 494)
        mwTetosPrev.setStyleSheet("/*-------------------------------- Tables -----------------------------------------*/\n"
"#tblInfo {\n"
"    background-color: transparent;\n"
"    \n"
"    font: 11pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"\n"
"    alternate-background-color: #F4F5F8;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"#tblInfo::item{\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    padding-left: 4px;\n"
"    background-color: white;\n"
"    border: 2px solid #3F4E8C;\n"
"\n"
"    border-radius: 7px;\n"
"\n"
"    min-height: 45px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"\n"
"    padding-left: 4px;\n"
"    background-color: white;\n"
"    border: 0px solid none;\n"
"\n"
"    border-radius: 4px;\n"
"\n"
"    min-height: 45px;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"    icon-color: white;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    icon-color: white;\n"
"}\n"
"/*-------------------------------- Frame -----------------------------------------*/\n"
"#frPrincipal {\n"
"    border: 0px solid none;\n"
"    \n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 0px;\n"
"\n"
"    background-color: white;\n"
"}\n"
"\n"
"#frTitulo {\n"
"    border-radius: 8px;\n"
"    background-color: #3F4E8C;\n"
"}\n"
"\n"
"/*-------------------------------- Label -----------------------------------------*/\n"
"QLabel {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#lbDtReferenteInfo, #lbValorInfo {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"#lbFiltrosInfo {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"#lbTitulo {\n"
"    font: 14pt \"Avenir LT Std\";\n"
"    color: white;\n"
"\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"/*-------------------------------- Push Buttons --------------------------------*/\n"
"#pbFiltros {\n"
"    background-image: url(:/filtros/filtros.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 8px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(mwTetosPrev)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frPrincipal = QtWidgets.QFrame(self.centralwidget)
        self.frPrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frPrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPrincipal.setObjectName("frPrincipal")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frPrincipal)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frConteudo = QtWidgets.QFrame(self.frPrincipal)
        self.frConteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frConteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frConteudo.setObjectName("frConteudo")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frConteudo)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frFiltros = QtWidgets.QFrame(self.frConteudo)
        self.frFiltros.setMinimumSize(QtCore.QSize(0, 40))
        self.frFiltros.setMaximumSize(QtCore.QSize(16777215, 160))
        self.frFiltros.setSizeIncrement(QtCore.QSize(0, 0))
        self.frFiltros.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frFiltros.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFiltros.setObjectName("frFiltros")
        self.gridLayout = QtWidgets.QGridLayout(self.frFiltros)
        self.gridLayout.setContentsMargins(8, 4, 8, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.pbFiltros = QtWidgets.QPushButton(self.frFiltros)
        self.pbFiltros.setMinimumSize(QtCore.QSize(35, 35))
        self.pbFiltros.setMaximumSize(QtCore.QSize(35, 35))
        self.pbFiltros.setText("")
        self.pbFiltros.setObjectName("pbFiltros")
        self.gridLayout.addWidget(self.pbFiltros, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.frDtReferente = QtWidgets.QFrame(self.frFiltros)
        self.frDtReferente.setMaximumSize(QtCore.QSize(220, 150))
        self.frDtReferente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frDtReferente.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frDtReferente.setObjectName("frDtReferente")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frDtReferente)
        self.verticalLayout_3.setContentsMargins(4, 4, 8, 4)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbDtReferenteInfo = QtWidgets.QLabel(self.frDtReferente)
        self.lbDtReferenteInfo.setObjectName("lbDtReferenteInfo")
        self.verticalLayout_3.addWidget(self.lbDtReferenteInfo, 0, QtCore.Qt.AlignTop)
        self.lbDtRefDe = QtWidgets.QLabel(self.frDtReferente)
        self.lbDtRefDe.setObjectName("lbDtRefDe")
        self.verticalLayout_3.addWidget(self.lbDtRefDe)
        self.dtDe = QtWidgets.QDateEdit(self.frDtReferente)
        self.dtDe.setMinimumSize(QtCore.QSize(0, 24))
        self.dtDe.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dtDe.setObjectName("dtDe")
        self.verticalLayout_3.addWidget(self.dtDe)
        self.lbDtRefAte = QtWidgets.QLabel(self.frDtReferente)
        self.lbDtRefAte.setObjectName("lbDtRefAte")
        self.verticalLayout_3.addWidget(self.lbDtRefAte)
        self.dtAte = QtWidgets.QDateEdit(self.frDtReferente)
        self.dtAte.setMinimumSize(QtCore.QSize(0, 24))
        self.dtAte.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dtAte.setObjectName("dtAte")
        self.verticalLayout_3.addWidget(self.dtAte)
        self.gridLayout.addWidget(self.frDtReferente, 1, 0, 1, 1)
        self.frValor = QtWidgets.QFrame(self.frFiltros)
        self.frValor.setMaximumSize(QtCore.QSize(150, 150))
        self.frValor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frValor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frValor.setObjectName("frValor")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frValor)
        self.verticalLayout_4.setContentsMargins(4, 4, 8, 4)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbValorInfo = QtWidgets.QLabel(self.frValor)
        self.lbValorInfo.setObjectName("lbValorInfo")
        self.verticalLayout_4.addWidget(self.lbValorInfo)
        self.lbValorDe = QtWidgets.QLabel(self.frValor)
        self.lbValorDe.setObjectName("lbValorDe")
        self.verticalLayout_4.addWidget(self.lbValorDe)
        self.leDe = QtWidgets.QLineEdit(self.frValor)
        self.leDe.setMaximumSize(QtCore.QSize(90, 16777215))
        self.leDe.setObjectName("leDe")
        self.verticalLayout_4.addWidget(self.leDe)
        self.lbValorPara = QtWidgets.QLabel(self.frValor)
        self.lbValorPara.setObjectName("lbValorPara")
        self.verticalLayout_4.addWidget(self.lbValorPara)
        self.leAte = QtWidgets.QLineEdit(self.frValor)
        self.leAte.setMaximumSize(QtCore.QSize(90, 16777215))
        self.leAte.setObjectName("leAte")
        self.verticalLayout_4.addWidget(self.leAte)
        self.gridLayout.addWidget(self.frValor, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frFiltros, 0, 0, 1, 1)
        self.tblInfo = QtWidgets.QTableWidget(self.frConteudo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblInfo.sizePolicy().hasHeightForWidth())
        self.tblInfo.setSizePolicy(sizePolicy)
        self.tblInfo.setMaximumSize(QtCore.QSize(16548754, 16777215))
        self.tblInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblInfo.setAlternatingRowColors(True)
        self.tblInfo.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblInfo.setObjectName("tblInfo")
        self.tblInfo.setColumnCount(3)
        self.tblInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(16)
        item.setFont(font)
        self.tblInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("TeX Gyre Adventor")
        font.setPointSize(16)
        item.setFont(font)
        self.tblInfo.setHorizontalHeaderItem(2, item)
        self.tblInfo.horizontalHeader().setCascadingSectionResizes(True)
        self.tblInfo.horizontalHeader().setStretchLastSection(True)
        self.tblInfo.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tblInfo, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frConteudo, 1, 0, 1, 1)
        self.frTitulo = QtWidgets.QFrame(self.frPrincipal)
        self.frTitulo.setMinimumSize(QtCore.QSize(0, 50))
        self.frTitulo.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frTitulo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTitulo.setObjectName("frTitulo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frTitulo)
        self.horizontalLayout.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbTitulo = QtWidgets.QLabel(self.frTitulo)
        self.lbTitulo.setMinimumSize(QtCore.QSize(0, 36))
        self.lbTitulo.setMaximumSize(QtCore.QSize(16777215, 42))
        self.lbTitulo.setObjectName("lbTitulo")
        self.horizontalLayout.addWidget(self.lbTitulo, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frTitulo, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frPrincipal)
        mwTetosPrev.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwTetosPrev)
        QtCore.QMetaObject.connectSlotsByName(mwTetosPrev)

    def retranslateUi(self, mwTetosPrev):
        _translate = QtCore.QCoreApplication.translate
        mwTetosPrev.setWindowTitle(_translate("mwTetosPrev", "MainWindow"))
        self.lbDtReferenteInfo.setText(_translate("mwTetosPrev", "Data referente"))
        self.lbDtRefDe.setText(_translate("mwTetosPrev", "De:"))
        self.dtDe.setDisplayFormat(_translate("mwTetosPrev", "MM/yyyy"))
        self.lbDtRefAte.setText(_translate("mwTetosPrev", "Até:"))
        self.dtAte.setDisplayFormat(_translate("mwTetosPrev", "MM/yyyy"))
        self.lbValorInfo.setText(_translate("mwTetosPrev", "Valor"))
        self.lbValorDe.setText(_translate("mwTetosPrev", "De:"))
        self.lbValorPara.setText(_translate("mwTetosPrev", "Até:"))
        item = self.tblInfo.horizontalHeaderItem(0)
        item.setText(_translate("mwTetosPrev", "id"))
        item = self.tblInfo.horizontalHeaderItem(1)
        item.setText(_translate("mwTetosPrev", "Ano"))
        item = self.tblInfo.horizontalHeaderItem(2)
        item.setText(_translate("mwTetosPrev", "Valor em R$ (Reais)"))
        self.lbTitulo.setText(_translate("mwTetosPrev", "Tetos previdenciários"))
import Resources.pgTetosPrevidenciarios


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwTetosPrev = QtWidgets.QMainWindow()
    ui = Ui_mwTetosPrev()
    ui.setupUi(mwTetosPrev)
    mwTetosPrev.show()
    sys.exit(app.exec_())
