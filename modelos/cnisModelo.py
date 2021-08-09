import re
import pandas as pd
from pathlib import Path
from typing import List

from PyPDF3 import PdfFileReader
from PyQt5.QtWidgets import QFileDialog

from helpers import strToFloat, dictIndicadores


class CNISModelo:

    def __init__(self, path: str = None):
        self.nitCliente = None
        self.cpfCliente = None
        self.nomeCliente = None
        self.dataNascimento = None
        self.nomeMae = None
        self.getInfo = True
        self.documento = None

        self.expRegData = "[0-1]{1}[0-9]{1}/[0-9]{4}"
        self.expRegDataMenor = "^[0-9]{2}/[0-9]{4}$"
        self.expRegDataMaior = "^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
        self.expRegNomeEmp = "^[A-Z]{2,20}"
        self.expRegNB = "[0-9]{10}"
        self.expRegEspecie = "[0-9]{0,3} - [A-Z]{2,40}"
        self.expRegCNPJ = "[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}"
        self.expRegNit = "[0-9]{3}\.[0-9]{5}\.[0-9]{2}-[0-9]{1}"
        self.expRegCPF = "[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}"
        self.expRegTipoVinculo = "[A-Z]{1}[a-z]{2,20}"
        self.expRegSalarioP = "[0-9]{1,4},[0-9]{2}"
        self.expRegSalarioM = "[0-9]{1,3}.[0-9]{1,3},[0-9]{2}"
        self.expRegSalarioG = "[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3},[0-9]{2}"
        self.situacoesPossiveis = ['ativo', 'indeferido', 'suspenso', 'cessado']

        self.infoASerPulada = ['NIT', 'Código Emp.', 'Origem do Vínculo', 'Data Fim', 'Tipo Filiado no Vínculo',
                               'Últ. Remun.', 'Indicadores', 'NB', 'Espécie', 'Situação', 'Relações Previdenciárias',
                               'Competência']

        self.qtdPaginas = 0

        self.dictIndicadores: dict = dictIndicadores
        self.dictRemuneracoes = {
            'seq': [],
            'remuneracao': [],
            'competencia': [],
            'indicadores': []
        }
        self.dictContribuicoes = {
            'seq': [],
            'competencia': [],
            'dataPagamento': [],
            'contribuicao': [],
            'salContribuicao': [],
            'indicadores': []
        }
        self.dictCabecalho = {
            'seq': [],
            'nit': [],
            'cdEmp': [],
            'nomeEmp': [],
            'dataInicio': [],
            'dataFim': [],
            'tipoVinculo': [],
            'indicadores': [],
            'ultRem': []
        }
        self.dictCabecalhoBeneficio = {
            'seq': [],
            'nit': [],
            'NB': [],
            'orgVinculo': [],
            'especie': [],
            'dataInicio': [],
            'dataFim': [],
            'situacao': []
        }
        self.dictDadosPessoais = {
            'nit': None,
            'nomeCompleto': None,
            'dataNascimento': None,
            'cpf': None,
            'nomeMae': None
        }

        self.pathCnis = path

    def carregaDoc(self, path: str):
        self.documento = PdfFileReader(open(path, 'rb'))
        self.qtdPaginas = self.documento.numPages

    def carregaDados(self):

        for pg in range(self.qtdPaginas):
            blocoRemuneracoes = False
            blocoContribuicoes = False
            pos = 0

            documentoLinhas = self.documento.getPage(pg).extractText().split('\n')

            if pg == 0:
                pos = self.extraiDadosPessoais(documentoLinhas)

            while pos in range(pos, len(documentoLinhas) - 1):
                if documentoLinhas[pos] == 'Remunerações':
                    blocoRemuneracoes = True
                    blocoContribuicoes = False
                if documentoLinhas[pos] == 'Contribuições':
                    blocoContribuicoes = True
                    blocoRemuneracoes = False

                if blocoContribuicoes and documentoLinhas[pos] != 'Contribuições':
                    pos = self.extrairContribuicoes(documentoLinhas, pos)
                    blocoContribuicoes = False

                elif blocoRemuneracoes and documentoLinhas[pos] != 'Remunerações':
                    pos = self.extrairRemueracoes(documentoLinhas, pos)
                    blocoRemuneracoes = False

                elif documentoLinhas[pos] == 'Seq.':
                    pos = self.trataExtrairCabecalhos(documentoLinhas, pos)

                pos += 1

    def trataExtrairCabecalhos(self, documentoLinhas, posInicio):
        if any(filter(lambda item: re.fullmatch(self.expRegNB, item), documentoLinhas[posInicio:posInicio+16])):
            return self.extrairCabecalhosBeneficio(documentoLinhas, posInicio)
        else:
            return self.extrairCabecalhosPadrao(documentoLinhas, posInicio)

    def extrairCabecalhosPadrao(self, documentoLinhas, posInicio):

        seq = False
        nit = False
        cdEmp = False
        orgVinculo = False
        dataInicio = False
        dataFim = False
        tipoVinculo = False
        indicadores = False
        ultRem = False

        pos = posInicio
        dataPos = 1
        nomeEmp = ''

        for j in range(pos + 1, pos + 10):
            if documentoLinhas[j] not in self.infoASerPulada:

                if re.fullmatch(self.expRegNit, documentoLinhas[j]) is not None:
                    self.dictCabecalho['nit'].append(documentoLinhas[j])
                    nit = True
                elif re.fullmatch(self.expRegCNPJ, documentoLinhas[j]) is not None:
                    self.dictCabecalho['cdEmp'].append(documentoLinhas[j])
                    cdEmp = True
                # elif documentoLinhas[j] in self.dictIndicadores.keys():
                elif self.isIndicador(documentoLinhas[j]):
                    self.dictCabecalho['indicadores'].append(documentoLinhas[j])
                    indicadores = True
                elif re.match(self.expRegNomeEmp, documentoLinhas[j]) is not None and documentoLinhas[j]:
                    nomeEmp += documentoLinhas[j]
                    orgVinculo = True
                elif re.match(self.expRegDataMaior, documentoLinhas[j]):
                    if dataPos == 1:
                        self.dictCabecalho['dataInicio'].append(documentoLinhas[j])
                        dataPos += 1
                        dataInicio = True
                    else:
                        self.dictCabecalho['dataFim'].append(documentoLinhas[j])
                        dataFim = True
                        dataPos = 0
                elif re.match(self.expRegDataMenor, documentoLinhas[j]) is not None:
                    self.dictCabecalho['ultRem'].append(documentoLinhas[j])
                    ultRem = True
                elif re.match(self.expRegTipoVinculo, documentoLinhas[j]) is not None:
                    pularInfo = documentoLinhas[j]
                    if pularInfo not in self.infoASerPulada:
                        self.dictCabecalho['tipoVinculo'].append(documentoLinhas[j].replace(',', ''))
                        tipoVinculo = True
                elif documentoLinhas[j][0].isnumeric() and len(documentoLinhas[j]) <= 3:
                    self.dictCabecalho['seq'].append(documentoLinhas[j])
                    seq = True

        self.dictCabecalho['nomeEmp'].append(nomeEmp)
        if dataPos != 0:
            self.dictCabecalho['dataFim'].append('')
            dataFim = True

        if not seq:
            self.dictCabecalho['seq'].append('')
        if not nit:
            self.dictCabecalho['nit'].append('')
        if not cdEmp:
            self.dictCabecalho['cdEmp'].append('')
        # if not orgVinculo:
        #     self.dictCabecalho['orgVinculo'].append('')
        if not dataInicio:
            self.dictCabecalho['dataInicio'].append('')
        if not dataFim:
            self.dictCabecalho['dataFim'].append('')
        if not tipoVinculo:
            self.dictCabecalho['tipoVinculo'].append('')
        if not indicadores:
            self.dictCabecalho['indicadores'].append('')
        if not ultRem:
            self.dictCabecalho['ultRem'].append('')

        return pos + 10

    def extrairCabecalhosBeneficio(self, documentoLinhas, posInicio):

        seq = False
        nit = False
        nb = False
        orgVinculo = False
        dataFim = False
        situacao = False
        especie = False
        dataInicio = False

        pos = posInicio
        dataPos = 1

        for j in range(pos + 1, pos + 10):
            if documentoLinhas[j] not in self.infoASerPulada and documentoLinhas[j] not in self.dictIndicadores.keys():

                if re.fullmatch(self.expRegNit, documentoLinhas[j]) is not None:
                    self.dictCabecalhoBeneficio['nit'].append(documentoLinhas[j])
                    nit = True
                elif re.fullmatch(self.expRegNB, documentoLinhas[j]) is not None:
                    self.dictCabecalhoBeneficio['NB'].append(documentoLinhas[j])
                    nb = True
                elif re.match(self.expRegNomeEmp, documentoLinhas[j]) is not None and documentoLinhas[j].lower() in self.situacoesPossiveis:
                    self.dictCabecalhoBeneficio['situacao'].append(documentoLinhas[j])
                    situacao = True
                elif re.match(self.expRegDataMaior, documentoLinhas[j]):
                    if dataPos == 1:
                        self.dictCabecalhoBeneficio['dataInicio'].append(documentoLinhas[j])
                        dataPos += 1
                        dataInicio = True
                    else:
                        self.dictCabecalhoBeneficio['dataFim'].append(documentoLinhas[j])
                        dataFim = True
                        dataPos = 0
                elif documentoLinhas[j][0].isnumeric() and len(documentoLinhas[j]) <= 3:
                    self.dictCabecalhoBeneficio['seq'].append(documentoLinhas[j])
                    seq = True
                elif re.match(self.expRegEspecie, documentoLinhas[j]) is not None and documentoLinhas[j] not in self.situacoesPossiveis:
                    if re.match(self.expRegNomeEmp, documentoLinhas[j+1]) and documentoLinhas[j+1] not in self.situacoesPossiveis:
                        self.dictCabecalhoBeneficio['especie'].append(documentoLinhas[j] + ' ' + documentoLinhas[j+1])
                        pos += 1
                    else:
                        self.dictCabecalhoBeneficio['especie'].append(documentoLinhas[j])
                    especie = True
                elif re.match(self.expRegTipoVinculo, documentoLinhas[j]) is not None and documentoLinhas[j].lower() not in self.situacoesPossiveis:
                    self.dictCabecalhoBeneficio['orgVinculo'].append(documentoLinhas[j])
                    orgVinculo = True

        if dataPos != 0:
            self.dictCabecalhoBeneficio['dataFim'].append('')
            dataFim = True

        if not seq:
            self.dictCabecalhoBeneficio['seq'].append('')
        if not nit:
            self.dictCabecalhoBeneficio['nit'].append('')
        if not nb:
            self.dictCabecalhoBeneficio['NB'].append('')
        if not orgVinculo:
            self.dictCabecalhoBeneficio['orgVinculo'].append('')
        if not especie:
            self.dictCabecalhoBeneficio['especie'].append('')
        if not situacao:
            self.dictCabecalhoBeneficio['situacao'].append('')
        if not dataInicio:
            self.dictCabecalhoBeneficio['dataInicio'].append('')
        if not dataFim:
            self.dictCabecalhoBeneficio['dataFim'].append('')

        return posInicio + 10

    def extrairContribuicoes(self, documentoLinhas, posInicio):

        blocoContribuicoes = True
        ehContribuicao = False
        seq = self.dictCabecalho['seq'][-1]
        contSeq = 0

        pos = posInicio

        while blocoContribuicoes:

            if blocoContribuicoes and documentoLinhas[pos] != 'Contribuições':

                if re.fullmatch(self.expRegDataMenor, documentoLinhas[pos]) is not None:
                    self.dictContribuicoes['competencia'].append(documentoLinhas[pos])
                    contSeq += 1
                elif re.fullmatch(self.expRegDataMaior, documentoLinhas[pos]) is not None:
                    self.dictContribuicoes['dataPagamento'].append(documentoLinhas[pos])
                elif self.verificaSalario(documentoLinhas[pos]):
                    if ehContribuicao:
                        self.dictContribuicoes['contribuicao'].append(strToFloat(documentoLinhas[pos]))
                        if not self.verificaSalario(documentoLinhas[pos+1]):
                            ehContribuicao = False
                            if documentoLinhas[pos+1].replace(',', '') not in self.dictIndicadores.keys():
                                if re.fullmatch(self.expRegDataMenor, documentoLinhas[pos+1]) is None:
                                    blocoContribuicoes = False
                    else:
                        self.dictContribuicoes['salContribuicao'].append(strToFloat(documentoLinhas[pos]))
                        if documentoLinhas[pos + 1].replace(',', '') not in self.dictIndicadores.keys():
                            self.dictContribuicoes['indicadores'].append('')
                        if self.verificaSalario(documentoLinhas[pos+1]):
                            ehContribuicao = True
                elif documentoLinhas[pos].replace(',', '') in self.dictIndicadores.keys():
                    if documentoLinhas[pos+1] in self.dictIndicadores.keys():
                        self.dictContribuicoes['indicadores'].append(documentoLinhas[pos] + ' ' + documentoLinhas[pos+1])
                        pos += 1
                        if self.verificaSalario(documentoLinhas[pos+1]):
                            ehContribuicao = True
                        elif re.fullmatch(self.expRegDataMenor, documentoLinhas[pos+1]) is None:
                            blocoContribuicoes = False
                    else:
                        self.dictContribuicoes['indicadores'].append(documentoLinhas[pos])
                        if self.verificaSalario(documentoLinhas[pos+1]):
                            ehContribuicao = True
                        elif re.fullmatch(self.expRegDataMenor, documentoLinhas[pos+1]) is None:
                            blocoContribuicoes = False

            pos += 1

        # Adiciona o Seq de cada contribuição no dicionário de contribuições
        for i in range(contSeq):
            self.dictContribuicoes['seq'].append(seq)
        return pos

    def extrairRemueracoes(self, documentoLinhas, posInicio):

        blocoRemuneracoes = True
        pos = posInicio
        seq = self.dictCabecalho['seq'][-1]
        contSeq = 0

        while blocoRemuneracoes:

            if re.fullmatch(self.expRegData, documentoLinhas[pos]) != None:
                self.dictRemuneracoes['competencia'].append(documentoLinhas[pos])
                contSeq += 1
            elif documentoLinhas[pos][0].isnumeric():
                self.dictRemuneracoes['remuneracao'].append(strToFloat(documentoLinhas[pos]))
                if documentoLinhas[pos + 1].split(',')[0] not in self.dictIndicadores.keys():
                    self.dictRemuneracoes['indicadores'].append('')
                    if not documentoLinhas[pos + 1][0].isnumeric():
                        blocoRemuneracoes = False
            elif documentoLinhas[pos].split(',')[0] in self.dictIndicadores.keys():
                indicadores = (documentoLinhas[pos] + documentoLinhas[pos + 1]).split(',')

                if indicadores[0].strip() in self.dictIndicadores.keys():
                    if indicadores[1].strip() in self.dictIndicadores.keys():
                        self.dictRemuneracoes['indicadores'].append(
                            documentoLinhas[pos] + documentoLinhas[pos + 1])
                        documentoLinhas[pos + 1] = 'pula'
                    else:
                        self.dictRemuneracoes['indicadores'].append(documentoLinhas[pos])
                        if re.fullmatch(self.expRegData, documentoLinhas[pos + 1]) == None:
                            blocoRemuneracoes = False
                else:
                    self.dictRemuneracoes['indicadores'].append(documentoLinhas[pos])
            elif documentoLinhas[pos] == 'pula':
                pass
            else:
                blocoRemuneracoes = False

            pos += 1

        # Adiciona o Seq de cada contribuição no dicionário de contribuições
        for i in range(contSeq):
            self.dictRemuneracoes['seq'].append(seq)
        return pos

    def extraiDadosPessoais(self, documentoLinhas: str):
        read = False
        nomeCliente = False
        infoAPular = ['NIT:', 'CPF:', 'Nome:', 'Data de nascimento:', 'Nome da mãe:']

        posicaoAtual = None

        for pos in range(20):
            posicaoAtual = pos
            if documentoLinhas[pos] == 'NIT:':
                read = True

            if read and documentoLinhas[pos] not in infoAPular:
                if re.fullmatch(self.expRegNit, documentoLinhas[pos]) is not None:
                    self.dictDadosPessoais['nit'] = documentoLinhas[pos]
                elif re.fullmatch(self.expRegCPF, documentoLinhas[pos]) is not None:
                    self.dictDadosPessoais['cpf'] = documentoLinhas[pos]
                elif re.match(self.expRegNomeEmp, documentoLinhas[pos]) is not None:
                    if not nomeCliente:
                        self.dictDadosPessoais['nomeCompleto'] = documentoLinhas[pos]
                        nomeCliente = True
                    else:
                        self.dictDadosPessoais['nomeMae'] = documentoLinhas[pos]
                elif re.fullmatch(self.expRegDataMaior, documentoLinhas[pos]) is not None:
                    self.dictDadosPessoais['dataNascimento'] = documentoLinhas[pos]

        return posicaoAtual

    def gerarDataframe(self, informacao: str = 'cabecalhos'):

        if informacao.lower() == 'cabecalhos':
            return pd.DataFrame(self.dictCabecalho)
        elif informacao.lower() == 'cabecalhosbeneficio':
            return pd.DataFrame(self.dictCabecalhoBeneficio)
        elif informacao.lower() == 'remuneracoes':
            return pd.DataFrame(self.dictRemuneracoes)
        elif informacao.lower() == 'contribuicoes':
            return pd.DataFrame(self.dictContribuicoes)
        elif informacao.lower() == 'indicadores':
            return pd.DataFrame.from_dict(self.dictIndicadores, orient='index', columns=['Descrição'])
        else:
            return None

    def gerarCsv(self, path, informacao: str = 'cabecalhos'):
        df = self.gerarDataframe(informacao=informacao)
        df.to_csv(path)

    def buscaPath(self):
        home = str(Path.home())
        pathAux = None

        # Ambiente de desenvolvimento
        pathAux = QFileDialog.getOpenFileName(directory=home, options=QFileDialog.DontUseNativeDialog)

        # Ambiente de produção
        # pathAux = QFileDialog.getOpenFileName(directory=home)

        if pathAux[0] is not None and pathAux[0] != '':
            self.pathCnis = pathAux[0]

        if self.pathCnis is not None and self.pathCnis != '':
            self.carregaDoc(self.pathCnis)
            self.carregaDados()
            return self.pathCnis
        else:
            return None

    def getInfoPessoais(self, dataFrame: bool = False):
        if dataFrame:
            return pd.DataFrame.from_dict(self.dictDadosPessoais, orient='index', columns=['Descrição'])
        else:
            return self.dictDadosPessoais

    def isIndicador(self, info: str) -> bool:
        if ',' in info:
            return info[:info.find(',')] in self.dictIndicadores.keys()
        else:
            return info in self.dictIndicadores.keys()

    def getAllDict(self, toInsert: bool = False, clienteId: int = 0) -> dict:
        if toInsert:
            return {
                'cabecalho': self.dictCabecalho,
                'cabecalhoBeneficio': self.dictCabecalhoBeneficio,
                'remuneracoes': self.organizaParaInserir(self.dictRemuneracoes, clienteId),
                'contribuicoes': self.organizaParaInserir(self.dictContribuicoes, clienteId)
            }
        else:
            return {
                'cabecalho': self.dictCabecalho,
                'cabecalhoBeneficio': self.dictCabecalhoBeneficio,
                'remuneracoes': self.dictRemuneracoes,
                'contribuicoes': self.dictContribuicoes
            }

    def verificaSalario(self, salario: str):
        salarioP = re.match(self.expRegSalarioP, salario) is not None
        salarioM = re.match(self.expRegSalarioM, salario) is not None
        salarioG = re.match(self.expRegSalarioG, salario) is not None
        return salarioP or salarioM or salarioG

    def organizaParaInserir(self, dicionario: dict, clienteId: int):
        dicionariosRetorno: List[dict] = []
        qtdInfo: int = len(list(dicionario.values())[0])
        chaves: List[str] = list(dicionario.keys())

        for index in range(qtdInfo):
            dicionariosRetorno.append({
                chave: dicionario[chave][index] for chave in chaves
            })
            dicionariosRetorno[index]['clienteId'] = clienteId
        return dicionariosRetorno

    def __str__(self):
        dtRemuneracoes: pd.DataFrame = self.gerarDataframe(informacao='remuneracoes')
        dtContribuicoes: pd.DataFrame = self.gerarDataframe(informacao='contribuicoes')
        dtBeneficios: pd.DataFrame = self.gerarDataframe(informacao='cabecalhosbeneficio')

        return f"""
        ---------------------------------------------------------------
        = Nome Completo : {self.dictDadosPessoais['nomeCompleto']}
        = CPF : {self.dictDadosPessoais['cpf']}
        = Nome da mãe : {self.dictDadosPessoais['nomeMae']}
        ---------------------------------------------------------------
        DataFrame(Remuneracoes): {dtRemuneracoes.info}
        DataFrame(Contribuições): {dtContribuicoes.info}
        DataFrame(Benefícios): {dtBeneficios.info}"""
