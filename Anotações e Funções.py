#######################################################################

#Substring.  //[] para Selecionar o Caracter na string.

 P  Y  T  H  O  N             s = "Ola Mundo!"
 0  1  2  3  4  5 (->)        print(s[4])  //M
-6 -5 -4 -3 -2 -1 (<-)        print(s[-9]) //l 
                              
#######################################################################

#Forma de Escrever Diferente.  

nome = int(input("Digite um Valor:"))
x = "Matheus"
y = 2.50
print(" O Valor foi %d no nome de %s e %.2f de troco. "%(nome,x,y))

nome = (input("Nome= "))
sal = float(input("Salario= "))
print("O funcionário %s recebeu %.3f "%(nome,sal))

#String %s
#Inteiro %d
#Boleano %b
#Float %f

#######################################################################

#Operador de Concatenação.  //Junção de duas Strings;-Somente Strings.

x = "Matheus"
y = "Matos Nunes"
print("Prezado "+x+" "+y+"."+" Olá!")

#######################################################################

#Operador de Replicação.  //Repete Varias Vezes uma string.

print(10*"Matheus\n")
print("+"+10*"-"+"+")
print(("|"+" "*10+"|\n")*5,end="")
print("+"+10*"-"+"+")

#######################################################################

#Função Len()  //Informa quantos Caracteres tem a Variavel (a).

a = "Matheus Matos Nunes"
print(len(a))
x19

#######################################################################

#Função Capitalize()  //Transforma a Primeira letra da string em Maiúscula.

a = "matheus"
print(a.capitalize())
xMatheus

#######################################################################

#Função Upper()  //Transforma a string em Maiúscula. 

a = "Matheus"
print(a.upper())
xMATHEUS

a = "MATHEUS"
print(a.isupper())
xTrue

#######################################################################

#Função CaseFold()  //Transforma a string em Minusculo.

a = "MATHEUS"
print(a.casefold())
xmatheus

#######################################################################

#Função Lower()  //Transforma a string em Minusculo.

a = "MATHEUS"
print(a.lower())
xmatheus

a= "MATHEUS"
print(a.islower())
xFalse

#######################################################################

#Função Digit()  //Indentifica se é Digito e Informa.

a = "12345"
print(a.isdigit())
xTrue

a = "12345abc"
print(a.isdigit())
xFalse

#######################################################################

#Função Reaplese()  //Substitui a string da Váriavel. 

a = "Matheus Matos
print(a.reaplese("Matos","Nunes"))
xMatheus Nunes

#######################################################################

#Função Split()  //Substitui o parâmetro "- , *, / , + ,etc" por ",".

a = "Matheus-Matos-Nunes"
print(a.split("-"))
['Matheus','Matos','Nunes']

#######################################################################

#Função Find()  //Localiza onde começa a string ->.

a = "Matheus de Matos Matos"
print(a.find("Nunes"))
x17

#######################################################################

#Função Rfind()  //Localiza onde começa a string <-.

a = "Matheus de Matos Matos"
print(a.rfind("Matos"))
x5

#######################################################################

#Função In()  //Informa se tem uma string Dentro da Váriavel.

a = "Matheus de Matos Nunes"
print("Matos"in a)
xTrue

#######################################################################

#Função Count()  //Informa a Quantidade de Caracteres tem dentro da string.
 
a = "Matheus de Matos Nunes"
print(a.count("s"))
x3

#######################################################################

#Função Slices()  //Informa os Caracteres Solicitados.

s = "Olá, Mundo!"
print(s[1:3])
xlá

s = "Olá, Mundo"
print(s[:3])
xOlá

s = "Olá, Mundo"
print(s[5:])
xMundo!

s = "Olá Mundo"
print(s[:])
xOlá, Mundo!

#######################################################################
