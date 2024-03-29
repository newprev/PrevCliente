import datetime
import os.path
from math import floor, ceil
from peewee import ModelSelect
from typing import Union, Tuple, List

from modelos.tipoBeneficioORM import TipoBeneficioModel
from util.enums.aposentadoriaEnums import SubTipoAposentadoria, TipoAposentadoria, ContribSimulacao
from util.enums.configEnums import ImportantPaths
from util.enums.processoEnums import TipoBeneficioEnum, TipoProcesso, NaturezaProcesso
from util.enums.processoEnums import SituacaoProcesso

estCivil = ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)']

dictIndicadores = {
    '': '',
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
    'IREM-ACD': 'Remuneração possui parcela de acordo, convenção ou dissídio coletivo',
    'PADM-EMPR': 'Inconsistência temporal, admissão anterior ao início da atividade do empregador.',
    'PDT-NASC-FIL-INV': 'Idade do filiado menor que a permitida pela IN20 de outubro de 2007',
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

situacaoBeneficio = ['Indeferido', 'Cessado', 'Ativo']

tipoItemContribuicao = [
    ('C', 'CONTRIBUICAO'),
    ('B', 'BENEFICIO'),
    ('R', 'REMUNERACAO')
]

tipoItemOrigem = [
    ('C', 'CNIS'),
    ('N', 'NEWPREV'),
    ('S', 'SIMULACAO')
]


def getItemOrigem():
    return tipoItemOrigem


def getTipoItem():
    return tipoItemContribuicao


def getEscolaridade():
    return {
        'Fundamental Incompleto': 'FI',
        'Fundomantal Completo': 'FC',
        'Médio Incompleto': 'MI',
        'Médio Completo': 'MC',
        'Superior Incompleto': 'SI',
        'Superior Completo': 'SC',
    }


def getEscolaridadeBySigla(sigla: str):
    dictEscolaridade = getEscolaridade()
    for chave, valor in dictEscolaridade.items():
        if valor.upper() == sigla.upper():
            return chave


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


def getTipoTelefone():
    return {
        'Whatsapp': 'W',
        'Celular': 'C',
        'Fixo': 'F'
    }


def getTipoTelefoneBySigla(sigla: str):
    dictTipoTelefones = getTipoTelefone()
    for chave, valor in dictTipoTelefones.items():
        if valor.upper() == sigla.upper():
            return chave


def getPessoalRecado():
    return {
        'Pessoal': 'P',
        'Recado': 'R'
    }


def getPessoalRecadoBySigla(sigla: str):
    dictgetPessoalRecado = getPessoalRecado()
    for chave, valor in dictgetPessoalRecado.items():
        if valor.upper() == sigla.upper():
            return chave


def getConversoesMonetarias():
    return ['Valorizou', 'Desvalorizou']


def getRegrasApos():
    return (
        ('TCAR', 'TEMPO CONTRIBUICAO AR'),
        ('IDAR', 'IDADE AR'),
        ('RIDM', 'REDUCAO IDADE MINIMA'),
        ('RETC', 'REDUCAO TEMPO CONTRIBUICAO'),
        ('PD50', 'PEDAGIO 50'),
        ('P100', 'PEDAGIO 100'),
        ('POTR', 'TRANSICAO PONTOS'),
        ('8595', 'REGRA 8595')
    )


def getContribSimulacao():
    return (
        ('ULTI', 'REPETE O ÚLTIMO SALÁRIO'),
        ('TETO', 'TETO PREVIDENCIÁRIO'),
        ('SMIN', 'SALÁRIO MÍNIMO'),
        ('MANU', 'VALOR DEFINIDO MANUALMENTE'),
    )


def escritorioIdAtual() -> int:
    from cache.cacheEscritorio import CacheEscritorio

    escritorioCache = CacheEscritorio()
    escritorio = escritorioCache.carregarCache()
    if not escritorio:
        escritorio = escritorioCache.carregarCacheTemporario()

    return escritorio.escritorioId


def mascaraTelCel(telCel):
    if telCel in [None, 'None']:
        return ''
    elif len(telCel) == 10:
        return f'({telCel[0:2]}) {telCel[3:7]}-{telCel[7:]}'
    elif len(telCel) == 11:
        return f'({telCel[0:2]}) {telCel[2:3]}.{telCel[3:7]}-{telCel[7:]}'
    else:
        return telCel


def mascaraCNPJ(cnpj):
    if cnpj == '':
        return '-'
    elif cnpj is None or len(cnpj) != 14:
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
    if len(cep) == 0:
        return ''
    return f'{cep[:5]}-{cep[5:]}'


def mascaraNit(nit: int) -> str:
    strNit = str(nit)
    return f"{strNit[0:3]}.{strNit[3:8]}.{strNit[8:10]}-{strNit[10:]}"


def calculaDiaMesAno(totalDias: int) -> list:
    resto: int = 0

    anos = floor(totalDias / (30 * 12))
    resto = totalDias % (30 * 12)
    mes = floor(resto / 30)
    dias = resto % 30

    return [dias, mes, anos]


def mascaraFormaPagamento(pagamento: str):
    if (pagamento.upper() == 'CC'):
        return 'Cartão de crédito'
    else:
        return 'Outras opções'


def mascaraMeses(data: datetime.date):
    return f'{data.day} de {meses[data.month]} de {data.year}'


def verificaIndicadorProibitivo(indicadores: str) -> bool:
    indicadoresImpeditivos = ['PDT-NASC-FIL-INV', 'IREC-LC123', 'PREC-MENOR-MIN']

    if indicadores == '' or indicadores is None:
        return False
    elif indicadores != '' and ',' in indicadores:
        listaIndicadores = indicadores.split(',')
    elif len(indicadores) > 0 and ',' not in indicadores:
        listaIndicadores = [indicadores]
    else:
        return False

    for ind in listaIndicadores:
        if ind in indicadoresImpeditivos:
            return True

    return False


def dataUSAtoBR(dataUSA: str, comDias: bool = False) -> str:
    if dataUSA is None:
        return '-'

    if not isinstance(dataUSA, str):
        if comDias:
            return f"{dataUSA.day}/{dataUSA.month}/{dataUSA.year}"
        else:
            return f"{dataUSA.month}/{dataUSA.year}"

    if dataUSA == '':
        return dataUSA
    elif comDias:
        return f"{dataUSA[8:]}/{dataUSA[5:7]}/{dataUSA[:4]}"
    else:
        return f"{dataUSA[5:7]}/{dataUSA[:4]}"


def mascaraDinheiro(valor: float, simbolo: str = 'R$'):
    strValor = str(valor).replace('.', ',')
    pointPosition = strValor.find(",") - 3
    if pointPosition > 0:
        strFinal = strValor[:pointPosition] + '.' + strValor[pointPosition:]
        pointPosition = strFinal.find(".") - 3

        while pointPosition > 0:
            strFinal = strFinal[:pointPosition] + '.' + strFinal[pointPosition:]
            pointPosition = strFinal.find(".") - 3
    else:
        strFinal = strValor

    if strFinal.startswith('.'):
        return f"{simbolo} {strFinal[1:]}"
    else:
        return f"{simbolo} {strFinal}"


def mascaraNB(valor: int):
    strValor = str(valor)
    pointPosition = len(strValor) - 3
    if pointPosition > 0:
        strFinal = strValor[:pointPosition] + '.' + strValor[pointPosition:]
        pointPosition = strFinal.find(".") - 3

        while pointPosition > 0:
            strFinal = strFinal[:pointPosition] + '.' + strFinal[pointPosition:]
            pointPosition = strFinal.find(".") - 3
    else:
        strFinal = strValor

    if strFinal.startswith('.'):
        return f"{strFinal[1:]}"
    else:
        return f"{strFinal}"


def calculaIdadeFromString(dataNascimento: str) -> int:
    dataIdade = datetime.datetime.strptime(dataNascimento, '%d/%m/%Y')
    return int((datetime.datetime.now() - dataIdade).days / 365.25)


def dinheiroToFloat(valor: str):
    if valor == '' or valor == 'R$ ':
        return ''
    strSemCifrao = valor.replace('R$ ', '')
    semPontoDivisor = strSemCifrao.replace('.', '')
    comPontoDecimal = semPontoDivisor.replace(',', '.')

    return float(comPontoDecimal)


def floatToDinheiro(valor: Union[float, str]):
    if isinstance(valor, float):
        valor = str(valor)

    return valor.replace('.', ',')


def mascaraDataSql(data: str, short: bool = False):
    try:
        if short:
            dataRetorno = datetime.datetime.strptime(data, '%m/%Y')
        else:
            dataRetorno = datetime.datetime.strptime(data, '%d/%m/%Y')
        return dataRetorno
    except ValueError:
        return datetime.datetime.min


def datetimeToSql(data: datetime.datetime) -> str:
    if isinstance(data, str):
        return data
    else:
        return data.strftime('%Y-%m-%d %H:%M')


def dateToSql(data: datetime.date) -> str:
    return data.strftime('%Y-%m-%d')


def regraAposentadoria(sigla: str) -> SubTipoAposentadoria:
    tipo: TipoAposentadoria = TipoAposentadoria(sigla)
    aposIdade: tuple = (
        TipoAposentadoria.idadeAR,
        TipoAposentadoria.redIdadeMinima
    )
    aposTempoContribuicao: tuple = (
        TipoAposentadoria.tempoContribAR,
        TipoAposentadoria.redTempoContrib,
        TipoAposentadoria.pedagio50,
        TipoAposentadoria.pedagio100
    )
    aposPontos: tuple = (
        TipoAposentadoria.pontos,
        TipoAposentadoria.regra8595
    )
    if tipo in aposIdade:
        return SubTipoAposentadoria.Idade
    elif tipo in aposPontos:
        return SubTipoAposentadoria.Pontos
    elif tipo in aposTempoContribuicao:
        return SubTipoAposentadoria.TempoContrib
    else:
        raise TypeError('Tipo de aposentadoria não encontrado')


def strToFloat(valor: str) -> float:
    try:
        return float(valor)
    except ValueError:
        import re
        padrao = '.{0,20},[0-9]{1,2}'
        if re.match(padrao, valor):
            retorno = valor.replace('.', '').replace(',', '.')
        else:
            retorno = valor.replace(',', '')

        return strToFloat(retorno)
    except:
        return valor


def unmaskAll(info: str):
    return info.replace('.', '').replace('/', '').replace('\\', '').replace(',', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')


def strNatureza(natureza: int) -> str:
    if natureza == NaturezaProcesso.administrativo.value:
        return 'Administrativo'
    elif natureza == NaturezaProcesso.judicial.value:
        return 'Judcial'
    else:
        return '-'


def strTipoProcesso(tipoProcesso: TipoProcesso) -> str:
    if not isinstance(tipoProcesso, TipoProcesso) and isinstance(tipoProcesso, int):
        tipoProcesso = TipoProcesso(tipoProcesso)

    if tipoProcesso == TipoProcesso.Revisao:
        return 'Revisão'
    elif tipoProcesso == TipoProcesso.Concessao:
        return 'Concessão'
    elif tipoProcesso == TipoProcesso.RecEspecial:
        return 'Recurso Especial'
    elif tipoProcesso == TipoProcesso.RecOrdinario:
        return 'Recurso Ordinário'
    else:
        return '-'


def strTipoBeneficio(tipoBeneficio: int, subTipoApos: int) -> str:
    if not isinstance(tipoBeneficio, int) and isinstance(tipoBeneficio, TipoBeneficioModel):
        tipoBeneficio = tipoBeneficio.tipoId

    if tipoBeneficio == TipoBeneficioEnum.Aposentadoria.value:
        return strTipoAposentadoria(subTipoApos)
        # if subTipoApos == SubTipoAposentadoria.Idade.value:
        #     return 'Aposentadoria por idade'
        # elif subTipoApos == SubTipoAposentadoria.Rural.value:
        #     return 'Aposentadoria por idade - Rural'
        # elif subTipoApos == SubTipoAposentadoria.Especial.value:
        #     return 'Aposentadoria Especial'
        # elif subTipoApos == SubTipoAposentadoria.Deficiencia.value:
        #     return 'Aposentadoria da pessoa com deficiência'
        # elif subTipoApos == SubTipoAposentadoria.Invalidez.value:
        #     return 'Aposentadoria por invalidez'
        # elif subTipoApos == SubTipoAposentadoria.TempoContrib.value:
        #     return 'Aposentadoria por tempo de contribuição'
    elif tipoBeneficio == TipoBeneficioEnum.AuxDoenca.value:
        return 'Auxílio doença'
    elif tipoBeneficio == TipoBeneficioEnum.AuxReclusao.value:
        return 'Auxílio reclusão'
    elif tipoBeneficio == TipoBeneficioEnum.BeneIdoso.value:
        return 'Benefício assistencial ao idoso'
    elif tipoBeneficio == TipoBeneficioEnum.BeneDeficiencia.value:
        return 'Benefício assistencial à pessoa com deficiência'
    elif tipoBeneficio == TipoBeneficioEnum.PensaoMorte.value:
        return 'Pensão por morte'
    elif tipoBeneficio == TipoBeneficioEnum.SalMaternidade.value:
        return 'Salário maternidade'
    else:
        return ''


def strTipoBeneFacilitado(tipoBeneficio: TipoBeneficioEnum) -> str:
    if isinstance(tipoBeneficio, int):
        tipoBeneficio = TipoBeneficioEnum(tipoBeneficio)

    if tipoBeneficio == TipoBeneficioEnum.Aposentadoria:
        return 'Aposentadoria'
    elif tipoBeneficio == TipoBeneficioEnum.AuxDoenca:
        return 'Auxílio doença'
    elif tipoBeneficio == TipoBeneficioEnum.AuxAcidente:
        return 'Auxílio acidente'
    elif tipoBeneficio == TipoBeneficioEnum.AuxReclusao:
        return 'Auxílio reclusão'
    elif tipoBeneficio == TipoBeneficioEnum.BeneIdoso:
        return 'Benefício assistencial ao idoso'
    elif tipoBeneficio == TipoBeneficioEnum.BeneDeficiencia:
        return 'Benefício assistencial à pessoa com deficiência'
    elif tipoBeneficio == TipoBeneficioEnum.PensaoMorte:
        return 'Pensão por morte'
    elif tipoBeneficio == TipoBeneficioEnum.SalMaternidade:
        return 'Salário maternidade'
    else:
        return ''


def strTipoAposentadoria(tipoAposentadoria: str, verbose: bool = False) -> str:
    if tipoAposentadoria == TipoAposentadoria.tempoContribAR.value:
        if verbose:
            return "Aposentadoria por tempo de contribuição antes da reforma"
        else:
            return "Aposentadoria por tempo de contribuição"

    elif tipoAposentadoria == TipoAposentadoria.idadeAR.value:
        if verbose:
            return "Aposentadoria por idade antes da reforma"
        else:
            return "Aposentadoria por idade"

    elif tipoAposentadoria == TipoAposentadoria.redIdadeMinima.value:
        if verbose:
            return "Aposentadoria pela redução da idade mínima"
        else:
            return "Aposentadoria por idade"

    elif tipoAposentadoria == TipoAposentadoria.redTempoContrib.value:
        if verbose:
            return "Aposentadoria pela redução do tempo de contribuição"
        else:
            return "Aposentadoria por tempo de contribuição"

    elif tipoAposentadoria == TipoAposentadoria.pedagio50.value:
        if verbose:
            return "Aposentadoria pela regra de transição: Pedágio 50%"
        else:
            return "Pedágio 50%"

    elif tipoAposentadoria == TipoAposentadoria.pedagio100.value:
        if verbose:
            return "Aposentadoria pela regra de transição: Pedágio 100%"
        else:
            return "Pedágio 100%"

    elif tipoAposentadoria == TipoAposentadoria.pontos.value:
        if verbose:
            return "Aposentadoria por pontos pela regra de transição"
        else:
            return "Aposentadoria por pontos"

    elif tipoAposentadoria == TipoAposentadoria.regra8595.value:
        if verbose:
            return "Aposentadoria por pontos pela regra 85/95"
        else:
            return "Aposentadoria por pontos"


def buscaSql(caminhoSql: str) -> str:
    if os.path.exists(caminhoSql) and os.path.isfile(caminhoSql):
        sqlScript: str = ""

        with open(caminhoSql, encoding='utf-8', mode='r') as sql:
            script = sql.readlines()
            for linha in script:
                sqlScript += linha.replace("\\t", "")

        return sqlScript


def strTipoSimulacao(tipoSimulacao: str) -> str:
    if tipoSimulacao == ContribSimulacao.ULTI.name:
        return "Repetição da última contribuição"
    elif tipoSimulacao == ContribSimulacao.SMIN.name:
        return "Repetição do salário mínimo"
    elif tipoSimulacao == ContribSimulacao.TETO.name:
        return "Repetição do teto previdenciário"
    elif tipoSimulacao == ContribSimulacao.MANU.name:
        return "Repetição do valor definido manualmente"


def strSituacaoProcessual(situacao: SituacaoProcesso) -> str:
    if isinstance(situacao, int):
        situacao = SituacaoProcesso(situacao)

    if situacao == SituacaoProcesso.aDarEntrada:
        return "A dar entrada"
    elif situacao == SituacaoProcesso.arquivado:
        return "Arquivado"
    elif situacao == SituacaoProcesso.cancelado:
        return "Cancelado"
    elif situacao == SituacaoProcesso.finalizado:
        return "Finalizado"
    elif situacao == SituacaoProcesso.emAndamento:
        return "Andamento"
    else:
        return " - "


def pyToDefault(dicionario: dict) -> dict:

    dictReturn: dict = dict()
    for chave, valor in dicionario.items():

        if isinstance(valor, datetime.datetime):
            dictReturn[chave] = valor.strftime('%Y-%m-%d')
        elif isinstance(valor, datetime.date):
            dictReturn[chave] = valor.strftime('%Y-%m-%d')
        elif isinstance(valor, ModelSelect):
            dictReturn[chave] = pyToDefault(valor.get().toDict())
        else:
            dictReturn[chave] = valor

    return dictReturn


def calculaCoordenadas(qtdItens: int, colunas: int) -> List[Tuple]:
    coordenadas = []
    linha: int = 0
    totalLinhas: int = ceil(qtdItens/colunas)

    for total in range(totalLinhas):
        linha += 1

        for posColuna in range(0, colunas):
            coordenadas.append((linha, posColuna))
    return coordenadas


def comparaFiltrosAny(lista1: Union[str, List[str]], lista2: Union[str, List[str]]) -> bool:
    if isinstance(lista1, str) and isinstance(lista2, str):
        return lista1 == lista2

    elif isinstance(lista1, str) and isinstance(lista2, list):
        return any((lista1 == item for item in lista2))

    elif isinstance(lista1, list) and isinstance(lista2, str):
        return any((lista2 == item for item in lista1))

    else:
        for itemA in lista1:
            for itemB in lista2:
                if itemA == itemB:
                    return True

        return False


def pathTo(local: ImportantPaths):
    import os

    projectPath = os.path.normpath(os.path.join(os.curdir))
    if local == ImportantPaths.design:
        return os.path.join('Design')
    elif local == ImportantPaths.fonts:
        return os.path.join('Design', 'Fonts')


