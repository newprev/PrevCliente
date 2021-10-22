# -*- coding: utf-8 -*-
from typing import List
from dateutil.relativedelta import relativedelta
from peewee import fn

import datetime


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

    return idadeRelativa


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


def mascaraDataPequena(data: datetime.date, onlyYear=False):
    if isinstance(data, str):
        if len(data) <= 16:
            data = strToDatetime(data)
        else:
            data = strToDatetime(data)

    if onlyYear:
        return f'{data.year}'
    else:
        return f'{data.month}/{data.year}'


def mascaraData(data):
    if isinstance(data, str):
        if len(data) <= 16:
            data = strToDatetime(data)
        else:
            data = strToDatetime(data)

    return f'{data.day}/{data.month}/{data.year}'


def strAnoToDate(data: str) -> datetime.date:
    return datetime.date(year=int(data), month=1, day=1)


def strToDate(dataAvaliar: str):
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
