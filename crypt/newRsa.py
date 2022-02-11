import os
import rsa
from rsa import encrypt, decrypt, PrivateKey, PublicKey
from peewee import fn

from util.enums.databaseEnums import DatabaseEnum
from modelos.baseModelORM import database


class Crypt:

    def __init__(self):
        self.__pathPublica = self.__buscaPathPublica()
        self.__pathPrivada = self.__buscaPathPrivada()
        self.__chavePublica = self.buscaChavePublica()
        self.__chavePrivada = self.buscaChavePrivada()

    def __buscaPathPublica(self) -> str:
        chavePublica = os.path.normpath(os.path.join(os.getcwd(), os.pardir, 'PrevCliente', 'crypt', 'publicKey.txt'))
        if os.path.exists(chavePublica) and os.path.isfile(chavePublica):
            return chavePublica
        else:
            return ''

    def __buscaPathPrivada(self) -> str:
        chavePrivada = os.path.normpath(os.path.join(os.getcwd(), os.pardir, 'PrevCliente', 'crypt', '.privateKey.txt'))
        if os.path.exists(chavePrivada) and os.path.isfile(chavePrivada):
            return chavePrivada
        else:
            return ''

    def gerarChaves(self) -> bool:
        try:
            chavePrivada = os.path.join(os.getcwd(), os.pardir, 'PrevCliente', 'crypt', '.privateKey.txt')
            chavePrivada = os.path.normpath(chavePrivada)

            chavePublica = os.path.join(os.getcwd(), os.pardir, 'PrevCliente', 'crypt', 'publicKey.txt')
            chavePublica = os.path.normpath(chavePublica)

            chavPub, chavPriv = rsa.newkeys(400, poolsize=3)
            publicaBites = chavPub.save_pkcs1()
            privadaBites = chavPriv.save_pkcs1()

            with open(chavePublica, mode='w+b') as publica:
                publica.write(publicaBites)

            with open(chavePrivada, mode='w+b') as privada:
                privada.write(privadaBites)

            return True

        except Exception as err:
            print(f"avaliaGerarChaves: {err=}")
            return False

    def buscaChavePrivada(self) -> PrivateKey:
        if self.__pathPrivada != '':
            with open(self.__pathPrivada, mode='rb') as privada:
                privadaBites = privada.read()
                return PrivateKey.load_pkcs1(privadaBites)

    def buscaChavePublica(self) -> PublicKey:
        if self.__pathPublica != '':
            with open(self.__pathPublica, mode='rb') as publica:
                publicaBites = publica.read()
                return PublicKey.load_pkcs1(publicaBites)


@database.func()
def cifrar(mensagem: str) -> bytes:
    cripto = Crypt()
    chavePublica: PublicKey = cripto.buscaChavePublica()
    return encrypt(mensagem.encode('utf-8'), chavePublica)


@database.func()
def decifrar(mensagem: bytes) -> str:
    cripto = Crypt()
    chavePrivada: PrivateKey = cripto.buscaChavePrivada()
    return decrypt(mensagem, chavePrivada).decode('utf-8')
