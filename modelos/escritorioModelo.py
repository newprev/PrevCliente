import datetime


class EscritorioModelo:

    def __init__(self):
        self.escritorioId: int = None
        self.nomeEscritorio: str = None
        self.nomeFantasia: str = ''
        self.cnpj: str = ''
        self.cpf: str = ''
        self.telefone: str = ''
        self.email: str = ''
        self.inscEstadual: str = ''
        self.endereco: str = ''
        self.numero: int = None
        self.cep: str = ''
        self.complemento: str = ''
        self.cidade: str = ''
        self.estado: str = ''
        self.bairro: str = ''

    def toDict(self):
        dictUsuario = {
            'escritorioId': self.escritorioId,
            'nomeEscritorio': self.nomeEscritorio,
            'nomeFantasia': self.nomeFantasia,
            'cnpj': self.cnpj,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'email': self.email,
            'inscEstadual': self.inscEstadual,
            'endereco': self.endereco,
            'numero': self.numero,
            'cep': self.cep,
            'complemento': self.complemento,
            'cidade': self.cidade,
            'estado': self.estado,
            'bairro': self.bairro,
        }
        return dictUsuario

    def fromDict(self, dictEscritorio):
        if dictEscritorio['escritorioId'] is list or dictEscritorio['escritorioId'] is tuple:
            self.escritorioId = dictEscritorio['escritorioId'][0]
        else:
            self.escritorioId = dictEscritorio['escritorioId']

        self.nomeEscritorio = dictEscritorio['nomeEscritorio']
        self.nomeFantasia = dictEscritorio['nomeFantasia']
        self.cnpj = dictEscritorio['cnpj']
        self.telefone = dictEscritorio['telefone'],
        self.email = dictEscritorio['email'],
        self.cpf = dictEscritorio['cpf']
        self.inscEstadual = dictEscritorio['inscEstadual']
        self.endereco = dictEscritorio['endereco']
        self.numero = dictEscritorio['numero']
        self.estado = dictEscritorio['estado']
        self.cidade = dictEscritorio['cidade']
        self.bairro = dictEscritorio['bairro']
        self.cep = dictEscritorio['cep']
        self.complemento = dictEscritorio['complemento']

        return self

    def fromList(self, listEscritorio: list, retornaInst: bool = False):
        if listEscritorio is None:
            return None
        else:
            if len(listEscritorio) != 0:
                self.escritorioId = listEscritorio[0]
                self.nomeEscritorio = listEscritorio[1]
                self.nomeFantasia = listEscritorio[2]
                self.cnpj = listEscritorio[4]
                self.telefone = listEscritorio[5]
                self.email = listEscritorio[6]
                self.cpf = listEscritorio[7]
                self.inscEstadual = listEscritorio[8]
                self.endereco = listEscritorio[14]
                self.estado = listEscritorio[15]
                self.cidade = listEscritorio[16]
                self.numero = listEscritorio[17]
                self.bairro = listEscritorio[18]
                self.cep = listEscritorio[19]
                self.complemento = listEscritorio[20]
            if retornaInst:
                return self

    def __repr__(self):
        return f"""Escritorio(
            escritorioId: {self.escritorioId},
            nomeEscritorio: {self.nomeEscritorio},
            nomeFantasia: {self.nomeFantasia},
            cnpj: {self.cnpj},
            cpf: {self.cpf},
            inscEstadual: {self.inscEstadual},
            endereco: {self.endereco},
            numero: {self.numero},
            estado: {self.estado},
            cidade: {self.cidade},
            bairro: {self.bairro},
            cep: {self.cep},
            complemento: {self.complemento}
    """
