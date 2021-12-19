from enum import Enum


class TelaPosicao(Enum):
    Cliente = 0
    Resumo = 1
    Configuracoes = 2
    Ferramentas = 3
    Entrevista = 4
    InformacoesGerais = 5
    Calculos = 6
    Processo = 7


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