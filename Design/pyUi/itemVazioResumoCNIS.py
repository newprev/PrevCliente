# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/itemVazioResumoCNIS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WdgItemRes(object):
    def setupUi(self, WdgItemRes):
        WdgItemRes.setObjectName("WdgItemRes")
        WdgItemRes.resize(612, 144)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WdgItemRes.sizePolicy().hasHeightForWidth())
        WdgItemRes.setSizePolicy(sizePolicy)
        WdgItemRes.setStyleSheet("/*-------------------------------- Group box -----------------------------------------*/\n"
"#frMain {\n"
"    background-color: #F9F9F9;\n"
"    border-radius: 8px;\n"
"    border: 2px dashed #3F4E8C;\n"
"}\n"
"\n"
"/*-------------------------------- Labels -----------------------------------------*/\n"
"#lbInfoPrincipal {    \n"
"    font: 29 18pt \"Avenir LT Std\";\n"
"\n"
"    color: rgba(63, 78, 140, 150);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(WdgItemRes)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frMain = QtWidgets.QWidget(WdgItemRes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMain.sizePolicy().hasHeightForWidth())
        self.frMain.setSizePolicy(sizePolicy)
        self.frMain.setMinimumSize(QtCore.QSize(0, 140))
        self.frMain.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frMain.setObjectName("frMain")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frMain)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbInfoPrincipal = QtWidgets.QLabel(self.frMain)
        self.lbInfoPrincipal.setObjectName("lbInfoPrincipal")
        self.horizontalLayout_2.addWidget(self.lbInfoPrincipal, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frMain)

        self.retranslateUi(WdgItemRes)
        QtCore.QMetaObject.connectSlotsByName(WdgItemRes)

    def retranslateUi(self, WdgItemRes):
        _translate = QtCore.QCoreApplication.translate
        WdgItemRes.setWindowTitle(_translate("WdgItemRes", "Form"))
        self.lbInfoPrincipal.setText(_translate("WdgItemRes", "Não há vínculos registrados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WdgItemRes = QtWidgets.QWidget()
    ui = Ui_WdgItemRes()
    ui.setupUi(WdgItemRes)
    WdgItemRes.show()
    sys.exit(app.exec_())