create database Fabrica_108;
use Fabrica_108;

create table ADM(
id_adm int auto_increment not null,
cpf int (12) not null,
nome varchar (30) not null,
senha varchar (20) not null,
email varchar (50) not null,
primary key (id_adm)
);


create table Fabricas(
id_fabricas int auto_increment not null,
nome varchar (30) not null,
texto varchar (200) not null,
endimagem varchar (100) not null,
primary key (id_fabricas)
);


create table Vagas(
id_vagas int auto_increment not null,
representante varchar (30) not null,
nome varchar (30) not null,
cnpj int (10) not null,
email varchar (50) not null,
fone int (12) not null,
descricao_vaga varchar (100) not null,
primary key (id_vagas)
);


create table Banco_Talentos(
id_talentos int auto_increment not null,
nome varchar (30) not null,
fone int (12) not null,
rg int (12) not null,
cpf int (12) not null,
endereco varchar (50) not null,
linkedin varchar (100) not null,
primary key (id_talentos)
);


create table Edital(
id_edital int auto_increment not null,
nome varchar (30) not null,
dta_inicio datetime (10) not null,
dta_final datetime (10) not null,
endereco_arquivo varchar (30) not null,
primary key (id_edital)
);


create table Vagas_psg(
id_psg int auto_increment not null,
escolaridade varchar (30) not null,
email varchar (30) not null,
fone int (20) not null,
dta_nascimento varchar (12),
responsavel varchar (30) not null,
nome varchar (30) not null,
cpf int (20) not null,
id_edital integer,
constraint fk_VagasEdital foreign key (id_edital) references Edital (id_edital),
primary key (id_psg)
);


create table Projeto(
id_projeto int auto_increment not null,
cpf_titular int (20) not null,
email varchar (30) not null,
cnpj int (30) not null,
descricao varchar (100) not null,
id_edital integer,
constraint fl_ProjetoEdital foreign key (id_edital) references Edital (id_edital),
primary key (id_projeto)
);