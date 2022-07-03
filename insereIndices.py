from os import path
import os
from datetime import datetime
from Banco.daoInformacoes import DaoInformacoes
from connections import ConfigConnection
from modelos.indicesAtuMonetarioModelo import IndiceAtuMonetarioModelo
from util.enums.newPrevEnums import TiposConexoes

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

def carregaArquivo(path: str):
    with open(path, mode='r') as f:
        linhas = f.readlines()
        return (l[1:] if l[0] == ',' else l[:] for l in linhas)


def avaliaInfo(data: str, tipo: str):
    if tipo == 'nomeArquivo':
        return datetime.strptime(data, '%Y-%m')
    elif tipo == 'fator':
        return float(data.replace(',', '.'))
    elif tipo == 'dataReferente':
        if data[0].isdigit():
            return datetime.strptime(data, '%m/%y')
        else:
            for chave, valor in meses.items():
                if valor.lower()[:3] == data[:3]:
                    mes = f"{chave}"
                    if len(mes) == 1:
                        mes = '0' + mes
                    return datetime.strptime(f"{mes}/{data[4:]}", '%m/%y')


def main():
    tipoConexao = TiposConexoes.sqlite
    dbConnection = ConfigConnection(instanciaBanco=tipoConexao)
    db = dbConnection.getDatabase()

    pathArquivos = path.join(os.getcwd(), os.path.pardir, 'Documentos', 'indicesAtualizacao')
    listaArquivos = os.listdir(pathArquivos)
    daoInformacoes = DaoInformacoes(db)
    listaIndices = []

    for arquivo in listaArquivos:
        linhas = carregaArquivo(path.join(pathArquivos, arquivo))
        nomeArquivo: datetime = avaliaInfo(arquivo[:len(arquivo) - 4], 'nomeArquivo')
        for f in linhas:
            dataReferente = avaliaInfo(f[:f.find(',')], 'dataReferente')

            fator = avaliaInfo(f[f.find('"')+1:f.rfind('"')], 'fator')
            # print(f"{nomeArquivo} - {dataReferente} - {fator}")

            indiceAtu = IndiceAtuMonetarioModelo()
            indiceAtu.dataReferente = dataReferente
            indiceAtu.fator = fator
            indiceAtu.dib = nomeArquivo
            indiceAtu.dataCadastro = datetime.now()
            indiceAtu.dataUltAlt = datetime.now()

            listaIndices.append(indiceAtu)

        # print(f'- nomeArquivo: {nomeArquivo.date()} - linhas: {i}')
    print(f'Qtd de inserções: {len(listaIndices)}')
    daoInformacoes.insereListaIndicesAtuMonetario(listaIndices)

main()
