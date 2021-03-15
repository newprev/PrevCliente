import json
import os

import pymysql


class ConfigConnection:

    def __init__(self, instanciaBanco: str = None):

        self.__host = None
        self.__user = None
        self.__passwd = None
        self.__banco = None
        self.__port = None
        self.__instanciaBanco = instanciaBanco

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def user(self):
        return self.__user

    @property
    def passwd(self):
        return self.__passwd

    @property
    def banco(self):
        return self.__banco

    def getDatabase(self):
        dataSourcesDir = os.path.join(os.path.dirname(__file__), 'datasource')
        if self.__instanciaBanco.title() == 'Local':
            dbPath = os.path.join(dataSourcesDir, 'dbLocal.json')
        else:
            dbPath = os.path.join(dataSourcesDir, 'databaseCloud.json')

        with open(dbPath) as arquivo:
            config = json.load(arquivo)
            self.__host = config['host']
            self.__user = config['user']
            self.__passwd = config['passwd']
            self.__banco = config['banco']
            self.__port = int(config['port'])
            arquivo.close()

        return pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.banco,
            port=self.port
        )
