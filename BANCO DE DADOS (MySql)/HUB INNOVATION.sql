CREATE DATABASE HUB_INNOVATION;
USE HUB_INNOVATION;

-- DROP DATABASE HUB_INNOVATION;

CREATE TABLE SALA (
	ID_SALA INT PRIMARY KEY NOT NULL,
    IMG VARCHAR (255) NOT NULL,
    PALESTRA VARCHAR (255) NOT NULL,
    PALESTRANTE INT,
    VAGAS INT NOT NULL,
    CONSTRAINT FK_Palestrante FOREIGN KEY (PALESTRANTE) REFERENCES PALESTRANTE (ID_SPEAKER) 
);

CREATE TABLE PALESTRANTE (
	ID_SPEAKER INT AUTO_INCREMENT PRIMARY KEY,
	NOME VARCHAR (255) NOT NULL,
    DESCRICAO VARCHAR (255),
    LINKEDIN VARCHAR (255),
    INSTRAGRAM VARCHAR (255)
);

CREATE TABLE USUARIO (
	ID_USER INT AUTO_INCREMENT PRIMARY KEY,
	NOME VARCHAR (255) NOT NULL,
    E_MAIL VARCHAR (100) NOT NULL,
    TELEFONE VARCHAR (15) NOT NULL,
    CPF VARCHAR (14) NOT NULL,
	DATA_NASCIMENTO DATE NOT NULL,
    GENERO INT (1) NOT NULL,
    OPCAO_1 INT (1) DEFAULT 0,
    OPCAO_2 INT (1) DEFAULT 0
);

CREATE TABLE FORMS(
	ID_FORMS INT AUTO_INCREMENT PRIMARY KEY,
    USUARIO INT,
    PALESTRA INT,
    CONSTRAINT FK_UsuarioForms FOREIGN KEY (USUARIO) REFERENCES USUARIO (ID_USER),
    CONSTRAINT FK_PalestraForms FOREIGN KEY (PALESTRA) REFERENCES SALA (ID_SALA)
);

delimiter //	
CREATE TRIGGER TGR_VagaInsert AFTER INSERT
ON FORMS
FOR EACH ROW
BEGIN
	UPDATE SALA SET VAGAS = VAGAS - 1
    WHERE REFERENCIA = NEW.USUARIO;
END //

CREATE TRIGGER TGR_VagaDelete AFTER DELETE
ON FORMS
FOR EACH ROW
BEGIN
	UPDATE SALA SET VAGAS = VAGAS + 1
    WHERE REFERENCIA = OLD.USUARIO;
END //
delimiter ;

INSERT INTO SALA (ID_SALA, IMG, PALESTRA, PALESTRANTE, VAGAS) VALUES
	(312, '', 'Design 3D', 3, 15),
    (304, '', 'Banco de Dados', 1, 10),
    (201, '', 'Finanças', 5, 20),
    (120, '', 'Empreemdedorismo', 2, 25),
    (307, '', 'Linkedin', 6, 30),
    (305, '', 'Inteligencia Artificial', 10, 50),
    (246, '', 'Cortes de Cabelo', 9, 32),
    (202, '', 'Gerenciamento de Projeto', 7, 25),
    (100, '', 'Mercado de Trabalho', 4, 20),
    (304, '', 'Projeto HELP', 8, 100);

INSERT INTO PALESTRANTE (ID_SPEAKER, NOME, DESCRICAO, LINKEDIN, INSTAGRAM) VALUES
	(NULL, 'Vinicius Domunt', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Simone Castro', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Nathalia Arcuri', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Felipe Titto', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Ricardo Amorim', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Andrea Lorio', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Vivi Siqueira', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Ricardo Vargas', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'Marcelo Scharra', 'DESCRIÇÃO', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario'),
    (NULL, 'PROJETO HELP', 'Não te Julgo, Te Ajudo', 'https://www.linkedin.com/Usuario', 'https://www.instragram.com/Usuario');

INSERT INTO USUARIO (ID_USER, NOME, E_MAIL, TELEFONE, CPF, DATA_NASCIMENTO, GENERO, OPCAO_1, OPCAO_2) VALUES
	(),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    ();
    