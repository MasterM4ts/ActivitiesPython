-- Criação de um Banco de Dados --
create database Bike_Store;		
use Bike_Store;


-- Criação de Tabelas dentro do Banco de Dados --
-- Cada Tabela Contendo Atributos --
create table Acct_Typ_Cd_LU_Tab(
Acct_Code int auto_increment not null,
Accont_Type varchar (20) not null,
primary key (Acct_Code)
);


create table Customer(
Customer_ID int auto_increment not null,
Customer_Lname varchar (20) not null,
Customer_Fname varchar (20) not null,
Cust_street varchar (30) not null,
Cust_city varchar (50) not null,
St_code int (20) not null,
Cust_zip varchar (10) not null,
Cust_phone int (15) not null,
Fax_phone int (20) not null,
Acct_Code int (50) not null,
primary key (Customer_ID)
);


create table Customer_Account(
Customer_ID int auto_increment not null,
Last_purch_dte varchar (50) not null,
Last_pymt_dte varchar (50) not null,
Last_acct_trans_dte varchar (50) not null,
Trans_code int (50) not null,
Acct_balance float (50) not null,
primary key (Customer_ID)
);


create table Transaction_code(
Trans_code int auto_increment not null,
Transaction_description varchar (50) not null,
primary key (Trans_code)
);


create table Customer_Acct_Hist1(
Customer_ID int auto_increment not null,
Trans_dte varchar (20) not null,
Trans_code int (20) not null,
Old_acct_balance float (50) not null,
New_acct_balance float (50) not null,
primary key (Customer_ID)
);


create table Purchase_Order(
Seg_ID int auto_increment not null,
Purch_dte varchar (30) not null,
Custumer_ID int (30) not null,
Bar_code int (30) not null,
Serial_num int (35) not null,
Model_ID int (30) not null,
Quantity int (30) not null,
Price float (30) not null,
primary key (Seg_ID)
);


create table Parts_Inventory(
Bar_code int auto_increment not null,
Part_name varchar (30) not null,
Supplier_ID int (20) not null,
Prt_description varchar (30) not null,
Prt_cost float (30) not null,
Prt_price float (30) not null,
Quantity int (30) not null,
primary key (Bar_code)
);


create table Bike_Description(
Model_ID int auto_increment not null,
Model_name varchar (30) not null,
Inv_price float (30) not null,
Sale_price float (30) not null,
Description varchar (30) not null,
primary key (Model_ID)
);


create table Supplier(
Supplier_ID int auto_increment not null,
Supplier_name varchar (30) not null,
Sup_street varchar (30) not null,
Sup_city varchar (30) not null,
St_code int (20) not null,
Sup_zip int (10) not null,
Sup_phone int (20) not null,
Sup_fax varchar (30) not null,
primary key (Supplier_ID)
);


create table Bike_Inventory(
Seg_ID int auto_increment not null,
Serial_Number int (30) not null,
Supplier_ID int (30) not null,
Inventory_dte varchar (30) not null,
Model_ID int (30) not null,
primary key (Seg_ID)
);


create table State_Ikup(
St_code int auto_increment not null,
State_name varchar (30) not null,
primary key (St_code)
);