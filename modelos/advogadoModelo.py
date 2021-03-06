import datetime


class AdvogadoModelo:

    def __init__(self):
        self.escritorioId: int = None
        self.advogadoId: int = None
        self.nomeUsuario: str = None
        self.login: str = None
        self.senha: str = None
        self.email: str = None
        self.numeroOAB: str = None
        self.sobrenomeUsuario: str = None
        self.nacionalidade: str = None
        self.estadoCivil: str = None
        self.admin: bool = False
        self.ativo: bool = True
        self.confirmado: bool = True
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictUsuario = {
            'escritorioId': self.escritorioId,
            'advogadoId': self.advogadoId,
            'nomeUsuario': self.nomeUsuario,
            'login': self.login,
            'senha': self.senha,
            'email': self.email,
            'sobrenomeUsuario': self.sobrenomeUsuario,
            'nacionalidade': self.nacionalidade,
            'estadoCivil': self.estadoCivil,
            'numeroOAB': self.numeroOAB,
            'admin': self.admin,
            'confirmado': self.confirmado,
            'ativo': self.ativo,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictUsuario: dict, retornaInst: bool = True):

        if dictUsuario['advogadoId'] is list or dictUsuario['advogadoId'] is tuple:
            self.advogadoId = dictUsuario['advogadoId'][0]
        else:
            self.advogadoId = dictUsuario['advogadoId']

        if 'senha' in dictUsuario.keys():
            self.senha = dictUsuario['senha']

        if 'dataCadastro' in dictUsuario.keys():
            self.dataCadastro = dictUsuario['dataCadastro']

        if 'dataUltAlt' in dictUsuario.keys():
            self.dataUltAlt = dictUsuario['dataUltAlt']

        self.escritorioId = dictUsuario['escritorioId']
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

        if retornaInst:
            return self

    def fromList(self, listUsuario: list, retornaInst: bool = True):
        if listUsuario is None:
            return None
        else:
            if len(listUsuario) != 0:
                self.advogadoId = listUsuario[0]
                self.escritorioId = listUsuario[1]
                self.nomeUsuario = listUsuario[2]
                self.sobrenomeUsuario = listUsuario[3]
                self.login = listUsuario[4]
                self.senha = listUsuario[5]
                self.email = listUsuario[6]
                self.numeroOAB = listUsuario[7]
                self.nacionalidade = listUsuario[8]
                self.estadoCivil = listUsuario[9]
                self.admin = listUsuario[10]
                self.ativo = listUsuario[11]
                self.confirmado = listUsuario[12]
                self.dataCadastro = listUsuario[13]
                self.dataUltAlt = listUsuario[14]

            if retornaInst:
                return self

    def __repr__(self):
        return f"""Usuario(
            escritorioId: {self.escritorioId},
            advogadoId: {self.advogadoId},
            nomeUsuario: {self.nomeUsuario},
            login: {self.login},
            senha: {self.senha},
            sobrenomeUsuario: {self.sobrenomeUsuario},
            nacionalidade: {self.nacionalidade},
            email: {self.email},
            numeroOAB: {self.numeroOAB},
            estadoCivil: {self.estadoCivil},
            admin: {self.admin},
            confirmado: {self.confirmado},
            ativo: {self.ativo}"""

    def __eq__(self, other):
        instVariavel: bool = isinstance(self, type(other))
        if not instVariavel:
            return False

        senhaAuth: bool = self.senha == other.senha
        loginAuth: bool = self.login == other.login

        return senhaAuth and loginAuth

    def __bool__(self):
        return self.login is not None and self.nomeUsuario is not None
