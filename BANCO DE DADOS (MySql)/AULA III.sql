create database Estrutura;	
use Estrutura;	


create table EX2_CLIENTE(
codcliente int auto_increment not null,
nome varchar (30) not null,
datanascimento varchar (10) not null,
cpf varchar (30) not null,
primary key (codcliente)
);		


create table EX2_PEDIDO(
codpedido int auto_increment not null,
datapedido varchar (10) not null,
nf varchar (30) not null,
valortotal float (20) not null,
codcliente  integer,
constraint fk_PedidoCliente foreign key (codcliente) references EX2_CLIENTE (codcliente),
primary key (codpedido)
);		


create table EX2_ITEMPEDIDO(
numeroitem int auto_increment not null,
valorunitario float (30) not null,
quantidade int (20) not null,
codpedido integer,
codproduto integer,
constraint fk_ItempedidoPedido foreign key (codpedido) references EX2_PEDIDO (codpedido),
constraint fk_ItempedidoProduto foreign key (codproduto) references EX2_PRODUTO (codproduto),
primary key (numeroitem)
);	


create table EX2_PRODUTO(
codproduto int auto_increment not null,
descricao varchar (100) not null,
quantidade int (20) not null,
primary key (codproduto)
);


create table EX2_LOG(
codlog int auto_increment not null,
data varchar (10) not null,
descricao varchar (100) not null,
primary key (codlog)
);


create table EX2_REQUISICAO_COMPRA(
codrequisicaocompra int auto_increment not null,
data varchar (10) not null,
quantidade int (10) not null,
codproduto integer,
constraint fk_RequisicaoProduto foreign key (codproduto) references EX2_PRODUTO (codproduto),
primary key (codrequisicaocompra)
);

INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Matheus","2005-12-01","066.292.491-60");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Guilherme","2009-09-12","876.392.451-80");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Cristiane","1986-11-22","731.782.221-78");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Clecio","1980-06-11","967.291.511-79");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Eva","1978-09-10","766.282.151-53");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Signario","1976-09-11","576.202.671-67");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"José","1984-06-05","746.192.795-11");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Eduardo","2008-10-17","022.143.791-77");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Wellinginton","1985-09-02","785.392.571-67");
INSERT INTO EX2_CLIENTE(codcliente,nome,datanascimento,cpf) VALUES (null ,"Arlene","1987-10-21","054.882.691-52");
select * from EX2_CLIENTE;


INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "Iphad Apple", 1);
INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "Smartphone Samsung Galaxy", 2);
INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "Cama Box", 3);
INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "Geladeira Electrolux", 2);
INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "Techado Gamer", 1);
INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "Mause Gamer", 1);
INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "Munitor de 144hz", 1);
INSERT INTO EX2_PRODUTO(codproduto,descricao,quantidade) VALUES (null , "TV 4K Samsung", 2);
select * from EX2_PRODUTO;


INSERT INTO EX2_PEDIDO(codpedido, datapedido, nf, valortotal, codcliente) VALUES (null, "2023-12-01", "Notebook - Lenovo", 2500, 1);
INSERT INTO EX2_PEDIDO(codpedido, datapedido, nf, valortotal, codcliente) VALUES (null, "2023-09-12", "Computador de Mesa Gamer", 5500, 2);
INSERT INTO EX2_PEDIDO(codpedido, datapedido, nf, valortotal, codcliente) VALUES (null, "2023-11-22", "Produtos de Cabeleireiro", 2000, 3);
INSERT INTO EX2_PEDIDO(codpedido, datapedido, nf, valortotal, codcliente) VALUES (null, "2023-06-11", "Placas de Marceneiro", 7000, 4);
INSERT INTO EX2_PEDIDO(codpedido, datapedido, nf, valortotal, codcliente) VALUES (null, "2023-09-11", "Materiais de Construção", 10000, 6);
select * from EX2_PEDIDO;


INSERT INTO EX2_ITEMPEDIDO(numeroitem, valorunitario, quantidade, codpedido, codproduto) VALUES (null, 2500, 1, 1, 1);
INSERT INTO EX2_ITEMPEDIDO(numeroitem, valorunitario, quantidade, codpedido, codproduto) VALUES (null, 500, 1, 2, 5);
INSERT INTO EX2_ITEMPEDIDO(numeroitem, valorunitario, quantidade, codpedido, codproduto) VALUES (null, 1500, 1, 2, 6);
INSERT INTO EX2_ITEMPEDIDO(numeroitem, valorunitario, quantidade, codpedido, codproduto) VALUES (null, 3500, 1, 2, 4);
INSERT INTO EX2_ITEMPEDIDO(numeroitem, valorunitario, quantidade, codpedido, codproduto) VALUES (null, 2500, 1, 3, 3);
select * from EX2_ITEMPEDIDO;