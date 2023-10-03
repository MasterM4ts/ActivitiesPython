create database Cadastro;
use Cadastro;
-- drop database Cadastro;
create table Estado(
	ID_ESTADO int auto_increment primary key not null,
    ESTADO varchar (100) not null
);

create table Cidade(
	ID_CIDADE int auto_increment primary key not null,
    CIDADE varchar (100) not null
);

create table Sexo(
	ID_SEXO int auto_increment primary key not null,
    SEXO varchar (15) not null
);

create table Nacionalidade(
	ID_NACIONALIDADE int auto_increment primary key not null,
    NACIONALIDADE varchar (100) not null
);

create table Raca(
	ID_RACA int auto_increment primary key not null,
    RACA varchar (100) not null
);

create table Escolaridade(
	ID_ESCOLARIDADE int auto_increment primary key not null,
    ESCOLARIDADE varchar (100) not null
);

create table Cadastro_de_Cliente(
	CPF varchar (15) not null,
    NOME varchar (70) not null,
    RG varchar (10) not null,
    ID_ESTADO int,
    ID_CIDADE int,
    ID_SEXO int,
    ID_NACIONALIDADE int,
    FONE varchar (15) not null,
    ID_RACA int,
    ID_ESCOLARIDADE int,
    constraint FK_ESTADO foreign key (ID_ESTADO) references Estado (ID_ESTADO),
    constraint FK_CIDADE foreign key (ID_CIDADE) references Cidade (ID_CIDADE),
    constraint FK_SEXO foreign key (ID_SEXO) references Sexo (ID_SEXO),
    constraint FK_NACIONALIDADE foreign key (ID_NACIONALIDADE) references Nacionalidade (ID_NACIONALIDADE),
    constraint FK_RACA foreign key (ID_RACA) references Raca (ID_RACA),
    constraint FK_ESCOLARIDADE foreign key (ID_ESCOLARIDADE) references Escolaridade (ID_ESCOLARIDADE)
);

insert into Estado values 
	(NULL, 'Acre'),
	(NULL, 'Alagoas'),
	(NULL, 'Amapá'),
	(NULL, 'Amazonas'),
	(NULL, 'Bahia'),
	(NULL, 'Ceará'),
	(NULL, 'Distrito Federal'),
	(NULL, 'Espírito Santo'),
	(NULL, 'Goiás'),
	(NULL, 'Maranhão'),
	(NULL, 'Mato Grosso'),
	(NULL, 'Mato Grosso do Sul'),
	(NULL, 'Minas Gerais'),
	(NULL, 'Pará'),
	(NULL, 'Paraíba'),
	(NULL, 'Paraná'),
	(NULL, 'Pernambuco'),
	(NULL, 'Piauí'),
	(NULL, 'Rio de Janeiro'),
	(NULL, 'Rio Grande do Norte'),
	(NULL, 'Rio Grande do Sul'),
	(NULL, 'Rondônia'),
	(NULL, 'Roraima'),
	(NULL, 'Santa Catarina'),
	(NULL, 'São Paulo'),
	(NULL, 'Sergipe'),
	(NULL, 'Tocantins');

