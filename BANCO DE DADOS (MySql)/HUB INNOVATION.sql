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
    INSTAGRAM VARCHAR (255)
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
    SALA INT,
    CONSTRAINT FK_UsuarioForms FOREIGN KEY (USUARIO) REFERENCES USUARIO (ID_USER),
    CONSTRAINT FK_PalestraForms FOREIGN KEY (SALA) REFERENCES SALA (ID_SALA)
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
	(312, 'C:/User/Projeto/Imagens/img.png', 'Design 3D', 3, 15),
    (304, 'C:/User/Projeto/Imagens/img.png', 'Banco de Dados', 1, 10),
    (201, 'C:/User/Projeto/Imagens/img.png', 'Finanças', 5, 20),
    (120, 'C:/User/Projeto/Imagens/img.png', 'Empreemdedorismo', 2, 25),
    (307, 'C:/User/Projeto/Imagens/img.png', 'Linkedin', 6, 30),
    (305, 'C:/User/Projeto/Imagens/img.png', 'Inteligencia Artificial', 10, 50),
    (246, 'C:/User/Projeto/Imagens/img.png', 'Cortes de Cabelo', 9, 32),
    (202, 'C:/User/Projeto/Imagens/img.png', 'Gerenciamento de Projeto', 7, 25),
    (100, 'C:/User/Projeto/Imagens/img.png', 'Mercado de Trabalho', 4, 20),
    (309, 'C:/User/Projeto/Imagens/img.png', 'Projeto HELP', 8, 100);

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
	(NULL, 'Matheus', 'masterm4ts@gmail.com', '(67) 99931-7482', '066.292.491-60', '2005-12-01', 1, 1, 0),
    (NULL, 'Jesus', 'luzdomundo@gmail.com', '(67) 57777-9999', '777.797.999-40', '1000-10-10', 1, 1, 1),
    (NULL, 'Abraão', 'paidafe@gmail.com', '(67) 99632-1278', '045.352.690-70', '0005-06-26', 1, 1, 1),
    (NULL, 'Isaque', 'filhodapromesa@gmail.com', '(67) 95645-7812', '457.821.581-65', '0100-07-10', 1, 1, 0),
    (NULL, 'Jacó', 'lutoucomdeus@gmail.com', '(67) 94862-9137', '431.292.682-45', '0200-11-23', 1, 1, 1),
    (NULL, 'José', 'egito@gmail.com', '(67) 96819-2468', '794.468.591-79', '0300-03-22', 1, 1, 0),
    (NULL, 'Moisés', 'marvermelho@gmail.com', '(67) 92864-4682', '004.251.679-50', '0900-05-20', 1, 1, 0),
    (NULL, 'Josué', 'solelua@gmail.com', '(67) 99319-1793', '067.353.627-10', '0950-09-11', 1, 1, 0),
    (NULL, 'Davi', 'golias@gmail.com', '(67) 91643-2389', '791.222.451-30', '1200-04-16', 1, 1, 1),
    (NULL, 'Salomão', 'sabedoria@gmail.com', '(67) 92895-4591', '667.256.799-22', '1300-06-20', 1, 1, 1);

INSERT INTO FORMS (ID_FORMS, USUARIO, SALA) VALUES
	(NULL, 11, 309),
    (NULL, 12, 100),
    (NULL, 13, 201),
    (NULL, 14, 202),
    (NULL, 15, 246),
    (NULL, 16, 304),
    (NULL, 17, 305),
    (NULL, 18, 307),
    (NULL, 19, 309),
    (NULL, 20, 312);