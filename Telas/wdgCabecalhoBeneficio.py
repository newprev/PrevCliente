# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wdgCabecalhoBeneficio.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgCabecalhoBeneficio(object):
    def setupUi(self, wdgCabecalhoBeneficio):
        wdgCabecalhoBeneficio.setObjectName("wdgCabecalhoBeneficio")
        wdgCabecalhoBeneficio.resize(734, 144)
        wdgCabecalhoBeneficio.setStyleSheet("/*-------------------------------- Labels -----------------------------------------*/\n"
"#lbCdEmp {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 24px;\n"
"    font-weight: 900;\n"
"}\n"
"\n"
"#lbDataInicio, #lbDataFim, #lbSituacao {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#lbInfoDataInicio, #lbInfoDataFim, \n"
"#lbInfoSituacao, #lbInfoNb {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    color: white;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"/* --------------------------------- Frames --------------------------------- */\n"
"#frMain {\n"
"    /*background-color: white;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.761364, x2:0.296122, y2:0.415, stop:0 rgba(58, 171, 140, 255), stop:1 rgba(9, 212, 156, 255));\n"
"    border-radius: 8px;\n"
"/*    border: 1px solid grey;*/\n"
"}\n"
"\n"
"#frIcone {\n"
"    background: url(:/beneficio/beneficio.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"\n"
"/* --------------------------------- Push Button --------------------------------- */\n"
"#pbConfirmar {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#pbConfirmar:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: white;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 2px solid white;\n"
"    background-color: rgba(85, 87, 83, 70);\n"
"}\n"
"\n"
"#pbCancelar {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: rgb(60, 60, 60);\n"
"\n"
"    border-radius: 4px;\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#pbCancelar:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: rgb(60, 60, 60);\n"
"\n"
"    border-radius: 4px;\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    background-color: rgba(255, 255, 255, 120);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgCabecalhoBeneficio)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frMain = QtWidgets.QFrame(wdgCabecalhoBeneficio)
        self.frMain.setMinimumSize(QtCore.QSize(680, 140))
        self.frMain.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frMain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frMain)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frIcone = QtWidgets.QFrame(self.frame_3)
        self.frIcone.setMinimumSize(QtCore.QSize(36, 36))
        self.frIcone.setMaximumSize(QtCore.QSize(40, 40))
        self.frIcone.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frIcone.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frIcone.setObjectName("frIcone")
        self.horizontalLayout_3.addWidget(self.frIcone)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setContentsMargins(16, 0, 16, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cbxNomeBeneficio = QtWidgets.QComboBox(self.frame_8)
        self.cbxNomeBeneficio.setObjectName("cbxNomeBeneficio")
        self.horizontalLayout_5.addWidget(self.cbxNomeBeneficio)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lbInfoNb = QtWidgets.QLabel(self.frame_7)
        self.lbInfoNb.setGeometry(QtCore.QRect(10, 10, 171, 17))
        self.lbInfoNb.setObjectName("lbInfoNb")
        self.leNb = QtWidgets.QLineEdit(self.frame_7)
        self.leNb.setGeometry(QtCore.QRect(10, 30, 171, 25))
        self.leNb.setObjectName("leNb")
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lbInfoDataInicio = QtWidgets.QLabel(self.frame_5)
        self.lbInfoDataInicio.setGeometry(QtCore.QRect(10, 10, 91, 17))
        self.lbInfoDataInicio.setObjectName("lbInfoDataInicio")
        self.dtDataInicio = QtWidgets.QDateEdit(self.frame_5)
        self.dtDataInicio.setGeometry(QtCore.QRect(10, 30, 110, 26))
        self.dtDataInicio.setCalendarPopup(True)
        self.dtDataInicio.setObjectName("dtDataInicio")
        self.lbInfoDataFim = QtWidgets.QLabel(self.frame_5)
        self.lbInfoDataFim.setGeometry(QtCore.QRect(130, 10, 64, 17))
        self.lbInfoDataFim.setObjectName("lbInfoDataFim")
        self.dtDataFim = QtWidgets.QDateEdit(self.frame_5)
        self.dtDataFim.setGeometry(QtCore.QRect(130, 30, 110, 26))
        self.dtDataFim.setCalendarPopup(True)
        self.dtDataFim.setObjectName("dtDataFim")
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lbInfoSituacao = QtWidgets.QLabel(self.frame_6)
        self.lbInfoSituacao.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.lbInfoSituacao.setObjectName("lbInfoSituacao")
        self.cbxSituacao = QtWidgets.QComboBox(self.frame_6)
        self.cbxSituacao.setGeometry(QtCore.QRect(10, 30, 131, 25))
        self.cbxSituacao.setObjectName("cbxSituacao")
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.frMain)
        self.frame.setMinimumSize(QtCore.QSize(90, 0))
        self.frame.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbConfirmar = QtWidgets.QPushButton(self.frame)
        self.pbConfirmar.setMinimumSize(QtCore.QSize(0, 26))
        self.pbConfirmar.setObjectName("pbConfirmar")
        self.verticalLayout.addWidget(self.pbConfirmar)
        self.pbCancelar = QtWidgets.QPushButton(self.frame)
        self.pbCancelar.setMinimumSize(QtCore.QSize(0, 26))
        self.pbCancelar.setObjectName("pbCancelar")
        self.verticalLayout.addWidget(self.pbCancelar)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.frMain)

        self.retranslateUi(wdgCabecalhoBeneficio)
        QtCore.QMetaObject.connectSlotsByName(wdgCabecalhoBeneficio)

    def retranslateUi(self, wdgCabecalhoBeneficio):
        _translate = QtCore.QCoreApplication.translate
        wdgCabecalhoBeneficio.setWindowTitle(_translate("wdgCabecalhoBeneficio", "Form"))
        self.lbInfoNb.setText(_translate("wdgCabecalhoBeneficio", "Número do benefício:"))
        self.lbInfoDataInicio.setText(_translate("wdgCabecalhoBeneficio", "Data início:"))
        self.lbInfoDataFim.setText(_translate("wdgCabecalhoBeneficio", "Data fim:"))
        self.lbInfoSituacao.setText(_translate("wdgCabecalhoBeneficio", "Situação:"))
        self.pbConfirmar.setText(_translate("wdgCabecalhoBeneficio", "Confirmar"))
        self.pbCancelar.setText(_translate("wdgCabecalhoBeneficio", "Cancelar"))
import Resources.itemResumo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgCabecalhoBeneficio = QtWidgets.QWidget()
    ui = Ui_wdgCabecalhoBeneficio()
    ui.setupUi(wdgCabecalhoBeneficio)
    wdgCabecalhoBeneficio.show()
    sys.exit(app.exec_())
