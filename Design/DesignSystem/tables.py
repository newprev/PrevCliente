def newStyleSheetTable(nomeTabela: str):
    return """
#""" + nomeTabela + """ {
	background-color: transparent;
}

#""" + nomeTabela + """::item{
	margin: 4px;
}

QHeaderView::section {
    background-color: rgb(52, 73, 94);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
	min-height: 45px;
}

QHeaderView::down-arrow {
    icon-color: white;
}

QHeaderView::up-arrow {
    icon-color: white;
}"""