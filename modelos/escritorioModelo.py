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
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

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
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt

        }
        return dictUsuario

    def fromDict(self, dictEscritorio: dict):

        if dictEscritorio['escritorioId'] is list or dictEscritorio['escritorioId'] is tuple:
            self.escritorioId = dictEscritorio['escritorioId'][0]
        else:
            self.escritorioId = dictEscritorio['escritorioId']

        if isinstance(dictEscritorio['email'], list):
            self.email = dictEscritorio['email'][0]
        else:
            self.email = dictEscritorio['email']

        if isinstance(dictEscritorio['telefone'], list):
            self.telefone = dictEscritorio['telefone'][0]
        else:
            self.telefone = dictEscritorio['telefone']

        self.nomeEscritorio = dictEscritorio['nomeEscritorio']
        self.nomeFantasia = dictEscritorio['nomeFantasia']
        self.cnpj = dictEscritorio['cnpj']
        self.cpf = dictEscritorio['cpf']
        self.inscEstadual = dictEscritorio['inscEstadual']
        self.endereco = dictEscritorio['endereco']
        self.numero = dictEscritorio['numero']
        self.estado = dictEscritorio['estado']
        self.cidade = dictEscritorio['cidade']
        self.bairro = dictEscritorio['bairro']
        self.cep = dictEscritorio['cep']
        self.complemento = dictEscritorio['complemento']
        self.dataCadastro = dictEscritorio['dataCadastro']
        self.dataUltAlt = dictEscritorio['dataUltAlt']

        return self

    def fromList(self, listEscritorio: list, retornaInst: bool = True):
        if listEscritorio is None:
            return None
        else:
            if len(listEscritorio) != 0:
                self.escritorioId = listEscritorio[0]
                self.nomeEscritorio = listEscritorio[1]
                self.nomeFantasia = listEscritorio[2]
                self.cnpj = listEscritorio[3]
                self.cpf = listEscritorio[4]
                self.telefone = listEscritorio[5]
                self.email = listEscritorio[6]
                self.inscEstadual = listEscritorio[7]
                self.endereco = listEscritorio[8]
                self.numero = listEscritorio[9]
                self.cep = listEscritorio[10]
                self.complemento = listEscritorio[11]
                self.cidade = listEscritorio[12]
                self.estado = listEscritorio[13]
                self.bairro = listEscritorio[14]
                self.dataCadastro = listEscritorio[15]
                self.dataUltAlt = listEscritorio[16]

            if retornaInst:
                return self

    def __repr__(self):
        return f"""Escritorio(
            escritorioId: {self.escritorioId},
            nomeEscritorio: {self.nomeEscritorio},
            nomeFantasia: {self.nomeFantasia},
            cnpj: {self.cnpj},
            cpf: {self.cpf},
            email: {self.email},
            inscEstadual: {self.inscEstadual},
            endereco: {self.endereco},
            numero: {self.numero},
            estado: {self.estado},
            cidade: {self.cidade},
            bairro: {self.bairro},
            cep: {self.cep},
            complemento: {self.complemento},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}            
    """

    def __bool__(self):
        return self.escritorioId is not None
