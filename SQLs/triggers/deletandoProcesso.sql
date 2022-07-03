CREATE TRIGGER IF NOT EXISTS deletandoProcesso
	AFTER DELETE
		ON Processos

	BEGIN
		DELETE FROM IncidenteProcessual WHERE processoId = OLD.processoId;
	END;