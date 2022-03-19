from enum import Enum


class AtivApos(Enum):
    laborInsalubre = 0
    laborDeficiente = 1
    tempoMilitar = 2
    regimeProprio = 3
    tempoRural = 4
    professor = 5
    contribMenorSalMin = 6
    contribBaixaRenda = 7
    onzePorCento = 8
    indicativoCnis = 9
    editarCnis = 10
    editarCnisB = 11
    faltaLaborCnis = 12
    acaoTrabalhista = 13
    aprendiz = 14
    seminarista = 15


class ContribSimulacao(Enum):
    ULTI = 'REPETE O ÚLTIMO SALÁRIO'
    TETO = 'TETO PREVIDENCIÁRIO'
    SMIN = 'SALÁRIO MÍNIMO'
    MANU = 'VALOR DEFINIDO MANUALMENTE'


class DireitoAdquirido(Enum):
    lei821391 = 0
    lei987699 = 1
    ec1032019 = 2


class FatorTmpInsalubridade(Enum):
    # Fatores para sexo masculino
    baixoM = 1.4
    medioM = 1.75
    altoM = 2.33

    # Fatore para sexo feminino
    baixoF = 1.2
    medioF = 1.5
    altoF = 2.0


class GrauDeficiencia(Enum):
    baixo = 0
    medio = 1
    alto = 2

class IndiceReajuste(Enum):
    Selic = 'Selic'
    Ipca = 'Ipca'
    Igpm = 'Igpm'
    Ibovespa = 'Ibovespa'


class RegraTransicao(Enum):
    todas = 0
    pontos = 1
    reducaoIdadeMinima = 2
    pedagio50 = 3
    reducaoTempoContribuicao = 4
    pedagio100 = 5


class RegraGeralAR(Enum):
    fator85_95 = 0
    idade = 1
    tempoContribuicao = 2


class SubTipoAposentadoria(Enum):
    Idade = 0
    Rural = 1
    Deficiencia = 2
    Especial = 3
    TempoContrib = 4
    Invalidez = 5


class TelaAtiva(Enum):
    BuscaCliente = 0
    BuscaProcesso = 1

    # Sessão Geral
    Geral = 2

    # Sessão Aposentadoria
    Aposentadoria = 3

    # Sessão Gerar documentos
    Procuracao = 4
    DocsComp = 5
    DecHipo = 6


class TipoAposentadoria(Enum):
    tempoContribAR = 'TCAR'   # Tempo de contribuição antes da reforma
    idadeAR = 'IDAR'          # Idade antes da reforma
    redIdadeMinima = 'RIDM'   # Redução da idade mínima
    redTempoContrib = 'RETC'  # Redução do tempo de contribuição
    pedagio50 = 'PD50'        # Pedágio de 50%
    pedagio100 = 'P100'       # Pedágio de 50%
    pontos = 'POTR'           # Pontos pela regra de transição
    regra8595 = '8595'        # Pontos pela regra 85/95









