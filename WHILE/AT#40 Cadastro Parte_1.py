#Programa que Armazena Dados em uma Lista e Posteriormente Imprime esses Dados.
#Um Programa de Cadastro.

import os
cont = 0
list_name = []
list_sobname = []
list_end = []
list_bairro = []
list_cid = []
list_estado = []
list_pais = []
list_fone = []
list_cpf = []
list_peso = []
list_altura = []
list_idade = []
list_numCartao = []
list_email = []
list_cep = []
list_nota1 = []
list_nota2 = []
list_nota3 = []
list_nota4 = []
list_media = []
list_serie = []
list_classe = []
list_sexo = []
list_cor = []

while True:
    
    cont +=1
    
    print("="*25)
    print("\"Bem Vindo ao Cadastro\"")
    print("="*25)
    inicio = int(input("I| Digite 1 para Cadastro ou 0 para Sair: \n>> "))
    print("="*25)

    
    if inicio == 1:
        name = input("I| Digite seu Nome: \n>> ")
        sob_name = input("I| Digite seu Sobrenome: \n>> ")   
        endereco = input("I| Digite seu Endereço: \n>> ")   
        bairro = input("I| Digite seu Bairro: \n>> ")    
        cid = input("I| Digite sua Cidade: \n>> ")    
        estado = input("I| Digite seu Estado: \n>> ")   
        pais = input("I| Digite seu País: \n>> ")   
        fone = int(input("I| Digite seu Telefone: \n>> "))   
        cpf = input("I| Digite seu CPF: \n>> ")   
        peso = float(input("I| Digite seu Peso: \n>> "))  
        altura = float(input("I| Digite sua Altura: \n>> "))   
        idade = int(input("I| Digite sua Idade: \n>> "))   
        num_cartao = int(input("I| Digite o Número de Cartão: \n>> "))   
        email = input("I| Digite seu Email: \n>> ")  
        cep = input("I| Digite seu CEP: \n>> ")  
        nota_1 = float(input("I| Digite sua 1º Nota: \n>> "))
        nota_2 = float(input("I| Digite sua 2º Nota: \n>> ")) 
        nota_3 = float(input("I| Digite sua 3º Nota: \n>> "))
        nota_4 = float(input("I| Digite sua 4º Nota: \n>> "))
        media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
        serie = input("I| Digite sua Série: \n>> ")
        classe = input("I| Digite sua Classe: \n>> ")
        sexo = input("I| Digite seu Sexo: \n>> ")
        cor = input("I| Digite sua Cor: \n>> ")
        
        
        #Listas para Cada Dados.
        
        list_name.append(name)
        list_sobname.append(sob_name)
        list_end.append(endereco)
        list_bairro.append(bairro)
        list_cid.append(cid)
        list_estado.append(estado)
        list_pais.append(pais)
        list_fone.append(fone)
        list_cpf.append(cpf)
        list_peso.append(peso)
        list_altura.append(altura)
        list_idade.append(idade)
        list_numCartao.append(num_cartao)
        list_email.append(email)
        list_cep.append(cep)
        list_nota1.append(nota_1)
        list_nota2.append(nota_2)
        list_nota3.append(nota_3)
        list_nota4.append(nota_4)
        list_media.append(media)
        list_serie.append(serie)
        list_classe.append(classe)
        list_sexo.append(sexo)
        list_cor.append(cor)
        list_matricula = cont
        
        
        print("+"+"="*35+"+")
        print("I|"+" "*11+"\"Matricula\""+" "*11+"|I")
        print("+"+"="*35+"+")
        print("I| Matricula",list_matricula)
        print("+"+"="*10+"+")
        print("I| Nomes:",list_name)
        print("I| Sobrenomes:",list_sobname)
        print("I| Endereços:",list_end)
        print("I| Bairros:",list_bairro)
        print("I| Cidades:",list_cid)
        print("I| Estados:",list_estado)
        print("I| Paises",list_pais)
        print("I| Telefones:",list_fone)
        print("I| CPF:",list_cpf)
        print("I| Pesos:",list_peso)
        print("I| Alturas:",list_altura)
        print("I| Idades:",list_idade)
        print("I| Número de Cartões:",list_numCartao)
        print("I| Emails:",list_email)
        print("I| CEP:",list_cep)
        print("I| Notas 1º:",list_nota1)
        print("I| Notas 2º:",list_nota2)
        print("I| Notas 3º:",list_nota3)
        print("I| Notas 4º:",list_nota4)
        print("I| Médias:",list_media)
        print("I| Séries:",list_serie)
        print("I| Classes:",list_classe)
        print("I| Sexos:",list_sexo)
        print("I| Cores:",list_cor)
        print("+"+"="*35+"+")
        os.system("pause")
        os.system("cls")
    
    else:
        break