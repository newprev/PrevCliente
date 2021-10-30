from typing import List
import json
import os


def buscaSystemConfigs(configList: List = []) -> dict:
    diretorioConfig = os.path.join(os.getcwd(), 'Configs')
    if '.systemConfig.json' in os.listdir(os.path.join(os.getcwd(), 'Configs')):
        arquivoPath = os.path.join(diretorioConfig, '.systemConfig.json')
        with open(arquivoPath, encoding='utf-8', mode='r') as configs:
            configsJson: dict = json.load(configs)
            if len(configList) != 0:
                for chave in configsJson.keys():
                    if chave not in configList:
                        del configsJson[chave]

            return configsJson