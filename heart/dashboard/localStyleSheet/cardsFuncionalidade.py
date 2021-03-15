def inicializaCard(tipo: str):
    if tipo is None:
        tipo = ''

    if tipo.upper() == 'CLIENTE':
        backgroundImg = "background-image: url(:/cliente/customer.png);"
    elif tipo.upper() == 'ENTREVISTA':
        backgroundImg = "background-image: url(:/entrevista/entrevista.png);"
    else:
        backgroundImg = "background-image: url(:/cliente/customer.png);"

    return """QPushButton {
    font-family: "Fira Sans";
	color: white;

	background-color: qlineargradient(spread:pad, x1:0.481102, y1:0.688, x2:0.477, y2:0, stop:0 rgba(41, 128, 185, 255), stop:1 rgba(66, 147, 215, 255));
	border-radius: 10px;
	"""+ backgroundImg +"""
	background-repeat: no-repeat;
	background-position: center;
	text-align: bottom center;
	padding: 70px 0px 0px 0px;
}"""