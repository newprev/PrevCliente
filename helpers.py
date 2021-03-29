import datetime

estCivil = ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)']

dictIndicadores = {
    'AEXT-VI': 'Acerto de vínculo extemporâneo indeferido.',
    'AEXT-VT': 'Acerto de vínculo extemporâneo validado totalmente.',
    'AVRC-DEF': 'Acerto de vínculo extemporâneo deferido.',
    'IEAN': 'Exposição a agentes nocivos no grupo 25 anos.',
    'IGFIP-INF': 'Indicador de GFIP meramente informativa.',
    'ILEI123': 'Contribuição da competência foi recolhida com código da Lei Complementar 123/2006. (Plano simplificado de Previdência).',
    'IMEI': 'Contribuição da competência foi recolhida com código MEI.',
    'IREC-CIRURAL': 'Recolhimento com código de CI Rural sem homologação.',
    'IREC-FBR': 'Recolhimento facultativo baixa renda.',
    'IREC-INDPEND': 'Recolhimentos com indicadores e/ou pendências.',
    'IREC-LC123': 'Recolhimentos para fins da LC 123.',
    'IREC-LC123-SUP': 'Recolhimento / Complementação LC 123 superior ao salário mínimo.',
    'PADM-EMPR': 'Inconsistência temporal, admissão anterior ao início da atividade do empregador.',
    'PEMP-CAD': 'Falta de informações cadastrais do CNPJ ou CEI.',
    'PEXT': 'Pendência de vínculo extemporâneo não tratado.',
    'PREC-COD1821': 'Recolhimento com código de pagamento 1821 – Mandato Eletivo.',
    'PREC-CSE': 'Recolhimento GPS de Segurado Especial Pendente Comprovação.',
    'PREC-FBR': 'Recolhimento facultativo baixa renda não validado / homologado.',
    'PREC-FBR-ANT': 'Recolhimento facultativo baixa renda anterior a comp. 09/2011.',
    'PREC-LC123-ANT': 'Recolhimento com código da LC 123 anterior à competência 04/2007.',
    'PREC-MENOR-MIN': 'Recolhimento realizado é inferior ao valor mínimo.',
    'PREC-PMIG-DOM': 'Recolhimento inclusive sal.mat., e/ou período declarado empregado doméstico sem registro de vínculo.',
    'PREC-FACULTCONC': 'Recolhimento ou período atividade de contribuinte facultativo concomitante com outro TFV.',
    'PREM-EMPR': 'Remuneração antes do início da atividade do empregador.',
    'PREM-EXT': 'Remuneração da competência é extemporânea.',
    'PREM-FVIN': 'Remunerações posteriores ao fim do vínculo de trabalho.',
    'PREM-RET': 'Remuneração de prestador de serviço declarada em GFIP mas que não é considerada.',
    'PVIN-IRREG': 'Pendência de Vínculo Irregular.'
}

