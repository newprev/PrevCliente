import json
import os
import geocoder
import datetime

from docx.shared import Pt
from docxtpl import DocxTemplate, InlineImage

from modelos.clienteModelo import ClienteModelo
from modelos.escritorioModelo import EscritorioModelo
from modelos.advogadoModelo import AdvogadoModelo
from modelos.processosModelo import ProcessosModelo
from helpers import mascaraCep, mascaraTelCel, strTipoBeneficio, strTipoProcesso, mascaraCPF, mascaraMeses, getEstados, mascaraRG, strToDatetime

from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio

from newPrevEnums import NaturezaProcesso, TipoProcesso, TipoBeneficio, SubTipoAposentadoria, TamanhoData


class DocEntrevista:

    def __init__(self, procModel: ProcessosModelo, clientModel: ClienteModelo):
        self.cacheLogin = CacheLogin()
        self.cacheEscritorio = CacheEscritorio()

        self.advogado = self.getAdvogado()
        self.escritorio = self.getEscritorio()
        self.processo = procModel
        self.cliente = clientModel

        self.pathDocumento = os.path.join(os.getcwd(), 'DocGerados')
        self.pathTemplate = os.path.join(os.getcwd(), '.templates')
        self.pathTemplateAtual = ''
        self.pathConteudo = ''
        self.nomeArquivoSaida = f'{self.cliente.clienteId}'
        self.documento: DocxTemplate

        self.strCidadeAtual = self.getCidadeAtual()

        self.dictInfo: dict = {}

        # self.buscaPastaUsuario()

    def buscaPastaUsuario(self):
        listaDiretorios: list = os.listdir()

        for d in listaDiretorios:
            print(f"d -> {d}")

    def geraCabecalho(self):
        logo = InlineImage(self.documento, os.path.join(os.getcwd(), 'Resources', 'd3-grey.png'), Pt(24))

        self.dictInfo['nomeFantasia'] = self.escritorio.nomeFantasia
        self.dictInfo['endereco'] = self.escritorio.endereco
        self.dictInfo['numero'] = self.escritorio.numero
        self.dictInfo['cep'] = mascaraCep(self.escritorio.cep)
        self.dictInfo['telefone'] = mascaraTelCel(self.escritorio.telefone)
        self.dictInfo['emailEscritorio'] = self.escritorio.email
        self.dictInfo['logo'] = logo

    def geraSessaoInicialDocComp(self):

        self.dictInfo['nomeUsuario'] = self.advogado.nomeUsuario
        self.dictInfo['sobrenomeUsuario'] = self.advogado.sobrenomeUsuario
        self.dictInfo['tipoProcesso'] = strTipoProcesso(self.processo.tipoProcesso)
        self.dictInfo['tipoBeneficio'] = strTipoBeneficio(self.processo.tipoBeneficio, self.processo.subTipoApos)

    def geraCorpoProcuracao(self):
        estadoSigla: str = getEstados()[self.cliente.estado]
        siglaEscritorioEstado: str = self.escritorio.estado

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
        self.dictInfo['siglaEscritorioEstado'] = siglaEscritorioEstado
        self.dictInfo['enderecoEscritorio'] = self.escritorio.endereco
        self.dictInfo['escritorioNum'] = self.escritorio.numero
        self.dictInfo['bairroEscritorio'] = self.escritorio.bairro
        self.dictInfo['cidadeEscritorio'] = self.escritorio.cidade
        self.dictInfo['estadoEscritorio'] = self.escritorio.estado

        # Informações do processo
        self.dictInfo['tipoBeneficio'] = strTipoBeneficio(self.processo.tipoBeneficio, self.processo.subTipoApos)

        # Informações sobre a localidade atual
        self.dictInfo['cidadeAtual'] = self.strCidadeAtual
        self.dictInfo['dataAtual'] = mascaraMeses(datetime.datetime.now())

    def finalizaDocumento(self):
        self.documento.render(self.dictInfo)
        self.documento.save(os.path.join(self.pathDocumento, self.nomeArquivoSaida))

    def criaDocumentosComprobatorios(self):
        self.nomeArquivoSaida += f' - Doc comprobatorios.docx'
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'documentosNecessarios.docx')
        self.pathConteudo = self.getPathConteudo()
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraSessaoInicialDocComp()
        self.criaConteudoGeral()
        self.criaConteudoEspecifico()
        self.geraRodape()
        self.finalizaDocumento()
        self.limparConfiguracoes()

    def criaContratoHonorarios(self):
        self.nomeArquivoSaida += f" - Contrato de honorários.docx"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'contratoHonorarios.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraCorpoContrato()
        self.geraRodape()
        self.finalizaDocumento()
        self.limparConfiguracoes()
        
    def criaRequerimentoAdm(self):
        self.nomeArquivoSaida += f" - Requerimento admnistrativo.docx"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'requerimentoAdm.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()

        self.geraCorpoInicio()
        self.geraDosFatos()
        self.geraDosFundJurid()

        self.geraRodape()
        self.finalizaDocumento()
        self.limparConfiguracoes()

    def geraCorpoInicio(self):

        siglaEstadoCliente: str = getEstados()[self.cliente.estado]
        siglaEstadoEscritorio: str = self.escritorio.estado

        if not isinstance(self.advogado.email, list) and not isinstance(self.advogado.email, tuple):
            emailAdvogado = self.advogado.email
        else:
            if not isinstance(self.advogado.email[0], list) and not isinstance(self.advogado.email[0], tuple):
                emailAdvogado = self.advogado.email[0]
            else:
                emailAdvogado = self.advogado.email[0][0]

        # Conteúdo referente ao contratante (cliente)
        self.dictInfo['nomeCliente'] = self.cliente.nomeCliente
        self.dictInfo['sobrenomeCliente'] = self.cliente.sobrenomeCliente
        self.dictInfo['nacionalidadeCliente'] = 'brasileiro(a)'
        self.dictInfo['profissaoCliente'] = self.cliente.profissao
        self.dictInfo['rgCliente'] = mascaraRG(self.cliente.rgCliente)
        self.dictInfo['cpfCliente'] = mascaraCPF(self.cliente.cpfCliente)
        self.dictInfo['nomeMaeCliente'] = self.cliente.nomeMae
        self.dictInfo['dataNascimentoCliente'] = mascaraMeses(strToDatetime(self.cliente.dataNascimento, TamanhoData.gg))
        self.dictInfo['enderecoCliente'] = self.cliente.endereco
        self.dictInfo['numeroCliente'] = self.cliente.numero
        self.dictInfo['bairroCliente'] = self.cliente.bairro
        self.dictInfo['cidadeCliente'] = self.cliente.cidade
        self.dictInfo['siglaEstadoCliente'] = siglaEstadoCliente
        self.dictInfo['cepCliente'] = mascaraCep(self.cliente.cep)
        self.dictInfo['emailCliente'] = self.cliente.email

        # Conteúdo referente ao contratado (Advogado)
        self.dictInfo['nomeAdvogado'] = self.advogado.nomeUsuario
        self.dictInfo['sobrenomeAdvogado'] = self.advogado.sobrenomeUsuario
        self.dictInfo['nacionalidadeAdvogado'] = 'brasileiro(a)'
        self.dictInfo['estadoCivilAdvogado'] = self.advogado.estadoCivil
        self.dictInfo['siglaEstadoAdvogado'] = siglaEstadoEscritorio
        self.dictInfo['numeroOAB'] = self.advogado.numeroOAB
        self.dictInfo['emailAdvogado'] = emailAdvogado

        # Conteúdo referente ao escritório
        self.dictInfo['bairroEscritorio'] = self.escritorio.bairro
        self.dictInfo['cidadeEscritorio'] = self.escritorio.cidade
        self.dictInfo['estadoEscritorio'] = self.escritorio.estado
        self.dictInfo['estadoEscritorio'] = self.escritorio.estado

    def geraDosFatos(self):

        self.dictInfo['idadeCliente'] = self.cliente.idade
        self.dictInfo['tempoContribuicao'] = int(round(self.processo.tempoContribuicao/12, 0))
        self.dictInfo['pontosCliente'] = int(round(self.processo.tempoContribuicao/12, 0)) + self.cliente.idade

    def geraDosFundJurid(self):
        pass

    def geraCorpoContrato(self):

        siglaEstadoCliente: str = getEstados()[self.cliente.estado]
        siglaEstadoEscritorio: str = self.escritorio.estado

        # Conteúdo referente ao contratante (cliente)
        self.dictInfo['nomeCliente'] = self.cliente.nomeCliente
        self.dictInfo['sobrenomeCliente'] = self.cliente.sobrenomeCliente
        self.dictInfo['nacionalidadeCliente'] = 'brasileiro(a)'
        self.dictInfo['profissaoCliente'] = self.cliente.profissao
        self.dictInfo['estadoCivilCliente'] = self.cliente.estadoCivil
        self.dictInfo['rgCliente'] = mascaraRG(self.cliente.rgCliente)
        self.dictInfo['cpfCliente'] = mascaraCPF(self.cliente.cpfCliente)
        self.dictInfo['enderecoCliente'] = self.cliente.endereco
        self.dictInfo['numeroCliente'] = self.cliente.numero
        self.dictInfo['bairroCliente'] = self.cliente.bairro
        self.dictInfo['cidadeCliente'] = self.cliente.cidade
        self.dictInfo['siglaEstadoCliente'] = siglaEstadoCliente
        self.dictInfo['cepCliente'] = mascaraCep(self.cliente.cep)

        # Conteúdo referente ao contratado (Advogado)
        self.dictInfo['nomeAdvogado'] = self.advogado.nomeUsuario
        self.dictInfo['sobrenomeAdvogado'] = self.advogado.sobrenomeUsuario
        self.dictInfo['nacionalidadeAdvogado'] = 'brasileiro(a)'
        self.dictInfo['siglaEstadoAdvogado'] = siglaEstadoEscritorio
        self.dictInfo['numeroOAB'] = self.advogado.numeroOAB

        # Conteúdo referente ao Escritório
        self.dictInfo['enderecoEscritorio'] = self.escritorio.endereco
        self.dictInfo['numeroEscritorio'] = self.escritorio.numero
        self.dictInfo['bairroEscritorio'] = self.escritorio.bairro
        self.dictInfo['cidadeEscritorio'] = self.escritorio.cidade
        self.dictInfo['siglaEstadoEscritorio'] = siglaEstadoEscritorio
        self.dictInfo['telefoneEscritorio'] = mascaraTelCel(self.escritorio.telefone)
        self.dictInfo['emailEscritorio'] = self.escritorio.email
        self.dictInfo['cepEscritorio'] = mascaraCep(self.escritorio.cep)

        # Conteúdo referente ao documento
        self.dictInfo['cidadeAtual'] = self.strCidadeAtual
        self.dictInfo['dataAtual'] = mascaraMeses(datetime.datetime.now())

    def criaDeclaracaoHipo(self):
        self.nomeArquivoSaida += f" - Declaração de hipossuficiência.docx"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'decHipossuficiencia.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraCorpoDeclaracaoHipo()
        self.geraRodape()
        self.finalizaDocumento()
        self.limparConfiguracoes()

    def geraCorpoDeclaracaoHipo(self):

        # Conteúdo referente ao cliente
        self.dictInfo['nomeCliente'] = self.cliente.nomeCliente
        self.dictInfo['sobrenomeCliente'] = self.cliente.sobrenomeCliente
        self.dictInfo['estadoCivilCliente'] = self.cliente.estadoCivil
        self.dictInfo['profissaoCliente'] = self.cliente.profissao
        self.dictInfo['rgCliente'] = mascaraRG(self.cliente.rgCliente)
        self.dictInfo['cpfCliente'] = mascaraCPF(self.cliente.cpfCliente)
        self.dictInfo['enderecoCliente'] = self.cliente.endereco
        self.dictInfo['numeroCliente'] = self.cliente.numero
        self.dictInfo['bairroCliente'] = self.cliente.bairro
        self.dictInfo['cidadeCliente'] = self.cliente.cidade
        self.dictInfo['estadoCliente'] = self.cliente.estado
        self.dictInfo['cepCliente'] = mascaraCep(self.cliente.cep)
        self.dictInfo['emailCliente'] = self.cliente.email

        # Conteúdo referente ao documento
        self.dictInfo['cidadeAtual'] = self.strCidadeAtual
        self.dictInfo['dataAtual'] = mascaraMeses(datetime.datetime.now())

    def criaDecPensao(self):
        self.nomeArquivoSaida += f" - Declaração recebimento de pensão.docx"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'decPensaoApos.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraCorpoDeclaracaoPensao()
        self.geraRodape()
        self.finalizaDocumento()
        self.limparConfiguracoes()

    def geraCorpoDeclaracaoPensao(self):

        # Conteúdo referente ao cliente
        self.dictInfo['nomeCliente'] = self.cliente.nomeCliente
        self.dictInfo['sobrenomeCliente'] = self.cliente.sobrenomeCliente
        self.dictInfo['cpfCliente'] = mascaraCPF(self.cliente.cpfCliente)
        self.dictInfo['rgCliente'] = mascaraRG(self.cliente.rgCliente)
        self.dictInfo['cidadeCliente'] = self.cliente.cidade
        self.dictInfo['valorBeneficio'] = '45,00'

        # Conteúdo referente ao documento
        self.dictInfo['cidadeAtual'] = self.strCidadeAtual
        self.dictInfo['dataAtual'] = mascaraMeses(datetime.datetime.now())

    def geraRodape(self):

        # Conteúdo referente ao escritório
        self.dictInfo['telefoneEscritorio'] = self.escritorio.telefone
        self.dictInfo['emailEscritorio'] = self.escritorio.email
        self.dictInfo['enderecoEscritorio'] = self.escritorio.endereco
        self.dictInfo['numeroEscritorio'] = self.escritorio.numero
        self.dictInfo['cepEscritorio'] = self.escritorio.cep

    def getPathConteudo(self, soConteudo: bool = False) -> str:
        strPathConteudo: str = os.path.join(self.pathTemplate, 'conteudo')
        beneMaisGenericos: list = [
            TipoBeneficio.Aposentadoria.value,
            TipoBeneficio.AuxDoenca.value,
            TipoBeneficio.AuxReclusao.value
        ]
        if soConteudo:
            return strPathConteudo
        elif self.processo.tipoBeneficio in beneMaisGenericos:
            strPathConteudo = os.path.join(strPathConteudo, 'docGerais.txt')
        elif self.processo.tipoBeneficio == TipoBeneficio.BeneIdoso.value:
            strPathConteudo = os.path.join(strPathConteudo, 'docIdoso.txt')
        elif self.processo.tipoBeneficio == TipoBeneficio.BeneDeficiencia.value:
            strPathConteudo = os.path.join(strPathConteudo, 'docDeficiencia.txt')

        return strPathConteudo

    def criaConteudoGeral(self):
        self.dictInfo['conteudoGeral']: list = []

        with open(self.pathConteudo, 'r') as f:
            listaConteudo: list = f.readlines()

        for linha in listaConteudo:
            self.dictInfo['conteudoGeral'].append(linha.lstrip().replace('\n', ''))

    def criaConteudoEspecifico(self):
        pathConteudoEspecifico: str = self.getPathConteudo(soConteudo=True)

        tipoBeneEspecifico: list = [
            TipoBeneficio.BeneIdoso.value,
            TipoBeneficio.BeneDeficiencia.value
        ]

        if self.processo.tipoBeneficio in tipoBeneEspecifico:
            self.dictInfo['conteudoEspecifico'] = []
        else:
            pathConteudoEspecifico = os.path.join(pathConteudoEspecifico, 'conteudoEspecifico.json')

            with open(pathConteudoEspecifico, encoding='utf-8', mode='r') as f:
                conteudoDict: dict = json.load(f)

            if self.processo.tipoBeneficio == TipoBeneficio.Aposentadoria.value:
                conteudoEspecifico = conteudoDict['Aposentadoria'][SubTipoAposentadoria(self.processo.subTipoApos).name]
                if len(conteudoEspecifico.splitlines()) == 1:
                    conteudoEspecifico = [conteudoEspecifico]
            else:
                conteudoEspecifico = conteudoDict[TipoBeneficio(self.processo.tipoBeneficio).name].splitlines()

            self.dictInfo['conteudoEspecifico'] = conteudoEspecifico

    def gerarProcuracao(self):
        self.nomeArquivoSaida += f' - Procuração.docx'
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'procuracao.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraCorpoProcuracao()
        self.geraRodape()
        self.finalizaDocumento()
        self.limparConfiguracoes()

    def limparConfiguracoes(self):
        self.dictInfo = {}
        self.nomeArquivoSaida = f'{self.cliente.clienteId}'

    def getAdvogado(self) -> AdvogadoModelo:
        adv = self.cacheLogin.carregarCache()
        if not adv:
            return self.cacheLogin.carregarCacheTemporario()
        return adv

    def getCidadeAtual(self) -> str:
        cidadeAtualGeo = geocoder.ip('me')

        if cidadeAtualGeo.address is not None:
            return cidadeAtualGeo.address[:cidadeAtualGeo.address.find(',')]
        else:
            return self.escritorio.cidade

    def getEscritorio(self) -> EscritorioModelo:
        escritorio = self.cacheEscritorio.carregarCache()
        if not escritorio:
            return self.cacheEscritorio.carregarCacheTemporario()
        return escritorio


if __name__ == '__main__':
    import sys
    processo = ProcessosModelo()
    processo.tipoProcesso = 2
    processo.tipoBeneficio = 3
    processo.natureza = 2
    processo.estado = 'SP'
    processo.clienteId = 2
    processo.cidade = 'São Paulo'
    processo.advogadoId = 1
    processo.valorCausa = 1000000
    processo.dataInicio = datetime.datetime.now()
    processo.dataFim = datetime.datetime.now()
    processo.dataCadastro = datetime.datetime.now()
    processo.dataUltAlt = datetime.datetime.now()

    cliente = ClienteModelo()
    cliente.nomeCliente = 'Fulano'
    cliente.sobrenomeCliente = 'de Tal'
    cliente.numero = '12'
    cliente.numeroConta = '9851'
    cliente.numCartProf = 'edcx'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'
    cliente.nomeCliente = 'Fulano'


    docClass = DocEntrevista(
        ProcessosModelo()
    )
