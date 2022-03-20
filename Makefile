## Paths do projeto
ROOT = .

## Paths para o design
UI_PATH = Design/UI
PYUI_PATH = Design/pyUi
SRC_PATH = Resources

## Parâmetros para os builds dos designs
UI_FILE = arquivo.ui
SRC_FILE = arquivo.qrc
SQL_FILE = arquivo.sql

## @ Limpeza
cleanAll: ## Limpa todo o cache e exclui o banco de dados
	@echo 'Limpando o cache'
	@rm -f .sync/.syncFile.json && echo "---> .sync/.syncFile.json"
	@rm -f cache/.escritorio.json && echo "---> cache/.escritorio.json"
	@rm -f cache/.login.json && echo "---> cache/.login.json"
	@rm -f Banco/producao.db	&& echo "---> Banco/producao.db"
	@rm -f crypt/.privateKey.txt && echo "---> crypt/.privateKey.txt"
	@rm -f crypt/publicKey.txt && echo "---> crypt/publicKey.txt"


## @ Build
compile: ## Compila alguns arquivos do programa
	rm compilado/*
	cp processos/aposentadoria.py compilado/aposentadoria.py
	easycython compilado/aposentadoria.py
	rm -f *.so


## @ Build resources
ui2py: ## Cria o arquivo python (.py) a partir de um arquivo de layout (.ui) vindo do QDesign
	pyuic5 -x ${UI_PATH}/${UI_FILE}.ui -o ${PYUI_PATH}/${UI_FILE}.py
resources: ## Cria o arquivo de recurso do python my_resource.py a partir de um arquivo de recurso do QDesign
	pyrcc5 -o ${SRC_PATH}/${SRC_FILE}.py ${SRC_PATH}/${SRC_FILE}.qrc


## @ Backup
backupAll: ## Roda todos os scripts de backup dentro da pasta de backup
	sudo sqlite3 Banco/producao.db < ../backup/cTipoAposentadoria.sql
