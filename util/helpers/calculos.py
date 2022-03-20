import datetime

from dateutil.relativedelta import relativedelta
from typing import List

from modelos.vinculoORM import CnisVinculos
from modelos.itemContribuicao import ItemContribuicao

from util.helpers.dateHelper import reformaNoPeriodo, strToDate, normalizaData
from util.enums.periodosImportantesEnum import Reformas


def tempoContribPorVinculo(listaVinculos: List[CnisVinculos]) -> relativedelta:
    tempoContribuicao: relativedelta = relativedelta()
    passouDataReforma: bool = False

    for vinculo in listaVinculos:
        if reformaNoPeriodo(vinculo.dataInicio, vinculo.dataFim, Reformas.reforma2019.value):
            # Antes da reforma
            tempoContribuicao += relativedelta(Reformas.reforma2019.value, strToDate(vinculo.dataInicio))
            # Depois da reforma
            tempAux = relativedelta(strToDate(vinculo.dataFim), Reformas.reforma2019.value)
            tempAux.days = 0
            tempoContribuicao += tempAux
            passouDataReforma = True

            tempoContribuicao = normalizaData(tempoContribuicao)
            continue

        if not passouDataReforma:
            tempoContribuicao += relativedelta(strToDate(vinculo.dataFim), strToDate(vinculo.dataInicio))
        else:
            tempAux = relativedelta(strToDate(vinculo.dataFim), strToDate(vinculo.dataInicio))
            tempAux.days = 0
            tempoContribuicao += tempAux
            passouDataReforma = True

        tempoContribuicao = normalizaData(tempoContribuicao)

    return tempoContribuicao


def tempoContribPorCompetencias(listaContrib: List[ItemContribuicao], tempoEspecial: bool = False) -> relativedelta:
    tempoContrib: relativedelta = relativedelta()

    for index in range(len(listaContrib)):
        if index != 0 and listaContrib[index - 1].competencia == listaContrib[index].competencia:
            continue
                
        competenciaAtual = listaContrib[index]

        if not tempoEspecial and competenciaAtual.fatorInsalubridade is not None:
            # Soma o tempo com acrescimo do fator de insalubridade
            tempoContrib += relativedelta(days=30*competenciaAtual.fatorInsalubridade)

        elif tempoEspecial and competenciaAtual.fatorInsalubridade is not None:
            # Soma o tempo normalmente. Sem acréscimo do fator
            tempoContrib += relativedelta(months=1)

        elif tempoEspecial and competenciaAtual.fatorInsalubridade is None:
            # Não soma o tempo proque não tem fator de insalubridade
            continue

        else:
            # Tempo normal sem fator de insalubridade
            tempoContrib += relativedelta(months=1)

    return normalizaData(tempoContrib)
