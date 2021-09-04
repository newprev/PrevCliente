import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from newCheckBox import NewCheckBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.resize(500, 500)

        self.container = QFrame()
        self.container.setObjectName('container')
        self.container.setStyleSheet('#container { background-color: #222 }')
        self.layout = QVBoxLayout()

        self.toggle = NewCheckBox()
        self.layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


