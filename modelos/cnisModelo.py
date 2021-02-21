import re
import pandas as pd
import os
from pathlib import Path

from PyPDF3 import PdfFileReader
from PyQt5.QtWidgets import QFileDialog


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
        self.expRegCNPJ = "[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}"
        self.expRegNit = "[0-9]{3}\.[0-9]{5}\.[0-9]{2}-[0-9]{1}"
        self.expRegCPF = "[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}"
        self.expRegTipoVinculo = "[A-Z]{1}[a-z]{2,20}"

        self.infoASerPulada = ['NIT', 'Código Emp.', 'Origem do Vínculo', 'Data Fim', 'Tipo Filiado no Vínculo',
                               'Últ. Remun.', 'Indicadores']

        self.qtdPaginas = 0

        self.dictIndicadores = {
            'AEXT-VI': 'Acerto de vínculo extemporâneo indeferido.',
            'AEXT-VT': 'Acerto de vínculo extemporâneo validado totalmente.',
            'AVRC-DEF': 'Acerto de vínculo extemporâneo deferido.',
            'IEAN': 'Exposição a agentes nocivos no grupo 25 anos.',
            'IGFIP-INF': 'Indicador de GFIP meramente informativa.',
            'ILEI123': 'Contribuição da competência foi recolhida com código da Lei Complementar 123/2006. (Plano simplificado de Previdência).',
            'IMEI': 'Contribuição da competência foi recolhida com código MEI.',
            'IREC-CIRURAL': 'Recolhimento com código de CI Rural sem homologação.',
            'IREC-FBR': 'Recolhimento facultativo baixa renda.',
            'IREC-INDPEND': 'Recolhimentos com indicadores e/ou pendências.',
            'IREC-LC123': 'Recolhimentos para fins da LC 123.',
            'IREC-LC123-SUP': 'Recolhimento / Complementação LC 123 superior ao salário mínimo.',
            'PADM-EMPR': 'Inconsistência temporal, admissão anterior ao início da atividade do empregador.',
            'PEMP-CAD': 'Falta de informações cadastrais do CNPJ ou CEI.',
            'PEXT': 'Pendência de vínculo extemporâneo não tratado.',
            'PREC-COD1821': 'Recolhimento com código de pagamento 1821 – Mandato Eletivo.',
            'PREC-CSE': 'Recolhimento GPS de Segurado Especial Pendente Comprovação.',
            'PREC-FBR': 'Recolhimento facultativo baixa renda não validado / homologado.',
            'PREC-FBR-ANT': 'Recolhimento facultativo baixa renda anterior a comp. 09/2011.',
            'PREC-LC123-ANT': 'Recolhimento com código da LC 123 anterior à competência 04/2007.',
            'PREC-MENOR-MIN': 'Recolhimento realizado é inferior ao valor mínimo.',
            'PREC-PMIG-DOM': 'Recolhimento inclusive sal.mat., e/ou período declarado empregado doméstico sem registro de vínculo.',
            'PRECFACULTCONC': 'Recolhimento ou período atividade de contribuinte facultativo concomitante com outro TFV.',
            'PREM-EMPR': 'Remuneração antes do início da atividade do empregador.',
            'PREM-EXT': 'Remuneração da competência é extemporânea.',
            'PREM-FVIN': 'Remunerações posteriores ao fim do vínculo de trabalho.',
            'PREM-RET': 'Remuneração de prestador de serviço declarada em GFIP mas que não é considerada.',
            'PVIN-IRREG': 'Pendência de Vínculo Irregular.'
        }
        self.dictRemuneracoes = {
            'remuneracao': [],
            'competencia': [],
            'indicadores': []
        }
        self.dictContribuicoes = {
            'competencia': [],
            'dataPagamento': [],
            'contribuicao': [],
            'salContribuicao': [],
            'indicadores': []
        }
        self.dictCabecalho = {
            'Seq': [],
            'NIT': [],
            'cdEmp': [],
            'nomeEmp': [],
            'dataInicio': [],
            'dataFim': [],
            'tipoVinculo': [],
            'indicadores': [],
            'ultRem': []
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
                    pos = self.extrairCabecalhos(documentoLinhas, pos)

                pos += 1

    def extrairContribuicoes(self, documentoLinhas, posInicio):

        blocoContribuicoes = True
        proxContribuicao = False
        auxContribuicoes = 1

        pos = posInicio

        while blocoContribuicoes:

            if blocoContribuicoes and documentoLinhas[pos] != 'Contribuições':

                # Calcula blocos de contribuições
                if proxContribuicao:
                    self.dictContribuicoes['contribuicao'].append(documentoLinhas[pos])
                    proxContribuicao = len(re.findall(self.expRegData, documentoLinhas[pos + 1])) == 0 and \
                                       documentoLinhas[pos + 1][0].isnumeric()
                    auxContribuicoes = 1
                else:
                    if documentoLinhas[pos][0].isnumeric():
                        if auxContribuicoes == 1:
                            self.dictContribuicoes['competencia'].append(documentoLinhas[pos])
                        elif auxContribuicoes == 2:
                            self.dictContribuicoes['dataPagamento'].append(documentoLinhas[pos])
                        elif auxContribuicoes == 3:
                            self.dictContribuicoes['salContribuicao'].append(documentoLinhas[pos])
                            proxContribuicao = len(re.findall(self.expRegData, documentoLinhas[pos + 1])) == 0 and \
                                               documentoLinhas[pos + 1][0].isnumeric()
                            if documentoLinhas[pos + 1][0].isnumeric():
                                self.dictContribuicoes['indicadores'].append('')
                                auxContribuicoes = 0

                        auxContribuicoes += 1
                    elif documentoLinhas[pos] in self.dictIndicadores.keys():
                        self.dictContribuicoes['indicadores'].append(documentoLinhas[pos])
                        proxContribuicao = len(re.findall(self.expRegData, documentoLinhas[pos + 1])) == 0
                        if not proxContribuicao:
                            auxContribuicoes = 1
                        else:
                            auxContribuicoes += 1
                    else:
                        auxContribuicoes = 1
                        blocoContribuicoes = False
                        proxContribuicao = False
            pos += 1
        return pos

    def extrairRemueracoes(self, documentoLinhas, posInicio):

        blocoRemuneracoes = True
        pos = posInicio

        while blocoRemuneracoes:
            if re.fullmatch(self.expRegData, documentoLinhas[pos]) != None:
                self.dictRemuneracoes['competencia'].append(documentoLinhas[pos])
            elif documentoLinhas[pos][0].isnumeric():
                self.dictRemuneracoes['remuneracao'].append(documentoLinhas[pos])
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
        return pos

    def extrairCabecalhos(self, documentoLinhas, posInicio):

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

        for j in range(pos + 1, pos + 9):
            if re.fullmatch(self.expRegNit, documentoLinhas[j]) is not None:
                self.dictCabecalho['NIT'].append(documentoLinhas[j])
                nit = True
            elif re.fullmatch(self.expRegCNPJ, documentoLinhas[j]) is not None:
                self.dictCabecalho['cdEmp'].append(documentoLinhas[j])
                cdEmp = True
            elif re.match(self.expRegNomeEmp, documentoLinhas[j]) is not None and documentoLinhas[j] not in self.infoASerPulada:
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
                    self.dictCabecalho['tipoVinculo'].append(documentoLinhas[j])
                    tipoVinculo = True
            elif documentoLinhas[j][0].isnumeric():
                self.dictCabecalho['Seq'].append(documentoLinhas[j])
                seq = True

        self.dictCabecalho['nomeEmp'].append(nomeEmp)
        if dataPos != 0:
            self.dictCabecalho['dataFim'].append('')
            dataFim = True

        if not seq:
            self.dictCabecalho['Seq'].append('')
        if not nit:
            self.dictCabecalho['NIT'].append('')
        if not cdEmp:
            self.dictCabecalho['cdEmp'].append('')
        if not orgVinculo:
            self.dictCabecalho['orgVinculo'].append('')
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

        return pos + 9

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

        if informacao == 'cabecalhos':
            return pd.DataFrame(self.dictCabecalho)
        elif informacao == 'remuneracoes':
            return pd.DataFrame(self.dictRemuneracoes)
        elif informacao == 'contribuicoes':
            return pd.DataFrame(self.dictContribuicoes)
        elif informacao == 'indicadores':
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

    def getInfoPessoais(self, dataFrame: bool = False):
        if dataFrame:
            return pd.DataFrame.from_dict(self.dictDadosPessoais, orient='index', columns=['Descrição'])
        else:
            return self.dictDadosPessoais
