import datetime
from typing import List
import pandas as pd

from Daos.daoCalculos import DaoCalculos
from helpers import comparaMesAno, calculaDiaMesAno, mascaraDataSql, strToDatetime

from modelos.cnisCabecalhoModelo import CabecalhoModelo
from modelos.expSobrevidaModelo import ExpectativaSobrevidaModelo
from modelos.processosModelo import ProcessosModelo
from modelos.clienteModelo import ClienteModelo
from newPrevEnums import RegraTransicao, GeneroCliente, TamanhoData


# Reforma 13/11/2019
# Ar: Antes da reforma
# Dr: Depois da reforma


class CalculosAposentadoria:

    def __init__(self, processo: ProcessosModelo, cliente: ClienteModelo, db=None):
        self.processo = processo
        self.cliente = cliente
        self.daoCalculos = DaoCalculos(db)
        self.cabecalhos: list = list(self.daoCalculos.buscaCabecalhosClienteId(self.cliente.clienteId))
        self.listaRemuneracoes = list(self.daoCalculos.buscaTodasRemuneracoes(cliente.clienteId))
        self.listaContribuicoes = list(self.daoCalculos.buscaTodasContribuicoes(cliente.clienteId))

        self.mediaSalarial: float = self.calculaMediaSalarial()
        self.dataReforma: datetime.date = datetime.date(2019, 11, 13)
        self.fatorPrevidenciario: int = 1
        self.tempoContribCalculado: list = self.calculaTempoContribuicao()
        self.pontuacao: int = sum(self.tempoContribCalculado) + self.cliente.idade

        self.regrasTransicao = {
            RegraTransicao.pontos: self.regraTransPontos(),
            RegraTransicao.reducaoIdadeMinima: self.regraRedIdadeMinima(),
            RegraTransicao.pedagio50: self.regraPedagio50(),
            RegraTransicao.reducaoTempoContribuicao: self.regraRedTempoContrib()
        }

        self.valorBeneficios = {
            RegraTransicao.pontos: 0,
            RegraTransicao.reducaoIdadeMinima: 0,
            # TODO: Para calcular o valor do benefício, preciso saber qual o fator previdenciário
            RegraTransicao.pedagio50: 0
        }

        self.calculaBeneficios()

        print('\n\n------------------------------------- ')
        print(f'len(self.listaRemuneracoes): {len(self.listaRemuneracoes)}')
        print(f'len(self.listaContribuicoes): {len(self.listaContribuicoes)}')
        print(f'self.processo.tempoContribuicao: {self.processo.tempoContribuicao}')
        print(f'self.regrasTransicao: {self.regrasTransicao}')
        print(f'self.valorBeneficios: {self.valorBeneficios}')
        print(f'self.tempoContribCalculado: {self.tempoContribCalculado}')
        print('-------------------------------------\n\n')

    def calculaFatorPrevidenciario(self):
        """
        Cálculo do fator previdenciário

        :var<float>: tempCont - Tempo de contribuição até o momento da aposentadoria
        :var<float>: aliq - Alíquota de contribuição
        :var<float>: expSobrevida - Expectativa de sobrevida após a data do início do benefício (dib)
        :var<float>: idade - Idade do cliente na data do início do benefício

        :return<float>: fatorPrev  = ((tempCont * aliq) / expSobrevida) * (1 + (idade + (tempCont * aliq)) / 100)
        """
        tempCont: float = self.tempoContribCalculado[2] + ((self.tempoContribCalculado[0] / 30) + self.tempoContribCalculado[1] / 12)
        aliq: float = 0.31
        idade = self.cliente.idade
        expSobrevidaModelo: ExpectativaSobrevidaModelo = self.daoCalculos.buscaExpSobrevidaPorData(datetime.datetime.now(), idade)
        expSobrevida: int = expSobrevidaModelo.expectativaSobrevida

        fatorPrev = ((tempCont * aliq) / expSobrevida) * (1 + (idade + (tempCont * aliq)) / 100)

        print('\n\n------------------------------------ calculaFatorPrevidenciario')
        print(f"tempCont: {tempCont}")
        print(f"aliq: {aliq}")
        print(f"idade: {idade}")
        print(f"expSobrevida: {expSobrevida}")
        print(f"fatorPrev: {fatorPrev}")
        print('------------------------------------ calculaFatorPrevidenciario\n\n')
        return fatorPrev




    def calculaMediaSalarial(self):
        dfContribuicoes: pd.DataFrame = self.daoCalculos.buscaRemContPorData(self.cliente.clienteId, '1994-07-31')
        return dfContribuicoes['salContribuicao'].mean()

    def calculaTempoContribuicao(self, cabecalhos: list = None) -> List[int]:
        listTimedeltas: list = []
        totalDias: int = 0
        antesReforma: bool = True

        if cabecalhos is None:
            listaBanco: List[CabecalhoModelo] = self.cabecalhos
        else:
            listaBanco: List[CabecalhoModelo] = cabecalhos

        for cabecalho in listaBanco:
            
            if comparaMesAno(cabecalho.dataInicio, self.dataReforma) != 1:
                antesReforma = False
                
            if antesReforma:    
                if cabecalho.nb is not None:
                    if cabecalho.situacao != 'INDEFERIDO':
                        listTimedeltas.append(self.calculaTimedeltaAr(cabecalho, listaBanco))
                    else:
                        listTimedeltas.append(self.calculaTimedeltaAr(cabecalho, listaBanco, buscaProxJob=False))
                else:
                    listTimedeltas.append(self.calculaTimedeltaAr(cabecalho, listaBanco))
                    
            else:
                if cabecalho.nb is not None:
                    if cabecalho.situacao != 'INDEFERIDO':
                        listTimedeltas.append(self.calculaTimedeltaDr(cabecalho, listaBanco))
                    else:
                        listTimedeltas.append(self.calculaTimedeltaDr(cabecalho, listaBanco, buscaProxJob=False))
                else:
                    listTimedeltas.append(self.calculaTimedeltaDr(cabecalho, listaBanco))

        for delta in listTimedeltas:
            totalDias += delta.days

        return calculaDiaMesAno(totalDias)

    def calculaTimedeltaAr(self, cabecalho: CabecalhoModelo, listaCabecalhos: list, buscaProxJob: bool = True) -> datetime.timedelta:
        """
        Para o tempo de serviço antes da reforma previdenciária, 13/11/2019, o tempo de contribuição é calculado dia a dia.

        :return - timedalta com a diferença de dias de trabalho
        """

        if cabecalho.dataInicio is None or cabecalho.dataInicio == datetime.datetime.min:
            return datetime.timedelta(days=0)

        if cabecalho.dataFim is None or cabecalho.dataFim == datetime.datetime.min:
            if cabecalho.ultRem is None or cabecalho.ultRem == datetime.datetime.min:
                if not buscaProxJob:
                    return datetime.datetime.now() - cabecalho.dataInicio

                # Caso o registro não tenha dataFim nem ultRem, busca a dataInicio do próximo registro
                else:
                    if listaCabecalhos.index(cabecalho) + 1 >= len(listaCabecalhos):
                        return datetime.datetime.now() - cabecalho.dataInicio
                    else:
                        index = listaCabecalhos.index(cabecalho) + 1
                        cabecalhoAux: CabecalhoModelo = listaCabecalhos[index]
                        return cabecalhoAux.dataInicio - cabecalho.dataInicio
            else:
                return cabecalho.ultRem - cabecalho.dataInicio
        else:
            return cabecalho.dataFim - cabecalho.dataInicio

    def calculaTimedeltaDr(self, cabecalho: CabecalhoModelo, listaCabecalhos: list, buscaProxJob: bool = True) -> datetime.timedelta:
        """
        Após a reforma previdenciária, 13/11/2019, o tempo de contribuição é calculado mês a mês, descontando os casos que ocorrem o indicador 'PREC-MENOR-MIN'

        :return - timedalta com a diferença de dias de trabalho
        """

        somaIndicadores: int = 0
        indicadoresASubtrair = ['IREC-LC123', 'PREC-MENOR-MIN']

        if cabecalho.dataInicio is None or cabecalho.dataInicio == datetime.datetime.min:
            return datetime.timedelta(days=0)

        for remuneracao in self.listaRemuneracoes:
            if remuneracao.seq == cabecalho.seq:
                if remuneracao.indicadores in indicadoresASubtrair:
                    somaIndicadores += 1

        for contribuicao in self.listaContribuicoes:
            if contribuicao.seq == cabecalho.seq:
                if contribuicao.indicadores in indicadoresASubtrair:
                    somaIndicadores += 1

        if cabecalho.dataFim is None or cabecalho.dataFim == datetime.datetime.min:
            if cabecalho.ultRem is None or cabecalho.ultRem == datetime.datetime.min:
                if not buscaProxJob:
                    return datetime.datetime.now() - cabecalho.dataInicio

                # Caso o registro não tenha dataFim nem ultRem, busca a dataInicio do próximo registro
                else:
                    index = listaCabecalhos.index(cabecalho) + 1
                    cabecalhoAux: CabecalhoModelo = listaCabecalhos[index]
                    diferencaMeses: int = cabecalhoAux.dataInicio.month - cabecalho.dataInicio.month + 1 - somaIndicadores
                    return datetime.timedelta(days=30 * diferencaMeses)
            else:
                diferencaMeses: int = cabecalho.ultRem.month - cabecalho.dataInicio.month + 1 - somaIndicadores
                return datetime.timedelta(days=30 * diferencaMeses)
        else:
            diferencaMeses: int = cabecalho.dataFim.month - cabecalho.dataInicio.month + 1 - somaIndicadores
            return datetime.timedelta(days=30 * diferencaMeses)

    def regraTransPontos(self) -> bool:
        pontuacaoAtingida: bool = False
        tempoMinimoContrib: bool = False

        if self.cliente.genero == GeneroCliente.masculino.value:
            pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.masculino)
            tempoMinimoContrib = self.tempoContribCalculado[2] >= 35
        else:
            pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.feminino)
            tempoMinimoContrib = self.tempoContribCalculado[2] >= 30

        return pontuacaoAtingida and tempoMinimoContrib

    def regraRedIdadeMinima(self) -> bool:
        acrescimoMensal: float = 0
        acrescimoAnual: int = 0
        idadeMesesCliente: float = 0
        mesAtual: int = datetime.date.today().month
        mesNascCliente: int = strToDatetime(self.cliente.dataNascimento, TamanhoData.gg).month

        # Ginática matemática para caclular a qtd de meses até o aniversário do(a) cliente
        if mesAtual - mesNascCliente > 0:
            if mesAtual - mesNascCliente < 6:
                idadeMesesCliente = 0
            else:
                idadeMesesCliente = 0.5
        else:
            if 12 + (mesAtual - mesNascCliente) < 6:
                idadeMesesCliente = 0
            else:
                idadeMesesCliente = 0.5

        if mesAtual < 6:
            acrescimoMensal = 0
        elif 6 <= mesAtual < 12:
            acrescimoMensal = 0.5
        elif mesAtual == 12:
            acrescimoMensal = 1

        acrescimoAnual: int = datetime.date.today().year - self.dataReforma.year
        totalAcrescimo = acrescimoAnual * (1 + acrescimoMensal)

        if self.cliente.genero == 'M':
            if totalAcrescimo > 4:
                totalAcrescimo = 4
            return self.tempoContribCalculado[2] >= 35 and self.cliente.idade + idadeMesesCliente >= 61 + totalAcrescimo
        else:
            if totalAcrescimo > 6:
                totalAcrescimo = 6
            return self.tempoContribCalculado[2] >= 30 and self.cliente.idade + idadeMesesCliente >= 56 + totalAcrescimo

    def regraPedagio50(self) -> bool:
        listaCabecalhosPedagio = []
        tempoContribAntesReforma = 0

        for cabecalho in self.cabecalhos:
            if cabecalho.dataFim.date() <= self.dataReforma:
                listaCabecalhosPedagio.append(cabecalho)
        tempoContribAntesReforma = self.calculaTempoContribuicao(listaCabecalhosPedagio)[2]

        # print('***************************')
        # print(f"self.cliente.idade - (datetime.datetime.now().year - 2019): {self.cliente.idade - (datetime.datetime.now().year - 2019)}")
        # print(f'tempoContribAntesReforma: {tempoContribAntesReforma}')
        # print('***************************')

        if self.cliente.genero == 'M':
            return 35 - tempoContribAntesReforma <= 2
        else:
            return 30 - tempoContribAntesReforma <= 2

    def regraRedTempoContrib(self) -> bool:
        """
        Para as mulheres, a idade mínima para conquistar o benefício é acrescida de 6 meses a cada ano à partir de 2020.
        Em 2023, esse acréscimo é interrompido, permanecendo com o máximo de 62 anos.
        :return: bool
        """

        if self.cliente.genero == 'M':
            return self.tempoContribCalculado[2] >= 15 and self.cliente.idade >= 65
        else:
            mesAtual: int = datetime.date.today().month
            mesNascCliente: int = strToDatetime(self.cliente.dataNascimento, TamanhoData.gg).month

            if datetime.date.today().year >= 2023:
                acrescimoTotal: float = 2
            else:
                acrescimoTotal: float = 0.5 * (datetime.date.today().year - 2019)

            # Ginática matemática para caclular a qtd de meses até o aniversário do(a) cliente
            if mesAtual - mesNascCliente > 0:
                if mesAtual - mesNascCliente < 6:
                    idadeMesesCliente = 0
                else:
                    idadeMesesCliente = 0.5
            else:
                if 12 + (mesAtual - mesNascCliente) < 6:
                    idadeMesesCliente = 0
                else:
                    idadeMesesCliente = 0.5

            return self.tempoContribCalculado[2] >= 15 and self.cliente.idade + idadeMesesCliente >= 60 + acrescimoTotal

    def calculaPontosRegraPontos(self, generoCliente: GeneroCliente) -> bool:
        """
        Avalia a pontuação mínima e o tempo mínimo de contribuição (20 anos Homens / 15 anos Mulheres)
        :return bool
        """
        acrescimoAnual = datetime.date.today().year - 2019
        if generoCliente == GeneroCliente.masculino:
            if acrescimoAnual >= 9:
                acrescimoAnual = 9
            return self.pontuacao >= 96 + acrescimoAnual and self.tempoContribCalculado[2] >= 20
        else:
            if acrescimoAnual >= 14:
                acrescimoAnual = 14
            return self.pontuacao >= 86 + acrescimoAnual and self.tempoContribCalculado[2] >= 15

    def calculaBeneficios(self):
        """
        O método buscaRemContPorData retorna um DataFrame com as seguintes colunas: ['clienteId', 'infoId', 'competencia', 'salContribuicao', 'indicadores', 'tipoInfo']
        """
        if self.cliente.genero == 'M':
            tempoMinimo = 20
        else:
            tempoMinimo = 15

        if self.regrasTransicao[RegraTransicao.pontos]:
            self.valorBeneficios[RegraTransicao.pontos] = self.mediaSalarial * (0.6 + 2*(self.tempoContribCalculado[2] - tempoMinimo)/100)

        if self.regrasTransicao[RegraTransicao.reducaoIdadeMinima]:
            self.valorBeneficios[RegraTransicao.reducaoIdadeMinima] = self.mediaSalarial * (0.6 + 2 * (self.tempoContribCalculado[2] - tempoMinimo) / 100)

        if self.regrasTransicao[RegraTransicao.pedagio50]:
            self.fatorPrevidenciario = self.calculaFatorPrevidenciario()
            self.valorBeneficios[RegraTransicao.pedagio50] = 4

        if self.regrasTransicao[RegraTransicao.reducaoTempoContribuicao]:
            self.valorBeneficios[RegraTransicao.reducaoTempoContribuicao] = self.mediaSalarial * (0.6 + 2 * (self.tempoContribCalculado[2] - tempoMinimo) / 100)

