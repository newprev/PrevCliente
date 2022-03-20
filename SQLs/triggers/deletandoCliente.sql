CREATE TRIGGER IF NOT EXISTS deletandoCliente
	AFTER DELETE
		ON cliente

	BEGIN
		DELETE FROM telefones 		 WHERE clienteId = OLD.clienteId;
		DELETE FROM itemContribuicao WHERE clienteId = OLD.clienteId;
		DELETE FROM ClienteInfoBanco WHERE clienteId = OLD.clienteId;
		DELETE FROM ClienteProfissao WHERE clienteId = OLD.clienteId;
		DELETE FROM aposentadoria	 WHERE clienteId = OLD.clienteId;
		DELETE FROM cnisVinculos	 WHERE clienteId = OLD.clienteId;
		DELETE FROM ppp				 WHERE clienteId = OLD.clienteId;
	END;