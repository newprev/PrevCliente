# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wdgTelefone.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gboxTelefone(object):
    def setupUi(self, gboxTelefone):
        gboxTelefone.setObjectName("gboxTelefone")
        gboxTelefone.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gboxTelefone.sizePolicy().hasHeightForWidth())
        gboxTelefone.setSizePolicy(sizePolicy)
        gboxTelefone.setMinimumSize(QtCore.QSize(400, 200))
        gboxTelefone.setMaximumSize(QtCore.QSize(400, 200))
        gboxTelefone.setStyleSheet("/*---------------------------------------- Frames ----------------------------------------*/\n"
"#frNumero {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: transparent transparent rgb(227, 227, 227) transparent;\n"
"}\n"
"\n"
"#frPessoal{\n"
"    background-image: url(:/pessoal/recado.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#frTipo {\n"
"    background-image: url(:/tipo/celular.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#frMain{\n"
"    border: 2px groove rgb(58, 64, 90);\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"}\n"
"\n"
"/*---------------------------------------- Labels ----------------------------------------*/\n"
"#lbAtivo, #lbPessoal, #lbTipo {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    color: black;\n"
"}\n"
"\n"
"#lbNumero {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"/*---------------------------------------- Group Box ----------------------------------------*/\n"
"QGroupBox {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"    border: 1px solid transparent;\n"
"\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*\n"
"Style no arquivo: heart/dashboard/tabs/localStyleSheet/telefoneWdg.py\n"
"É necessário tirá-lo daqui para ativar e desativar no código\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-position: top left;\n"
"    background-color: #3A405A;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    color: white;\n"
"    padding: 4px 4px 4px 4px;\n"
"    left: 1px;\n"
"    top: 2px;\n"
"}*/")
        gboxTelefone.setFlat(True)
        gboxTelefone.setCheckable(False)
        self.gridLayout = QtWidgets.QGridLayout(gboxTelefone)
        self.gridLayout.setContentsMargins(0, 24, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frMain = QtWidgets.QFrame(gboxTelefone)
        self.frMain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frMain)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frTipo_2 = QtWidgets.QFrame(self.frMain)
        self.frTipo_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTipo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTipo_2.setObjectName("frTipo_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frTipo_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frTipo = QtWidgets.QFrame(self.frTipo_2)
        self.frTipo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTipo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTipo.setObjectName("frTipo")
        self.verticalLayout_2.addWidget(self.frTipo)
        self.lbTipo = QtWidgets.QLabel(self.frTipo_2)
        self.lbTipo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTipo.setObjectName("lbTipo")
        self.verticalLayout_2.addWidget(self.lbTipo)
        self.gridLayout_2.addWidget(self.frTipo_2, 2, 1, 1, 1)
        self.frAtivo = QtWidgets.QFrame(self.frMain)
        self.frAtivo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAtivo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAtivo.setObjectName("frAtivo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frAtivo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbAtivo = QtWidgets.QLabel(self.frAtivo)
        self.lbAtivo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbAtivo.setObjectName("lbAtivo")
        self.horizontalLayout_2.addWidget(self.lbAtivo)
        self.hlAtivo = QtWidgets.QHBoxLayout()
        self.hlAtivo.setObjectName("hlAtivo")
        self.horizontalLayout_2.addLayout(self.hlAtivo)
        self.gridLayout_2.addWidget(self.frAtivo, 0, 1, 1, 1)
        self.frNumero = QtWidgets.QFrame(self.frMain)
        self.frNumero.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frNumero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNumero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNumero.setObjectName("frNumero")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frNumero)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbNumero = QtWidgets.QLabel(self.frNumero)
        self.lbNumero.setScaledContents(False)
        self.lbNumero.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lbNumero.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbNumero.setObjectName("lbNumero")
        self.horizontalLayout.addWidget(self.lbNumero)
        self.gridLayout_2.addWidget(self.frNumero, 0, 0, 1, 1)
        self.frPessoal_2 = QtWidgets.QFrame(self.frMain)
        self.frPessoal_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frPessoal_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPessoal_2.setObjectName("frPessoal_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frPessoal_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frPessoal = QtWidgets.QFrame(self.frPessoal_2)
        self.frPessoal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frPessoal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPessoal.setObjectName("frPessoal")
        self.verticalLayout.addWidget(self.frPessoal)
        self.lbPessoal = QtWidgets.QLabel(self.frPessoal_2)
        self.lbPessoal.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPessoal.setObjectName("lbPessoal")
        self.verticalLayout.addWidget(self.lbPessoal)
        self.gridLayout_2.addWidget(self.frPessoal_2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frMain, 0, 0, 1, 1)

        self.retranslateUi(gboxTelefone)
        QtCore.QMetaObject.connectSlotsByName(gboxTelefone)

    def retranslateUi(self, gboxTelefone):
        _translate = QtCore.QCoreApplication.translate
        gboxTelefone.setWindowTitle(_translate("gboxTelefone", "GroupBox"))
        gboxTelefone.setTitle(_translate("gboxTelefone", "Principal"))
        self.lbTipo.setText(_translate("gboxTelefone", "WahtsApp"))
        self.lbAtivo.setText(_translate("gboxTelefone", "Ativo"))
        self.lbNumero.setText(_translate("gboxTelefone", "(11) 9.9999-9999"))
        self.lbPessoal.setText(_translate("gboxTelefone", "Pessoal / Recado"))
import Resources.wdgTelefone


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gboxTelefone = QtWidgets.QGroupBox()
    ui = Ui_gboxTelefone()
    ui.setupUi(gboxTelefone)
    gboxTelefone.show()
    sys.exit(app.exec_())
