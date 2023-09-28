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
    
-- insert into Cadastro_de_Cliente values