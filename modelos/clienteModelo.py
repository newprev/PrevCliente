import datetime
from .telefoneModelo import TelefoneModelo


class ClienteModelo:

    def __init__(self):
        self.escritorioId: int = None
        self.clienteId: int = None
        self.nomeCliente: str = None
        self.sobrenomeCliente: str = None
        self.genero: str = None
        self.idade: int = None
        self.dataNascimento: datetime = None
        self.email: str = ''
        self.rgCliente: str = ''
        self.cpfCliente: str = ''
        self.nomeBanco: str = ''
        self.agenciaBanco: str = ''
        self.numeroConta: str = ''
        self.pixCliente: str = ''
        self.grauEscolaridade: str = ''
        self.senhaINSS: str = ''
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
        self.telefone: TelefoneModelo = None
        self.complemento: str = ''
        self.dataCadastro: datetime = datetime.datetime.now()
        self.dataUltAlt: datetime = datetime.datetime.now()
        self.pathCnis: str = ''

    def toDict(self):
        dictUsuario = {
            'escritorioId': self.escritorioId,
            'clienteId': self.clienteId,
            'nomeCliente': self.nomeCliente,
            'sobrenomeCliente': self.sobrenomeCliente,
            'genero': self.genero,
            'idade': self.idade,
            'dataNascimento': self.dataNascimento,
            'email': self.email,
            'rgCliente': self.rgCliente,
            'cpfCliente': self.cpfCliente,
            'nomeBanco': self.nomeBanco,
            'agenciaBanco': self.agenciaBanco,
            'numeroConta': self.numeroConta,
            'pixCliente': self.pixCliente,
            'grauEscolaridade': self.grauEscolaridade,
            'senhaINSS': self.senhaINSS,
            'numCartProf': self.numCartProf,
            'nit': self.nit,
            'nomeMae': self.nomeMae,
            'estadoCivil': self.estadoCivil,
            'endereco': self.endereco,
            'estado': self.estado,
            'cidade': self.cidade,
            'bairro': self.bairro,
            'cep': self.cep,
            'telefone': self.telefone,
            'complemento': self.complemento,
            'pathCnis': self.pathCnis
        }
        return dictUsuario

    def fromDict(self, dictCliente):
        self.escritorioId = dictCliente['escritorioId']
        self.clienteId = dictCliente['clienteId']
        self.nomeCliente = dictCliente['nomeCliente']
        self.sobrenomeCliente = dictCliente['sobrenomeCliente']
        self.genero = dictCliente['genero']
        self.idade = dictCliente['idade']
        self.dataNascimento = dictCliente['dataNascimento']
        self.email = dictCliente['email']
        self.rgCliente = dictCliente['rgCliente']
        self.cpfCliente = dictCliente['cpfCliente']
        self.nomeBanco = dictCliente['nomeBanco']
        self.agenciaBanco = dictCliente['agenciaBanco']
        self.numeroConta = dictCliente['numeroConta']
        self.pixCliente = dictCliente['pixCliente']
        self.grauEscolaridade = dictCliente['grauEscolaridade']
        self.senhaINSS = dictCliente['senhaINSS']
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
        self.telefone = TelefoneModelo().fromList(dictCliente['telefone'])
        self.complemento = dictCliente['complemento']
        self.pathCnis = dictCliente['pathCnis']

    def fromList(self, listCliente: list, retornaInst: bool = False):
        if listCliente is None:
            return None
        else:
            if len(listCliente) != 0:
                self.escritorioId = listCliente[0]
                self.clienteId = listCliente[1]
                self.nomeCliente = listCliente[2]
                self.sobrenomeCliente = listCliente[3]
                self.genero = listCliente[4]
                self.idade = listCliente[5]
                self.dataNascimento = listCliente[6]
                self.email = listCliente[7]
                self.rgCliente = listCliente[8]
                self.cpfCliente = listCliente[9]
                self.nomeBanco = listCliente[10]
                self.agenciaBanco = listCliente[11]
                self.numeroConta = listCliente[12]
                self.pixCliente = listCliente[13]
                self.grauEscolaridade = listCliente[14]
                self.senhaINSS = listCliente[15]
                self.numCartProf = listCliente[16]
                self.nit = listCliente[17]
                self.nomeMae = listCliente[18]
                self.estadoCivil = listCliente[19]
                self.profissao = listCliente[20]
                self.endereco = listCliente[21]
                self.estado = listCliente[22]
                self.cidade = listCliente[23]
                self.numero = listCliente[24]
                self.bairro = listCliente[25]
                self.cep = listCliente[26]
                self.complemento = listCliente[27]
                self.dataCadastro = listCliente[28]
                self.dataUltAlt = listCliente[29]

                self.telefone = TelefoneModelo().fromList(listCliente[30:])
                # pathCnis: {self.pathCnis}
            if retornaInst:
                return self

    def __repr__(self):
        return f"""
        Cliente(
            escritorioId: {self.escritorioId},
            clienteId: {self.clienteId},
            nomeCliente: {self.nomeCliente},
            sobrenomeCliente: {self.sobrenomeCliente},
            genero: {self.genero},
            idade: {self.idade},
            dataNascimento: {self.dataNascimento},
            email: {self.email},
            rgCliente: {self.rgCliente},
            cpfCliente: {self.cpfCliente},
            nomeBanco: {self.nomeBanco},
            agenciaBanco: {self.agenciaBanco},
            numeroConta: {self.numeroConta},
            pixCliente: {self.pixCliente},
            grauEscolaridade: {self.grauEscolaridade},
            senhaINSS: {self.senhaINSS},
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
            telefone: {self.telefone},
            complemento: {self.complemento},
            pathCnis: {self.pathCnis}"""

    def __bool__(self):
        return self.nit != '' and self.nit is not None
