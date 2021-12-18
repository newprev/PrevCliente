import os.path

from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtSvg import QSvgGenerator
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QRect, QSize
from ..DesignSystem.colors import *


class NewMenuButton(QPushButton):
    def __init__(
            self,
            texto: str = '',
            height: int = 40,
            minimumWidth: int = 50,
            textPadding: int = 0,
            textColor: str = NewTextColor.whiteText.value,
            iconPath: str = '',
            iconColor: str = NewColorsWhite.white100.value,
            pbColor: str = NewColorsPrimary.primary.value,
            pbColorHover: str = NewColorsPrimary.p200.value,
            pbColorPressed: str = NewColorsPrimary.p400.value,
            pbChecked: bool = False,
            parent=None
    ):
        super(NewMenuButton, self).__init__(parent=parent)
        self.setText(texto)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        self.minimumWidth = minimumWidth
        self.textPadding = textPadding
        self.textColor = textColor
        self.iconPath = iconPath
        self.iconColor = iconColor
        self.pbColor = pbColor
        self.pbColorHover = pbColorHover
        self.pbColorPressed = pbColorPressed
        self.pbChecked = pbChecked

        self.defineStyleSheet(
            textPadding=self.textPadding,
            textColor=self.textColor,
            pbColor=self.pbColor,
            pbColorHover=self.pbColorHover,
            pbColorPressed=self.pbColorPressed,
            pbChecked=self.pbChecked
        )

    def defineStyleSheet(
            self,
            textPadding: int = 55,
            textColor: str = NewTextColor.whiteText.value,
            pbColor: str = NewColorsPrimary.primary.value,
            pbColorHover: str = NewColorsPrimary.p200.value,
            pbColorPressed: str = NewColorsSuccess.green200.value,
            pbChecked: bool = False,
    ):
        style = f"""
        QPushButton {{
            color: {textColor};
            background-color: {pbColor};
            padding-left: {textPadding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {pbColorHover};
        }}
        QPushButton:pressed {{
            background-color: {pbColorPressed};
        }}
        """

        pressionado = f"""
        QPushButton {{
            background-color: {pbColorHover};
            border-right: 5px solid white;
        }}
"""
        if not pbChecked:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + pressionado)

    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        qpainter = QPainter()
        qpainter.begin(self)
        qpainter.setRenderHint(QPainter.Antialiasing)
        qpainter.setPen(Qt.NoPen)

        rectangle = QRect(0, 0, self.minimumWidth, self.height())
        self.desenhaIcone(qpainter, rectangle, self.iconPath, self.iconColor)
        qpainter.end()

    def desenhaIcone(self, qp: QPainter, rect: QRect, image: str, cor: str):
        rootPath = os.path.join(os.getcwd(), os.path.pardir, os.path.pardir)
        srcPath = 'Resources'
        path = os.path.join(rootPath, srcPath)
        iconPath = os.path.normpath(os.path.join(path, image))
        color = QColor(cor)

        # Renderizando icone
        icon: QPixmap = QPixmap(iconPath)

        icon = icon.scaled(24, 24)

        print(f"{rect.width()=}")
        print(f"{rect.height()=}")

        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        # qp.drawPixmap(
        #     (rect.width() - icon.width()) / 2,
        #     (rect.height() - icon.height()) / 2,
        #     icon
        # )
        qp.drawImage(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
