# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoGuiaEntrevista.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frEtapaEntrevista(object):
    def setupUi(self, frEtapaEntrevista):
        frEtapaEntrevista.setObjectName("frEtapaEntrevista")
        frEtapaEntrevista.resize(400, 50)
        frEtapaEntrevista.setStyleSheet("#frEtapaEntrevista{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frIcone{\n"
"    background-image: url(:/escolha/entrevista-uncheck.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#lbInfo{\n"
"    font-family: \"Ubuntu\";\n"
"    font-size: 12px;\n"
"\n"
"    color: white;\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(frEtapaEntrevista)
        self.horizontalLayout.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frIcone = QtWidgets.QFrame(frEtapaEntrevista)
        self.frIcone.setMinimumSize(QtCore.QSize(24, 24))
        self.frIcone.setMaximumSize(QtCore.QSize(24, 24))
        self.frIcone.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frIcone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frIcone.setObjectName("frIcone")
        self.horizontalLayout.addWidget(self.frIcone)
        self.lbInfo = QtWidgets.QLabel(frEtapaEntrevista)
        self.lbInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo.setObjectName("lbInfo")
        self.horizontalLayout.addWidget(self.lbInfo, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.retranslateUi(frEtapaEntrevista)
        QtCore.QMetaObject.connectSlotsByName(frEtapaEntrevista)

    def retranslateUi(self, frEtapaEntrevista):
        _translate = QtCore.QCoreApplication.translate
        frEtapaEntrevista.setWindowTitle(_translate("frEtapaEntrevista", "Frame"))
        self.lbInfo.setText(_translate("frEtapaEntrevista", "TextLabel"))
import Resources.infoGuiaEntrevista


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frEtapaEntrevista = QtWidgets.QFrame()
    ui = Ui_frEtapaEntrevista()
    ui.setupUi(frEtapaEntrevista)
    frEtapaEntrevista.show()
    sys.exit(app.exec_())
