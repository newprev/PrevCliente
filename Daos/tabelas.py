from newPrevEnums import TiposConexoes


class TabelasConfig:

    def __init__(self, tipoBanco: TiposConexoes = TiposConexoes.local):

        self.__tblCliente = 'cliente'
        self.__tblCnisRemuneracoes = 'cnisRemuneracoes'
        self.__tblCnisBeneficios = 'cnisBeneficios'
        self.__tblCnisContribuicoes = 'cnisContribuicoes'
        self.__tblCnisCabecalhos = 'cnisCabecalhos'
        self.__tblIndicadores = 'indicadores'
        self.__tblEspecieBenef = 'especieBenef'
        self.__tblTetosPrev = 'tetosPrev'
        self.__tblConvMon = 'convMon'
        self.tipoBanco = tipoBanco


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
            nomeCliente VARCHAR(20) NOT NULL,
            sobrenomeCliente VARCHAR(30) NOT NULL,
            idade INT NOT NULL,
            dataNascimento DATETIME NOT NULL,
            telefone VARCHAR(11) NULL,
            email VARCHAR(40) NOT NULL,
            rgCliente VARCHAR(9) NOT NULL,
            cpfCliente VARCHAR(11) NULL,
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
            bairro VARCHAR(30) NULL,
            cep VARCHAR(8) NOT NULL,
            complemento VARCHAR(30) NULL,
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
            clienteId INT NOT NULL,
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
            clienteId INT NOT NULL,
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
            clienteId INT NOT NULL,
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
            clienteId INT NOT NULL,
            seq INT NOT NULL,
            nit VARCHAR(14) NOT NULL,
            cdEmp VARCHAR(18) NOT NULL,
            nomeEmp VARCHAR(100) NOT NULL,
            dataInicio DATETIME NOT NULL,
            dataFim DATETIME NOT NULL,
            tipoVinculo VARCHAR(30) NOT NULL,
            indicadores VARCHAR(25) NOT NULL,
            ultRem DATETIME NOT NULL,
            dadoOrigem VARCHAR(15) NOT NULL,
            dataCadastro DATETIME NOT NULL,
            dataUltAlt DATETIME NOT NULL{bottom}
        """

    # Comando SQL para criar tabela de indicadores
    @property
    def sqlCreateIndicadores(self):
        if self.tipoBanco != TiposConexoes.sqlite:
            cabecalho = 'indicadoresId VARCHAR(20) NOT NULL,'
            bottom = """,
            PRIMARY KEY (indicadoresId)
        );"""
        else:
            cabecalho = 'indicadoresId VARCHAR(20) PRIMARY KEY,'
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
    def tblCliente(self):
        return self.__tblCliente

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
