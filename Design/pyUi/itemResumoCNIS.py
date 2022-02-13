# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/itemResumoCNIS.ui'
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
"#gbMain {\n"
"    background-color: #F9F9F9;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #3F4E8C;\n"
"}\n"
"\n"
"#gbMain::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"#gbMain::indicator:unchecked {\n"
"    image: url(:/selecionado/CheckBoxFalse.png);\n"
"}\n"
"\n"
"#gbMain::indicator:checked {\n"
"    image: url(:/selecionado/checkBoxTrue.png);\n"
"}\n"
"\n"
"/*-------------------------------- Labels -----------------------------------------*/\n"
"#lbCdEmp {\n"
"    font: 16pt \"Avenir LT Std\";\n"
"    font-weight: 750;\n"
"\n"
"    color: #3F4E8C;\n"
"}\n"
"\n"
"#lbCNPJouNB {\n"
"    font: 11pt \"Avenir LT Std\";\n"
"    line-height: 16px;\n"
"    color: #3F4E8C;\n"
"}\n"
"\n"
"#lbInfoDataInicio, \n"
"#lbInfoDataFim, #lbInfoSituacao,\n"
"#lbDataInicio, #lbDataFim, \n"
"#lbSituacao {\n"
"    font: 11pt \"Avenir LT Std\";\n"
"    line-height: 16px;\n"
"    color: #3F4E8C;\n"
"}\n"
"\n"
"#lbInfoFalta {\n"
"    font: 10pt \"Avenir LT Std\";\n"
"    line-height: 16px;\n"
"    color: #3F4E8C;\n"
"}\n"
"\n"
"/* --------------------------------- Frames --------------------------------- */\n"
"#frInfoTag {\n"
"    background-image: url(:/opcoes/information-blue-16.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"\n"
"    background-color: transparent;\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"/* --------------------------------- Push Button --------------------------------- */\n"
"#pbEditar {\n"
"    background-image: url(:/opcoes/blueEditar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"\n"
"    background-color: transparent;\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"#pbRemover {\n"
"    background-image: url(:/opcoes/redDeletar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"\n"
"    background-color: transparent;\n"
"    border: 0px solid none;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(WdgItemRes)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gbMain = QtWidgets.QWidget(WdgItemRes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbMain.sizePolicy().hasHeightForWidth())
        self.gbMain.setSizePolicy(sizePolicy)
        self.gbMain.setMinimumSize(QtCore.QSize(0, 140))
        self.gbMain.setMaximumSize(QtCore.QSize(16777215, 13215644))
        self.gbMain.setObjectName("gbMain")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gbMain)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(12, 12, 0, 0)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbCdEmp = QtWidgets.QLabel(self.frame_3)
        self.lbCdEmp.setMinimumSize(QtCore.QSize(0, 0))
        self.lbCdEmp.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lbCdEmp.setWordWrap(True)
        self.lbCdEmp.setObjectName("lbCdEmp")
        self.verticalLayout_3.addWidget(self.lbCdEmp)
        self.lbCNPJouNB = QtWidgets.QLabel(self.frame_3)
        self.lbCNPJouNB.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbCNPJouNB.setObjectName("lbCNPJouNB")
        self.verticalLayout_3.addWidget(self.lbCNPJouNB)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
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
        self.gridLayout = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.lbInfoDataInicio = QtWidgets.QLabel(self.frame_7)
        self.lbInfoDataInicio.setObjectName("lbInfoDataInicio")
        self.gridLayout.addWidget(self.lbInfoDataInicio, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbDataInicio = QtWidgets.QLabel(self.frame_7)
        self.lbDataInicio.setObjectName("lbDataInicio")
        self.gridLayout.addWidget(self.lbDataInicio, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16548798, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbInfoDataFim = QtWidgets.QLabel(self.frame_5)
        self.lbInfoDataFim.setObjectName("lbInfoDataFim")
        self.gridLayout_2.addWidget(self.lbInfoDataFim, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbDataFim = QtWidgets.QLabel(self.frame_5)
        self.lbDataFim.setObjectName("lbDataFim")
        self.gridLayout_2.addWidget(self.lbDataFim, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbInfoSituacao = QtWidgets.QLabel(self.frame_6)
        self.lbInfoSituacao.setObjectName("lbInfoSituacao")
        self.gridLayout_3.addWidget(self.lbInfoSituacao, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbSituacao = QtWidgets.QLabel(self.frame_6)
        self.lbSituacao.setObjectName("lbSituacao")
        self.gridLayout_3.addWidget(self.lbSituacao, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frOpcoes = QtWidgets.QFrame(self.gbMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frOpcoes.sizePolicy().hasHeightForWidth())
        self.frOpcoes.setSizePolicy(sizePolicy)
        self.frOpcoes.setMinimumSize(QtCore.QSize(120, 0))
        self.frOpcoes.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frOpcoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frOpcoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frOpcoes.setObjectName("frOpcoes")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frOpcoes)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.frOpcoes)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 24)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbRemover = QtWidgets.QPushButton(self.frame)
        self.pbRemover.setMinimumSize(QtCore.QSize(40, 40))
        self.pbRemover.setMaximumSize(QtCore.QSize(40, 40))
        self.pbRemover.setText("")
        self.pbRemover.setObjectName("pbRemover")
        self.horizontalLayout_3.addWidget(self.pbRemover)
        self.pbEditar = QtWidgets.QPushButton(self.frame)
        self.pbEditar.setMinimumSize(QtCore.QSize(40, 40))
        self.pbEditar.setMaximumSize(QtCore.QSize(40, 40))
        self.pbEditar.setText("")
        self.pbEditar.setObjectName("pbEditar")
        self.horizontalLayout_3.addWidget(self.pbEditar)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.frDadoFaltante = QtWidgets.QFrame(self.frOpcoes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frDadoFaltante.sizePolicy().hasHeightForWidth())
        self.frDadoFaltante.setSizePolicy(sizePolicy)
        self.frDadoFaltante.setMinimumSize(QtCore.QSize(120, 24))
        self.frDadoFaltante.setMaximumSize(QtCore.QSize(16777215, 24))
        self.frDadoFaltante.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frDadoFaltante.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDadoFaltante.setObjectName("frDadoFaltante")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frDadoFaltante)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbInfoFalta = QtWidgets.QLabel(self.frDadoFaltante)
        self.lbInfoFalta.setObjectName("lbInfoFalta")
        self.horizontalLayout_6.addWidget(self.lbInfoFalta, 0, QtCore.Qt.AlignVCenter)
        self.frInfoTag = QtWidgets.QFrame(self.frDadoFaltante)
        self.frInfoTag.setMinimumSize(QtCore.QSize(24, 24))
        self.frInfoTag.setMaximumSize(QtCore.QSize(24, 24))
        self.frInfoTag.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoTag.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoTag.setObjectName("frInfoTag")
        self.horizontalLayout_6.addWidget(self.frInfoTag)
        self.gridLayout_4.addWidget(self.frDadoFaltante, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frOpcoes)
        self.horizontalLayout.addWidget(self.gbMain)

        self.retranslateUi(WdgItemRes)
        QtCore.QMetaObject.connectSlotsByName(WdgItemRes)

    def retranslateUi(self, WdgItemRes):
        _translate = QtCore.QCoreApplication.translate
        WdgItemRes.setWindowTitle(_translate("WdgItemRes", "Form"))
        self.lbCdEmp.setText(_translate("WdgItemRes", "DROGARIA COMERCIAL LTDA"))
        self.lbCNPJouNB.setText(_translate("WdgItemRes", "CNPJ: 45.652.000-1/32"))
        self.lbInfoDataInicio.setText(_translate("WdgItemRes", "Data início:"))
        self.lbDataInicio.setText(_translate("WdgItemRes", "TextLabel"))
        self.lbInfoDataFim.setText(_translate("WdgItemRes", "Data fim:"))
        self.lbDataFim.setText(_translate("WdgItemRes", "TextLabel"))
        self.lbInfoSituacao.setText(_translate("WdgItemRes", "Situação:"))
        self.lbSituacao.setText(_translate("WdgItemRes", "Situação:"))
        self.lbInfoFalta.setText(_translate("WdgItemRes", "Dado faltante"))
import Resources.itemResumoCNIS


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WdgItemRes = QtWidgets.QWidget()
    ui = Ui_WdgItemRes()
    ui.setupUi(WdgItemRes)
    WdgItemRes.show()
    sys.exit(app.exec_())
