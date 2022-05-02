from PyQt5.QtWidgets import QHBoxLayout, QGridLayout, QVBoxLayout, QListWidget, QListView
from typing import Union


def limpaLayout(layout: Union[QHBoxLayout, QGridLayout, QVBoxLayout,QListWidget, QListView]):
    """
    Solução do eyllanesc (https://stackoverflow.com/users/6622587/eyllanesc), usuário do StackOverflow
    Página da solução: https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
    """

    for i in reversed(range(layout.count())):
        if layout.itemAt(i).widget() is not None:
            layout.itemAt(i).widget().setParent(None)
