import datetime

from dateutil.relativedelta import relativedelta
from typing import List

from modelos.vinculoORM import CnisVinculos
from modelos.itemContribuicao import ItemContribuicao

from util.helpers.dateHelper import reformaNoPeriodo, strToDate, normalizaData, atividadesConcorrentes, calculaTempoVinculosConcorrentes
from util.enums.periodosImportantesEnum import Evento


def tempoContribPorVinculo(listaVinculos: List[CnisVinculos], dataLimite: datetime.date = None) -> relativedelta:
    tempoContribuicao: relativedelta = relativedelta()
    passouDataReforma: bool = False
    atingiuDataLimite: bool = False

    for vinculo in listaVinculos:
        dataInicio = strToDate(vinculo.dataInicio)
        dataFim = strToDate(vinculo.dataFim)

        if dataInicio is None or dataFim is None:
            continue

        if dataLimite is not None:
            if dataLimite < dataInicio:
                break
            elif dataInicio <= dataLimite <= dataFim:
                atingiuDataLimite = True
                dataFim = dataLimite

        if reformaNoPeriodo(dataInicio, dataFim, Evento.reforma2019.value):
            # Antes da reforma
            tempoContribuicao += relativedelta(Evento.reforma2019.value, dataInicio)
            # Depois da reforma
            tempAux = relativedelta(dataFim, Evento.reforma2019.value)
            tempAux.days = 0
            tempoContribuicao += tempAux
            passouDataReforma = True

            tempoContribuicao = normalizaData(tempoContribuicao)
            continue

        if not passouDataReforma:
            tempoContribuicao += relativedelta(dataFim, dataInicio)
        else:
            tempAux = relativedelta(dataFim, dataInicio)
            tempAux.days = 0
            tempoContribuicao += tempAux
            passouDataReforma = True

        tempoContribuicao = normalizaData(tempoContribuicao)
        if atingiuDataLimite:
            break

    tempoContribuicao -= tempoVinculosConcorrentes(listaVinculos)
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


def tempoVinculosConcorrentes(listaDeVinculos: List[CnisVinculos]) -> relativedelta:
    tempoConcorrenteRetorno = relativedelta()

    for index in range(len(listaDeVinculos)):
        if index == len(listaDeVinculos) - 1:
            continue

        dataIniA = strToDate(listaDeVinculos[index].dataInicio)
        dataFimA = strToDate(listaDeVinculos[index].dataFim)
        dataIniB = strToDate(listaDeVinculos[index + 1].dataInicio)
        dataFimB = strToDate(listaDeVinculos[index + 1].dataFim)

        if atividadesConcorrentes(dataIniA, dataFimA, dataIniB, dataFimB):
            tempoConcorrenteRetorno += calculaTempoVinculosConcorrentes(dataIniA, dataFimA, dataIniB, dataFimB)

    return tempoConcorrenteRetorno
