# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/UI/newListaClientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgListaClientes(object):
    def setupUi(self, wdgListaClientes):
        wdgListaClientes.setObjectName("wdgListaClientes")
        wdgListaClientes.resize(1254, 508)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdgListaClientes.sizePolicy().hasHeightForWidth())
        wdgListaClientes.setSizePolicy(sizePolicy)
        wdgListaClientes.setStyleSheet("/*#wdgListaClientes {\n"
"    background-color: white;\n"
"}*/")
        self.gridLayout = QtWidgets.QGridLayout(wdgListaClientes)
        self.gridLayout.setContentsMargins(0, 8, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frPrincipal = QtWidgets.QFrame(wdgListaClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frPrincipal.sizePolicy().hasHeightForWidth())
        self.frPrincipal.setSizePolicy(sizePolicy)
        self.frPrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frPrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPrincipal.setObjectName("frPrincipal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frPrincipal)
        self.verticalLayout.setContentsMargins(24, 0, 24, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frCabecalhoLista = QtWidgets.QFrame(self.frPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frCabecalhoLista.sizePolicy().hasHeightForWidth())
        self.frCabecalhoLista.setSizePolicy(sizePolicy)
        self.frCabecalhoLista.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frCabecalhoLista.setStyleSheet("/*------------------------------------------ Frames ------------------------------------------*/\n"
"#frBusca {\n"
"    background-color: rgb(244, 244, 244);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#frCabecalhoLista {\n"
"    background-color: white;\n"
"}\n"
"\n"
"#frInfoIconeBusca {\n"
"    background-image: url(:/cabecalho/checkSuccess.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: transparent;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/*------------------------------------------ Line Edit ------------------------------------------*/\n"
"#leBusca {\n"
"    border: 0px solid gray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: rgb(244, 244, 244);\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"/*------------------------------------------ Push Buttons ------------------------------------------*/\n"
"#pbNovoCliente {\n"
"    background-color: #3F4E8C;\n"
"    border-radius: 8px;\n"
"\n"
"    font: 14pt \"Avenir LT Std\";\n"
"    color: white;\n"
"    \n"
"    padding: 8px;\n"
"}\n"
"\n"
"#pbCalculadora {\n"
"    background-color: white;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #3F4E8C;\n"
"\n"
"    font: 12pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"    \n"
"    padding: 8px;\n"
"}\n"
"\n"
"#pbFiltro {\n"
"    background-image: url(:/cabecalho/filtros.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: rgb(239, 239, 239);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#pbBusca {\n"
"    background-image: url(:/cabecalho/busca.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    background-color: rgb(244, 244, 244);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"/*------------------------------------------ Labels ------------------------------------------*/\n"
"#lbInfoCliente {\n"
"    font: 18pt \"Avenir LT Std\";\n"
"    color: #3F4E8C;\n"
"    font-weight: 750;\n"
"}\n"
"\n"
"#lbInfoBusca {\n"
"    font: 10pt \"Avenir LT Std\";\n"
"    color: #6F757B;\n"
"}")
        self.frCabecalhoLista.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCabecalhoLista.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalhoLista.setObjectName("frCabecalhoLista")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frCabecalhoLista)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frCabecalhoLista)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbInfoCliente = QtWidgets.QLabel(self.frame_2)
        self.lbInfoCliente.setObjectName("lbInfoCliente")
        self.horizontalLayout_4.addWidget(self.lbInfoCliente, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frAreaBusca = QtWidgets.QFrame(self.frCabecalhoLista)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frAreaBusca.sizePolicy().hasHeightForWidth())
        self.frAreaBusca.setSizePolicy(sizePolicy)
        self.frAreaBusca.setMinimumSize(QtCore.QSize(250, 0))
        self.frAreaBusca.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAreaBusca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAreaBusca.setObjectName("frAreaBusca")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frAreaBusca)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frBusca = QtWidgets.QFrame(self.frAreaBusca)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frBusca.sizePolicy().hasHeightForWidth())
        self.frBusca.setSizePolicy(sizePolicy)
        self.frBusca.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBusca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBusca.setObjectName("frBusca")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frBusca)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leBusca = QtWidgets.QLineEdit(self.frBusca)
        self.leBusca.setObjectName("leBusca")
        self.horizontalLayout_2.addWidget(self.leBusca)
        self.pbBusca = QtWidgets.QPushButton(self.frBusca)
        self.pbBusca.setMinimumSize(QtCore.QSize(24, 24))
        self.pbBusca.setMaximumSize(QtCore.QSize(24, 24))
        self.pbBusca.setText("")
        self.pbBusca.setObjectName("pbBusca")
        self.horizontalLayout_2.addWidget(self.pbBusca)
        self.gridLayout_2.addWidget(self.frBusca, 0, 0, 1, 2, QtCore.Qt.AlignVCenter)
        self.frInfoCliEncontrados = QtWidgets.QFrame(self.frAreaBusca)
        self.frInfoCliEncontrados.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoCliEncontrados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoCliEncontrados.setObjectName("frInfoCliEncontrados")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frInfoCliEncontrados)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frInfoIconeBusca = QtWidgets.QFrame(self.frInfoCliEncontrados)
        self.frInfoIconeBusca.setMinimumSize(QtCore.QSize(24, 24))
        self.frInfoIconeBusca.setMaximumSize(QtCore.QSize(24, 24))
        self.frInfoIconeBusca.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInfoIconeBusca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoIconeBusca.setObjectName("frInfoIconeBusca")
        self.horizontalLayout_5.addWidget(self.frInfoIconeBusca)
        self.lbInfoBusca = QtWidgets.QLabel(self.frInfoCliEncontrados)
        self.lbInfoBusca.setObjectName("lbInfoBusca")
        self.horizontalLayout_5.addWidget(self.lbInfoBusca)
        self.gridLayout_2.addWidget(self.frInfoCliEncontrados, 1, 0, 1, 2, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frAreaBusca)
        self.frame = QtWidgets.QFrame(self.frCabecalhoLista)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbFiltro = QtWidgets.QPushButton(self.frame)
        self.pbFiltro.setMinimumSize(QtCore.QSize(32, 32))
        self.pbFiltro.setMaximumSize(QtCore.QSize(32, 32))
        self.pbFiltro.setText("")
        self.pbFiltro.setObjectName("pbFiltro")
        self.horizontalLayout_3.addWidget(self.pbFiltro, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_5 = QtWidgets.QFrame(self.frCabecalhoLista)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(16)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pbCalculadora = QtWidgets.QPushButton(self.frame_5)
        self.pbCalculadora.setMinimumSize(QtCore.QSize(165, 40))
        self.pbCalculadora.setObjectName("pbCalculadora")
        self.horizontalLayout_10.addWidget(self.pbCalculadora)
        self.pbNovoCliente = QtWidgets.QPushButton(self.frame_5)
        self.pbNovoCliente.setMinimumSize(QtCore.QSize(165, 40))
        self.pbNovoCliente.setObjectName("pbNovoCliente")
        self.horizontalLayout_10.addWidget(self.pbNovoCliente)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frCabecalhoLista, 0, QtCore.Qt.AlignTop)
        self.frMiddle = QtWidgets.QFrame(self.frPrincipal)
        self.frMiddle.setStyleSheet("/*----------------------------------- Frame ---------------------------------------*/\n"
"#frColorArquivado {\n"
"    background-color: #FF345E;\n"
"    border-radius: 4px;\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"#frColorAtivo {\n"
"    background-color: #23E386;\n"
"    border-radius: 4px;\n"
"    border: 0px solid none;\n"
"}\n"
"\n"
"/*----------------------------------- Label ---------------------------------------*/\n"
"#lbAtivos, #lbArquivados {\n"
"    font: 10pt \"Avenir LT Std\";\n"
"    color: black;\n"
"}")
        self.frMiddle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMiddle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMiddle.setObjectName("frMiddle")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frMiddle)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.frame_3 = QtWidgets.QFrame(self.frMiddle)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frColorAtivo = QtWidgets.QFrame(self.frame_3)
        self.frColorAtivo.setMinimumSize(QtCore.QSize(8, 8))
        self.frColorAtivo.setMaximumSize(QtCore.QSize(8, 8))
        self.frColorAtivo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frColorAtivo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frColorAtivo.setObjectName("frColorAtivo")
        self.horizontalLayout_8.addWidget(self.frColorAtivo, 0, QtCore.Qt.AlignVCenter)
        self.lbAtivos = QtWidgets.QLabel(self.frame_3)
        self.lbAtivos.setObjectName("lbAtivos")
        self.horizontalLayout_8.addWidget(self.lbAtivos, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frMiddle)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frColorArquivado = QtWidgets.QFrame(self.frame_4)
        self.frColorArquivado.setMinimumSize(QtCore.QSize(8, 8))
        self.frColorArquivado.setMaximumSize(QtCore.QSize(8, 8))
        self.frColorArquivado.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frColorArquivado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frColorArquivado.setObjectName("frColorArquivado")
        self.horizontalLayout_9.addWidget(self.frColorArquivado, 0, QtCore.Qt.AlignVCenter)
        self.lbArquivados = QtWidgets.QLabel(self.frame_4)
        self.lbArquivados.setObjectName("lbArquivados")
        self.horizontalLayout_9.addWidget(self.lbArquivados)
        self.horizontalLayout_7.addWidget(self.frame_4)
        spacerItem2 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frMiddle, 0, QtCore.Qt.AlignTop)
        self.frTabela = QtWidgets.QFrame(self.frPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frTabela.sizePolicy().hasHeightForWidth())
        self.frTabela.setSizePolicy(sizePolicy)
        self.frTabela.setStyleSheet("/*------------------------------------------- Table Widget -------------------------------------------*/\n"
"#tblClientes {\n"
"    selection-background-color: #F9F9F9;\n"
"    selection-color: grey;\n"
"    gridline-color: white;\n"
"\n"
"    border: 0px solid transparent;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: white;\n"
"    padding-left: 4px;\n"
"    border: 0px solid white;\n"
"    min-height: 45px;\n"
"}\n"
"\n"
"#tblClientes::item:last {\n"
"    selection-background-color: black;\n"
"    selection-color: grey;\n"
"    gridline-color: black;\n"
"    border: 0px solid transparent;\n"
"}\n"
"\n"
"#tblClientes::item {\n"
"    padding: 2px 24px 2px 24px;\n"
"}")
        self.frTabela.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTabela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTabela.setObjectName("frTabela")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frTabela)
        self.horizontalLayout_6.setContentsMargins(36, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tblClientes = QtWidgets.QTableWidget(self.frTabela)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblClientes.sizePolicy().hasHeightForWidth())
        self.tblClientes.setSizePolicy(sizePolicy)
        self.tblClientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblClientes.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblClientes.setProperty("showDropIndicator", False)
        self.tblClientes.setDragDropOverwriteMode(False)
        self.tblClientes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblClientes.setShowGrid(False)
        self.tblClientes.setGridStyle(QtCore.Qt.NoPen)
        self.tblClientes.setCornerButtonEnabled(True)
        self.tblClientes.setObjectName("tblClientes")
        self.tblClientes.setColumnCount(9)
        self.tblClientes.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/status/green-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tblClientes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Avenir LT Std")
        font.setPointSize(11)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Avenir LT Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(63, 78, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Avenir LT Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(63, 78, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Avenir LT Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(63, 78, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Avenir LT Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(63, 78, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblClientes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Avenir LT Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(63, 78, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblClientes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tblClientes.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(0, 7, item)
        self.tblClientes.horizontalHeader().setCascadingSectionResizes(True)
        self.tblClientes.horizontalHeader().setMinimumSectionSize(70)
        self.tblClientes.horizontalHeader().setSortIndicatorShown(False)
        self.tblClientes.horizontalHeader().setStretchLastSection(False)
        self.tblClientes.verticalHeader().setVisible(False)
        self.tblClientes.verticalHeader().setHighlightSections(False)
        self.tblClientes.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_6.addWidget(self.tblClientes, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frTabela, 0, QtCore.Qt.AlignTop)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frPrincipal, 0, 0, 1, 1)

        self.retranslateUi(wdgListaClientes)
        QtCore.QMetaObject.connectSlotsByName(wdgListaClientes)

    def retranslateUi(self, wdgListaClientes):
        _translate = QtCore.QCoreApplication.translate
        wdgListaClientes.setWindowTitle(_translate("wdgListaClientes", "Form"))
        self.lbInfoCliente.setText(_translate("wdgListaClientes", "Clientes"))
        self.leBusca.setPlaceholderText(_translate("wdgListaClientes", "Pesquise por cliente ou processo"))
        self.lbInfoBusca.setText(_translate("wdgListaClientes", "6 clientes encontrados"))
        self.pbCalculadora.setText(_translate("wdgListaClientes", "Calculadora rápida"))
        self.pbNovoCliente.setText(_translate("wdgListaClientes", "Novo cliente"))
        self.lbAtivos.setText(_translate("wdgListaClientes", "Ativos"))
        self.lbArquivados.setText(_translate("wdgListaClientes", "Arquivados"))
        self.tblClientes.setSortingEnabled(True)
        item = self.tblClientes.verticalHeaderItem(0)
        item.setText(_translate("wdgListaClientes", "Teste"))
        item = self.tblClientes.horizontalHeaderItem(0)
        item.setText(_translate("wdgListaClientes", "clienteId"))
        item = self.tblClientes.horizontalHeaderItem(2)
        item.setText(_translate("wdgListaClientes", "Nome"))
        item = self.tblClientes.horizontalHeaderItem(3)
        item.setText(_translate("wdgListaClientes", "E-mail"))
        item = self.tblClientes.horizontalHeaderItem(4)
        item.setText(_translate("wdgListaClientes", "Contato"))
        item = self.tblClientes.horizontalHeaderItem(5)
        item.setText(_translate("wdgListaClientes", "Cidade"))
        item = self.tblClientes.horizontalHeaderItem(6)
        item.setText(_translate("wdgListaClientes", "Documentos"))
        item = self.tblClientes.horizontalHeaderItem(8)
        item.setText(_translate("wdgListaClientes", "arquivado"))
        __sortingEnabled = self.tblClientes.isSortingEnabled()
        self.tblClientes.setSortingEnabled(False)
        item = self.tblClientes.item(0, 0)
        item.setText(_translate("wdgListaClientes", "1"))
        item = self.tblClientes.item(0, 2)
        item.setText(_translate("wdgListaClientes", "Israel"))
        item = self.tblClientes.item(0, 3)
        item.setText(_translate("wdgListaClientes", "israel.gomes@gmail.com"))
        item = self.tblClientes.item(0, 4)
        item.setText(_translate("wdgListaClientes", "(11) 9.7275-7721"))
        item = self.tblClientes.item(0, 5)
        item.setText(_translate("wdgListaClientes", "São Paulo - SP"))
        item = self.tblClientes.item(0, 6)
        item.setText(_translate("wdgListaClientes", "4/5"))
        item = self.tblClientes.item(0, 7)
        item.setText(_translate("wdgListaClientes", ":"))
        self.tblClientes.setSortingEnabled(__sortingEnabled)
import Resources.newListaClientes


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgListaClientes = QtWidgets.QWidget()
    ui = Ui_wdgListaClientes()
    ui.setupUi(wdgListaClientes)
    wdgListaClientes.show()
    sys.exit(app.exec_())
