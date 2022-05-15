import json
import os
import geocoder
import datetime
from typing import List
from pathlib import Path

from docx.shared import Pt
from docxtpl import DocxTemplate, InlineImage
from jinja2 import Environment, FileSystemLoader, Template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

from modelos.configGeraisORM import ConfigGerais
from systemLog.logs import NewLogging

from modelos.clienteORM import Cliente
from modelos.clienteProfissao import ClienteProfissao
from modelos.escritoriosORM import Escritorios
from modelos.advogadoORM import Advogados
from modelos.itemContribuicao import ItemContribuicao
from modelos.processosORM import Processos

from util.helpers.dateHelper import strToDatetime
from util.enums.processoEnums import TipoBeneficioEnum
from util.enums.geracaoDocumentos import EnumDocumento
from util.helpers.helpers import mascaraCep, mascaraTelCel, strTipoProcesso, mascaraCPF, mascaraMeses, getEstados, mascaraRG, strTipoBeneFacilitado, regraAposentadoria
from util.helpers.dateHelper import mascaraDataPequena
from util.popUps import popUpOkAlerta

from cache.cachingLogin import CacheLogin
from cache.cacheEscritorio import CacheEscritorio

from dateutil.relativedelta import relativedelta


class GeracaoDocumentos:
    dirCliente: str

    def __init__(self, procModel: Processos, clientModel: Cliente):
        self.cacheLogin = CacheLogin()
        self.cacheEscritorio = CacheEscritorio()
        self.apiLogger = NewLogging().buscaLogger()

        self.advogado = self.getAdvogado()
        self.escritorio = self.getEscritorio()
        self.processo = procModel
        self.cliente = clientModel
        self.configGerais: ConfigGerais = self.buscaConfigGerais()

        self.infoProfissional: ClienteProfissao = self.getinfoProfissional()

        self.pathDocumento = self.configGerais.pathDocGerados
        self.pathTemplate = os.path.join(os.getcwd(), '.templates')
        self.pathTemplateAtual = ''
        self.pathConteudo = ''
        self.nomeArquivoSaida = ''
        self.dirCliente = f'{self.cliente.clienteId}-{self.cliente.nomeCliente}'
        self.documento: DocxTemplate

        self.strCidadeAtual = self.getCidadeAtual()

        self.dictInfo: dict = {}
        if not self.verificaPathOk():
            self.criaDiretorioCliente()

        # self.buscaPastaUsuario()

    def ajeitaTblItensContrib(self, itens: List[ItemContribuicao]) -> list:
        listaItensTbl: list = []
        for item in itens:
            listaItensTbl.append([
                f"{mascaraDataPequena(item.competencia)}",
                f"R$ {item.contribuicao}",
            ])

        return listaItensTbl

    def buscaConfigGerais(self) -> ConfigGerais:
        try:
            return ConfigGerais.select().where(ConfigGerais.advogadoId == self.advogado.advogadoId).get()
        except Exception as err:
            self.apiLogger.error('Não foi possível encontrar as configurações do advogado.', extra={"err": err})
            popUpOkAlerta("Não foi possível encontrar as configurações do sistema. Entre em contato com o suporte.")
            return None

    def buscaPastaUsuario(self):
        listaDiretorios: list = os.listdir()

        for d in listaDiretorios:
            print(f"d -> {d}")

    def buscaPathCss(self, tipoDocumento: EnumDocumento):
        pathCss = ''

        if tipoDocumento == EnumDocumento.procuracao:
            pathCss = os.path.join(self.pathTemplate, 'css', 'procuracaoStyles.css')

        elif tipoDocumento == EnumDocumento.decHipossuficiencia:
            pathCss = os.path.join(self.pathTemplate, 'css', 'decHipossuficienciaStyles.css')

        elif tipoDocumento == EnumDocumento.docsComprobatorios:
            pathCss = os.path.join(self.pathTemplate, 'css', 'docsComprobatorios.css')

        if os.path.isfile(pathCss):
            return pathCss
        else:
            raise Exception()

    def buscaPathResetCss(self):
        pathCss = os.path.join(self.pathTemplate, 'css', 'reset.css')
        return pathCss

    def carregaTemplate(self, tipoDocumento: EnumDocumento):
        if not os.path.isfile(self.pathTemplateAtual):
            self.apiLogger.error("Não encontrou o template desejado", extra={"URI": self.pathTemplateAtual})
            raise FileNotFoundError('Não encontrou o template desejado')

        pathTemplateHtml: str = os.path.join(self.pathTemplate, 'html')
        nomeTemplate: str = ''
        if tipoDocumento == EnumDocumento.procuracao:
            nomeTemplate = 'procuracao.html'
        elif tipoDocumento == EnumDocumento.decHipossuficiencia:
            nomeTemplate = 'decHipossuficiencia.html'
        elif tipoDocumento == EnumDocumento.docsComprobatorios:
            nomeTemplate = 'docsComprobatorios.html'

        try:
            temp = FileSystemLoader(searchpath=pathTemplateHtml)
            environment = Environment(loader=temp)
            jTemplate: Template = environment.get_template(nomeTemplate)
            return jTemplate

        except Exception as err:
            self.apiLogger.error("Não foi possível gerar o template", extra={"err": err})
            raise SyntaxError('Deu merda, maninho...')
            
    def criaContratoHonorarios(self):
        self.nomeArquivoSaida += f"Contrato de honorários.docx"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'contratoHonorarios.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraCorpoContrato()
        self.geraRodape()
        self.finalizaDocumento(EnumDocumento.honorarios)
        self.limparConfiguracoes()

    def criaConteudoEspecifico(self):
        pathConteudoEspecifico: str = self.getPathConteudo(soConteudo=True)

        tipoBeneEspecifico: list = [
            TipoBeneficioEnum.BeneIdoso.value,
            TipoBeneficioEnum.BeneDeficiencia.value
        ]

        if self.processo.tipoBeneficio.tipoId in tipoBeneEspecifico:
            self.dictInfo['conteudoEspecifico'] = []
        else:
            pathConteudoEspecifico = os.path.join(pathConteudoEspecifico, 'conteudoEspecifico.json')

            with open(pathConteudoEspecifico, encoding='utf-8', mode='r') as f:
                conteudoDict: dict = json.load(f)

            if self.processo.tipoBeneficio.tipoId == TipoBeneficioEnum.Aposentadoria.value:
                conteudoEspecifico = conteudoDict['Aposentadoria'][regraAposentadoria(self.processo.regraAposentadoria).name]
                if len(conteudoEspecifico.splitlines()) == 1:
                    conteudoEspecifico = [conteudoEspecifico]
            else:
                conteudoEspecifico = conteudoDict[TipoBeneficioEnum(self.processo.tipoBeneficio.tipoId).name].splitlines()

            if isinstance(conteudoEspecifico, str):
                self.dictInfo['conteudoEspecifico'] = [conteudoEspecifico]
            else:
                self.dictInfo['conteudoEspecifico'] = conteudoEspecifico

    def criaDiretorioCliente(self):
        pathAtual: Path = Path(self.configGerais.pathDocGerados)
        pathAtual = pathAtual / self.dirCliente
        pathAtual.mkdir(parents=True, exist_ok=True)

    def criaDeclaracaoHipo(self):
        # self.nomeArquivoSaida += f"Declaração de hipossuficiência.docx"
        self.nomeArquivoSaida += f"Declaração de hipossuficiência.pdf"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'html', 'decHipossuficiencia.html')

        self.geraCabecalho()
        self.geraCorpoDeclaracaoHipo()
        self.geraRodape()
        self.finalizaDocumento(EnumDocumento.decHipossuficiencia)
        self.limparConfiguracoes()

    def criaDecPensao(self):
        self.nomeArquivoSaida += f"Declaração recebimento de pensão.docx"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'decPensaoApos.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraCorpoDeclaracaoPensao()
        self.geraRodape()
        self.finalizaDocumento(EnumDocumento.decPensionista)
        self.limparConfiguracoes()

    def criaDocumentosComprobatorios(self):
        self.nomeArquivoSaida += f'Doc comprobatorios.pdf'
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'html', 'docsComprobatorios.html')
        self.pathConteudo = self.getPathConteudo()

        self.geraCabecalho()
        self.geraSessaoInicialDocComp()
        self.geraConteudoGeral()
        self.criaConteudoEspecifico()
        self.geraRodape()
        self.finalizaDocumento(EnumDocumento.docsComprobatorios)
        self.limparConfiguracoes()

    def criaRequerimentoAdm(self, itens: List[ItemContribuicao]):
        self.nomeArquivoSaida += f"Requerimento admnistrativo.docx"
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'requerimentoAdm.docx')
        self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()

        self.geraCorpoInicio()
        self.geraDosFatos(itens)
        self.geraDosFundJurid()

        self.geraRodape()
        self.finalizaDocumento(EnumDocumento.requerimento)
        self.limparConfiguracoes()

    def criaProcuracao(self):
        # self.nomeArquivoSaida += f'Procuração.docx'
        self.nomeArquivoSaida += f'Procuração.pdf'
        self.pathTemplateAtual = os.path.join(self.pathTemplate, 'html', 'procuracao.html')
        # self.documento = DocxTemplate(self.pathTemplateAtual)

        self.geraCabecalho()
        self.geraCorpoProcuracao()
        self.geraRodape()
        self.finalizaDocumento(EnumDocumento.procuracao)
        self.limparConfiguracoes()
        
    def finalizaDocumento(self, tipoDocumento: EnumDocumento):
        if not self.verificaPathOk():
            self.criaDiretorioCliente()

        nomeArquivoSaida = str(Path(self.pathDocumento) / self.dirCliente / self.nomeArquivoSaida)
        template = self.carregaTemplate(tipoDocumento)
        pathStyles = self.buscaPathCss(tipoDocumento)

        build = template.render(self.dictInfo)

        htmlNewPrev = HTML(string=build, base_url=self.pathTemplate)
        cssStyles = CSS(filename=pathStyles)
        fontConfig = FontConfiguration()
        htmlNewPrev.write_pdf(nomeArquivoSaida, stylesheets=[cssStyles], font_config=fontConfig)

    def geraConteudoGeral(self):
        self.dictInfo['conteudoGeral']: list = []

        try:
            with open(self.pathConteudo, 'r') as f:
                listaConteudo: list = f.readlines()

            for linha in listaConteudo:
                self.dictInfo['conteudoGeral'].append(linha.lstrip().replace('\n', ''))

        except IsADirectoryError as err:
            print(f"geraConteudoGeral - {err=}")
            self.apiLogger.error("Erro ao buscar o diretório de conteúdo geral.", extra={"err": err})

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
        self.dictInfo['nomeAdvogado'] = self.advogado.nomeAdvogado
        self.dictInfo['sobrenomeAdvogado'] = self.advogado.sobrenomeAdvogado
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
            
    def geraCabecalho(self):
        # logo = InlineImage(self.documento, os.path.join(os.getcwd(), 'Resources', 'd3-grey.png'), Pt(24))
        logo = os.path.join(os.getcwd(), '.templates', 'img', 'Logo DJ.jpg')

        self.dictInfo['nomeFantasia'] = self.escritorio.nomeFantasia
        self.dictInfo['endereco'] = self.escritorio.endereco
        self.dictInfo['numero'] = self.escritorio.numero
        self.dictInfo['cep'] = mascaraCep(self.escritorio.cep)
        self.dictInfo['telefone'] = mascaraTelCel(self.escritorio.telefone)
        self.dictInfo['emailEscritorio'] = self.escritorio.email
        self.dictInfo['logo'] = logo

    def geraSessaoInicialDocComp(self):

        self.dictInfo['nomeAdvogado'] = self.advogado.nomeAdvogado
        self.dictInfo['sobrenomeAdvogado'] = self.advogado.sobrenomeAdvogado
        self.dictInfo['tipoProcesso'] = strTipoProcesso(self.processo.tipoProcesso)
        self.dictInfo['tipoBeneficio'] = strTipoBeneFacilitado(self.processo.tipoBeneficio.tipoId)

    def geraCorpoProcuracao(self):
        estadoSigla: str = getEstados()[self.cliente.estado]
        siglaEscritorioEstado: str = self.escritorio.estado

        # Informações do cliente
        self.dictInfo['nomeCliente'] = self.cliente.nomeCliente
        self.dictInfo['sobrenomeCliente'] = self.cliente.sobrenomeCliente
        self.dictInfo['nacionalidade'] = 'brasileiro(a)'
        self.dictInfo['estadoCivil'] = self.cliente.estadoCivil
        self.dictInfo['profissao'] = self.infoProfissional.nomeProfissao
        self.dictInfo['rg'] = mascaraRG(self.cliente.rgCliente)
        self.dictInfo['estadoSigla'] = estadoSigla
        self.dictInfo['email'] = self.cliente.email
        self.dictInfo['cpf'] = mascaraCPF(self.cliente.cpfCliente)
        self.dictInfo['endereco'] = self.cliente.endereco
        self.dictInfo['cidade'] = self.cliente.cidade
        self.dictInfo['numero'] = self.cliente.numero
        self.dictInfo['bairro'] = self.cliente.bairro

        # Informações do advogado
        self.dictInfo['nomeAdvogado'] = self.advogado.nomeAdvogado
        self.dictInfo['sobrenomeAdvogado'] = self.advogado.sobrenomeAdvogado
        self.dictInfo['nacionalidadeAdvogado'] = self.advogado.nacionalidade
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
        self.dictInfo['tipoBeneficio'] = strTipoBeneFacilitado(self.processo.tipoBeneficio)

        # Informações sobre a localidade atual
        self.dictInfo['cidadeAtual'] = self.strCidadeAtual
        self.dictInfo['dataAtual'] = mascaraMeses(datetime.datetime.now())

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
        self.dictInfo['dataNascimentoCliente'] = mascaraMeses(strToDatetime(self.cliente.dataNascimento))
        self.dictInfo['enderecoCliente'] = self.cliente.endereco
        self.dictInfo['numeroCliente'] = self.cliente.numero
        self.dictInfo['bairroCliente'] = self.cliente.bairro
        self.dictInfo['cidadeCliente'] = self.cliente.cidade
        self.dictInfo['siglaEstadoCliente'] = siglaEstadoCliente
        self.dictInfo['cepCliente'] = mascaraCep(self.cliente.cep)
        self.dictInfo['emailCliente'] = self.cliente.email

        # Conteúdo referente ao contratado (Advogado)
        self.dictInfo['nomeAdvogado'] = self.advogado.nomeAdvogado
        self.dictInfo['sobrenomeAdvogado'] = self.advogado.sobrenomeAdvogado
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

    def geraDosFatos(self, itensContribuicao: List[ItemContribuicao]):
        # listaTempoContribuicao = calculaDiaMesAno(self.processo.tempoContribuicao)
        # TODO: Data usada para teste
        tempoContrib = relativedelta(years=25, months=10)

        self.dictInfo['idadeCliente'] = self.cliente.idade
        self.dictInfo['pontosCliente'] = tempoContrib.years + self.cliente.idade

        self.dictInfo['diasContribuicao'] = f"e 0 dias"
        self.dictInfo['mesesContribuicao'] = f"{tempoContrib.months} meses"
        self.dictInfo['anosContribuicao'] = f"{tempoContrib.years} anos"

        if len(itensContribuicao) > 0:
            self.dictInfo['tblCabecalho'] = ["Competência", "Contribuição"]
            self.dictInfo['contribuicoes'] = self.ajeitaTblItensContrib(itensContribuicao)

    def geraDosFundJurid(self):
        pass

    def geraCorpoDeclaracaoHipo(self):

        # Conteúdo referente ao cliente
        self.dictInfo['nomeCliente'] = self.cliente.nomeCliente
        self.dictInfo['sobrenomeCliente'] = self.cliente.sobrenomeCliente
        self.dictInfo['estadoCivilCliente'] = self.cliente.estadoCivil
        self.dictInfo['profissaoCliente'] = self.infoProfissional.nomeProfissao
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
        self.dictInfo['telefoneEscritorio'] = mascaraTelCel(self.escritorio.telefone)
        self.dictInfo['emailEscritorio'] = self.escritorio.email
        self.dictInfo['enderecoEscritorio'] = self.escritorio.endereco
        self.dictInfo['numeroEscritorio'] = self.escritorio.numero
        self.dictInfo['cepEscritorio'] = mascaraCep(self.escritorio.cep)

    def getPathConteudo(self, soConteudo: bool = False) -> str:
        strPathConteudo: str = os.path.join(self.pathTemplate, 'conteudo')
        beneMaisGenericos: list = [
            TipoBeneficioEnum.Aposentadoria.value,
            TipoBeneficioEnum.AuxDoenca.value,
            TipoBeneficioEnum.AuxReclusao.value
        ]
        if soConteudo:
            return strPathConteudo
        elif self.processo.tipoBeneficio.tipoId in beneMaisGenericos:
            strPathConteudo = os.path.join(strPathConteudo, 'docGerais.txt')

        elif self.processo.tipoBeneficio.tipoId == TipoBeneficioEnum.BeneIdoso.value:
            strPathConteudo = os.path.join(strPathConteudo, 'docIdoso.txt')

        elif self.processo.tipoBeneficio.tipoId == TipoBeneficioEnum.BeneDeficiencia.value:
            strPathConteudo = os.path.join(strPathConteudo, 'docDeficiencia.txt')

        return strPathConteudo

    def getAdvogado(self) -> Advogados:
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

    def getEscritorio(self) -> Escritorios:
        escritorio = self.cacheEscritorio.carregarCache()
        if not escritorio:
            return self.cacheEscritorio.carregarCacheTemporario()
        return escritorio

    def getinfoProfissional(self) -> ClienteProfissao:
        try:
            self.apiLogger.debug("Buscando info profissional para gerar documentos")
            return ClienteProfissao.get_by_id(self.cliente.clienteId)
        except Exception as err:
            print(f"getinfoProfissional: {err}")
            self.apiLogger.error("Não conseguiu econtrar as informações profissionais", extra={"err": err})
    
    def limparConfiguracoes(self):
        self.dictInfo = {}
        self.nomeArquivoSaida = ''

    def verificaPathOk(self) -> bool:
        pathAtual = Path(self.configGerais.pathDocGerados) / self.dirCliente
        return pathAtual.exists() and pathAtual.is_dir()


if __name__ == '__main__':
    processo = Processos()
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

    cliente = Cliente()
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
