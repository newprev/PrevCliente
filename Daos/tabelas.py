from newPrevEnums import TiposConexoes


class TabelasConfig:

    def __init__(self, tipoBanco: TiposConexoes = TiposConexoes.local):

        self.__tblAdvogados = 'advogados'
        self.__tblEscritorios = 'escritorios'
        self.__tblCliente = 'cliente'
        self.__tblTelefones = 'telefones'
        self.__tblProcessos = 'processos'
        self.__tblCnisRemuneracoes = 'cnisRemuneracoes'
        self.__tblCnisBeneficios = 'cnisBeneficios'
        self.__tblCnisContribuicoes = 'cnisContribuicoes'
        self.__tblCnisCabecalhos = 'cnisCabecalhos'
        self.__tblIndicadores = 'indicadores'
        self.__tblEspecieBenef = 'especieBenef'
        self.__tblTetosPrev = 'tetosPrev'
        self.__tblConvMon = 'convMon'
        self.tipoBanco = tipoBanco


    # Comando SQL para criar tabela de advogados
    @property
    def sqlCreateAdvogados(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'advogadoId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (advogadoId)
        );"""
        else:
            cabecalho = 'advogadoId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblAdvogados}(
            {cabecalho}
            escritorioId INTEGER REFERENCES {self.tblEscritorios}(escritorioId) ON DELETE CASCADE,
            nomeUsuario VARCHAR(20) NOT NULL,
            sobrenomeUsuario VARCHAR(40) NOT NULL,
            login VARCHAR(30) NOT NULL,
            senha VARCHAR(30) NOT NULL,
            email VARCHAR(40) NOT NULL,
            numeroOAB VARCHAR(9) NOT NULL,
            nacionalidade VARCHAR(40) NOT NULL,
            estadoCivil VARCHAR(20) NOT NULL,
            admin BOOLEAN NOT NULL,
            ativo BOOLEAN NOT NULL,
            confirmado BOOLEAN NOT NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de escritorios
    @property
    def sqlCreateEscritorios(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'escritorioId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (escritorioId)
        );"""
        else:
            cabecalho = 'escritorioId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblEscritorios}(
            {cabecalho}
            nomeEscritorio VARCHAR(50) NOT NULL,
            nomeFantasia VARCHAR(50) NOT NULL,
            cnpj VARCHAR(14) NULL,
            cpf VARCHAR(11) NOT NULL,
            telefone VARCHAR(11) NULL,
            email VARCHAR(60) NOT NULL,
            inscEstadual VARCHAR(9) NULL,
            endereco VARCHAR(80) NULL,
            numero INT NOT NULL,
            cep VARCHAR(8) NULL,
            complemento VARCHAR(50) NOT NULL,
            cidade VARCHAR(30) NULL,
            estado VARCHAR(2) NOT NULL,
            bairro VARCHAR(50) NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de clientes
    @property
    def sqlCreateCliente(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'clienteId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (clienteId)
        );"""
        else:
            cabecalho = 'clienteId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblCliente}(
            {cabecalho}
            escritorioId INTEGER REFERENCES {self.tblAdvogados}(escritorioId) ON DELETE CASCADE,
            nomeCliente VARCHAR(20) NOT NULL,
            sobrenomeCliente VARCHAR(30) NOT NULL,
            idade INT NOT NULL,
            dataNascimento DATETIME NOT NULL,
            telefone VARCHAR(11) NULL,
            email VARCHAR(40) NOT NULL,
            rgCliente VARCHAR(9) NOT NULL,
            cpfCliente VARCHAR(11) NULL,
            nomeBanco VARCHAR(40) NULL,
            agenciaBanco VARCHAR(10) NULL,
            numeroConta VARCHAR(15) NULL,
            pixCliente VARCHAR(40) NULL,
            grauEscolaridade VARCHAR(30) NULL,
            senhaINSS VARCHAR(60) NULL,
            numCarteiraProf VARCHAR(15) NULL,
            serieCarteiraProf VARCHAR(15) NULL,
            quaCarteiraProf VARCHAR(15) NULL,
            nit VARCHAR(14) NOT NULL,
            nomeMae VARCHAR(40) NOT NULL,
            estadoCivil VARCHAR(15) DEFAULT 'SOLTEIRO(A)',
            profissao VARCHAR(30) NOT NULL,
            endereco VARCHAR(50) NOT NULL,
            estado VARCHAR(20) NOT NULL,
            cidade VARCHAR(30) NOT NULL,
            numero INT NOT NULL,
            bairro VARCHAR(30) NULL,
            cep VARCHAR(8) NOT NULL,
            complemento VARCHAR(30) NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de telefones
    @property
    def sqlCreateTelefones(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'telefoneId INT AUTO_INCREMENT,'
            bottom = """,
                PRIMARY KEY (telefoneId)
            );"""
        else:
            cabecalho = 'telefoneId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
            CREATE TABLE IF NOT EXISTS {self.tblTelefones}(
                {cabecalho}
                clienteId INTEGER REFERENCES {self.tblCliente}(clienteId) ON DELETE CASCADE,
                numero VARCHAR(11) NOT NULL,
                tipoTelefone VARCHAR(1) NOT NULL,
                pessoalRecado VARCHAR(1) NOT NULL,
                ativo BOOLEAN NOT NULL,
                dataCadastro DATETIME NOT NULL,
                dataUltAlt DATETIME NOT NULL{bottom}
            """

    # Comando SQL para criar tabela de processos
    @property
    def sqlCreateProcessos(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'processoId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (processoId)
        );"""
        else:
            cabecalho = 'processoId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.__tblProcessos}(
            {cabecalho}
            clienteId INTEGER REFERENCES {self.__tblCliente}(clienteId) ON DELETE CASCADE,
            advogadoId INTEGER REFERENCES {self.__tblAdvogados}(advogadoId) ON DELETE CASCADE,
            numeroProcesso VARCHAR(20) NULL,
            natureza INT NOT NULL,
            tipoProcesso INT NOT NULL,
            tipoBeneficio INT NOT NULL,
            subTipoApos INT NOT NULL,
            estado VARCHAR(2) NULL,
            cidade VARCHAR(40) NOT NULL,
            situacaoId INT NOT NULL DEFAULT 1,
            tempoContribuicao INT NULL, 
            dib DATETIME NULL,
            der DATETIME NULL,
            dataInicio DATETIME NULL,
            dataFim DATETIME NULL,
            incidenteProcessual INT NULL,
            valorCausa FLOAT VARCHAR(15) NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando que cria tabela de remunerações
    @property
    def sqlCreateCnisRemuneracoes(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'remuneracoesId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (remuneracoesId)
        );"""
        else:
            cabecalho = 'remuneracoesId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblCnisRemuneracoes}(
            {cabecalho}
            clienteId INTEGER REFERENCES {self.tblCliente}(clienteId) ON DELETE CASCADE,
            seq INT NOT NULL,
            competencia DATETIME NOT NULL,
            remuneracao FLOAT NOT NULL,
            indicadores VARCHAR(25) NOT NULL,
            dadoOrigem VARCHAR(15) NOT NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando que cria tabela de contribuições
    @property
    def sqlCreateCnisContribuicoes(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'contribuicoesId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (contribuicoesId)
        );"""
        else:
            cabecalho = 'contribuicoesId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblCnisContribuicoes}(
            {cabecalho}
            clienteId INTEGER REFERENCES {self.tblCliente}(clienteId) ON DELETE CASCADE,
            seq INT NOT NULL,
            competencia DATETIME NOT NULL,
            dataPagamento DATETIME NOT NULL,
            contribuicao FLOAT NOT NULL,
            salContribuicao FLOAT NOT NULL,
            indicadores VARCHAR(25) NOT NULL,
            dadoOrigem VARCHAR(15) NOT NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando que cria tabela de benefícios
    @property
    def sqlCreateCnisBeneficios(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'beneficiosId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (beneficiosId)
        );"""
        else:
            cabecalho = 'beneficiosId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblCnisBeneficios}(
            {cabecalho}
            clienteId INTEGER REFERENCES {self.tblCliente}(clienteId) ON DELETE CASCADE,
            seq INT NOT NULL,
            nb BIGINT NOT NULL,
            especie VARCHAR(45) NOT NULL,
            dataInicio DATETIME NOT NULL,
            dataFim DATETIME NOT NULL,
            situacao VARCHAR(25) NOT NULL,
            dadoOrigem VARCHAR(15) NOT NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de cabeçalhos do CNIS
    @property
    def sqlCreateCnisCabecalhos(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'cabecalhosId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (cabecalhosId)
        );"""
        else:
            cabecalho = 'cabecalhosId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblCnisCabecalhos}(
            {cabecalho}
            clienteId INTEGER REFERENCES {self.tblCliente}(clienteId) ON DELETE CASCADE,
            seq INT NOT NULL,
            nit VARCHAR(14) NOT NULL,
            nb BIGINT NULL,
            cdEmp VARCHAR(18) NULL,
            nomeEmp VARCHAR(100) NULL,
            dataInicio DATETIME NOT NULL,
            dataFim DATETIME NULL,
            tipoVinculo VARCHAR(30) NULL,
            orgVinculo VARCHAR(30) NULL,
            especie VARCHAR(70) NULL,
            indicadores VARCHAR(25) NULL,
            ultRem DATETIME NULL,
            dadoOrigem VARCHAR(15) NOT NULL,
            situacao VARCHAR(20) NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de indicadores
    @property
    def sqlCreateIndicadores(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = """
                indicadorId VARCHAR(20) NOT NULL,
                resumo VARCHAR(300) NOT NULL,
                fonte VARCHAR(300) NOT NULL,
                dataUltAlt DATETIME NOT NULL"""
            bottom = """,
            PRIMARY KEY (indicadoresId)
        );"""
        else:
            cabecalho = """
                indicadorId VARCHAR(20) PRIMARY KEY,
                resumo VARCHAR(300) NOT NULL,
                fonte VARCHAR(300) NOT NULL,
                dataUltAlt DATETIME NOT NULL,"""
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblIndicadores}(
            {cabecalho}
            descricao VARCHAR(120) NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de espécies dos benefícios
    @property
    def sqlCreateEspecieBenef(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'especieId VARCHAR(3) NOT NULL,'
            bottom = """,
            PRIMARY KEY (especieId)
        );"""
        else:
            cabecalho = 'especieId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblEspecieBenef}(
            {cabecalho}
            descricao VARCHAR(120) NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de tetos previdenciários
    @property
    def sqlCreateTetosPrev(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'tetosPrevId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (tetosPrevId, dataValidade)
        );"""
        else:
            cabecalho = 'tetosPrevId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblTetosPrev}(
            {cabecalho}
            dataValidade DATETIME NOT NULL,
            valor FLOAT NOT NULL,
            dataUltAlt DATETIME NOT NULL,
            dataCadastro DATETIME NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de conversão monetária
    @property
    def sqlCreateConvMon(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'convMonId INT AUTO_INCREMENT,'
            bottom = """,
            PRIMARY KEY (convMonId)
        );"""
        else:
            cabecalho = 'convMonId INTEGER PRIMARY KEY AUTOINCREMENT,'
            bottom = f""");"""
        return f"""
        CREATE TABLE IF NOT EXISTS {self.tblConvMon}(
            {cabecalho}
            nomeMoeda VARCHAR(20) NOT NULL,
            fator FLOAT NOT NULL,
            dataInicial DATETIME NOT NULL,
            dataFinal DATETIME NOT NULL,
            conversao VARCHAR(15) NOT NULL,
            moedaCorrente BOOLEAN NOT NULL,
            sinal VARCHAR(5) NOT NULL,
            dataUltAlt DATETIME NOT NULL,
            dataCadastro DATETIME NOT NULL{bottom}
        """

    @property
    def tblEscritorios(self):
        return self.__tblEscritorios

    @property
    def tblAdvogados(self):
        return self.__tblAdvogados

    @property
    def tblCliente(self):
        return self.__tblCliente

    @property
    def tblTelefones(self):
        return self.__tblTelefones

    @property
    def tblProcessos(self):
        return self.__tblProcessos

    @property
    def tblCnisRemuneracoes(self):
        return self.__tblCnisRemuneracoes

    @property
    def tblCnisContribuicoes(self):
        return self.__tblCnisContribuicoes

    @property
    def tblCnisBeneficios(self):
        return self.__tblCnisBeneficios

    @property
    def tblCnisCabecalhos(self):
        return self.__tblCnisCabecalhos

    @property
    def tblIndicadores(self):
        return self.__tblIndicadores

    @property
    def tblEspecieBenef(self):
        return self.__tblEspecieBenef

    @property
    def tblTetosPrev(self):
        return self.__tblTetosPrev

    @property
    def tblConvMon(self):
        return self.__tblConvMon
