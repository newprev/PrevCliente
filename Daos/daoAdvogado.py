import sqlite3
from datetime import datetime

from Daos.tabelas import TabelasConfig
from pymysql import connections
from modelos.advogadoModelo import AdvogadoModelo

class DaoAdvogado:

    def __init__(self, db: connections=None):
        self.db = db
        self.config = TabelasConfig()

    def insereAdvogado(self, advogado: AdvogadoModelo):
        pass
