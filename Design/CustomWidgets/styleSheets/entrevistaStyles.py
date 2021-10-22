def iconeEscolhido(escolhido: bool) -> str:
    if escolhido:
        return """
        #frIcone{
	background-image: url(:/escolha/entrevista-check.png);
	background-position: center;
	background-repeat: no-repeat;
}"""
    else:
        return """
        #frIcone{
	background-image: url(:/escolha/entrevista-uncheck.png);
	background-position: center;
	background-repeat: no-repeat;
}"""