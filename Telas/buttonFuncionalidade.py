# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buttonFuncionalidade.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgFuncionalidade(object):
    def setupUi(self, wdgFuncionalidade):
        wdgFuncionalidade.setObjectName("wdgFuncionalidade")
        wdgFuncionalidade.resize(252, 252)
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgFuncionalidade)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbFuncionalidade = QtWidgets.QPushButton(wdgFuncionalidade)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbFuncionalidade.sizePolicy().hasHeightForWidth())
        self.pbFuncionalidade.setSizePolicy(sizePolicy)
        self.pbFuncionalidade.setMinimumSize(QtCore.QSize(100, 100))
        self.pbFuncionalidade.setMaximumSize(QtCore.QSize(100, 100))
        self.pbFuncionalidade.setStyleSheet("#pbFuncionalidade {\n"
"    font-family: \"Fira Sans\";\n"
"    color: white;\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.481102, y1:0.688, x2:0.477, y2:0, stop:0 rgba(41, 128, 185, 255), stop:1 rgba(66, 147, 215, 255));\n"
"    border-radius: 10px;\n"
"    background-image: url(:/cliente/customer.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: top;\n"
"    text-align: bottom center;\n"
"    padding: 4px 0px 4px 0px;\n"
"}")
        self.pbFuncionalidade.setFlat(True)
        self.pbFuncionalidade.setObjectName("pbFuncionalidade")
        self.horizontalLayout.addWidget(self.pbFuncionalidade, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.retranslateUi(wdgFuncionalidade)
        QtCore.QMetaObject.connectSlotsByName(wdgFuncionalidade)

    def retranslateUi(self, wdgFuncionalidade):
        _translate = QtCore.QCoreApplication.translate
        wdgFuncionalidade.setWindowTitle(_translate("wdgFuncionalidade", "Form"))
        self.pbFuncionalidade.setText(_translate("wdgFuncionalidade", "Funcionalidade"))
import Resources.dashboardButton


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgFuncionalidade = QtWidgets.QWidget()
    ui = Ui_wdgFuncionalidade()
    ui.setupUi(wdgFuncionalidade)
    wdgFuncionalidade.show()
    sys.exit(app.exec_())
