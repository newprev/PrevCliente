cleanAll:
	@echo 'Limpando o cache'
	@rm -f .sync/.syncFile && echo "---> .sync/.syncFile"
	@rm -f cache/.escritorio.json && echo "---> cache/.escritorio.json"
	@rm -f cache/.login.json && echo "---> cache/.login.json"
	@rm -f Daos/producao.db	&& echo "---> Daos/producao.db"

compile:
	rm compilado/*
	cp processos/aposentadoria.py compilado/aposentadoria.py
	easycython compilado/aposentadoria.py
	rm -f *.so