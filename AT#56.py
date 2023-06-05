#Programa Aero Porto.
#Efetua Cadastro de Cliente,Passagem,Avião e Tripulação.
#Imprime um Registro Contendo Todas as Informações Digitadas pelo Usuário. 

import os
inicio = 1
cadastro_cliente = []
cadastro_passagem = []
cadastro_aviao = []
cadastro_tripulacao = []

while inicio != 0:
    try:
        inicio = int(input("I| Digite a Opção:\n1 >> Cadastro Cliente\n2 >> Cadastro Passagem\n3 >> Cadastro Avião\n4 >> Cadastro Tripulação\n>>"))
        os.system("pause")
        os.system("cls")
    except ValueError:
        print("-"*20)
        print("I| \"Opção Invalida\"\n\"Tente Novamente\"")
        print("-"*20)
        os.system("pause")
        os.system("cls")
    except:
        print("-"*20)
        print("\"Erro Desconhecido\"")
        print("-"*20)
        os.system("pause")
        os.system("cls")
    
    if inicio == 1:
        print("+"+"="*37+"+")
        print("I| Bem Vindo ao Cadastro de Clientes I|")
        print("+"+"="*37+"+")
        nome = input("I| Digite seu Nome:\n>> ")
        sob_nome = input("I| Digite seu Sobrenome:\n>>")
        rg = input("I| Digite seu RG:\n>> ")
        cpf = input("I| Digite seu CPF:\n>> ")
        endereco = input("I| Informe seu Endereço:\n>> ")
        
        while True:
            try:
                fone = int(input("I| Qual o seu Telefone:\n>> "))
            except ValueError:
                print("-"*33)
                print("I| Digite Somente Número Inteiro.")
                print("-"*33)
                os.system("pause")
                os.system("cls")
            else:
                break
        
        while True:
            try:
                idade = int(input("I| Qual a sua Idade:\n>> "))
            except ValueError:
                print("-"*33)
                print("I| Digite Somente Número Inteiro.")
                print("-"*33)
                os.system("pause")
                os.system("cls")
            else:
                break

        cadastro_cliente.append([nome,sob_nome,rg,cpf,endereco,fone,idade])
        
        print("-"*35)    
        print("I| Cadastro de Cliente Concluido |I")
        print("-"*35)  
        print("I| Nome: %s"%nome)
        print("I| Sobrenome: %s"%sob_nome)
        print("I| RG: %s"%rg)
        print("I| CPF: %s"%cpf)
        print("I| Endereço: %s"%endereco)
        print("I| Telefone: %d"%fone)
        print("I| Idade: %d"%idade)
        print("-"*24)
        os.system("pause")
        os.system("cls")  

    elif inicio == 2:
        print("+"+"="*39+"+")
        print("I| Bem Vindo ao Cadastro de Passagem I|")
        print("+"+"="*39+"+")
        destino = input("I| Qual o Destino de Viagem:\n>> ")
        origem = input("I| Qual a Origem da Viagem:\n>> ")
        
        while True:
            try:
                duracao = int(input("I| Qual a Duração de Dias da Viagem:\n>> "))
            except ValueError:
                print("-"*33)
                print("I| Digite Somente Número Inteiro.")
                print("-"*33)
                os.system("pause")
                os.system("cls")
            else:
                break

        
        while True:
            try:
                valor_passagem = float(input("I| Qual o Valor da Passagem:\n>> "))
            except ValueError:
                print("-"*40)
                print("I| Digite Somente Número Real. ex:(1.00)")
                print("-"*40)
                os.system("pause")
                os.system("cls")
            else:
                break
 
        valor_passagem = valor_passagem - 5/100
        cadastro_passagem.append([destino,origem,duracao,valor_passagem])
        print("-"*36)
        print("I| Cadastro de Passagem Concluida I|")
        print("-"*36)
        print("I| Destino: %s"%destino)
        print("I| Origem: %s"%origem)
        print("I| Duração: %d"%duracao)
        print("I| Valor Passagem Com Desconto de 5%: %.2f"%valor_passagem)
        print("-"*45)
        os.system("pause")
        os.system("cls")
    
    elif inicio == 3:
        print("+"+"="*36+"+")
        print("I| Bem Vindo ao Cadastro do Avião I|")
        print("+"+"="*36+"+")
        modelo_aviao = input("I| Qual o Modelo do Avião:\n>> ")
        
        while True:
            try:
                ano = int(input("I| Qual o Ano do Avião:\n>> "))
            except ValueError:
                    print("-"*33)
                    print("I| Digite Somente Número Inteiro.")
                    print("-"*33)
                    os.system("pause")
                    os.system("cls")
            else:
                break
        
        
        horas = input("I| Quantas Horas de Voo:\n>> ")
        cor = input("I| Qual a Cor do Avião:\n>> ")

        while True:
            try:
                quant_passageiros = int(input("I| Digite a Quantidade de Passageiros:\n>> "))
            except ValueError:
                    print("-"*33)
                    print("I| Digite Somente Número Inteiro.")
                    print("-"*33)
                    os.system("pause")
                    os.system("cls")
            else:
                break

        cadastro_aviao.append([modelo_aviao,ano,horas,cor,quant_passageiros])
        print("-"*33)
        print("I| Cadastro de Avião Concluido |I")
        print("-"*33)
        print("I| Modelo: %s"%modelo_aviao)
        print("I| Ano: %d"%ano)
        print("I| Horas de Viagem: %s"%horas)
        print("I| Cor: %s"%cor)
        print("I| Quantidade de Passageiros: %d"%quant_passageiros)
        print("-"*35)
        os.system("pause")
        os.system("cls")
    
    elif inicio == 4:
        print("+"+"="*43+"+")
        print("I| Bem Vindo ao Cadastro da Tripulação I|")
        print("+"+"="*43+"+")
        nome_tripulante = input("I| Qual o seu Nome\n>> ")
        desc_cargo = input("I| Qual a seu Cargo:\n>> ")
        
        while True:
            try:
                idade_tripulante = int(input("I| Qual sua Idade:\n>> "))
            except ValueError:
                    print("-"*33)
                    print("I| Digite Somente Número Inteiro.")
                    print("-"*33)
                    os.system("pause")
                    os.system("cls")
            else:
                break
        
        data_admissao = input("I| Qual a Data de sua Admissão:\n>> ")
        
        while True:
            try:
                fone_tripulante = int(input("I| Qual o seu Telefone:\n>> "))
            except ValueError:
                print("-"*33)
                print("I| Digite Somente Número Inteiro.")
                print("-"*33)
                os.system("pause")
                os.system("cls")
            else:
                break

        cadastro_tripulacao.append([nome_tripulante,desc_cargo,idade_tripulante,data_admissao,fone_tripulante])
        print("-"*38)
        print("I| Cadastro da Tripulação Concluido |I")
        print("-"*38)
        print("I| Nome: %s"%nome_tripulante)
        print("I| Cargo: %s"%desc_cargo)
        print("I| Idade: %d"%idade_tripulante)
        print("I| Data Admissão: %s"%data_admissao)
        print("I| Telefone: %d"%fone_tripulante)
        print("-"*35)
        os.system("pause")
        os.system("cls")
    
    elif inicio == 0:
        print("="*38)
        num_registro = int(input("I| Qual Registro Deseja Analizar:\n>> "))
        print("="*38)
        print("I| Registro %d"%num_registro)
        print("I| Cadastro Cliente: %d | %s"%(num_registro,cadastro_cliente[num_registro-1]))
        print("I| Cadastro Passagem: %d | %s"%(num_registro,cadastro_passagem[num_registro-1]))
        print("I| Cadastro Avião: %d | %s"%(num_registro,cadastro_aviao[num_registro-1]))
        print("I| Cadastro Tripulação: %d | %s"%(num_registro,cadastro_tripulacao[num_registro-1]))
        print("="*38)
        os.system("pause")
        print("I| Programa Encerrado.")
        print("I| Obrigado Por Utilizalo.")
        print("-"*26)
        break