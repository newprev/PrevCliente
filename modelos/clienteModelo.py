import datetime


class ClienteModelo:

    def __init__(self):
        self.clienteId: int = None
        self.nomeCliente: str = None
        self.sobrenomeCliente: str = None
        self.idade: int = None
        self.dataNascimento: datetime = None
        self.email: str = None
        self.telefone: str = None
        self.rgCliente: str = None
        self.cpfCliente: str = None
        self.numCartProf: str = None
        self.nit: str = None
        self.nomeMae: str = None
        self.estadoCivil: str = None
        self.profissao: str = None
        self.endereco: str = None
        self.estado: str = None
        self.cidade: str = None
        self.bairro: str = None
        self.cep: str = None
        self.complemento: str = None
        self.pathCnis: str = None

    def toDict(self):
        dictUsuario = {
            'clienteId': self.clienteId,
            'nomeCliente': self.nomeCliente,
            'sobrenomeCliente': self.sobrenomeCliente,
            'idade': self.idade,
            'dataNascimento': self.dataNascimento,
            'telefone': self.telefone,
            'email': self.email,
            'rgCliente': self.rgCliente,
            'cpfCliente': self.cpfCliente,
            'numCartProf': self.numCartProf,
            'nit': self.nit,
            'nomeMae': self.nomeMae,
            'estadoCivil': self.estadoCivil,
            'endereco': self.endereco,
            'estado': self.estado,
            'cidade': self.cidade,
            'bairro': self.bairro,
            'cep': self.cep,
            'complemento': self.complemento,
            'pathCnis': self.pathCnis
        }
        return dictUsuario

    def fromDict(self, dictCliente):
        self.clienteId = dictCliente['clienteId'],
        self.nomeCliente = dictCliente['nomeCliente'],
        self.sobrenomeCliente = dictCliente['sobrenomeCliente'],
        self.idade = dictCliente['idade'],
        self.dataNascimento = dictCliente['dataNascimento'],
        self.telefone = dictCliente['telefone'],
        self.email = dictCliente['email'],
        self.rgCliente = dictCliente['rgCliente'],
        self.cpfCliente = dictCliente['cpfCliente'],
        self.numCartProf = dictCliente['numCartProf'],
        self.nit = dictCliente['nit'],
        self.nomeMae = dictCliente['nomeMae'],
        self.estadoCivil = dictCliente['estadoCivil'],
        self.endereco = dictCliente['endereco']
        self.estado = dictCliente['estado']
        self.cidade = dictCliente['cidade']
        self.bairro = dictCliente['bairro']
        self.cep = dictCliente['cep']
        self.complemento = dictCliente['complemento']
        self.pathCnis = dictCliente['pathCnis']

    def fromList(self, listCliente: list):
        self.clienteId = listCliente[0]
        self.nomeCliente = listCliente[1]
        self.sobrenomeCliente = listCliente[2]
        self.idade = listCliente[3]
        self.dataNascimento = listCliente[4]
        self.telefone = listCliente[5]
        self.email = listCliente[6]
        self.rgCliente = listCliente[7]
        self.cpfCliente = listCliente[8]
        self.numCartProf = listCliente[9]
        self.serieCarteiraProf = listCliente[10]
        self.quaCarteiraProf = listCliente[11]
        self.nit = listCliente[12]
        self.nomeMae = listCliente[13]
        self.estadoCivil = listCliente[14]
        self.endereco = listCliente[15]
        self.estado = listCliente[16]
        self.cidade = listCliente[17]
        self.bairro = listCliente[18]
        self.cep = listCliente[19]
        self.complemento = listCliente[20]
        # pathCnis: {self.pathCnis}

    def __repr__(self):
        return f"""Cliente(
            clienteId: {self.clienteId},
            nomeCliente: {self.nomeCliente},
            sobrenomeCliente: {self.sobrenomeCliente},
            idade: {self.idade},
            dataNascimento: {self.dataNascimento},
            telefone: {self.telefone},
            email: {self.email},
            rgCliente: {self.rgCliente},
            cpfCliente: {self.cpfCliente},
            numCartProf: {self.numCartProf},
            nit: {self.nit},
            nomeMae: {self.nomeMae},
            estadoCivil: {self.estadoCivil},
            endereco: {self.endereco},
            estado: {self.estado},
            cidade: {self.cidade},
            bairro: {self.bairro},
            cep: {self.cep},
            complemento: {self.complemento},
            pathCnis: {self.pathCnis}"""
