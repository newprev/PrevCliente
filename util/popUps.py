from PyQt5.QtWidgets import QMessageBox
from typing import Callable


def popUpOkAlerta(mensagem, titulo: str = 'Atenção!', erro: str = None, funcao=None):
    pop = QMessageBox()
    pop.setWindowTitle(titulo)
    pop.setText(mensagem)
    pop.setIcon(QMessageBox.Warning)
    pop.setStandardButtons(QMessageBox.Ok)

    if erro is not None:
        pop.setDetailedText(f"{erro=}")

    if funcao is not None:
        x = pop.exec_()
        funcao()
    else:
        x = pop.exec_()


def popUpSimCancela(mensagem, titulo: str = 'Atenção!', funcaoSim: Callable = None, funcaoCancela: Callable = None):
    pop = QMessageBox()
    pop.setWindowTitle(titulo)
    pop.setText(mensagem)
    pop.setIcon(QMessageBox.Warning)
    pop.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
    pop.setDefaultButton(QMessageBox.Cancel)

    x = pop.exec_()
    if x == QMessageBox.Yes:
        funcaoSim()
    elif x == QMessageBox.Cancel:
        if funcaoCancela is not None:
            funcaoCancela()
        return False
    else:
        raise Warning(f'Ocorreu um erro inesperado')
