import os
import geocoder
import datetime

from docx.shared import Pt
from docxtpl import DocxTemplate, InlineImage

from modelos.clienteModelo import ClienteModelo
from modelos.escritorioModelo import EscritorioModelo
from modelos.advogadoModelo import AdvogadoModelo
from modelos.processosModelo import ProcessosModelo
from helpers import mascaraCep, mascaraTelCel, strNatureza, strTipoBeneficio, strTipoProcesso, mascaraCPF, mascaraMeses, getEstados, mascaraRG

from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio

from newPrevEnums import NaturezaProcesso, TipoProcesso, TipoBeneficio


class DocEntrevista:

    def __init__(self, procModel: ProcessosModelo, clientModel: ClienteModelo):
        self.cacheLogin = CacheLogin()
        self.cacheEscritorio = CacheEscritorio()

        self.advogado = self.getAdvogado()
        self.escritorio = self.getEscritorio()
        self.processo = procModel
        self.cliente = clientModel

        self.pathDocumento = os.path.join(os.getcwd(), 'DocGerados')
        self.templatesPath = os.path.join(os.getcwd(), '.templates')
        self.pathTemplate = ''
        self.nomeArquivo = f'{self.cliente.clienteId}'
        self.documento: DocxTemplate

        self.dictInfo: dict = {}

    def criaCabecalho(self):
        logo = InlineImage(self.documento, os.path.join(os.getcwd(), 'Resources', 'd3-grey.png'), Pt(24))

        self.dictInfo['nomeFantasia'] = self.escritorio.nomeFantasia
        self.dictInfo['endereco'] = self.escritorio.endereco
        self.dictInfo['numero'] = self.escritorio.numero
        self.dictInfo['cep'] = mascaraCep(self.escritorio.cep)
        self.dictInfo['telefone'] = mascaraTelCel(self.escritorio.telefone)
        self.dictInfo['emailEscritorio'] = self.escritorio.email
        self.dictInfo['logo'] = logo

    def criaSessaoInicialDocComp(self):

        self.dictInfo['nomeUsuario'] = self.advogado.nomeUsuario
        self.dictInfo['sobrenomeUsuario'] = self.advogado.sobrenomeUsuario
        self.dictInfo['natureza'] = strNatureza(self.processo.natureza)
        self.dictInfo['tipoProcesso'] = strTipoProcesso(self.processo.tipoProcesso)
        self.dictInfo['tipoBeneficio'] = strTipoBeneficio(self.processo.tipoBeneficio)

    def criaCorpoProcuracao(self):
        cidadeAtualGeo = geocoder.ip('me')

        if cidadeAtualGeo.address is not None:
            strCidadeAtual = cidadeAtualGeo.address[:cidadeAtualGeo.address.find(',')]
        else:
            strCidadeAtual = self.escritorio.cidade
        estadoSigla: str = getEstados()[self.cliente.estado]

        # Informações do cliente
        self.dictInfo['nomeCliente'] = self.cliente.nomeCliente
        self.dictInfo['sobrenomeCliente'] = self.cliente.sobrenomeCliente
        self.dictInfo['nacionalidade'] = 'brasileiro(a)'
        self.dictInfo['estadoCivil'] = self.cliente.estadoCivil
        self.dictInfo['profissao'] = self.cliente.profissao
        self.dictInfo['rg'] = mascaraRG(self.cliente.rgCliente)
        self.dictInfo['estadoSigla'] = estadoSigla
        self.dictInfo['email'] = self.cliente.email
        self.dictInfo['cpf'] = mascaraCPF(self.cliente.cpfCliente)
        self.dictInfo['endereco'] = self.cliente.endereco
        self.dictInfo['cidade'] = self.cliente.cidade
        self.dictInfo['numero'] = self.cliente.numero
        self.dictInfo['bairro'] = self.cliente.bairro

        # Informações do advogado
        self.dictInfo['nomeUsuario'] = self.advogado.nomeUsuario
        self.dictInfo['sobrenomeUsuario'] = self.advogado.sobrenomeUsuario
        self.dictInfo['nacionalidade'] = self.advogado.nacionalidade
        self.dictInfo['estadoCivil'] = self.advogado.estadoCivil
        self.dictInfo['escritorioEstado'] = self.escritorio.estado
        self.dictInfo['numeroOAB'] = self.advogado.numeroOAB

        # Informações do escritório
        self.dictInfo['escritorioEnd'] = self.escritorio.endereco
        self.dictInfo['escritorioNum'] = self.escritorio.numero
        self.dictInfo['escritorioBairro'] = self.escritorio.bairro
        self.dictInfo['escritorioCidade'] = self.escritorio.cidade
        self.dictInfo['escritorioEstado'] = self.escritorio.estado

        # Informações do processo
        self.dictInfo['tipoBeneficio'] = strTipoBeneficio(self.processo.tipoBeneficio)

        # Informações sobre a localidade atual
        self.dictInfo['cidadeAtual'] = strCidadeAtual
        self.dictInfo['dataAtual'] = mascaraMeses(datetime.datetime.now())

    def finalizaDocumento(self):
        self.documento.render(self.dictInfo)
        self.documento.save(os.path.join(self.pathDocumento, self.nomeArquivo))

    def gerarDocumentosComprobatorios(self):
        self.nomeArquivo += f' - Doc comprobatorios.docx'
        self.pathTemplate = os.path.join(self.templatesPath, 'documentosNecessarios.docx')
        self.documento = DocxTemplate(self.pathTemplate)

        self.criaCabecalho()
        self.criaSessaoInicialDocComp()
        self.finalizaDocumento()
        self.limparConfiguracoes()

    def gerarProcuracao(self):
        self.nomeArquivo += f' - Procuração.docx'
        self.pathTemplate = os.path.join(self.templatesPath, 'procuracao.docx')
        self.documento = DocxTemplate(self.pathTemplate)

        self.criaCabecalho()
        self.criaCorpoProcuracao()
        self.finalizaDocumento()
        self.limparConfiguracoes()

    def limparConfiguracoes(self):
        self.dictInfo = {}
        self.nomeArquivo = f'{self.cliente.clienteId}'

    def getAdvogado(self) -> AdvogadoModelo:
        adv = self.cacheLogin.carregarCache()
        if not adv:
            return self.cacheLogin.carregarCacheTemporario()
        return adv

    def getEscritorio(self) -> EscritorioModelo:
        escritorio = self.cacheEscritorio.carregarCache()
        if not escritorio:
            return self.cacheEscritorio.carregarCacheTemporario()
        return escritorio


