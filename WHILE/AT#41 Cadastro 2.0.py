#Programa que Armazena Dados em uma Lista e Posteriormente Imprime esses Dados ou Consultar os Cadastros Realizados.
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
list_matricula = []

while True:
    
    cont +=1
    
    print("="*27)
    print(" "*2+"\"Bem Vindo ao Cadastro\"")
    print("="*27)
    inicio = int(input("I| Digite a Opção Desejada: \n1 >> Cadastro \n2 >> Consulta \n0 >> Sair: \n>> "))
    print("="*27)
    
    #Cadastro de Maticulas.
    
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
        list_matricula.append(cont)
        
        #Inpressão de Dados
        
        print("+"+"="*35+"+")
        print("I|"+" "*6+"\"Matricula Concluida\""+" "*6+"|I")
        print("+"+"="*35+"+")
        print("I| Matricula >>%d<<"%cont)
        print("+"+"="*10+"+")
        print("I| Nomes: %s"%name)
        print("I| Sobrenomes: %s"%sob_name)
        print("I| Endereços: %s"%endereco)
        print("I| Bairros: %s"%bairro)
        print("I| Cidades: %s"%cid)
        print("I| Estados: %s"%estado)
        print("I| Paises: %s"%pais)
        print("I| Telefones: %d"%fone)
        print("I| CPF: %s"%cpf)
        print("I| Pesos: %.2f"%peso)
        print("I| Alturas: %.2f"%altura)
        print("I| Idades: %d"%idade)
        print("I| Número de Cartões: %d"%num_cartao)
        print("I| Emails: %s"%email)
        print("I| CEP: %s"%cep)
        print("I| Notas 1º: %.2f"%nota_1)
        print("I| Notas 2º: %.2f"%nota_2)
        print("I| Notas 3º: %.2f"%nota_3)
        print("I| Notas 4º: %.2f"%nota_4)
        print("I| Médias: %.2f"%media)
        print("I| Séries: %s"%serie)
        print("I| Classes:%s"%classe)
        print("I| Sexos: %s"%sexo)
        print("I| Cores: %s"%cor)
        print("+"+"="*35+"+")
        
        os.system("pause")
        os.system("cls")


    #Consulta de Matriculas Realizadas.
    
    elif inicio == 2:
        busca = int(input("I| Digite a Matricula: \n>> "))
        print("+"+"="*10+"+")
        print("I| Matricula %s"%list_matricula[busca-1])
        print("+"+"="*10+"+")
        print("I| Nomes: %s"%list_name[busca-1])
        print("I| Sobrenomes: %s"%list_sobname[busca-1])
        print("I| Endereços: %s"%list_end[busca-1])
        print("I| Bairros: %s"%list_bairro[busca-1])
        print("I| Cidades: %s"%list_cid[busca-1])
        print("I| Estados: %s"%list_estado[busca-1])
        print("I| Paises: %s"%list_pais[busca-1])
        print("I| Telefones: %s"%list_fone[busca-1])
        print("I| CPF: %s"%list_cpf[busca-1])
        print("I| Pesos: %s"%list_peso[busca-1])
        print("I| Alturas: %s"%list_altura[busca-1])
        print("I| Idades: %s"%list_idade[busca-1])
        print("I| Número de Cartões: %s"%list_numCartao[busca-1])
        print("I| Emails: %s"%list_email[busca-1])
        print("I| CEP: %s"%list_cep[busca-1])
        print("I| Notas 1º: %s"%list_nota1[busca-1])
        print("I| Notas 2º: %s"%list_nota2[busca-1])
        print("I| Notas 3º: %s"%list_nota3[busca-1])
        print("I| Notas 4º: %s"%list_nota4[busca-1])
        print("I| Médias: %s"%list_media[busca-1])
        print("I| Séries: %s"%list_serie[busca-1])
        print("I| Classes: %s"%list_classe[busca-1])
        print("I| Sexos: %s"%list_sexo[busca-1])
        print("I| Cores: %s"%list_cor[busca-1])
        print("+"+"="*35+"+")
        os.system("pause")
        os.system("cls")
    
    else:
        break