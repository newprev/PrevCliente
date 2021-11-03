from enum import Enum


class TipoAposentadoria(Enum):
    tempoContribAR = 'TCAR'   # Tempo de contribuição antes da reforma
    idadeAR = 'IDAR'          # Idade antes da reforma
    redIdadeMinima = 'RIDM'   # Redução da idade mínima
    redTempoContrib = 'RETC'  # Redução do tempo de contribuição
    pedagio50 = 'PD50'        # Pedágio de 50%
    pedagio100 = 'P100'       # Pedágio de 50%
    pontos = 'POTR'           # Pontos pela regra de transição
    regra8595 = '8595'        # Pontos pela regra 85/95


class TipoSimulacao(Enum):
    ULTI = 'REPETE O ÚLTIMO SALÁRIO'
    TETO = 'TETO PREVIDENCIÁRIO'
    SMIN = 'SALÁRIO MÍNIMO'
    MANU = 'VALOR DEFINIDO MANUALMENTE'
