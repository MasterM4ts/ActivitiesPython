create database Produtos;
use Produtos;

create table PRODUTOS(
	REFERENCIA varchar (3) primary key,
    DESCRICAO varchar (50) unique,
    ESTOQUE int not null default 0
);

insert into PRODUTOS values
	('001', 'Feijão', 10);
    
insert into PRODUTOS values
    ('002', 'Arroz', 5);
    
insert into PRODUTOS values
    ('003', 'Farinha', 15);
    
create table ITENVENDA(
	VENDA int,
    PRODUTO varchar (3),
    QUANTIDADE int
);

delimiter $
create trigger Tgr_itenVenda_insert after insert
on ITENVENDA
for each row
begin
	update PRODUTOS set ESTOQUE = ESTOQUE - new.QUANTIDADE
    where REFERENCIA = new.PRODUTO;
end$

create trigger Trg_itenVenda_Delete after delete
on ITENVENDA
for each row
begin
	update PRODUTOS set ESTOQUE = ESTOQUE + old.QUANTIDADE
    where REFERENCIA = old.PRODUTO;
end$
delimiter ;

select * from ITENVENDA;
select * from PRODUTOS;

insert into ITENVENDA values
    (1, '001', 3);

insert into ITENVENDA values
    (1, '002', 1);

insert into ITENVENDA values
    (1, '003', 5);
    
delete from ITENVENDA where PRODUTO = '001';