insert into Cidade values 
	(NULL, 'Rio Branco'),
	(NULL, 'Cruzeiro do Sul'),
	(NULL, 'Sena Madureira'),
	(NULL, 'Tarauacá'),
	(NULL, 'Feijo'),
	(NULL, 'Batalha'),
	(NULL, 'Belo Monte'),
    (NULL, 'Coité do Nóia'),
    (NULL, 'Craíbas'),
    (NULL, 'Feira Grande'),
	(NULL, 'Macapá'),
	(NULL, 'Santana'),
    (NULL, 'Porto Grande'),
    (NULL, 'Mazagão'),
    (NULL, 'Laranjal do Jari'),
	(NULL, 'Manaus'),
	(NULL, 'Parintins'),
    (NULL, 'Itacoatiara'),
    (NULL, 'Manacapuru'),
    (NULL, 'Tefé'),
	(NULL, 'Salvador'),
	(NULL, 'Feira de Santana'),
    (NULL, 'Vitória da Conquista'),
    (NULL, 'Camaçari'),
    (NULL, 'LLhéus'),
	(NULL, 'Senador Sá'),
	(NULL, 'Altaneira'),
    (NULL, 'Jaguaribe'),
    (NULL, 'Pacujá'),
    (NULL, 'Fortaleza'),
	(NULL, 'Brasília'),
	(NULL, 'Samambaia'),
    (NULL, 'Guará'),
    (NULL, 'Ceilândia'),
    (NULL, 'Taguatinga'),
	(NULL, 'Serra'),
	(NULL, 'Vila Velha'),
    (NULL, 'Cariacica'),
    (NULL, 'Vitória'),
    (NULL, 'Colatina'),
	(NULL, 'Aparecida de Goiânia'),
	(NULL, 'Anápolis'),
    (NULL, 'Rio Verde'),
    (NULL, 'Águas Lindas de Goiás'),
    (NULL, 'Goiânia'),
	(NULL, 'São Luís'),
	(NULL, 'Imperatriz'),
    (NULL, 'São José de Ribamar'),
    (NULL, 'Timon'),
    (NULL, 'Caxias'),
	(NULL, 'Cuiabá'),
	(NULL, 'Várzea Grande'),
    (NULL, 'Rondonópolis'),
    (NULL, 'Sinop'),
    (NULL, 'Sorriso'),
	(NULL, 'Campo Grande'),
	(NULL, 'Dourados'),
    (NULL, 'Corumbá'),
    (NULL, 'Ponta Porã'),
    (NULL, 'Três Lagoas'),
	(NULL, 'Belo Horizonte'),
	(NULL, 'Uberlândia'),
    (NULL, 'Contagem'),
    (NULL, 'Betim'),
    (NULL, 'Riberão das Neves'),
	(NULL, 'Belém'),
	(NULL, 'Santarém'),
    (NULL, 'Marabá'),
    (NULL, 'Ananindeua'),
    (NULL, 'Itaituba'),
	(NULL, 'João Pessoa'),
	(NULL, 'Campinas Grande'),
    (NULL, 'Santa Rita'),
    (NULL, 'Patos'),
    (NULL, 'São Bento'),
	(NULL, 'Curitiba'),
	(NULL, 'Londrina'),
    (NULL, 'Maringá'),
    (NULL, 'Ponta Grossa'),
    (NULL, 'Cascavel'),
	(NULL, 'Recife'),
	(NULL, 'Jaboatão'),
    (NULL, 'Guararapes'),
    (NULL, 'Paulista'),
    (NULL, 'Olinda'),
	(NULL, 'Teresina'),
	(NULL, 'Parnaíba'),
    (NULL, 'Picos'),
    (NULL, 'Pirpiri'),
    (NULL, 'José de Freitas'),
	(NULL, 'Rio de Janeiro'),
	(NULL, 'São Gonçalo'),
    (NULL, 'Nova Iguaçu'),
    (NULL, 'Duque de Caxias'),
    (NULL, 'Niterói'),
	(NULL, 'Natal'),
	(NULL, 'Mossoró'),
    (NULL, 'Parnamirim'),
    (NULL, 'Macaíba'),
    (NULL, 'Caicó'),
	(NULL, 'Porto Alegre'),
	(NULL, 'Caxias do Sul'),
    (NULL, 'Canoas'),
    (NULL, 'Santa Cruz do Sul'),
    (NULL, 'Rio Grande'),
	(NULL, 'Porto Velho'),
	(NULL, 'Ji-Paraná'),
    (NULL, 'Ariquemes'),
    (NULL, 'Vilhena'),
    (NULL, 'Cacoal'),
	(NULL, 'Boa Vista'),
	(NULL, 'Rorainópolis'),
    (NULL, 'Alto Alegre'),
    (NULL, 'Caracaraí'),
    (NULL, 'Amajari'),
	(NULL, 'Frorianópolis'),
	(NULL, 'São José'),
    (NULL, 'Joinville'),
    (NULL, 'Blumenau'),
    (NULL, 'Bombinhas'),
	(NULL, 'Aquidabã'),
	(NULL, 'Aracaju'),
    (NULL, 'Carira'),
    (NULL, 'Riachão do Dantas'),
    (NULL, 'Campo do Brito'),
	(NULL, 'Palmas'),
	(NULL, 'Araguaína'),
    (NULL, 'Gurupi'),
    (NULL, 'Porto Nacional'),
    (NULL, 'Guaraí'),
	(NULL, 'São Paulo'),
	(NULL, 'Guarulhos'),
    (NULL, 'Campinas'),
    (NULL, 'Santo André'),
    (NULL, 'Riberão Preto');
    
insert into Sexo values 
	(NULL, 'Masculino'),
    (NULL, 'Feminino'),
    (NULL, 'Outros');

insert into Nacionalidade values
		(NULL, 'Brasileiro'),
        (NULL, 'Estrangeiro');
        
insert into Raca values
	(NULL, 'Brancos'),
	(NULL, 'Pardos'),
    (NULL, 'Negros'),
	(NULL, 'Indígenas'),
	(NULL, 'Amarelos');

insert into Escolaridade values
	(NULL, 'Educação Infantil'),
    (NULL, 'Fundamental'),
    (NULL, 'Ensino Médio'),
    (NULL, 'Ensino Superior'),
    (NULL, 'Pós-graduação'),
    (NULL, 'Mestrado'),
    (NULL, 'Doutorado'),
	(NULL, 'Escola');
    
