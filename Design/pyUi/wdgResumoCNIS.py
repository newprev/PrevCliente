# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/wdgResumoCNIS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgResumoCnis(object):
    def setupUi(self, wdgResumoCnis):
        wdgResumoCnis.setObjectName("wdgResumoCnis")
        wdgResumoCnis.resize(1181, 575)
        wdgResumoCnis.setStyleSheet("#wdgCadastroCliente {\n"
"    background-color: white;\n"
"}\n"
"\n"
"#frCabecalho, #frMiolo, #frRodape {\n"
"    background-color: white;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(wdgResumoCnis)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frPrincipal = QtWidgets.QFrame(wdgResumoCnis)
        self.frPrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frPrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPrincipal.setObjectName("frPrincipal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frPrincipal)
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frCabecalho = QtWidgets.QFrame(self.frPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frCabecalho.sizePolicy().hasHeightForWidth())
        self.frCabecalho.setSizePolicy(sizePolicy)
        self.frCabecalho.setMinimumSize(QtCore.QSize(0, 90))
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frCabecalho.setStyleSheet("/*------------------------------------------- Frame -------------------------------------------*/\n"
"#frFirulaEmpresa, #frFirulaContrib,\n"
"#frFirulaBeneficios {\n"
"    background-color: #3F4E8C;\n"
"    border: 0px solid none;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#frFirulaContrib,\n"
"#frFirulaBeneficios {\n"
"    background-color: white;\n"
"    border: 0px solid none;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"/*------------------------------------------- Push Button -------------------------------------------*/\n"
"#pbVoltar {\n"
"    background-image: url(:/cabecalho/back.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: #F4F5F8;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#pbVoltar:hover {\n"
"    background-image: url(:/voltar/back.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: rgb(228, 233, 248);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#pbEmpresas {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"\n"
"    background-color: transparent;\n"
"    border: 0px solid none;\n"
"\n"
"    margin: 4px;\n"
"}\n"
"\n"
"#pbBeneficios,\n"
"#pbContrib {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: black;\n"
"\n"
"    background-color: transparent;\n"
"    border: 0px solid none;\n"
"\n"
"    margin: 4px;\n"
"}\n"
"\n"
"/*------------------------------------------- Label -------------------------------------------*/\n"
"#lbInfoTitulo {\n"
"    font: 16pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"#lbNomeCliente {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"\n"
"    padding: 4px;\n"
"}\n"
"\n"
"#lbCpfCliente {\n"
"    font: 11pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"\n"
"    padding: 4px;\n"
"}")
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frCabecalho)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frTitulo = QtWidgets.QFrame(self.frCabecalho)
        self.frTitulo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTitulo.setObjectName("frTitulo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frTitulo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbVoltar = QtWidgets.QPushButton(self.frTitulo)
        self.pbVoltar.setMinimumSize(QtCore.QSize(40, 40))
        self.pbVoltar.setMaximumSize(QtCore.QSize(40, 40))
        self.pbVoltar.setText("")
        self.pbVoltar.setObjectName("pbVoltar")
        self.horizontalLayout.addWidget(self.pbVoltar)
        self.lbInfoTitulo = QtWidgets.QLabel(self.frTitulo)
        self.lbInfoTitulo.setObjectName("lbInfoTitulo")
        self.horizontalLayout.addWidget(self.lbInfoTitulo, 0, QtCore.Qt.AlignVCenter)
        self.frInfoPessoal = QtWidgets.QFrame(self.frTitulo)
        self.frInfoPessoal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoPessoal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoPessoal.setObjectName("frInfoPessoal")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frInfoPessoal)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbNomeCliente = QtWidgets.QLabel(self.frInfoPessoal)
        self.lbNomeCliente.setObjectName("lbNomeCliente")
        self.verticalLayout_3.addWidget(self.lbNomeCliente)
        self.lbCpfCliente = QtWidgets.QLabel(self.frInfoPessoal)
        self.lbCpfCliente.setObjectName("lbCpfCliente")
        self.verticalLayout_3.addWidget(self.lbCpfCliente)
        self.horizontalLayout.addWidget(self.frInfoPessoal)
        spacerItem = QtWidgets.QSpacerItem(883, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frBotoes = QtWidgets.QFrame(self.frTitulo)
        self.frBotoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBotoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBotoes.setObjectName("frBotoes")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frBotoes)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frEmpresas = QtWidgets.QFrame(self.frBotoes)
        self.frEmpresas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEmpresas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEmpresas.setObjectName("frEmpresas")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frEmpresas)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pbEmpresas = QtWidgets.QPushButton(self.frEmpresas)
        self.pbEmpresas.setCheckable(True)
        self.pbEmpresas.setChecked(False)
        self.pbEmpresas.setObjectName("pbEmpresas")
        self.verticalLayout_6.addWidget(self.pbEmpresas, 0, QtCore.Qt.AlignBottom)
        self.frFirulaEmpresa = QtWidgets.QFrame(self.frEmpresas)
        self.frFirulaEmpresa.setMinimumSize(QtCore.QSize(0, 4))
        self.frFirulaEmpresa.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frFirulaEmpresa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frFirulaEmpresa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFirulaEmpresa.setObjectName("frFirulaEmpresa")
        self.verticalLayout_6.addWidget(self.frFirulaEmpresa, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frEmpresas)
        self.frContrib = QtWidgets.QFrame(self.frBotoes)
        self.frContrib.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frContrib.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frContrib.setObjectName("frContrib")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frContrib)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pbContrib = QtWidgets.QPushButton(self.frContrib)
        self.pbContrib.setObjectName("pbContrib")
        self.verticalLayout_5.addWidget(self.pbContrib, 0, QtCore.Qt.AlignBottom)
        self.frFirulaContrib = QtWidgets.QFrame(self.frContrib)
        self.frFirulaContrib.setMinimumSize(QtCore.QSize(0, 4))
        self.frFirulaContrib.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frFirulaContrib.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frFirulaContrib.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFirulaContrib.setObjectName("frFirulaContrib")
        self.verticalLayout_5.addWidget(self.frFirulaContrib, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frContrib)
        self.frBeneficios = QtWidgets.QFrame(self.frBotoes)
        self.frBeneficios.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBeneficios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBeneficios.setObjectName("frBeneficios")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frBeneficios)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pbBeneficios = QtWidgets.QPushButton(self.frBeneficios)
        self.pbBeneficios.setObjectName("pbBeneficios")
        self.verticalLayout_4.addWidget(self.pbBeneficios, 0, QtCore.Qt.AlignBottom)
        self.frFirulaBeneficios = QtWidgets.QFrame(self.frBeneficios)
        self.frFirulaBeneficios.setMinimumSize(QtCore.QSize(0, 4))
        self.frFirulaBeneficios.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frFirulaBeneficios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frFirulaBeneficios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFirulaBeneficios.setObjectName("frFirulaBeneficios")
        self.verticalLayout_4.addWidget(self.frFirulaBeneficios, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frBeneficios)
        self.horizontalLayout.addWidget(self.frBotoes)
        self.verticalLayout_2.addWidget(self.frTitulo)
        self.verticalLayout.addWidget(self.frCabecalho)
        self.frMiolo = QtWidgets.QFrame(self.frPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMiolo.sizePolicy().hasHeightForWidth())
        self.frMiolo.setSizePolicy(sizePolicy)
        self.frMiolo.setStyleSheet("/*-------------------------------------------  Stack --------------------------------------------*/\n"
"#stkCliente {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/*-------------------------------------------  Widget --------------------------------------------*/\n"
"#pgEmpresas, #pgContribuicoes, \n"
"#pgBeneficios {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/*-------------------------------------------  Label --------------------------------------------*/\n"
"\n"
"\n"
"/*-------------------------------------------  Frame --------------------------------------------*/\n"
"\n"
"\n"
"/*---------------------------- Push Button ----------------------------------*/\n"
"#pbInserir {\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    \n"
"    border: 2px solid #3F4E8C;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/*----------------------------  Line Edit ---------------------------------------*/\n"
"\n"
"\n"
"/*----------------------- Scroll Area  and  QWidget ------------------------*/\n"
"#scaPrincipal, #wdgScroll {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/*------------------------------ Check Box -------------------------------------*/\n"
"\n"
"\n"
"/*----------------------------- Combo box --------------------------------------*/\n"
"\n"
"\n"
"/*----------------------------- Date Edit --------------------------------------*/\n"
"")
        self.frMiolo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMiolo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMiolo.setObjectName("frMiolo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frMiolo)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stkCliente = QtWidgets.QStackedWidget(self.frMiolo)
        self.stkCliente.setObjectName("stkCliente")
        self.pgEmpresas = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pgEmpresas.sizePolicy().hasHeightForWidth())
        self.pgEmpresas.setSizePolicy(sizePolicy)
        self.pgEmpresas.setObjectName("pgEmpresas")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.pgEmpresas)
        self.gridLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_8.setHorizontalSpacing(32)
        self.gridLayout_8.setVerticalSpacing(16)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame = QtWidgets.QFrame(self.pgEmpresas)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(479, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pbInserir = QtWidgets.QPushButton(self.frame_2)
        self.pbInserir.setMinimumSize(QtCore.QSize(80, 0))
        self.pbInserir.setObjectName("pbInserir")
        self.horizontalLayout_3.addWidget(self.pbInserir)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.scaPrincipal = QtWidgets.QScrollArea(self.frame)
        self.scaPrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scaPrincipal.setWidgetResizable(True)
        self.scaPrincipal.setObjectName("scaPrincipal")
        self.wdgScroll = QtWidgets.QWidget()
        self.wdgScroll.setGeometry(QtCore.QRect(0, 0, 586, 406))
        self.wdgScroll.setObjectName("wdgScroll")
        self.scaPrincipal.setWidget(self.wdgScroll)
        self.gridLayout_4.addWidget(self.scaPrincipal, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 0, 1, 1, 1)
        self.stkCliente.addWidget(self.pgEmpresas)
        self.pgContribuicoes = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pgContribuicoes.sizePolicy().hasHeightForWidth())
        self.pgContribuicoes.setSizePolicy(sizePolicy)
        self.pgContribuicoes.setObjectName("pgContribuicoes")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.pgContribuicoes)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_7.setHorizontalSpacing(32)
        self.gridLayout_7.setVerticalSpacing(16)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stkCliente.addWidget(self.pgContribuicoes)
        self.pgBeneficios = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pgBeneficios.sizePolicy().hasHeightForWidth())
        self.pgBeneficios.setSizePolicy(sizePolicy)
        self.pgBeneficios.setObjectName("pgBeneficios")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pgBeneficios)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_3.setHorizontalSpacing(32)
        self.gridLayout_3.setVerticalSpacing(16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stkCliente.addWidget(self.pgBeneficios)
        self.gridLayout_2.addWidget(self.stkCliente, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frMiolo)
        self.frRodape = QtWidgets.QFrame(self.frPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frRodape.sizePolicy().hasHeightForWidth())
        self.frRodape.setSizePolicy(sizePolicy)
        self.frRodape.setStyleSheet("/*----------------------------------------- Push Button---------------------------------------------*/\n"
"#pbSalvarDados {\n"
"    \n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: white;\n"
"\n"
"    background-color: #3F4E8C;\n"
"    border-radius: 8px;\n"
"\n"
"    padding: 16px;\n"
"}")
        self.frRodape.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frRodape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frRodape.setObjectName("frRodape")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frRodape)
        self.horizontalLayout_5.setContentsMargins(16, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout.addWidget(self.frRodape)
        self.gridLayout.addWidget(self.frPrincipal, 0, 0, 1, 1)

        self.retranslateUi(wdgResumoCnis)
        self.stkCliente.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgResumoCnis)

    def retranslateUi(self, wdgResumoCnis):
        _translate = QtCore.QCoreApplication.translate
        wdgResumoCnis.setWindowTitle(_translate("wdgResumoCnis", "Form"))
        self.lbInfoTitulo.setText(_translate("wdgResumoCnis", "Resumo do CNIS"))
        self.lbNomeCliente.setText(_translate("wdgResumoCnis", "nomeCliente"))
        self.lbCpfCliente.setText(_translate("wdgResumoCnis", "cpfCliente"))
        self.pbEmpresas.setText(_translate("wdgResumoCnis", "Empresas"))
        self.pbContrib.setText(_translate("wdgResumoCnis", "Contribuições"))
        self.pbBeneficios.setText(_translate("wdgResumoCnis", "Benefícios"))
        self.pbInserir.setText(_translate("wdgResumoCnis", "Inserir"))
import wdgResumoCNIS_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgResumoCnis = QtWidgets.QWidget()
    ui = Ui_wdgResumoCnis()
    ui.setupUi(wdgResumoCnis)
    wdgResumoCnis.show()
    sys.exit(app.exec_())
