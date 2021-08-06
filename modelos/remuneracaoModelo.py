import datetime

from helpers import strToDatetime
from newPrevEnums import TamanhoData


class RemuneracoesModelo:

    def __init__(self):
        self.remuneracoesId: int = None
        self.clienteId: int = None
        self.seq: int = None
        self.competencia: datetime = None
        self.remuneracao: float = None
        self.indicadores: str = None
        self.dadoOrigem: str = None
        self.dataUltAlt: datetime = None
        self.dataCadastro: datetime = None

    def toDict(self):
        dictUsuario = {
            'remuneracoesId': self.remuneracoesId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'competencia': self.competencia,
            'remuneracao': self.remuneracao,
            'indicadores': self.indicadores,
            'dadoOrigem': self.dadoOrigem,
            'dataUltAlt': self.dataUltAlt,
            'dataCadastro': self.dataCadastro
        }
        return dictUsuario

    def fromDict(self, dictRemuneracoes):
        self.remuneracoesId = dictRemuneracoes['remuneracoesId']
        self.clienteId = dictRemuneracoes['clienteId']
        self.seq = dictRemuneracoes['seq']
        self.competencia = dictRemuneracoes['competencia']
        self.remuneracao = dictRemuneracoes['remuneracao']
        self.dataCadastro = dictRemuneracoes['dataCadastro']
        self.dadoOrigem = dictRemuneracoes['dadoOrigem']
        self.indicadores = dictRemuneracoes['indicadores']
        self.dataUltAlt = dictRemuneracoes['dataUltAlt']

    def fromList(self, listRemuneracoes: list, retornaInst: bool = True):
        self.remuneracoesId = listRemuneracoes[0]
        self.clienteId = listRemuneracoes[1]
        self.seq = listRemuneracoes[2]
        self.competencia = strToDatetime(listRemuneracoes[3], TamanhoData.gg)
        self.remuneracao = listRemuneracoes[4]
        self.indicadores = listRemuneracoes[5]
        self.dadoOrigem = listRemuneracoes[6]
        self.dataCadastro = listRemuneracoes[7]
        self.dataUltAlt = listRemuneracoes[8]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""Remuneracoes(
            remuneracoesId: {self.remuneracoesId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            competencia: {self.competencia},
            remuneracao: {self.remuneracao},
            indicadores: {self.indicadores},
            dadoOrigem: {self.dadoOrigem},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """
