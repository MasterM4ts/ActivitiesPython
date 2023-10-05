create database Epic_Games;
use Epic_Games;

create table Jogos (
	ID varchar (100) primary key not null,
    NOME varchar (200),
    JOGO_SLUG varchar (100),
    PRECO varchar (50),
    DATA_DE_LANCAMENTO varchar (50),
    PLATAFORMA varchar (50),
    DESCRICAO varchar (300),
    DESENVOLVEDOR varchar (70),
    EDITOR varchar (70),
    GENEROS varchar (100)
 );
 
create table Requisitos_Necessarios (
	ID int auto_increment primary key not null,
    SISTEMA_OPERACIONAL varchar (100),
    PROCESSADOR varchar (150),
    MEMORIA varchar (70),
    GRAFICOS varchar (200),
    ESPACO varchar (100),
    ID_JOGO varchar (100) not null,
    constraint FK_JOGO foreign key (ID_JOGO) references Jogos (ID)
);

