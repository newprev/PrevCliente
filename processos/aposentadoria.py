import datetime
from typing import List

from Daos.daoCalculos import DaoCalculos
from helpers import comparaMesAno, calculaDiaMesAno

from modelos.cnisCabecalhoModelo import CabecalhoModelo
from modelos.processosModelo import ProcessosModelo
from modelos.clienteModelo import ClienteModelo
from newPrevEnums import NaturezaProcesso, TipoProcesso, GeneroCliente


# Reforma 13/11/2019
# Ar: Antes da reforma
# Dr: Depois da reforma


class CalculosAposentadoria:

    def __init__(self, processo: ProcessosModelo, cliente: ClienteModelo, db=None):
        self.processo = processo
        self.cliente = cliente
        self.cabecalhos: list = []
        self.daoCalculos = DaoCalculos(db)
        self.listaRemuneracoes = list(self.daoCalculos.buscaTodasRemuneracoes(cliente.clienteId))
        self.listaContribuicoes = list(self.daoCalculos.buscaTodasContribuicoes(cliente.clienteId))
        self.tempoContribCalculado: list = self.calculaTempoContribuicao()
        self.pontuacao: int = sum(self.tempoContribCalculado) + self.cliente.idade

        print(f"calculaPontosRegraPontos: {self.regraTransPontos()}")

        print(' ------------------------------------- ')
        print(f'len(self.listaRemuneracoes): {len(self.listaRemuneracoes)}')
        print(f'len(self.listaContribuicoes): {len(self.listaContribuicoes)}')
        print(f'self.processo.tempoContribuicao: {self.processo.tempoContribuicao}')

        print(' ------------------------------------- ')

    def calculaTempoContribuicao(self) -> List[int]:
        dataReforma: datetime.date = datetime.date(2019, 11, 13)
        listTimedeltas: list = []
        totalDias: int = 0
        antesReforma: bool = True

        listaBanco: List[CabecalhoModelo] = list(self.daoCalculos.buscaCabecalhosClienteId(self.cliente.clienteId))

        for cabecalho in listaBanco:
            
            if comparaMesAno(cabecalho.dataInicio, dataReforma) != 1:
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

    def regraTransPontos(self):
        pontuacaoAtingida: bool = False
        tempoMinimoContrib: bool = False

        if self.cliente.genero == GeneroCliente.masculino.value:
            pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.masculino)
            tempoMinimoContrib = self.tempoContribCalculado[2] >= 35
        else:
            pontuacaoAtingida = self.calculaPontosRegraPontos(GeneroCliente.feminino)
            tempoMinimoContrib = self.tempoContribCalculado[2] >= 30

        print(f"self.tempoContribCalculado[2]: {self.tempoContribCalculado[2]}")
        print(f"self.pontuacao: {self.pontuacao}")

        return pontuacaoAtingida and tempoMinimoContrib

    def calculaPontosRegraPontos(self, generoCliente: GeneroCliente) -> bool:
        acrescimoAnual = datetime.date.today().year - 2019
        if generoCliente == GeneroCliente.masculino:
            return self.pontuacao >= 96 + acrescimoAnual
        else:
            return self.pontuacao >= 96 + acrescimoAnual
