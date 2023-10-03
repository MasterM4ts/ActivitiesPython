use Cadastro;

update Cidade set CIDADE = 'Abaixo de M' where CIDADE like 'A%' or CIDADE like 'B%'
or CIDADE like 'C%' or CIDADE like 'D%' or CIDADE like 'E%' or CIDADE like 'F%' or CIDADE like 'G%'
or CIDADE like 'H%' or CIDADE like 'I%' or CIDADE like 'J%' or CIDADE like 'K%' or CIDADE like 'L%' 
or CIDADE like 'M%';

update Cidade set CIDADE = 'Acima de M' where CIDADE like 'N%' or CIDADE like 'O%'
or CIDADE like 'P%' or CIDADE like 'Q%' or CIDADE like 'R%' or CIDADE like 'S%' or CIDADE like 'T%'
or CIDADE like 'U%' or CIDADE like 'V%' or CIDADE like 'W%' or CIDADE like 'X%' or CIDADE like 'Y%' 
or CIDADE like 'Z%';

select * from Cidade;

update Estado set ESTADO = 'Região Norte' where ESTADO = 'Acre' or ESTADO = 'Amapá' 
or ESTADO = 'Amazonas' or ESTADO = 'Pará' or ESTADO = 'Rondônia' or ESTADO = 'Roraima' 
or ESTADO = 'Tocantins';

update Estado set ESTADO = 'Região Nordeste' where ESTADO = 'Alagoas' or ESTADO = 'Bahia' 
or ESTADO = 'Ceará' or ESTADO = 'Maranhão' or ESTADO = 'Paraíba' or ESTADO = 'Piauí' 
or ESTADO = 'Rio Grande do Norte' or ESTADO = 'Sergipe' or ESTADO = 'Pernambuco';

update Estado set ESTADO = 'Região Centro-Oeste' where ESTADO = 'Distrito Federal' 
or ESTADO = 'Goiás' or ESTADO = 'Mato Grosso' or ESTADO = 'Mato Grosso do Sul';

update Estado set ESTADO = 'Região Sudeste' where ESTADO = 'Espirito Santo' or ESTADO = 'Minas Gerais' 
or ESTADO = 'Rio de Janeiro' or ESTADO = 'São Paulo';

update Estado set ESTADO = 'Região Sul' where ESTADO = 'Paraná' or ESTADO = 'Rio Grande do Sul' 
or ESTADO = 'Santa Catarina';

select * from Estado;

update Nacionalidade set NACIONALIDADE = 'Fora do Brasil' where NACIONALIDADE = 'Estrangeiro';

select * from Nacionalidade;