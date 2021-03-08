class ClienteModelo:

    def __init__(self):
        self.clienteId: int = None
        self.nomeCliente: str = None
        self.sobrenomeCliente: str = None
        self.telefone: str = None
        self.email: str = None
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

    def __repr__(self):
        return f"""Cliente(\nclienteId: {self.clienteId},
            nomeCliente: {self.nomeCliente},
            sobrenomeCliente: {self.sobrenomeCliente},
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
