# -*- coding: utf-8 -*-
from typing import List
from dateutil.relativedelta import relativedelta
from peewee import fn

import datetime

from util.enums.newPrevEnums import ComparaData


def atividadesConcorrentes(dataIniAtivA: datetime.date = datetime.date.min, dataFimAtvA: datetime.date = datetime.date.min, dataIniAtivB: datetime.date = datetime.date.min, dataFimAtivB: datetime.date = datetime.date.min) -> bool:
    conflitoInicio: bool = dataIniAtivA <= dataIniAtivB <= dataFimAtvA
    conflitoFim: bool = dataIniAtivA <= dataFimAtivB <= dataFimAtvA

    return conflitoInicio or conflitoFim


def atividadeSecundaria(atividadeA, atividadeB) -> int:
    tempoContribA: int = (strToDate(atividadeA.dataFim) - strToDate(atividadeA.dataInicio)).days
    tempoContribB: int = (strToDate(atividadeB.dataFim) - strToDate(atividadeB.dataInicio)).days

    if tempoContribA > tempoContribB or tempoContribA == tempoContribB:
        return atividadeB.seq
    else:
        return atividadeA.seq


def calculaIdade(dtNascimento, dtLimite) -> relativedelta:
    """
    Parte da solução do @[Tomasz Zielinski] e @Williams
    :param dtNascimento:
    :param dtLimite:
    :return: relativedelta
    """

    if not (isinstance(dtNascimento, type(datetime.datetime)) or isinstance(dtNascimento, type(datetime.date))):
        dtNascimento = strToDate(dtNascimento)

    if not (isinstance(dtLimite, datetime.datetime) or isinstance(dtLimite, datetime.date)):
        dtLimite = strToDate(dtLimite)

    idadeRelativa = relativedelta(dtLimite, dtNascimento)
    if idadeRelativa.years < 0:
        idadeRelativa = relativedelta(dtNascimento, dtNascimento)

    return idadeRelativa


def calculaQtdContribuicoes(dataInicio: datetime.date, dataFim: datetime.date) -> int:
    """
    Como o CNIS conta o primeiro mês como uma contribuição, a simples diferênça entre as datas não é suficiente para calcular
    com precisão a quantidade de contribuições. Para ajustar, é preciso adicionar mais uma unidade.
    """
    dataRelativa = relativedelta(dataInicio, dataFim)
    return abs(dataRelativa.years*12 + dataRelativa.months) + 1


def calculaQtdContrib(dataRelativa: relativedelta) -> int:
    """
        Como o CNIS conta o primeiro mês como uma contribuição, a simples diferênça entre as datas não é suficiente para calcular
        com precisão a quantidade de contribuições. Para ajustar, é preciso adicionar mais uma unidade.
        """
    return abs(dataRelativa.years*12 + dataRelativa.months) + 1


def calculaIdadeAutomatica(dataNascimento) -> str:
    if isinstance(dataNascimento, str):
        dataAUsar = strToDate(dataNascimento)
    elif isinstance(dataNascimento, datetime.date):
        dataAUsar = dataNascimento
    else:
        return ''

    idade: relativedelta = relativedelta(datetime.date.today(), dataAUsar)

    return f"{idade.years} anos {idade.months} meses e {idade.days} dias"


def dataConflitante(competencia: datetime.date, seqAtual: int, clienteId: int) -> bool:
    from modelos.itemContribuicao import ItemContribuicao

    itensEncontrados: List[ItemContribuicao] = ItemContribuicao.select().where(
        ItemContribuicao.clienteId == clienteId,
        ItemContribuicao.seq << [seqAtual-1, seqAtual+1],
        ItemContribuicao.competencia.year == competencia.year,
        ItemContribuicao.competencia.month == competencia.month
    )

    return len(itensEncontrados) > 1


def dataIdealReforma(dataReforma: datetime.date, dataInicio: datetime.date) -> datetime.date:
    dataAnteriorReforma = dataInicio
    while dataAnteriorReforma + relativedelta(months=1) < dataReforma:
        dataAnteriorReforma += relativedelta(months=1)

    return dataAnteriorReforma


def mascaraDataPequena(data: datetime.date, onlyYear=False):
    if isinstance(data, str):
        if len(data) <= 16:
            data = strToDatetime(data)
        else:
            data = strToDatetime(data)

    if onlyYear:
        return f'{data.year}'
    else:
        if len(str(data.month)) == 1:
            return f'0{data.month}/{data.year}'
        else:
            return f'{data.month}/{data.year}'


def mascaraData(data):
    if isinstance(data, str):
        if len(data) <= 16:
            data = strToDatetime(data)
        else:
            data = strToDatetime(data)

    return f'{data.day:02}/{data.month:02}/{data.year}'


def eliminaHoraDias(data: datetime.datetime):
    try:
        if isinstance(data, type(datetime.datetime)):
            return data.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        elif isinstance(data, type(datetime.date)):
            return data.replace(day=1)
        elif isinstance(data, str):
            return datetime.datetime.strptime(data, '%Y-%m-%d').date().replace(day=1)
    except TypeError as err:
        print(f'eliminaHoraDias ({type(err)}): {err}')


def comparaMesAno(dataInicio: datetime.datetime, dataFim: datetime.datetime, comparacao: ComparaData) -> int:
    if isinstance(dataInicio, str):
        dataInicio = strToDate(dataInicio)

    inicio = eliminaHoraDias(dataInicio)
    fim = eliminaHoraDias(dataFim)

    if isinstance(inicio, datetime.datetime):
        inicio = inicio.date()
    if isinstance(fim, datetime.datetime):
        fim = fim.date()

    if comparacao == ComparaData.igual:
        return inicio == fim
    elif comparacao == ComparaData.posterior:
        return inicio > fim
    elif comparacao == ComparaData.anterior:
        return inicio < fim
    else:
        raise Exception()


def strAnoToDate(data: str) -> datetime.date:
    return datetime.date(year=int(data), month=1, day=1)


def strToDate(dataAvaliar: str) -> datetime.date:
    dateFormats: List[str] = ['%d/%m/%Y', '%m/%Y', '%Y-%m-%d', '%Y-%m-%d %H:%M:%S']

    # if isinstance(dataAvaliar, type(datetime.datetime)):
    if isinstance(dataAvaliar, datetime.datetime):
        return dataAvaliar.date()
    # elif isinstance(dataAvaliar, type(datetime.date)):
    elif isinstance(dataAvaliar, datetime.date):
        return dataAvaliar
    else:
        for formato in dateFormats:
            try:
                dataRetorno = datetime.datetime.strptime(dataAvaliar, formato).date()
                return dataRetorno
            except ValueError:
                pass
            except Exception as err:
                print(f'strToDate: ({type(dataAvaliar)}) {dataAvaliar} - ({type(err)}) {err}')
                raise


def strToDatetime(data: str) -> datetime.datetime:
    if not isinstance(data, str):
        data = data.strftime('%Y-%m-%d %H:%M')

    dateFormats: List[str] = ['%Y-%m-%d %H:%M', '%d/%m/%Y', '%m/%Y', '%Y-%m-%d', '%Y-%m-%d %H:%M:%S']
    for formato in dateFormats:
        try:
            dataRetorno = datetime.datetime.strptime(data, formato)
            return dataRetorno
        except ValueError as err:
            pass
