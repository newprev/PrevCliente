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
    Ferramentas = 3
    Entrevista = 4
    InformacoesGerais = 5
    Calculos = 6
    Processo = 7

class TelaAtual(Enum):
    Cliente = 0
    CadastroCliente = 1
    InfoCliente = 2

class Icone(Enum):
    cliente = 'url(:/funcionalidade/cliente.png)'
    resumo = 'url(:/funcionalidade/resumoCNIS.png)'
    entrevista = 'url(:/funcionalidade/interview.png)'
    processos = 'url(:/funcionalidade/processos.png)'

class TextoBotao(Enum):
    cliente = 'Cliente'
    resumo = 'Resumo CNIS'
    entrevista = 'Entrevista'
    processos = 'Processos'