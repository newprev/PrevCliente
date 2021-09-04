from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class NewCheckBox(QCheckBox):
    def __init__(
            self,
            width=60,
            bg_color="#777",
            circle_color="#DDD",
            active_color="#00BCff",
            animation_curve=QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self)

        # Parametrização padrão
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        # Cores
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Animação
        self._circle_position = 3  # Margem inicial (Primeiro parâmetro do "drawEllipse")
        # self.animation = QPropertyAnimation(self, b"circle_position")
        # self.animation.setEasingCurve(animation_curve)
        # self.animation.setDuration(500)

        self.stateChanged.connect(self.startAnimation)

    @property
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def paintEvent(self, evt):

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.width(), self.height())

        # Criando background
        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 22, 22)

        p.end()

    def startAnimation(self, value):
        # self.animation.stop()
        # if value:
        #     self.animation.setEndValue(self.width() - 25)
        # else:
        #     self.animation.setEndValue(3)
        #
        # self.animation.start()

        if value:
            self.circle_position = self.width() - 25
        else:
            # self.animation.setEndValue(3)
            self.circle_position = 3

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)