dictEspecies = {
    "01": "Pensão por Morte de Trabalhador Rural",
    "02": "Pensão por Morte Acidentária Trabalhador Rural",
    "03": "Pensão por Morte de Empregador Rural",
    "04": "Aposentadoria por Invalidez Trabalhador Rural",
    "05": "Aposentadoria Invalidez Acidentária Trabalhador Rural",
    "06": "Aposentadoria Invalidez Empregador Rural",
    "07": "Aposentadoria por Velhice Trabalhador Rural",
    "08": "Aposentadoria por Idade Empregador Rural",
    "09": "Compl. Acidente Trabalho p/Trabalhador (rural)",
    "10": "Auxílio Doença Acidentário Trabalhador Rural",
    "11": "Amparo Previdenc. Invalidez Trabalhador Rural",
    "12": "Amparo Previdenc. Idade Trabalhador Rural",
    "13": "Auxílio Doenca Trabalhador Rural",
    "15": 'Auxílio Reclusão Trabalhador Rural',
    "19": 'Pensão de Estudante (lei 7.004/82)',
    "20": 'Pensão por Morte de Ex Diplomata',
    "21": 'Pensão por Morte Previdenciária',
    "22": 'Pensão por Morte Estatutária',
    "23": 'Pensão por Morte de Ex Combatente',
    "24": 'Pensão Especial (ato Institucional)',
    "25": 'Auxílio Reclusão',
    "26": 'Pensão por Morte Especial',
    "27": 'Pensão Morte Servidor Público Federal',
    "28": 'Pensão por Morte Regime Geral',
    "29": 'Pensão por Morte Ex Combatente Marítimo',
    "30": 'Renda Mensal Vitalícia por Incapacidade',
    "31": 'Auxílio doença Previdenciário',
    "32": 'Aposentadoria Invalidez Previdenciária',
    "33": 'Aposentadoria Invalidez Aeronauta',
    "34": 'Aposentadoria Inval. Ex Combatente Marítimo',
    "35": 'Auxílio Doença do Ex Combatente',
    "36": 'Auxílio Acidente Previdenciário',
    "37": 'Aposentadoria Extranumerário Capin',
    "38": 'Aposentadoria Extranum. Funcionário Público',
    "39": 'Auxílio Invalidez Estudante',
    "40": 'Renda Mensal Vitalícia por Idade',
    "41": 'Aposentadoria por Idade',
    "42": 'Aposentadoria por Tempo de Contribuição',
    "43": 'Aposentadoria por Tempo Serviço Ex Combatente',
    "44": 'Aposentadoria Especial de Aeronauta',
    "45": 'Aposentadoria Tempo Serviço Jornalista',
    "46": 'Aposentadoria Especial',
    "47": 'Abono Permanência em Serviço 35 Anos',
    "48": 'Abono Permanência em Serviço 30 Anos',
    "49": 'Aposentadoria Ordinária',
    "50": 'Auxílio Doença Extinto Plano Básico',
    "51": 'Aposentadoria Invalidez Extinto Plano Básico',
    "52": 'Aposentadoria Idade Extinto Plano Básico',
    "53": 'Auxílio Reclusão Extinto Plano Básico',
    "54": 'Pensão Indenizatória a Cargo da União',
    "55": 'Pensão por Morte Extinto Plano Básico',
    "56": 'Pensão Vitalícia Sindrome Talidomida',
    "57": 'Aposentadoria Tempo de Serviço de Professor',
    "58": 'Aposentadoria de Anistiados',
    "59": 'Pensão por Morte de Anistiados',
    "60": 'Benefício Indenizatório a cargo da União',
    "61": 'Auxílio Natalidade',
    "62": 'Auxílio Funeral',
    "63": 'Auxílio Funeral Trabalhador Rural',
    "64": 'Auxílio Funeral Empregador Rural',
    "65": 'Pecúlio Especial Servidor Autárquico',
    "66": 'Pec. Esp. Servidor Autárquico',
    "67": 'Pecúlio Obrigatório Ex Ipase',
    "68": 'Pecúlio Especial de Aposentados',
    "69": 'Pecúlio de Estudante',
    "70": 'Restituição Contrib. P/Seg. S/Carência',
    "71": 'Salário Família Previdenciário',
    "72": 'Aposentadoria Tempo Serviço Lei de Guerra',
    "73": 'Salário Família Estatutário',
    "74": 'Complemento de Pensão a Conta da União',
    "75": 'Complemento de Aposentadoria a Conta da União',
    "76": 'Salário Família Estatutário',
    "77": 'Salário Fam. Estatutário Servidor Sinpas',
    "78": 'Aposentadoria Idade Lei de Guerra',
    "79": 'Vantagens de Servidor Aposentado',
    "80": 'Auxílio Salário Maternidade',
    "81": 'Aposentadoria Compulsória Ex Sasse',
    "82": 'Aposentadoria Tempo de Serviço Ex Sasse',
    "83": 'Aposentadoria por Invalidez Ex Sasse',
    "84": 'Pensão por Morte Ex Sasse',
    "85": 'Pensão Vitalícia Seringueiros',
    "86": 'Pensão Vitalícia Dependentes Seringueiro',
    "87": 'Amp. Social Pessoa Portadora Deficiência',
    "88": 'Amparo Social ao Idoso',
    "89": 'Pensão Esp. Vitimas Hemodiálise Caruaru',
    "90": 'Simples Assist. Médica p/ Acidente Trabalhador',
    "91": 'Auxílio Doenca por Acidente do Trabalho',
    "92": 'Aposentadoria Invalidez Acidente Trabalho',
    "93": 'Pensão por Morte Acidente do Trabalho',
    "94": 'Auxílio Acidente',
    "95": 'Auxílio Suplementar Acidente Trabalho',
    "96": 'Pensão Especial Hanseníase Lei 11520/07',
    "97": 'Pecúlio por Morte Acidente do Trabalho',
    "98": 'Abono Anual de Acidente de Trabalho',
    "99": 'Afastamento Até 15 Dias Acidente Trabalhador',
}

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


def getConversoesMonetarias():
    return ['Valorizou', 'Desvalorizou']


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
    if pointPosition > 0:
        strFinal = strValor[:pointPosition] + '.' + strValor[pointPosition:]
    else:
        strFinal = strValor

    if strFinal.startswith('.'):
        return f"R$ {strFinal[1:]}"
    else:
        return f"R$ {strFinal}"


def dinheiroToFloat(valor: str):
    if valor == '' or valor == 'R$ ':
        return ''
    strSemCifrao = valor.replace('R$ ', '')
    semPontoDivisor = strSemCifrao.replace('.', '')
    comPontoDecimal = semPontoDivisor.replace(',', '.')

    return float(comPontoDecimal)


def mascaraDataSql(data: str, short: bool = False):
    try:
        if short:
            dataRetorno = datetime.datetime.strptime(data, '%m/%Y')
        else:
            dataRetorno = datetime.datetime.strptime(data, '%d/%m/%Y')
        return dataRetorno
    except ValueError:
        return datetime.datetime.min


def strToDatetime(data: str, short: bool = False):
    try:
        if short:
            return datetime.datetime.strptime(data, '%m/%Y')
        else:
            return datetime.datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        return datetime.datetime.min


def strToFloat(valor: str) -> float:
    try:
        retorno = valor.replace('.', '').replace(',', '.')
        return float(retorno)
    except ValueError:
        return valor


def unmaskAll(info: str):
    return info.replace('.', '').replace('/', '').replace('\\', '').replace(',', '').replace('-', '')
