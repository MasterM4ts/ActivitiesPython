create database Mercado;
use Mercado;

create table Fornecedor(
cod_fornecedor varchar (5) not null,
nome varchar (100) not null,
cidade_sede varchar (100) not null,
grupo_cod_fornecedor varchar (100),
primary key (cod_fornecedor)
);

create table Material(
cod_material int auto_increment not null,
cod_fornecedor varchar (5),
nome varchar (100) not null,
descricao varchar (200) not null,
primary key (cod_material),
constraint fk_MaterialFornecedor foreign key (cod_fornecedor) references Fornecedor (cod_fornecedor)
);

insert into Fornecedor values ("ABC","ABC Materiais Eletricos","Vitoria",null);
insert into Material values (null, null,"Tomada eletrica 10A Nova", 'Tomada eletrica 10A padrão novo');

select * from Fornecedor;
select * from Material;