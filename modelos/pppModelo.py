import datetime


class PppModelo:

    def __init__(self):
        self.pppId: str = None
        self.cnpj: str = None
        self.nomeEmpresa: str = None
        self.cnae: str = None
        self.sitEmpregado: datetime = None
        self.nit: datetime = None
        self.dataNascimento: datetime = None
        self.genero: datetime = None
        self.ctps: datetime = None
        self.dataAdminssao: datetime = None
        self.regimeRevezamento: datetime = None
        self.dataRegistro: datetime = None
        self.numCAT: datetime = None
        self.profissiografiaData: datetime = None
        self.profissiografiaDesc: datetime = None
        self.exposicaoDataInicio: datetime = None
        self.exposicaoDataFim: datetime = None
        self.exposicaoTipo: datetime = None
        self.exposicaoFator: datetime = None
        self.exposicaoIntensidade: datetime = None
        self.exposicaoTecnicaUtilizada: datetime = None
        self.eficEpc: datetime = None
        self.eficEpi: datetime = None
        self.caEpi: datetime = None
        self.dataUltAlt: datetime = None

    def toDict(self):
        dictPpp = {
            'pppId': self.pppId,
            'cnpj': self.cnpj,
            'nomeEmpresa': self.nomeEmpresa,
            'cnae': self.cnae,
            'sitEmpregado': self.sitEmpregado,
            'nit': self.nit,
            'dataNascimento': self.dataNascimento,
            'genero': self.genero,
            'ctps': self.ctps,
            'dataAdminssao': self.dataAdminssao,
            'dataRegistro': self.dataRegistro,
            'numCAT': self.numCAT,
            'profissiografiaData': self.profissiografiaData,
            'profissiografiaDesc': self.profissiografiaDesc,
            'exposicaoDataInicio': self.exposicaoDataInicio,
            'exposicaoDataFim': self.exposicaoDataFim,
            'exposicaoTipo': self.exposicaoTipo,
            'exposicaoFator': self.exposicaoFator,
            'exposicaoIntensidade': self.exposicaoIntensidade,
            'exposicaoTecnicaUtilizada': self.exposicaoTecnicaUtilizada,
            'eficEpc': self.eficEpc,
            'eficEpi': self.eficEpi,
            'caEpi': self.caEpi,
            'dataUltAlt': self.dataUltAlt
        }
        return dictPpp

    def fromDict(self, dictPpp):
        self.pppId = dictPpp['pppId']
        self.cnpj = dictPpp['cnpj']
        self.nomeEmpresa = dictPpp['nomeEmpresa']
        self.cnae = dictPpp['cnae']
        self.sitEmpregado = dictPpp['sitEmpregado']
        self.nit = dictPpp['nit']
        self.dataNascimento = dictPpp['dataNascimento']
        self.genero = dictPpp['genero']
        self.ctps = dictPpp['ctps']
        self.dataAdminssao = dictPpp['dataAdminssao']
        self.dataRegistro = dictPpp['dataRegistro']
        self.numCAT = dictPpp['numCAT']
        self.profissiografiaData = dictPpp['profissiografiaData']
        self.profissiografiaDesc = dictPpp['profissiografiaDesc']
        self.exposicaoDataInicio = dictPpp['exposicaoDataInicio']
        self.exposicaoDataFim = dictPpp['exposicaoDataFim']
        self.exposicaoTipo = dictPpp['exposicaoTipo']
        self.exposicaoFator = dictPpp['exposicaoFator']
        self.exposicaoIntensidade = dictPpp['exposicaoIntensidade']
        self.exposicaoTecnicaUtilizada = dictPpp['exposicaoTecnicaUtilizada']
        self.eficEpc = dictPpp['eficEpc']
        self.eficEpi = dictPpp['eficEpi']
        self.caEpi = dictPpp['caEpi']
        self.dataUltAlt = dictPpp['dataUltAlt']
        return self

    def fromList(self, listCliente: list, retornaInst: bool = True):
        self.pppId = listCliente[0]
        self.cnpj = listCliente[1]
        self.nomeEmpresa = listCliente[2]
        self.cnae = listCliente[3]
        self.sitEmpregado = listCliente[4]
        self.nit = listCliente[5]
        self.dataNascimento = listCliente[6]
        self.genero = listCliente[7]
        self.ctps = listCliente[8]
        self.dataAdminssao = listCliente[9]
        self.dataRegistro = listCliente[10]
        self.numCAT = listCliente[11]
        self.profissiografiaData = listCliente[12]
        self.profissiografiaDesc = listCliente[13]
        self.exposicaoDataInicio = listCliente[14]
        self.exposicaoDataFim = listCliente[15]
        self.exposicaoTipo = listCliente[16]
        self.exposicaoFator = listCliente[17]
        self.exposicaoIntensidade = listCliente[18]
        self.exposicaoTecnicaUtilizada = listCliente[19]
        self.eficEpc = listCliente[20]
        self.eficEpi = listCliente[21]
        self.caEpi = listCliente[22]
        self.dataUltAlt = listCliente[23]

        if retornaInst:
            return self

    def __repr__(self):
        return f"""PppModelo(
            pppId: {self.pppId},
            cnpj: {self.cnpj},
            nomeEmpresa: {self.nomeEmpresa},
            cnae: {self.cnae},
            sitEmpregado: {self.sitEmpregado},
            nit: {self.nit},
            dataNascimento: {self.dataNascimento},
            genero: {self.genero},
            ctps: {self.ctps},
            dataAdminssao: {self.dataAdminssao},
            dataRegistro: {self.dataRegistro},
            numCAT: {self.numCAT},
            profissiografiaData: {self.profissiografiaData},
            profissiografiaDesc: {self.profissiografiaDesc},
            exposicaoDataInicio: {self.exposicaoDataInicio},
            exposicaoDataFim: {self.exposicaoDataFim},
            exposicaoTipo: {self.exposicaoTipo},
            exposicaoFator: {self.exposicaoFator},
            exposicaoIntensidade: {self.exposicaoIntensidade},
            exposicaoTecnicaUtilizada: {self.exposicaoTecnicaUtilizada},
            eficEpc: {self.eficEpc},
            eficEpi: {self.eficEpi},
            caEpi: {self.caEpi},
            dataUltAlt: {self.dataUltAlt}
        )"""
