import datetime


class ClienteModelo:

    def __init__(self):
        self.advogadoId: int = None
        self.clienteId: int = None
        self.nomeCliente: str = None
        self.sobrenomeCliente: str = None
        self.idade: int = None
        self.dataNascimento: datetime = None
        self.email: str = ''
        self.telefone: str = ''
        self.rgCliente: str = ''
        self.cpfCliente: str = ''
        self.numCartProf: str = ''
        self.nit: str = ''
        self.nomeMae: str = ''
        self.estadoCivil: str = ''
        self.profissao: str = ''
        self.endereco: str = ''
        self.numero: int = 0
        self.estado: str = ''
        self.cidade: str = ''
        self.bairro: str = ''
        self.cep: str = ''
        self.complemento: str = ''
        self.dataCadastro: datetime = datetime.datetime.now()
        self.dataUltAlt: datetime = datetime.datetime.now()
        self.pathCnis: str = ''

    def toDict(self):
        dictUsuario = {
            'advogadoId': self.advogadoId,
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
        self.advogadoId = dictCliente['advogadoId']
        self.clienteId = dictCliente['clienteId']
        self.nomeCliente = dictCliente['nomeCliente']
        self.sobrenomeCliente = dictCliente['sobrenomeCliente']
        self.idade = dictCliente['idade']
        self.dataNascimento = dictCliente['dataNascimento']
        self.telefone = dictCliente['telefone']
        self.email = dictCliente['email']
        self.rgCliente = dictCliente['rgCliente']
        self.cpfCliente = dictCliente['cpfCliente']
        self.numCartProf = dictCliente['numCartProf']
        self.nit = dictCliente['nit']
        self.nomeMae = dictCliente['nomeMae']
        self.estadoCivil = dictCliente['estadoCivil']
        self.endereco = dictCliente['endereco']
        self.numero = dictCliente['numero']
        self.estado = dictCliente['estado']
        self.cidade = dictCliente['cidade']
        self.bairro = dictCliente['bairro']
        self.cep = dictCliente['cep']
        self.complemento = dictCliente['complemento']
        self.pathCnis = dictCliente['pathCnis']

    def fromList(self, listCliente: list, retornaInst: bool = False):
        if listCliente is None:
            return None
        else:
            if len(listCliente) != 0:
                # for num, info in enumerate(listCliente):
                #     print(f"{num} - {info}")
                self.advogadoId = listCliente[0]
                self.clienteId = listCliente[1]
                self.nomeCliente = listCliente[2]
                self.sobrenomeCliente = listCliente[3]
                self.idade = listCliente[4]
                self.dataNascimento = listCliente[5]
                self.telefone = listCliente[6]
                self.email = listCliente[7]
                self.rgCliente = listCliente[8]
                self.cpfCliente = listCliente[9]
                self.numCartProf = listCliente[10]
                self.nit = listCliente[11]
                self.nomeMae = listCliente[12]
                self.estadoCivil = listCliente[13]
                self.profissao = listCliente[14]
                self.endereco = listCliente[15]
                self.estado = listCliente[16]
                self.cidade = listCliente[17]
                self.numero = listCliente[18]
                self.bairro = listCliente[19]
                self.cep = listCliente[20]
                self.complemento = listCliente[21]
                self.dataCadastro = listCliente[22]
                self.dataUltAlt = listCliente[23]
                # pathCnis: {self.pathCnis}
            if retornaInst:
                return self

    def __repr__(self):
        return f"""Cliente(
            advogadoId: {self.advogadoId},
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
            numero: {self.numero},
            estado: {self.estado},
            cidade: {self.cidade},
            bairro: {self.bairro},
            cep: {self.cep},
            complemento: {self.complemento},
            pathCnis: {self.pathCnis}"""

    def __bool__(self):
        return self.nit != ''
