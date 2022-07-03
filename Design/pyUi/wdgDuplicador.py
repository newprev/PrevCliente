# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/wdgDuplicador.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwDuplicador(object):
    def setupUi(self, mwDuplicador):
        mwDuplicador.setObjectName("mwDuplicador")
        mwDuplicador.resize(530, 300)
        mwDuplicador.setMinimumSize(QtCore.QSize(530, 300))
        mwDuplicador.setMaximumSize(QtCore.QSize(530, 320))
        mwDuplicador.setStyleSheet("#mwDuplicador {\n"
"    background-color: transparent;\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"/*------------------- Spin Box ---------------------*/\n"
"QSpinBox {\n"
"    \n"
"    font: 14pt \"Avenir LT Std\";\n"
"    color: #606970;\n"
"\n"
"    padding: 8px 16px;\n"
"\n"
"    background: #F9F9F9;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; \n"
"\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-image: url(:/upDown/up.png);\n"
"    border-width: 1px;\n"
"\n"
"    margin: 5px 4px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; \n"
"\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    border-image: url(:/upDown/down.png);\n"
"    border-width: 1px;\n"
"\n"
"    margin: 3px 4px;\n"
"}\n"
"\n"
"/*------------------- Frame ---------------------*/\n"
"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 8px;\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"/*------------------- Label ---------------------*/\n"
"QLabel {\n"
"    font-family: Avenir LT Pro;\n"
"    font-style: normal;\n"
"    font-weight: normal;\n"
"    font-size: 16px;\n"
"    line-height: 24px;\n"
"\n"
"    color: #606970;\n"
"}\n"
"\n"
"#lbInfoTitulo {\n"
"    font: 20pt \"Bebas Neue\";\n"
"    font-weight: 650;\n"
"    color: #009E38;\n"
"}\n"
"\n"
"/*------------------- Push Button ---------------------*/\n"
"#pbReplicar {\n"
"    \n"
"    font: 18pt \"Avenir LT Std\";\n"
"    font-weight: 750;\n"
"    color: white;    \n"
"\n"
"    background: #009E38;\n"
"\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-bottom-left-radius: 8px;\n"
"\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"#pbFechar {\n"
"    background-color: white;\n"
"    background-image: url(:/fechar/closeLarge.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    border: 0px solid none;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mwDuplicador)
        self.centralwidget.setMinimumSize(QtCore.QSize(530, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(530, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frShadow = QtWidgets.QFrame(self.centralwidget)
        self.frShadow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frShadow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frShadow.setObjectName("frShadow")
        self.gridLayout = QtWidgets.QGridLayout(self.frShadow)
        self.gridLayout.setContentsMargins(18, 18, 18, 18)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frMain = QtWidgets.QFrame(self.frShadow)
        self.frMain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frMain)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frCabecalho = QtWidgets.QFrame(self.frMain)
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frCabecalho)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frTitulo = QtWidgets.QFrame(self.frCabecalho)
        self.frTitulo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTitulo.setObjectName("frTitulo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frTitulo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbInfoTitulo = QtWidgets.QLabel(self.frTitulo)
        self.lbInfoTitulo.setObjectName("lbInfoTitulo")
        self.horizontalLayout.addWidget(self.lbInfoTitulo, 0, QtCore.Qt.AlignHCenter)
        self.pbFechar = QtWidgets.QPushButton(self.frTitulo)
        self.pbFechar.setText("")
        self.pbFechar.setObjectName("pbFechar")
        self.horizontalLayout.addWidget(self.pbFechar, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frTitulo)
        self.frMiolo = QtWidgets.QFrame(self.frCabecalho)
        self.frMiolo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMiolo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMiolo.setObjectName("frMiolo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frMiolo)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbInfoMiolo = QtWidgets.QLabel(self.frMiolo)
        self.lbInfoMiolo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfoMiolo.setWordWrap(True)
        self.lbInfoMiolo.setObjectName("lbInfoMiolo")
        self.horizontalLayout_2.addWidget(self.lbInfoMiolo)
        self.verticalLayout.addWidget(self.frMiolo)
        self.frBottom = QtWidgets.QFrame(self.frCabecalho)
        self.frBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBottom.setObjectName("frBottom")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frBottom)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sbQtdMeses = QtWidgets.QSpinBox(self.frBottom)
        self.sbQtdMeses.setObjectName("sbQtdMeses")
        self.horizontalLayout_3.addWidget(self.sbQtdMeses)
        self.lbInfoMeses = QtWidgets.QLabel(self.frBottom)
        self.lbInfoMeses.setObjectName("lbInfoMeses")
        self.horizontalLayout_3.addWidget(self.lbInfoMeses)
        self.verticalLayout.addWidget(self.frBottom, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frCabecalho)
        self.pbReplicar = QtWidgets.QPushButton(self.frMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbReplicar.sizePolicy().hasHeightForWidth())
        self.pbReplicar.setSizePolicy(sizePolicy)
        self.pbReplicar.setMinimumSize(QtCore.QSize(0, 55))
        self.pbReplicar.setMaximumSize(QtCore.QSize(16777215, 55))
        self.pbReplicar.setObjectName("pbReplicar")
        self.verticalLayout_2.addWidget(self.pbReplicar)
        self.gridLayout.addWidget(self.frMain, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frShadow, 0, 0, 1, 1)
        mwDuplicador.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwDuplicador)
        QtCore.QMetaObject.connectSlotsByName(mwDuplicador)

    def retranslateUi(self, mwDuplicador):
        _translate = QtCore.QCoreApplication.translate
        mwDuplicador.setWindowTitle(_translate("mwDuplicador", "MainWindow"))
        self.lbInfoTitulo.setText(_translate("mwDuplicador", "DESEJA REPLICAR A COMPETÊNCIA?"))
        self.lbInfoMiolo.setText(_translate("mwDuplicador", "A réplica serve para quando você possui um período de contribuições e competências iguais."))
        self.lbInfoMeses.setText(_translate("mwDuplicador", "meses"))
        self.pbReplicar.setText(_translate("mwDuplicador", "Replicar"))
import Resources.wdgDuplicador


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwDuplicador = QtWidgets.QMainWindow()
    ui = Ui_mwDuplicador()
    ui.setupUi(mwDuplicador)
    mwDuplicador.show()
    sys.exit(app.exec_())
