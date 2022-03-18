def selectItensDados(clienteId: int):
    strComando = f"""
    SELECT
        icon.competencia,
        icon.contribuicao,
        IFNULL(iam.fator, 1),
        IFNULL(tp.valor, 6433) AS teto
    FROM itemContribuicao icon
    LEFT JOIN indiceAtuMonetaria iam
        ON STRFTIME('%Y-%m', iam.dataReferente) = STRFTIME('%Y-%m', icon.competencia)
            AND STRFTIME('%Y-%m', iam.dib) = STRFTIME('%Y-%m', '2019-11-01')
    LEFT JOIN tetosPrev tp
        ON STRFTIME('%Y-%m', tp.dataValidade) = STRFTIME('%Y-%m', icon.competencia)
    WHERE icon.clienteId = {clienteId}
    ORDER BY competencia
    """
    return strComando

def buscaIndicesByClienteId(clienteId: int, indices: list = []) -> str:
    if len(indices) == 0:
        indices.append('')

    if 0 <= len(indices) <= 1:

        strComando = f"""
        SELECT indicadores FROM cnisVinculos
            WHERE clienteId = {clienteId}
                AND indicadores LIKE '%{indices[0]}%'

        UNION ALL

        SELECT indicadores FROM cnisContribuicoes
            WHERE clienteId = {clienteId}
                AND indicadores LIKE '%{indices[0]}%'

        UNION ALL

        SELECT indicadores FROM cnisRemuneracoes
            WHERE clienteId = {clienteId}
                AND indicadores LIKE '%{indices[0]}%';"""
    else:
        strOr: str = ''
        for condicao in indices:
            strOr += f"""
            indicadores LIKE '%{condicao}%' OR"""
        strOr = strOr.removesuffix(' OR')

        strComando = f"""
        SELECT indicadores FROM cnisVinculos
            WHERE clienteId = {clienteId}
                AND ({strOr})

        UNION ALL

        SELECT indicadores FROM cnisContribuicoes
            WHERE clienteId = {clienteId}
                AND ({strOr})

        UNION ALL

        SELECT indicadores FROM cnisRemuneracoes
            WHERE clienteId = {clienteId}
                AND ({strOr})"""

    return strComando

def remuEContrib(clienteId: int, seq: int) -> str:
    return f"""
    SELECT
    --Contribuições
    con.itemContribuicaoId, con.seq, con.competencia, 
    IFNULL(con.salContribuicao, 0) AS salContribuicao, con.indicadores,
    
    --Conversão monetária
    cm.sinal, cm.convMonId, cm.nomeMoeda
    
    --Tetos previdenciários
FROM itemContribuicao con
    JOIN convMon cm 
        ON con.competencia >= cm.dataInicial
            AND con.competencia <= cm.dataFinal
WHERE con.clienteId = {clienteId}
    AND con.seq = {seq};
            """