from enum import Enum


class FerramentasEInfo(Enum):
    convMon = 0         # Conversão monetária
    expSobrevida = 1    # Expexctativa de sobrevida
    indicadores = 2     # Indicadores do CNIS
    tetos = 3           # Tetos monetários
    carenciasLei91 = 4  # Carências de contribuições desde 1991 até 2019
    atuMonetaria = 5    # Atualizações monetárias
    salarioMinimo = 6   # Atualizações Salários mínimmos desde 1994
    ipca = 7            # Ipca mensal
    tipoBeneficio = 8   # Tipos de benefício
