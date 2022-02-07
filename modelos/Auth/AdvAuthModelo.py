from modelos.advogadoORM import Advogados


class AdvAuthModelo:

    def __init__(self):
        self.advogadoId: int = None
        self.escritorioId: int = None
        self.login: str = None
        self.senha: str = None
        self.numeroOAB: str = None
        self.email: str = None
        self.ativo: bool = True

    def toDict(self) -> dict:
        dictAuth = {
            'advogadoId': self.advogadoId,
            'escritorioId': self.escritorioId,
            'login': self.login,
            'senha': self.senha,
            'numeroOAB': self.numeroOAB,
            'email': self.email,
            'ativo': self.ativo,
        }
        return dictAuth

    def fromDict(self, dictAuth: dict, retornaInst: bool = True):
        self.senha = dictAuth['senha']
        self.escritorioId = dictAuth['escritorioId']
        self.login = dictAuth['login']
        self.numeroOAB = dictAuth['numeroOAB']
        self.email = dictAuth['email']
        self.advogadoId = dictAuth['advogadoId']

        if 'ativo' not in dictAuth.keys():
            self.ativo = False
        else:
            self.ativo = True

        if retornaInst:
            return self

    def fromList(self, listUsuario: list, retornaInst: bool = False):
        if listUsuario is None:
            return None
        else:
            if len(listUsuario) != 0:
                self.advogadoId = listUsuario[0]
                self.escritorioId = listUsuario[1]
                self.login = listUsuario[2]
                self.senha = listUsuario[3]
                self.numeroOAB = listUsuario[4]
                self.email = listUsuario[5]
            if retornaInst:
                return self

    def __repr__(self):
        return f"""
        ClientAuth(
            advogadoId: {self.advogadoId},
            escritorioId: {self.escritorioId},
            login: {self.login},
            senha: {self.senha},
            numeroOAB: {self.numeroOAB},
            email: {self.email},
            ativo: {self.ativo},
"""
    
    def __eq__(self, other):
        instVariavel: bool = isinstance(other, Advogados)
        if not instVariavel:
            return False

        senhaAuth: bool = self.senha == other.senha
        loginAuth: bool = self.login == other.login
        emailAuth: bool = self.email == other.email
        idAuth: bool = self.advogadoId == self.advogadoId

        return (loginAuth and senhaAuth) or (emailAuth and senhaAuth) or (idAuth and senhaAuth)

    def __bool__(self):
        lga: bool = self.senha is not None and self.login is not None and self.ativo
        lIda: bool = self.login is not None and self.advogadoId is not None and self.ativo
        return lga or lIda