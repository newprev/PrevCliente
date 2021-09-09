# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wdgCabecalhoContribuicao.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgCabecalhoContribuicao(object):
    def setupUi(self, wdgCabecalhoContribuicao):
        wdgCabecalhoContribuicao.setObjectName("wdgCabecalhoContribuicao")
        wdgCabecalhoContribuicao.resize(734, 144)
        wdgCabecalhoContribuicao.setStyleSheet("/*-------------------------------- Labels -----------------------------------------*/\n"
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
"#lbInfoDataInicio, #lbInfoDataFim, #lbInfoSituacao {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"/* --------------------------------- Frames --------------------------------- */\n"
"#frMain {\n"
"    /*background-color: white;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.459, y2:0.511, stop:0 rgba(255, 226, 89, 255), stop:1 rgba(255, 167, 81, 255));\n"
"    border-radius: 8px;\n"
"/*    border: 1px solid grey;*/\n"
"}\n"
"\n"
"#frIcone {\n"
"    background: url(:/remuneracao/remuneracao.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"\n"
"/* --------------------------------- Push Button --------------------------------- */\n"
"#pbCancelar{\n"
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
"#pbCancelar:hover {\n"
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
"#pbConfirmar {\n"
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
"#pbConfirmar:hover {\n"
"    font-family: \"TeX Gyre Adventor\";\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: rgb(60, 60, 60);\n"
"\n"
"    border-radius: 4px;\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    background-color: rgba(255, 255, 255, 120);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgCabecalhoContribuicao)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frMain = QtWidgets.QFrame(wdgCabecalhoContribuicao)
        self.frMain.setMinimumSize(QtCore.QSize(680, 140))
        self.frMain.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frMain.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMain.setObjectName("frMain")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frMain)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frMain)
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
        self.leNomeEmp = QtWidgets.QLineEdit(self.frame_8)
        self.leNomeEmp.setObjectName("leNomeEmp")
        self.horizontalLayout_5.addWidget(self.leNomeEmp)
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
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lbInfoSituacao = QtWidgets.QLabel(self.frame_7)
        self.lbInfoSituacao.setGeometry(QtCore.QRect(10, 10, 64, 17))
        self.lbInfoSituacao.setObjectName("lbInfoSituacao")
        self.leCNPJ = QtWidgets.QLineEdit(self.frame_7)
        self.leCNPJ.setGeometry(QtCore.QRect(10, 30, 171, 25))
        self.leCNPJ.setObjectName("leCNPJ")
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16548798, 16777215))
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
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lbInfoDataFim = QtWidgets.QLabel(self.frame_6)
        self.lbInfoDataFim.setGeometry(QtCore.QRect(10, 10, 64, 17))
        self.lbInfoDataFim.setObjectName("lbInfoDataFim")
        self.dtDataFim = QtWidgets.QDateEdit(self.frame_6)
        self.dtDataFim.setGeometry(QtCore.QRect(10, 30, 110, 26))
        self.dtDataFim.setCalendarPopup(True)
        self.dtDataFim.setObjectName("dtDataFim")
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.frMain)
        self.frame.setMinimumSize(QtCore.QSize(80, 0))
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
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frMain)

        self.retranslateUi(wdgCabecalhoContribuicao)
        QtCore.QMetaObject.connectSlotsByName(wdgCabecalhoContribuicao)

    def retranslateUi(self, wdgCabecalhoContribuicao):
        _translate = QtCore.QCoreApplication.translate
        wdgCabecalhoContribuicao.setWindowTitle(_translate("wdgCabecalhoContribuicao", "Form"))
        self.lbInfoSituacao.setText(_translate("wdgCabecalhoContribuicao", "CNPJ:"))
        self.lbInfoDataInicio.setText(_translate("wdgCabecalhoContribuicao", "Data início:"))
        self.lbInfoDataFim.setText(_translate("wdgCabecalhoContribuicao", "Data fim:"))
        self.pbConfirmar.setText(_translate("wdgCabecalhoContribuicao", "Confirmar"))
        self.pbCancelar.setText(_translate("wdgCabecalhoContribuicao", "Cancelar"))
import Resources.itemResumo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgCabecalhoContribuicao = QtWidgets.QWidget()
    ui = Ui_wdgCabecalhoContribuicao()
    ui.setupUi(wdgCabecalhoContribuicao)
    wdgCabecalhoContribuicao.show()
    sys.exit(app.exec_())