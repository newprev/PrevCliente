from PyQt5.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout, QGridLayout
from typing import Union


def limpaLayout(layout: Union[QHBoxLayout, QLayout, QVBoxLayout, QGridLayout]):
    for index in reversed(range(layout.count())):
        layout.takeAt(index).widget().setParent(None)
