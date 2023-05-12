#######################################################################

#Substring.  //[] para Selecionar o Caracter na string.

 P  Y  T  H  O  N             s = "Ola Mundo!"
 0  1  2  3  4  5 (->)        print(s[4])  //M
-6 -5 -4 -3 -2 -1 (<-)        print(s[-9]) //l 
                              
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

#Forma de Escrita Diferente.  

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

#Método Capitalize()  //Transforma a Primeira letra da string em Maiúscula.

a = "matheus"
print(a.capitalize())
xMatheus

#######################################################################

#Método Upper()  //Transforma a string em Maiúscula. 

a = "Matheus"
print(a.upper())
xMATHEUS

a = "MATHEUS"
print(a.isupper())
xTrue

#######################################################################

#Método CaseFold()  //Transforma a string em Minusculo.

a = "MATHEUS"
print(a.casefold())
xmatheus

#######################################################################

#Método Lower()  //Transforma a string em Minusculo.

a = "MATHEUS"
print(a.lower())
xmatheus

a= "MATHEUS"
print(a.islower())
xFalse

#######################################################################

#Método Digit()  //Indentifica se é Digito e Informa.

a = "12345"
print(a.isdigit())
xTrue

a = "12345abc"
print(a.isdigit())
xFalse

#######################################################################

#Método Reaplese()  //Substitui a string da Váriavel. 

a = "Matheus Matos
print(a.reaplese("Matos","Nunes"))
xMatheus Nunes

#######################################################################

#Método Split()  //Substitui o parâmetro "- , *, / , + ,etc" por ",".

a = "Matheus-Matos-Nunes"
print(a.split("-"))
['Matheus','Matos','Nunes']

#######################################################################

#Função Find()  //Localiza onde começa a string ->.

a = "Matheus de Matos Matos"
print(a.find("Nunes"))
x17

#######################################################################

#Método Rfind()  //Localiza onde começa a string <-.

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

#Lista  //Lista string,folat,inteiro e outra lista.

list = ["Matheus",17,"Anos",1,12,2005]
print(list)
print(type(list))
x['Matheus',17,'Anos',1,12,2005]
<class 'list'>


#Utilização Função //LEN()//

list = ["Matheus",17,"Anos",1,12,2005]
print(len(list))
x6

#[2]Índice da lista,[0]Índice do Caracter Dentro da Lista.

list = ["Matheus",17,"Anos",1,12,2005]
print(list[2][0])
xA

#[2]Índice da lista,[0]Índice da Sublista.

list = ["Matheus",17,[56,57,"Fortnite"],"Anos",1,12,2005]
print(list[2][1])
x57

#[2]Índice da lista,[2]Índice da Sublista,[0]Índice do Caracter Dentro da Sublista.

list = ["Matheus",17,[56,57,"Fortnite"],"Anos",1,12,2005]
print(list[2][2][0])
xF

#######################################################################

#Função In,Not e Not in.

animais = ["gato","cachorro"]
print("gato" in animais)
xTrue

print("Arara" not in animais)
xTrue

a = [1,2,3,[56,57,58],4,5]
print(57 in a)
xFalse

#######################################################################

#Concatenação.

a = [1,2,3,4,5]
print(a + [6,7,8,9,10])
x[1,2,3,4,5,6,7,8,9,10]

#######################################################################

#Max,Min e Sum.

a = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(max(a))
x10
print(min(a))
x1
print(sum(a))
x45

#Operações Matematicas com Funções.

a = [1,2,3,4,5,6,7,8,9,10]
print(sum(a) "/,+,-,*" len(a))
x5.5

#######################################################################

#Substituição Lista.

frutas = ["Banana","Maçã","Cereja"]
frutas[0] = "Pera"
frutas[-1] = "Laranja"
print(frutas)
x['Pera','Maçã','Laranja']

#Substituir Índice Lista.

lista = ["Flor","Azul",[1,"Casa"]]
lista[2][1] = "Escola"
print(lista)
x['Flor', 'Azul', [1, 'Escola']]

#Exclusão Índice Lista.

lista = [1,2,3,4]
print(lista)
print(len(lista))

lista[1:3] = []
print(lista)
print(len(lista))

#Incerir Elemento em uma Lista.

a = ["a","b","c"]
a[1:1] = ["x ","y"]
print(a)
x['a','x','y','b','c']

#Incerir Sublista.

a = [4,2,8,6,5]
a[2] = [True]
print(a)
x[4,2[True],6,5]

#######################################################################

#Esclusão Índice Lista. //DEL//

list = ["um","dois","três"]
del list[1]
print(list)
x['dois','três']

list = ["a","b","c","d","e","f"]
del list[1:5]
print(list)
x['a','f']

#######################################################################

#Anexação Valor.  \\Append\\   //Adiciona ao Final da Lista.(Fila)

a = [81,82,83]
a.append(5)
print(a)
x[81,82,83,5]

#######################################################################

#Ordenaçao da Lista.  \\Sort\\  //Ordem Crecente.

a = [8,5,4,3]
a.sort()
x[3,4,5,8]
print(a)

#######################################################################

#Ordenaçao da Lista.  \\Reverse\\  //Ordem Decrecente.

a = [8,5,4,3]
a.sort(reverse=True)
print(a)
x[8,5,4,3]

#######################################################################

#Retorna a Posição Índicial do Elemento na Primeira Aparição. \\Index\\

a = [1,2,3,4,5,4,6]
print(a.index(4))
x3

#######################################################################

#Insere o Valor na Posição do Ídice Desejado.  \\Insert\\

a = [1,2,3,4]
a.insert(2,100)
print(a)
x[1,2,100,3,4]

#######################################################################

#Informa Quantidade de Aparições o Elemento.  \\Cont\\

a = [1,2,3,4,5,6,4]
print(a.cont(4))
x2

#######################################################################

#Remoção do Ultimo Elemento da Lista.  \\Pop\\

a = [1,2,3,4]
a.pop()
print(a)
x[1,2,3]

a = [1,2,3,4]
a.pop()
print(a)
x[2,3,4]

#######################################################################