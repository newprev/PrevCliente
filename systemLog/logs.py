import logging.config
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import os
from logging import *

from datetime import datetime
from typing import Set


class NewLogging:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NewLogging, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.logApi: Logger = None

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
        self.logApi = getLogger('logApi')
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
        sentry_sdk.init(
            "https://0ff1b7f5532d427f9cd4b3bcac8f413c@o1205113.ingest.sentry.io/6345373",

            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0,
            integrations=[sentryIntegration]
        )


class FiltroSistema(Filter):
    def filter(self, record: LogRecord) -> bool:
        arquivosSemInteresse: Set[str] = {
            'selector_events.py',
            'base.py',
            'autoreload.py',
            'log.py'
        }
        return record.filename not in arquivosSemInteresse
