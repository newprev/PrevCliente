from enum import Enum


class EtapaCadastraCliente(Enum):
    pessoal = 0
    profissional = 1
    bancarias = 2
    finaliza = 3

class Navegacao(Enum):
    anterior = 0
    proximo = 1

class TelaPosicao(Enum):
    Cliente = 0
    Resumo = 1
    Configuracoes = 2
    Entrevista = 3
    Ferramentas = 4
    InformacoesGerais = 5
    Calculos = 6
    Processo = 7

class TelaAtual(Enum):
    Cliente = 0
    CadastroCliente = 1
    InfoCliente = 2
    Entrevista = 3

class Icone(Enum):
    cliente = ':/funcionalidade/blueCliente.png'
    resumo = ':/ferramentas/blueResumoCNIS.png'
    entrevista = ':/funcionalidade/blueInterview.png'
    processos = ':/funcionalidade/blueProcessos.png'
    indicadores = ':/ferramentas/blueResumoCNIS.png'
    ipca = ':/ferramentas/blueIndices.png'
    tetos = ':/ferramentas/blueCalculadora.png'
    expSobrevida = ':/ferramentas/blueIndices.png'
    configSistema = ':/configuracoes/settingsDarker.png'

class TextoBotao(Enum):
    cliente = 'Cliente'
    resumo = 'Resumo CNIS'
    entrevista = 'Entrevista'
    processos = 'Processos'
    indicadores = 'Indicadores'
    ipca = 'IPCA mensal'
    tetos = 'Tetos prev.'
    expSobrevida = 'Expectativa sobrevida'
    configSistema = 'Sistema'