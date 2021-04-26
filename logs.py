from enum import Enum
from colorama import Fore, init, Back, deinit
import os
from datetime import datetime

from helpers import datetimeToSql


class Prioridade(Enum):
    saidaComun = 200
    saidaImportante = 300
    sync = 400

class TipoEdicao(Enum):
    select = 0
    insert = 1
    delete = 2
    update = 3
    dropTable = 4
    createTable = 5
    erro = 6


def logPrioridade(mensagem: str, tipoEdicao: TipoEdicao = TipoEdicao.select, priodiade: Prioridade = Prioridade.saidaComun):
    init(autoreset=True)
    path = os.path.join(os.getcwd(), 'Daos', 'historicoLogs', f'{datetime.now().date()}-log.txt')

    if tipoEdicao == tipoEdicao.insert or tipoEdicao == TipoEdicao.update:
        corDaFonte = Fore.YELLOW
    elif tipoEdicao == TipoEdicao.delete:
        corDaFonte = Fore.MAGENTA
    elif tipoEdicao == TipoEdicao.createTable or tipoEdicao == TipoEdicao.dropTable:
        corDaFonte = Fore.LIGHTGREEN_EX
    elif tipoEdicao == TipoEdicao.erro:
        corDaFonte = Fore.RED
    else:
        corDaFonte = Fore.CYAN

    if priodiade == Prioridade.saidaComun:
        corDoFundo = Back.RESET
    elif priodiade == Prioridade.saidaImportante:
        corDoFundo = Back.YELLOW
        corDaFonte = Fore.LIGHTWHITE_EX
    elif priodiade == Prioridade.sync:
        corDoFundo = Back.GREEN
        corDaFonte = Fore.LIGHTWHITE_EX

    with open(path, mode='a', encoding='utf-8') as log:
        log.write(datetimeToSql(datetime.now()) + ' -> ' + mensagem + '\n')
        log.flush()

    print(corDaFonte + corDoFundo + mensagem)
    deinit()
