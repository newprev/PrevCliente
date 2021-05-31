import datetime


class TelefoneModelo:

    def __init__(self):
        self.telefoneId: int = None
        self.clienteId: int = None
        self.numero: str = None
        self.tipoTelefone: str = None
        self.pessoalRecado: str = None
        self.ativo: bool = True
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictUsuario = {
            'telefoneId': self.telefoneId,
            'clienteId': self.clienteId,
            'numero': self.numero,
            'tipoTelefone': self.tipoTelefone,
            'pessoalRecado': self.pessoalRecado,
            'ativo': self.ativo,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictTelefone):
        self.telefoneId = dictTelefone['telefoneId'],
        self.clienteId = dictTelefone['clienteId'],
        self.numero = dictTelefone['numero'],
        self.tipoTelefone = dictTelefone['tipoTelefone'],
        self.pessoalRecado = dictTelefone['pessoalRecado'],
        self.ativo = dictTelefone['ativo'],
        self.dataCadastro = dictTelefone['dataCadastro'],
        self.dataUltAlt = dictTelefone['dataUltAlt'],

    def fromList(self, listTelefone: list, retornaInst: bool = True):
        self.telefoneId = listTelefone[0]
        self.clienteId = listTelefone[1]
        self.numero = listTelefone[2]
        self.tipoTelefone = listTelefone[3]
        self.pessoalRecado = listTelefone[4]

        if listTelefone[5] is not None:
            self.ativo = listTelefone[5]

        if len(listTelefone) == 7:
            self.dataCadastro = listTelefone[6]
            self.dataUltAlt = listTelefone[7]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""
        Telefone(
                telefoneId: {self.telefoneId},
                clienteId: {self.clienteId},
                numero: {self.numero},
                tipoTelefone: {self.tipoTelefone},
                pessoalRecado: {self.pessoalRecado},
                ativo: {self.ativo},
                dataCadastro: {self.dataCadastro},
                dataUltAlt: {self.dataUltAlt},
            """
