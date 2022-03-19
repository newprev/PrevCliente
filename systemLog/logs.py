from colorama import Fore, init, Back, deinit
import os
from datetime import datetime

from util.enums.logEnums import TipoLog
from util.enums.newPrevEnums import *

from util.helpers.helpers import datetimeToSql


def logPrioridade(mensagem: str, tipoEdicao: TipoEdicao = TipoEdicao.select, tipoLog: TipoLog = TipoLog.DataBase, priodiade: Prioridade = Prioridade.saidaComum):
    init(autoreset=True)

    if tipoLog == TipoLog.DataBase:
        path = os.path.join(os.getcwd(), 'systemLog', 'historicoLogs', f'{datetime.now().date()}-DataBaseLog.txt')
    elif tipoLog == TipoLog.Cache:
        path = os.path.join(os.getcwd(), 'systemLog', 'historicoLogs', f'{datetime.now().date()}-CacheLog.txt')
    else:
        path = os.path.join(os.getcwd(), 'systemLog', 'historicoLogs', f'{datetime.now().date()}-RestLog.txt')

    if tipoEdicao == tipoEdicao.insert or tipoEdicao == TipoEdicao.update:
        corDaFonte = Fore.YELLOW
    elif tipoEdicao == TipoEdicao.delete:
        corDaFonte = Fore.MAGENTA
    elif tipoEdicao == TipoEdicao.createTable or tipoEdicao == TipoEdicao.dropTable:
        corDaFonte = Fore.LIGHTGREEN_EX
    elif tipoEdicao == TipoEdicao.api:
        corDaFonte = Fore.BLUE
    elif tipoEdicao == TipoEdicao.cache:
        corDaFonte = Fore.GREEN
    elif tipoEdicao == TipoEdicao.erro:
        corDaFonte = Fore.RED
    else:
        corDaFonte = Fore.CYAN

    if priodiade == Prioridade.saidaComum:
        corDoFundo = Back.RESET
    elif priodiade == Prioridade.saidaImportante:
        corDoFundo = Back.YELLOW
        corDaFonte = Fore.LIGHTWHITE_EX
    elif priodiade == Prioridade.sync:
        corDoFundo = Back.RESET
        corDaFonte = Fore.LIGHTWHITE_EX

    with open(path, mode='a', encoding='utf-8') as log:
        log.write(datetimeToSql(datetime.now()) + ' -> ' + mensagem + '\n')
        log.flush()

    print(corDaFonte + corDoFundo + mensagem)
    deinit()
