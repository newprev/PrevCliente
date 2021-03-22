import datetime

estCivil = ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)']

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

def getEstados():
    return {
        'Acre': 'AC',
        'Alagoas': 'AL',
        'Amapá': 'AP',
        'Amazonas': 'AM',
        'Bahia': 'BA',
        'Ceará': 'CE',
        'Distrito Federal': 'DF',
        'Espírito Santo': 'ES',
        'Goiás': 'GO',
        'Maranhão': 'MA',
        'Mato Grosso': 'MT',
        'Mato Grosso do Sul': 'MS',
        'Minas Gerais': 'MG',
        'Pará': 'PA',
        'Paraíba': 'PB',
        'Paraná': 'PR',
        'Pernambuco': 'PE',
        'Piauí': 'PI',
        'Rio de Janeiro': 'RJ',
        'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS',
        'Rondônia': 'RO',
        'Roraima': 'RR',
        'Santa Catarina': 'SC',
        'São Paulo': 'SP',
        'Sergipe': 'SE',
        'Tocantins': 'TO'
    }

def getEstadoBySigla(uf: str):
    dictEstados = getEstados()
    for chave, valor in dictEstados.items():
        if valor.upper() == uf.upper():
            return chave

def mascaraTelCel(telCel):
    if telCel is None or len(telCel) == 10:
        return f'({telCel[0:2]}) {telCel[3:7]}-{telCel[7:]}'
    elif telCel is None or len(telCel) == 11:
        return f'({telCel[0:2]}) {telCel[2:3]}.{telCel[3:7]}-{telCel[7:]}'
    else:
        return telCel

def mascaraCNPJ(cnpj):
    if cnpj is None or len(cnpj) != 14:
        return cnpj
    else:
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'

def mascaraCPF(cpf: str):
    if cpf is None or len(cpf) != 11:
        return cpf
    else:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def mascaraRG(rg: str):
    if rg is None or len(rg) != 9:
        return rg
    else:
        return f'{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}'

def mascaraCep(cep: str):
    return f'{cep[:5]}-{cep[5:]}'

def mascaraNit(nit: int) -> str:
    strNit = str(nit)
    return f"{strNit[0:3]}.{strNit[3:8]}.{strNit[8:10]}-{strNit[10:]}"

def calculaIdadeFromString(dataNascimento: str) -> int:
    dataIdade = datetime.datetime.strptime(dataNascimento, '%d/%m/%Y')
    return int((datetime.datetime.now() - dataIdade).days / 365.25)

def macaraFormaPagamento(pagamento: str):
    if (pagamento.upper() == 'CC'):
        return 'Cartão de crédito'
    else:
        return 'Outras opções'

def mascaraMeses(data: datetime.date):
    return f'{data.day} de {meses[data.month]} de {data.year}'

def mascaraDataPequena(data: datetime.date):
    return f'{data.month}/{data.year}'

def mascaraDinheiro(valor: float):
    strValor = str(valor).replace('.', ',')
    pointPosition = strValor.find(",") - 3
    strFinal = strValor[:pointPosition] + '.' + strValor[pointPosition:]
    if strFinal.startswith('.'):
        return f"R$ {strFinal[1:]}"
    else:
        return f"R$ {strFinal}"

def mascaraDataSql(data: datetime, short: bool = False):
    try:
        if short:
            dataRetorno = datetime.datetime.strptime(data, '%m/%Y')
        else:
            dataRetorno = datetime.datetime.strptime(data, '%d/%m/%Y')
        return dataRetorno
    except ValueError:
        return datetime.datetime.min

def strToFloat(valor: str) -> float:
    retorno = valor.replace('.', '').replace(',', '.')
    return float(retorno)

def unmaskAll(info: str):
    return info.replace('.', '').replace('/', '').replace('\\', '').replace(',', '').replace('-', '')
