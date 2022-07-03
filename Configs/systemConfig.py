from typing import List
import json
import os
from pathlib import Path

from systemLog.logs import NewLogging


# def buscaSystemConfigs(configList: List = []) -> dict:
#     diretorioConfig = os.path.join(os.getcwd(), 'Configs')
#     if '.systemConfig.json' in os.listdir(os.path.join(os.getcwd(), 'Configs')):
#         arquivoPath = os.path.join(diretorioConfig, '.systemConfig.json')
#         with open(arquivoPath, encoding='utf-8', mode='r') as configs:
#             configsJson: dict = json.load(configs)
#             if len(configList) != 0:
#                 for chave in configsJson.keys():
#                     if chave not in configList:
#                         del configsJson[chave]
#
#             return configsJson


def pathPadraoDocsGerados() -> str:
    try:
        pathPadrao: Path = Path() / 'DocGerados'
        if not pathPadrao.exists():
            pathPadrao.mkdir()
            return str(pathPadrao.absolute())

        elif pathPadrao.exists() and pathPadrao.is_dir():
            return str(pathPadrao.absolute())
    except Exception as err:
        apiLogger = NewLogging().buscaLogger()
        apiLogger.error('Não foi possível encontrar o diretório padrão DecsGerados', extra={'err': err})
        print(f'Não foi possível encontrar o diretório padrão DecsGerados - {err=}')
        return ''
