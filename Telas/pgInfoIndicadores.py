# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pgInfoIndicadores.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
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
"    border: 1px solid black;\n"
"}\n"
"\n"
"/* ----------------------------------------------- Label ----------------------------------------------- */\n"
"#lbTitulo, #lbSigla {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"#lbSubtitulo, #lbSiglaCbx, #lbIndicadorDesc {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 12px;\n"
"    \n"
"    background-color: transparent;\n"
"}")
        self.wdgMain = QtWidgets.QWidget(mwInfoIndicadores)
        self.wdgMain.setObjectName("wdgMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wdgMain)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frMain = QtWidgets.QFrame(self.wdgMain)
        self.frMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frMain)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frCabecalho = QtWidgets.QFrame(self.frMain)
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.lbTitulo = QtWidgets.QLabel(self.frCabecalho)
        self.lbTitulo.setGeometry(QtCore.QRect(20, 10, 371, 31))
        self.lbTitulo.setObjectName("lbTitulo")
        self.lbSubtitulo = QtWidgets.QLabel(self.frCabecalho)
        self.lbSubtitulo.setGeometry(QtCore.QRect(20, 40, 431, 17))
        self.lbSubtitulo.setObjectName("lbSubtitulo")
        self.verticalLayout_2.addWidget(self.frCabecalho)
        self.frConteudo = QtWidgets.QFrame(self.frMain)
        self.frConteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frConteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frConteudo.setObjectName("frConteudo")
        self.lbSiglaCbx = QtWidgets.QLabel(self.frConteudo)
        self.lbSiglaCbx.setGeometry(QtCore.QRect(20, 10, 151, 17))
        self.lbSiglaCbx.setObjectName("lbSiglaCbx")
        self.cbxIndicadores = QtWidgets.QComboBox(self.frConteudo)
        self.cbxIndicadores.setGeometry(QtCore.QRect(20, 30, 181, 25))
        self.cbxIndicadores.setObjectName("cbxIndicadores")
        self.frDescricao = QtWidgets.QFrame(self.frConteudo)
        self.frDescricao.setGeometry(QtCore.QRect(260, 10, 480, 450))
        self.frDescricao.setMinimumSize(QtCore.QSize(480, 450))
        self.frDescricao.setMaximumSize(QtCore.QSize(450, 450))
        self.frDescricao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frDescricao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDescricao.setObjectName("frDescricao")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frDescricao)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbSigla = QtWidgets.QLabel(self.frDescricao)
        self.lbSigla.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbSigla.setObjectName("lbSigla")
        self.verticalLayout_3.addWidget(self.lbSigla)
        self.lbIndicadorDesc = QtWidgets.QLabel(self.frDescricao)
        self.lbIndicadorDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbIndicadorDesc.setWordWrap(True)
        self.lbIndicadorDesc.setObjectName("lbIndicadorDesc")
        self.verticalLayout_3.addWidget(self.lbIndicadorDesc)
        self.verticalLayout_2.addWidget(self.frConteudo)
        self.verticalLayout.addWidget(self.frMain)
        mwInfoIndicadores.setCentralWidget(self.wdgMain)

        self.retranslateUi(mwInfoIndicadores)
        QtCore.QMetaObject.connectSlotsByName(mwInfoIndicadores)

    def retranslateUi(self, mwInfoIndicadores):
        _translate = QtCore.QCoreApplication.translate
        mwInfoIndicadores.setWindowTitle(_translate("mwInfoIndicadores", "MainWindow"))
        self.lbTitulo.setText(_translate("mwInfoIndicadores", "Informações dos indicadores"))
        self.lbSubtitulo.setText(_translate("mwInfoIndicadores", "Encontre todas as informações dos indicadores do CNIS"))
        self.lbSiglaCbx.setText(_translate("mwInfoIndicadores", "Siglas dos indicadores"))
        self.lbSigla.setText(_translate("mwInfoIndicadores", "TextLabel"))
        self.lbIndicadorDesc.setText(_translate("mwInfoIndicadores", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwInfoIndicadores = QtWidgets.QMainWindow()
    ui = Ui_mwInfoIndicadores()
    ui.setupUi(mwInfoIndicadores)
    mwInfoIndicadores.show()
    sys.exit(app.exec_())