insert into Cadastro_de_Cliente values 
	('066.467.454-82', 'Matheus', '2.475.684', 15, 2, 1, 1, '(67) 99931-7482', 1, 2),
    ('123.456.789-01', 'Maria Silva', '3.456.789', 20, 5, 2, 1, '(11) 1234-5678', 4, 4),
	('987.654.321-09', 'João Pereira','7.654.321', 22, 10, 1, 2, '(21) 9876-5432', 5, 2),
	('456.789.123-45', 'Ana Santos', '6.789.123', 17, 15, 2, 1, '(31) 4567-8901', 1, 2),
	('789.123.456-78', 'Pedro Oliveira', '9.123.456', 6, 25, 1, 1, '(41) 7890-1234', 2, 2),
	('234.567.890-12', 'Laura Martins', '4.567.890', 14, 2, 2, 2, '(51) 2345-6789', 2, 2),
	('345.678.901-23', 'André Almeida', '5.678.901', 25, 20, 1, 1, '(61) 3456-7890', 5, 2),
	('567.890.123-45', 'Sofia Costa', '7.890.123', 14, 12, 2, 1, '(71) 5678-9012', 4, 2),
	('678.901.234-56', 'Lucas Rodrigues', '8.901.234', 12, 8, 1, 1, '(81) 6789-0123', 4, 2),
	('789.012.345-67', 'Isabela Fernandes', '9.012.345', 1, 6, 2, 2, '(91) 7890-1234', 3, 2),
	('890.123.456-78', 'Diego Santos', '0.123.456', 7, 7, 1, 1, '(101) 8901-2345', 3, 2),
	('901.234.567-89', 'Gabriela Lima', '1.234.567', 11, 9, 2, 2, '(111) 9012-3456', 1, 2),
	('123.890.123-90', 'Mateus Ferreira', '3.890.123', 18, 17, 1, 1, '(121) 1234-5678', 3, 2),
	('234.567.890-10', 'Carla Oliveira', '4.567.890', 21, 10, 2, 2, '(131) 2345-6789', 1, 2),
	('345.890.123-21', 'Andréia Santos', '5.890.123', 23, 7, 2, 2, '(141) 3456-7890', 4, 2),
	('456.123.890-32', 'Rafaela Almeida', '6.123.890', 5, 14, 2, 1, '(151) 4567-8901', 1, 2),
	('567.234.890-43', 'Gustavo Silva', '7.234.890', 10, 22, 1, 2, '(161) 5678-9012', 3, 2),
	('678.345.890-54', 'Carolina Rodrigues', '8.345.890', 2, 21, 2, 1, '(171) 6789-0123', 1, 2),
	('789.456.123-65', 'Thiago Costa', '9.456.123', 1, 19, 1, 1, '(181) 7890-1234', 5, 2),
	('890.567.234-76', 'Juliana Fernandes', '0.567.234', 16, 20, 2, 1, '(191) 8901-2345', 2, 2),
	('901.678.345-87', 'Eduardo Lima', '1.678.345', 8, 23, 1, 2, '(201) 9012-3456', 1, 2);
    

select CC.NOME, C.CIDADE from Cadastro_de_Cliente as CC join Cidade as C on CC.ID_CIDADE = C.ID_CIDADE;
select CC.NOME, E.ESTADO from Cadastro_de_Cliente as CC join Estado as E on CC.ID_ESTADO = E.ID_ESTADO;
select CC.NOME, CC.CPF, R.RACA from Cadastro_de_Cliente as CC join Raca as R on CC.ID_RACA = R.ID_RACA;
select CC.NOME, N.NACIONALIDADE from Cadastro_de_Cliente as CC join Nacionalidade as N on CC.ID_NACIONALIDADE = N.ID_NACIONALIDADE;
select CC.NOME, ES.ESCOLARIDADE from Cadastro_de_Cliente as CC join Escolaridade as ES on CC.ID_ESCOLARIDADE = ES.ID_ESCOLARIDADE;

select CC.NOME, C.CIDADE, E.ESTADO from Cadastro_de_Cliente as CC join Cidade as C on CC.ID_CIDADE = C.ID_CIDADE 
join Estado as E on CC.ID_ESTADO = E.ID_ESTADO;

select CC.NOME, C.CIDADE, E.ESTADO, CC.FONE, CC.RG, S.SEXO, N.NACIONALIDADE, R.RACA, ES.ESCOLARIDADE from Cadastro_de_Cliente as CC 
join Cidade as C on CC.ID_CIDADE = C.ID_CIDADE 
join Estado as E on CC.ID_ESTADO = E.ID_ESTADO 
join Sexo as S on CC.ID_SEXO = S.ID_SEXO 
join Nacionalidade as N on CC.ID_NACIONALIDADE = N.ID_NACIONALIDADE 
join Raca as R on CC.ID_RACA = R.ID_RACA 
join Escolaridade as ES on CC.ID_ESCOLARIDADE = ES.ID_ESCOLARIDADE;