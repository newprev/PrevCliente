import json
import logging.config
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk import set_user
import os
from logging import *

from datetime import datetime

from modelos.advogadoORM import Advogados
from util.enums.logEnums import NomeLogger


class NewLogging:
    logConectado: bool = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NewLogging, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.logApi: Logger = getLogger(NomeLogger.apiLogger.value)

        if not self.logConectado:
            self.iniciaConfiguracao()
            self.conectarComSentry()

    def iniciaConfiguracao(self):
        # Handler Root
        if logging.root.hasHandlers():
            logging.root.handlers.clear()
        stdoutFormatter: Formatter = Formatter("[%(asctime)s] %(levelname)s <%(module)s> --> %(message)s")
        stdoutHandler = StreamHandler()
        stdoutHandler.setFormatter(stdoutFormatter)
        logging.root.setLevel(WARNING)
        logging.root.addHandler(stdoutHandler)

        # Handler API
        apiFormatter: Formatter = Formatter("[%(asctime)s] %(levelname)s <%(module)s> --> %(message)s")
        apiLogPath: str = os.path.join(os.curdir, 'systemLog', 'historicoLogs', f'{datetime.now().date()}_API.txt')
        apiHandler = FileHandler(apiLogPath, 'a')
        apiHandler.setFormatter(apiFormatter)
        if self.logApi.hasHandlers():
            self.logApi.handlers.clear()
        self.logApi.setLevel(INFO)
        self.logApi.addHandler(apiHandler)

    def buscaLogger(self) -> Logger:
        return self.logApi

    def conectarComSentry(self):
        sentryIntegration = LoggingIntegration(
            level=INFO,
            event_level=INFO
        )
        pathConfig = os.path.join(os.getcwd(), 'systemLog', 'logConfig.json')

        with open(pathConfig, encoding='utf-8', mode='r') as jsonConfig:
            sentryDsn = json.load(jsonConfig)['sentry_dsn']

        sentry_sdk.init(
            sentryDsn,

            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0,
            integrations=[sentryIntegration]
        )
        self.logConectado = True

    def setAdvLogado(self, advogadoLogado: Advogados):
        advDict: dict = {
            "id": advogadoLogado.advogadoId,
            "email": advogadoLogado.email
        }
        set_user(advDict)
