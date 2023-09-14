-- criar o BD ecommerce

create database ecommerce; 
use ecommerce;

---------------------------------------------

create table produtos(
    id_prod int(5) auto_increment not null,
    nome_prod varchar(100) not null,
    descricao text,
    modelo varchar(50) not null,
    id_categoria int(5),
    id_fabricante int(5),
    primary key (id_prod)
    );
    
    
    
create table clientes (
    id_cli int(5) auto_increment not null,
    nome varchar(100) not null,
    cpf varchar(30),
    telefone varchar(50),
    sexo enum('F','M'),
    cadastro datetime,
    primary key (id_cli)
    ); 


create table pedidos(
	num_pedido int(5) auto_increment not null,
	data datetime,
	status varchar(50),
	id_cli int(5),
	primary key (num_pedido),
	constraint fk_PedidosClientes foreign key (id_cli) references clientes(id_cli)
    );

    
create table pedido_item(
	idtem_pedido int(5) auto_increment not null,
	num_pedido int(5) not null,
    qtde int(5) not null,
    valor_unit decimal(10,2) not null,
    total decimal(10,2) not null,
    id_prod int(5),
	primary key (idtem_pedido),
    constraint fk_Pedidoitem_Pedidos foreign key (num_pedido) references pedidos(num_pedido),
    constraint fk_Pedido_itemProdutos foreign key  (id_prod) references produtos(id_prod)
    );

create table estoque_produtos(
	id_estoque int auto_increment not null,
	quantidade int(5) not null,
	quant_min int(5),
	id_prod int(5),
	primary key (id_estoque),
	constraint fk_EstoqueProdutos foreign key (id_prod) references produtos(id_prod)
	);
        
        
	insert into clientes values (null,'João', 02102202324,'6799999999','M',now());
    insert into clientes values (null,'Tadeu', 02102202366,'6799999999','M',now());
    insert into clientes values (null,'Francisco', 02102202399,'6799999999','M',now());
    insert into clientes values (null,'Maria', 02102202377,'6799999999','F',now());
    insert into clientes values (null,'Antonia',02102202388,'6799999999','F',now());
    insert into clientes values (null,'Matheus',06629249160,'67999317482','M',now());
    
    select * from clientes;
    
    insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);
    insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);
    insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);
    insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);
    insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);

    insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);
    insert into produtos values (null,'Processador AMD','4.2Ghz','Ryzen5',null,null);
    insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);
    insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null,null);
	
    
	select * from produtos;
    describe table estoque_produtos;
	

	insert into estoque_produtos values (null,80,10,1);
    insert into estoque_produtos values (null,44,5,9);
    insert into estoque_produtos values (null,55,5,8);
    insert into estoque_produtos values (null,36,5,7);
    insert into estoque_produtos values (null,49,5,6);
    insert into estoque_produtos values (null,100,5,1);
    insert into estoque_produtos values (null,100,5,2);
    insert into estoque_produtos values (null,100,5,3);
    insert into estoque_produtos values (null,100,5,4);
    insert into estoque_produtos values (null,100,5,5);
    