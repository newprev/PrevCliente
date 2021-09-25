# -*- coding: utf-8 -*-
from typing import List

from dateutil.relativedelta import relativedelta
# from modelos.cabecalhoORM import CnisCabecalhos
import datetime


def calculaIdade(dtNascimento, dtLimite) -> relativedelta:
    """
    Solução do @[Tomasz Zielinski] e @Williams
    :param dtNascimento:
    :param dtLimite:
    :return: List[dias, meses, anos]
    """

    if not (isinstance(dtNascimento, type(datetime.datetime)) or isinstance(dtNascimento, type(datetime.date))):
        dtNascimento = strToDatetime(dtNascimento)

    if not (isinstance(dtLimite, datetime.datetime) or isinstance(dtLimite, datetime.date)):
        dtLimite = strToDatetime(dtLimite)

    idadeRelativa = relativedelta(dtLimite, dtNascimento)

    return idadeRelativa


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


def strAnoToDate(data: str) -> datetime.date:
    return datetime.date(year=int(data), month=1, day=1)


def strToDate(dataAvaliar: str):
    dateFormats: List[str] = ['%d/%m/%Y', '%m/%Y', '%Y-%m-%d']

    if isinstance(dataAvaliar, type(datetime.datetime)):
        return dataAvaliar.date()
    elif isinstance(dataAvaliar, type(datetime.date)):
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
