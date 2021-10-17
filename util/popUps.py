from PyQt5.QtWidgets import QMessageBox


def popUpOkAlerta(mensagem, titulo: str = 'Atenção!', erro: str = None):
    pop = QMessageBox()
    pop.setWindowTitle(titulo)
    pop.setText(mensagem)
    pop.setIcon(QMessageBox.Warning)
    pop.setStandardButtons(QMessageBox.Ok)

    if erro is not None:
        pop.setDetailedText(erro)

    x = pop.exec_()


def popUpSimCancela(mensagem, titulo: str = 'Atenção!', funcao=None):
    pop = QMessageBox()
    pop.setWindowTitle(titulo)
    pop.setText(mensagem)
    pop.setIcon(QMessageBox.Warning)
    pop.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
    pop.setDefaultButton(QMessageBox.Cancel)

    x = pop.exec_()
    if x == QMessageBox.Yes:
        funcao()
    elif x == QMessageBox.Cancel:
        return False
    else:
        raise Warning(f'Ocorreu um erro inesperado')