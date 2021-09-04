from util.helpers import strToDatetime
from dateutil.relativedelta import relativedelta
from datetime import date, datetime


def calculaIdade(dtNascimento, dtLimite) -> relativedelta:
    """
    Solução do @[Tomasz Zielinski] e @Williams
    :param dtNascimento:
    :param dtLimite:
    :return: List[dias, meses, anos]
    """

    if not (isinstance(dtNascimento, datetime) or isinstance(dtNascimento, date)):
        dtNascimento = strToDatetime(dtNascimento)

    if not (isinstance(dtLimite, datetime) or isinstance(dtLimite, date)):
        dtLimite = strToDatetime(dtLimite)

    idadeDias = (dtLimite - dtNascimento).days

    idadeRelativa = relativedelta(idadeDias)

    return idadeRelativa


def mascaraDataPequena(data: datetime.date):
    if isinstance(data, str):
        if len(data) <= 16:
            data = strToDatetime(data)
        else:
            data = strToDatetime(data)

    return f'{data.month}/{data.year}'
