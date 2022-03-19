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


def tempoContribPorCompetencias(listaContrib: List[ItemContribuicao], especial: bool = False) -> relativedelta:
    tempoContrib: relativedelta = relativedelta()

    for index in range(len(listaContrib)):
        if index == len(listaContrib) - 1:
            continue

        competenciaAntes: datetime.date = strToDate(listaContrib[index].competencia)
        competenciaDepois: datetime.date = strToDate(listaContrib[index + 1].competencia)
        tempoAux = relativedelta(competenciaDepois, competenciaAntes)

        if not especial and listaContrib[index + 1].fatorInsalubridade is not None:
            tempoAux = tempoAux * listaContrib[index + 1].fatorInsalubridade

        tempoContrib += tempoAux

    return tempoContrib