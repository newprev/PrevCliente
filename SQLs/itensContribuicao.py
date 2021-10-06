
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
