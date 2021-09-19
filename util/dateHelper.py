# -*- coding: utf-8 -*-
from util.helpers import strToDatetime
from dateutil.relativedelta import relativedelta
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


def strAnoToDate(data: str) -> datetime.date:
    return datetime.date(year=int(data), month=1, day=1)
