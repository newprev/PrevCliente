import datetime


class AdvogadoModelo:

    def __init__(self):
        self.escritorioId: int = None
        self.usuarioId: int = None
        self.nomeUsuario: str = None
        self.login: str = None
        self.email: str = None
        self.numeroOAB: str = None
        self.sobrenomeUsuario: str = None
        self.nacionalidade: str = None
        self.estadoCivil: str = None
        self.admin: bool = False
        self.ativo: bool = True
        self.confirmado: bool = True
        self.dataCadastro: datetime = None

    def toDict(self):
        dictUsuario = {
            'escritorioId': self.escritorioId,
            'usuarioId': self.usuarioId,
            'nomeUsuario': self.nomeUsuario,
            'login': self.login,
            'email': self.email,
            'sobrenomeUsuario': self.sobrenomeUsuario,
            'nacionalidade': self.nacionalidade,
            'estadoCivil': self.estadoCivil,
            'numeroOAB': self.numeroOAB,
            'admin': self.admin,
            'confirmado': self.confirmado,
            'ativo': self.ativo
        }
        return dictUsuario

    def fromDict(self, dictUsuario):
        self.escritorioId = dictUsuario['escritorioId']
        if dictUsuario['usuarioId'] is list or dictUsuario['usuarioId'] is tuple:
            self.usuarioId = dictUsuario['usuarioId'][0]
        else:
            self.usuarioId = dictUsuario['usuarioId']

        self.nomeUsuario = dictUsuario['nomeUsuario']
        self.login = dictUsuario['login']
        # self.telefone = dictUsuario['telefone'],
        self.email = dictUsuario['email'],
        self.sobrenomeUsuario = dictUsuario['sobrenomeUsuario']
        self.nacionalidade = dictUsuario['nacionalidade']
        self.numeroOAB = dictUsuario['numeroOAB']
        self.estadoCivil = dictUsuario['estadoCivil']
        self.admin = dictUsuario['admin']
        self.confirmado = dictUsuario['confirmado']
        self.ativo = dictUsuario['ativo']
        return self

    def fromList(self, listUsuario: list, retornaInst: bool = False):
        if listUsuario is None:
            return None
        else:
            if len(listUsuario) != 0:
                self.escritorioId = listUsuario[0]
                self.usuarioId = listUsuario[0]
                self.nomeUsuario = listUsuario[1]
                self.login = listUsuario[4]
                self.email = listUsuario[6]
                self.sobrenomeUsuario = listUsuario[7]
                self.nacionalidade = listUsuario[8]
                self.numeroOAB = listUsuario[14]
                self.estadoCivil = listUsuario[17]
                self.admin = listUsuario[19]
                self.confirmado = listUsuario[20]
                self.dataCadastro = listUsuario[21]
            if retornaInst:
                return self

    def __repr__(self):
        return f"""Usuario(
            escritorioId: {self.escritorioId},
            usuarioId: {self.usuarioId},
            nomeUsuario: {self.nomeUsuario},
            login: {self.login},
            sobrenomeUsuario: {self.sobrenomeUsuario},
            nacionalidade: {self.nacionalidade},
            email: {self.email},
            numeroOAB: {self.numeroOAB},
            estadoCivil: {self.estadoCivil},
            admin: {self.admin},
            confirmado: {self.confirmado},
            ativo: {self.ativo}"""
