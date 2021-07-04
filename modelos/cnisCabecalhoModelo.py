import datetime

from helpers import strToDatetime
from newPrevEnums import TamanhoData


class CabecalhoModelo:

    def __init__(self):
        self.cabecalhosId: int = None
        self.clienteId: int = None
        self.seq: int = None
        self.nit: str = None
        self.nb: int = None
        self.cdEmp: str = None
        self.nomeEmp: str = None
        self.dataInicio: datetime = None
        self.dataFim: datetime = None
        self.tipoVinculo: str = None
        self.orgVinculo: str = None
        self.especie: str = None
        self.indicadores: str = None
        self.ultRem: datetime = None
        self.dadoOrigem: str = None
        self.situacao: str = None
        self.dataCadastro: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictUsuario = {
            'cabecalhosId': self.cabecalhosId,
            'clienteId': self.clienteId,
            'seq': self.seq,
            'nit': self.nit,
            'nb': self.nb,
            'cdEmp': self.cdEmp,
            'nomeEmp': self.nomeEmp,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'tipoVinculo': self.tipoVinculo,
            'orgVinculo': self.orgVinculo,
            'especie': self.especie,
            'indicadores': self.indicadores,
            'ultRem': self.ultRem,
            'dadoOrigem': self.dadoOrigem,
            'situacao': self.situacao,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictUsuario

    def fromDict(self, dictCabecalho):
        self.cabecalhosId = dictCabecalho['cabecalhosId']
        self.clienteId = dictCabecalho['clienteId']
        self.seq = dictCabecalho['seq']
        self.nit = dictCabecalho['nit']
        self.nb = dictCabecalho['nb']
        self.cdEmp = dictCabecalho['cdEmp']
        self.nomeEmp = dictCabecalho['nomeEmp']
        self.dataInicio = dictCabecalho['dataInicio']
        self.dataFim = dictCabecalho['dataFim']
        self.tipoVinculo = dictCabecalho['tipoVinculo']
        self.orgVinculo = dictCabecalho['orgVinculo']
        self.especie = dictCabecalho['especie']
        self.indicadores = dictCabecalho['indicadores']
        self.ultRem = dictCabecalho['ultRem']
        self.dadoOrigem = dictCabecalho['dadoOrigem']
        self.situacao = dictCabecalho['situacao']
        self.dataCadastro = dictCabecalho['dataCadastro']
        self.dataUltAlt = dictCabecalho['dataUltAlt']

    def fromList(self, listCabecalho: list, retornaInst: bool = True):
        self.cabecalhosId = listCabecalho[0]
        self.clienteId = listCabecalho[1]
        self.seq = listCabecalho[2]
        self.nit = listCabecalho[3]
        self.nb = listCabecalho[4]
        self.cdEmp = listCabecalho[5]
        self.nomeEmp = listCabecalho[6]

        if listCabecalho[7] is not None:
            self.dataInicio = strToDatetime(listCabecalho[7], tamanho=TamanhoData.gg)
        else:
            self.dataInicio = listCabecalho[7]

        if listCabecalho[8] is not None:
            self.dataFim = strToDatetime(listCabecalho[8], tamanho=TamanhoData.gg)
        else:
            self.dataFim = listCabecalho[8]

        self.tipoVinculo = listCabecalho[9]
        self.orgVinculo = listCabecalho[10]
        self.especie = listCabecalho[11]
        self.indicadores = listCabecalho[12]

        if listCabecalho[13] is not None:
            self.ultRem = strToDatetime(listCabecalho[13], tamanho=TamanhoData.gg)
        else:
            self.ultRem = listCabecalho[13]

        self.dadoOrigem = listCabecalho[14]
        self.situacao = listCabecalho[15]
        self.dataCadastro = strToDatetime(listCabecalho[16], tamanho=TamanhoData.g)
        self.dataUltAlt = strToDatetime(listCabecalho[17], tamanho=TamanhoData.g)

        if retornaInst:
            return self

    def __repr__(self):
        return f"""Cabecalho(
            cabecalhosId: {self.cabecalhosId},
            clienteId: {self.clienteId},
            seq: {self.seq},
            nit: {self.nit},
            seq: {self.nb},
            cdEmp: {self.cdEmp},
            nomeEmp: {self.nomeEmp},
            dataInicio: {self.dataInicio},
            dataFim: {self.dataFim},
            tipoVinculo: {self.tipoVinculo},
            orgVinculo: {self.orgVinculo},
            especie: {self.especie},
            indicadores: {self.indicadores},
            ultRem: {self.ultRem},
            dadoOrigem: {self.dadoOrigem},
            situacao: {self.situacao},
            dataCadastro: {self.dataCadastro},
            dataUltAlt: {self.dataUltAlt}
            """

    def __eq__(self, other):
        return self.cabecalhosId == other.cabecalhosId
