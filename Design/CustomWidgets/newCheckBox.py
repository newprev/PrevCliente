from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class NewCheckBox(QCheckBox):
    def __init__(
            self,
            width=60,
            bg_color="#777",
            circle_color="#DDD",
            active_color="#048BA8",
            animation_curve=QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self)

        # Parametrização padrão
        self.setFixedSize(width, width/2)
        self.setCursor(Qt.PointingHandCursor)
        self.widthCircle = 2 * self.height() / 3
        self.heightCircle = 6 * self.height() / 10
        self.posYCircle = self.height()/2 - self.heightCircle/2


        # Cores
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Animação
        self._circle_position = self.height()/4  # Margem inicial (Primeiro parâmetro do "drawEllipse")
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
            p.drawEllipse(self._circle_position, self.posYCircle, self.widthCircle, self.heightCircle)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, self.posYCircle, self.widthCircle, self.heightCircle)

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
            self.circle_position = self.width() - (self.height()/4 + 0.9*self.widthCircle)
        else:
            # self.animation.setEndValue(3)
            self.circle_position = self.height()/4

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)




