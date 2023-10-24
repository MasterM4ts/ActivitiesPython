create database Titanic;

use Titanic;


create table Passageiros(
	Passenger int not null,
    Survived varchar (1) not null,
    Pclasse int not null,
    Name varchar (255) not null,
    Sex varchar (255) not null,
    Age varchar (255),
    SibSp varchar (1) not null,
    Parch varchar (1) not null,
    Ticket varchar (255) not null,
    Fare varchar (255) not null,
    Cabin varchar (255),
    Embarked varchar (1) not null
);

select count(Survived) from Passageiros where Survived = '1';
select count(Survived) from Passageiros where Age < 12 and Survived = '1';
select count(Survived) from Passageiros where Age < 12 and Survived = '0';
select count(Survived) from Passageiros where Sex = 'famale' and Survived = '1';
select count(Survived) from Passageiros where Sex = 'male' and Survived = '1';