from util.enums.telaEnums import TelaPosicao


def inicializaCard(tipo: TelaPosicao):
    if tipo == TelaPosicao.Cliente:
        backgroundImg = "background-image: url(:/cliente/customer.png);"
    elif tipo == TelaPosicao.Entrevista:
        backgroundImg = "background-image: url(:/entrevista/entrevista.png);"
    elif tipo == TelaPosicao.Calculos:
        backgroundImg = "background-image: url(:/calculos/calculos.png);"
    elif tipo == TelaPosicao.Resumo:
        backgroundImg = "background-image: url(:/resumo/resumo.png);"
    elif tipo == TelaPosicao.Processo:
        backgroundImg = "background-image: url(:/processo/search.png);"
    else:
        backgroundImg = "background-image: url(:/cliente/customer.png);"

    return """QPushButton {
    font-family: "TeX Gyre Adventor";
	color: white;

	background-color: qlineargradient(spread:pad, x1:0.481102, y1:0.688, x2:0.477, y2:0, stop:0 rgba(41, 128, 185, 255), stop:1 rgba(66, 147, 215, 255));
	border-radius: 10px;
	"""+ backgroundImg +"""
	background-repeat: no-repeat;
	background-position: center;
	text-align: bottom center;
	padding: 70px 0px 0px 0px;
}"""