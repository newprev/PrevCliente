from typing import List


# Parte da solução é do sth [user:56338] - https://stackoverflow.com/questions/3229419/how-to-pretty-print-nested-dictionaries
def prettyPrintDict(dicionario: dict, indent=0):
    if isinstance(dicionario, dict):
        qtdeValores: int = len(dicionario.keys())
    else:
        qtdeValores = 0

    for chave, valor in dicionario.items():
        qtdeValores -= 1
        print('\t' * indent + f"{chave}", end='')
        if isinstance(valor, dict):
            print(': {')
            prettyPrintDict(valor, indent=indent+1)
        elif isinstance(valor, list):
            print('\t' * (indent+1) + str(valor))
        else:
            print(f': {valor}', end='')
            if qtdeValores > 0:
                print(',')
            else:
                print('\n' + '\t' * (indent-1) + '}')

        """
        chave1 : {
            }"""


def divideListaEmPartes(lista: List, qtdElemNaLista: int) -> List:
    continueAdicionando = True
    inicio: int = 0
    fim: int = qtdElemNaLista
    listaFinal: List = []

    if fim <= len(lista):
        listaFinal.append(lista[inicio:fim])
    else:
        listaFinal.append(lista)
        return listaFinal

    while continueAdicionando:
        if fim + qtdElemNaLista < len(lista):
            inicio = fim
            fim += qtdElemNaLista
            listaFinal.append(lista[inicio:fim])
        elif fim == len(lista):
            continueAdicionando = False
        else:
            inicio = fim
            listaFinal.append(lista[inicio:])
            continueAdicionando = False

    return listaFinal


def loading(ligado: bool):
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import Qt

    if ligado:
        QApplication.setOverrideCursor(Qt.WaitCursor)
    else:
        QApplication.restoreOverrideCursor()
