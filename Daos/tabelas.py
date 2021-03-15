class TabelasConfig:

    def __init__(self):

        self.__tblCliente = 'cliente'
        self.__tblCnisRemuneracoes = 'cnisRemuneracoes'
        self.__tblCnisBeneficios = 'cnisBeneficios'
        self.__tblCnisContribuicoes = 'cnisContribuicoes'

#     # Comando SQL para criar tabela de clientes
        self.__sqlCreateCliente = f"""CREATE TABLE IF NOT EXISTS {self.tblCliente}(
                    clienteId INT AUTO_INCREMENT,
                    nomeCliente VARCHAR(20) NOT NULL,
                    sobrenomeCliente VARCHAR(30) NOT NULL,
                    telefone VARCHAR(11) NULL,
                    email VARCHAR(40) NOT NULL,
                    rgCliente VARCHAR(8) NOT NULL,
                    cpfCliente VARCHAR(11) NULL,
                    numCarteiraProf VARCHAR(15) NULL,
                    serieCarteiraProf VARCHAR(15) NULL,
                    quaCarteiraProf VARCHAR(15) NULL,
                    nit VARCHAR(14) NOT NULL,
                    nomeMae VARCHAR(40) NOT NULL,
                    estadoCivil VARCHAR(15) NOT NULL DEFAULT 'SOLTEIRO(A)',
                    profissao VARCHAR(30) NOT NULL,
                    endereco VARCHAR(50) NOT NULL,
                    estado VARCHAR(20) NOT NULL,
                    cidade VARCHAR(30) NOT NULL,
                    bairro VARCHAR(30) NULL,
                    cep VARCHAR(8) NOT NULL,
                    complemento VARCHAR(30) NULL,
                    dataCadastro DATETIME NOT NULL,
                    dataUltAlt DATETIME NOT NULL,
                    PRIMARY KEY (clienteId)
                );"""

        # Comando que cria tabela de remunerações
        self.__sqlCreateCnisRemuneracoes = f"""CREATE TABLE IF NOT EXISTS {self.tblCnisRemuneracoes}(
                    remuneracoesId INT AUTO_INCREMENT,
                    clienteId INT NOT NULL,
                    seq INT NOT NULL,
                    competencia DATETIME NOT NULL,
                    remuneracao FLOAT NOT NULL,
                    indicadores VARCHAR(25) NOT NULL,
                    dataCadastro DATETIME NOT NULL,
                    dataUltAlt DATETIME NOT NULL,
                    PRIMARY KEY (remuneracoesId)
                );"""

        # Comando que cria tabela de contribuições
        self.__sqlCreateCnisContribuicoes = f"""CREATE TABLE IF NOT EXISTS {self.tblCnisContribuicoes}(
                    contribuicoesId INT AUTO_INCREMENT,
                    clienteId INT NOT NULL,
                    seq INT NOT NULL,
                    competencia DATETIME NOT NULL,
                    dataPagamento DATETIME NOT NULL,
                    contribuicao FLOAT NOT NULL,
                    salContribuicao FLOAT NOT NULL,
                    indicadores VARCHAR(25) NOT NULL,
                    dataCadastro DATETIME NOT NULL,
                    dataUltAlt DATETIME NOT NULL,
                    PRIMARY KEY (contribuicoesId)
                );"""

        # Comando que cria tabela de benefícios
        self.__sqlCreateCnisBeneficios = f"""CREATE TABLE IF NOT EXISTS {self.tblCnisBeneficios}(
                    beneficiosId INT AUTO_INCREMENT,
                    clienteId INT NOT NULL,
                    seq INT NOT NULL,
                    nb BIGINT NOT NULL,
                    especie VARCHAR(45) NOT NULL,
                    dataInicio DATETIME NOT NULL,
                    dataFim DATETIME NOT NULL,
                    situacao VARCHAR(25) NOT NULL,
                    dataCadastro DATETIME NOT NULL,
                    dataUltAlt DATETIME NOT NULL,
                    PRIMARY KEY (beneficiosId)
                );"""

    @property
    def sqlCreateCliente(self):
        return self.__sqlCreateCliente

    @property
    def sqlCreateCnisRemuneracoes(self):
        return self.__sqlCreateCnisRemuneracoes

    @property
    def sqlCreateCnisContribuicoes(self):
        return self.__sqlCreateCnisContribuicoes

    @property
    def sqlCreateCnisBeneficios(self):
        return self.__sqlCreateCnisBeneficios

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
