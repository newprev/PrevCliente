from enum import Enum
from colorama import Fore, init, Back, deinit

class Prioridade(Enum):
    saidaComun = 200
    saidaImportante = 300

class TipoEdicao(Enum):
    select = 0
    insert = 1
    delete = 2
    update = 3
    dropTable = 4
    createTable = 5


def logPrioridade(mensagem: str, tipoEdicao: TipoEdicao = TipoEdicao.select, priodiade: Prioridade = Prioridade.saidaComun):
    init(autoreset=True)

    if tipoEdicao == tipoEdicao.insert or tipoEdicao == TipoEdicao.update:
        corDaFonte = Fore.YELLOW
    elif tipoEdicao == TipoEdicao.delete:
        corDaFonte = Fore.MAGENTA
    elif tipoEdicao == TipoEdicao.createTable or tipoEdicao == TipoEdicao.dropTable:
        corDaFonte = Fore.LIGHTGREEN_EX
    else:
        corDaFonte = Fore.CYAN

    if priodiade == Prioridade.saidaComun:
        corDoFundo = Back.RESET
    elif priodiade == Prioridade.saidaImportante:
        corDoFundo = Back.YELLOW
        corDaFonte = Fore.LIGHTWHITE_EX

    print(corDaFonte + corDoFundo + mensagem)
    deinit()
