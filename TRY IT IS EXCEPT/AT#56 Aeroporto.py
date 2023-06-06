#Programa Aeroporto.
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
        print("+"+"="*30+"+")
        inicio = int(input("I| Digite a Opção:\n"+"-"*21+"\n1 >> Cadastro Cliente\n2 >> Cadastro Passagem\n3 >> Cadastro Avião\n4 >> Cadastro Tripulação\n0 >> Registro(Encerrar Programa)\n>> "))
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
        sob_nome = input("I| Digite seu Sobrenome:\n>> ")
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
 
        valor_passagem -= 5/100
        cadastro_passagem.append([destino,origem,duracao,valor_passagem])
        print("-"*36)
        print("I| Cadastro de Passagem Concluida I|")
        print("-"*36)
        print("I| Destino: %s"%destino)
        print("I| Origem: %s"%origem)
        print("I| Duração: %d"%duracao)
        print("I| Valor Passagem Com Desconto de 5%: ",valor_passagem)
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
        inicio = 1
        while inicio != 0:
            print("="*40)
            inicio = int(input("I| Digite:\n1 >> Registro de Cadastro de Cliente\n2 >> Registro de Cadastro de Passagem\n3 >> Registro de Cadastro de Avião\n4 >> Registro de Cadastro de Tripulação\n0 >> Finalizar Programa\n>> "))
            
            if inicio == 1:
                try:
                    print("="*38)
                    num_registro = int(input("I| Qual Registro De Cadastro Deseja Analizar:\n>> "))
                    print("="*38)
                    print("I| Registro %d"%num_registro)
                    num_registro -=1
                    print("I| Cadastro Cliente: %d |"%num_registro)
                    for i in cadastro_cliente:
                        print("-"*35)  
                        print("I| Nome: ",cadastro_cliente[num_registro][0])
                        print("I| Sobrenome: ",cadastro_cliente[num_registro][1])
                        print("I| RG: ",cadastro_cliente[num_registro][2])
                        print("I| CPF: ",cadastro_cliente[num_registro][3])
                        print("I| Endereço: ",cadastro_cliente[num_registro][4])
                        print("I| Telefone: ",cadastro_cliente[num_registro][5])
                        print("I| Idade: ",cadastro_cliente[num_registro][6])
                        print("-"*24)
                    os.system("pause")
                except ValueError:
                    print("-"*33)
                    print("I| Registro Não Encontrado\n\"Tente Denovo\"")
                    print("-"*33)
                    os.system("pause")
                    os.system("cls")

            elif inicio == 2:
                try:  
                    print("-"*35)
                    num_registro = int(input("I| Qual Registro De Passaporte Deseja Analizar:\n>> "))
                    print("I| Registro %d"%num_registro)
                    num_registro -=1
                    print("I| Cadastro Passagem: %d |"%num_registro)
                    for i in cadastro_passagem:
                        print("-"*36)
                        print("I| Destino: ",cadastro_passagem[num_registro][0])
                        print("I| Origem: ",cadastro_passagem[num_registro][1])
                        print("I| Duração: ",cadastro_passagem[num_registro][2])
                        print("I| Valor Passagem Com Desconto de 5%: ",cadastro_passagem[num_registro][3])
                        print("-"*45)
                    os.system("pause")
                except ValueError:
                    print("-"*33)
                    print("I| Registro Não Encontrado\n\"Tente Denovo\"")
                    print("-"*33) 
                    os.system("pause")
                    os.system("cls")
            
            elif inicio == 3:
                try:
                    print("-"*35) 
                    num_registro = int(input("I| Qual Registro De Avião Deseja Analizar:\n>> "))
                    print("I| Registro %d"%num_registro)
                    num_registro -=1
                    print("I| Cadastro Avião: %d |"%num_registro)
                    for i in cadastro_aviao:
                        print("-"*33)
                        print("I| Modelo: ",cadastro_aviao[num_registro][0])
                        print("I| Ano: ",cadastro_aviao[num_registro][1])
                        print("I| Horas de Viagem: ",cadastro_aviao[num_registro][2])
                        print("I| Cor: ",cadastro_aviao[num_registro][3])
                        print("I| Quantidade de Passageiros: ",cadastro_aviao[num_registro][4])
                        print("-"*35)
                    os.system("pause")
                except ValueError:
                    print("-"*33)
                    print("I| Registro Não Encontrado\n\"Tente Denovo\"")
                    print("-"*33)
                    os.system("pause")
                    os.system("cls")
            
            elif inicio == 4:
                try:
                    print("-"*35)
                    num_registro = int(input("I| Qual Registro Da Tripulação Deseja Analizar:\n>> "))
                    print("I| Registro %d"%num_registro)
                    num_registro -=1
                    print("I| Cadastro Tripulação: %d |"%num_registro)
                    for i in cadastro_tripulacao:
                        print("-"*38)
                        print("I| Nome: ",cadastro_tripulacao[num_registro][0])
                        print("I| Cargo: ",cadastro_tripulacao[num_registro][1])
                        print("I| Idade: ",cadastro_tripulacao[num_registro][2])
                        print("I| Data Admissão: ",cadastro_tripulacao[num_registro][3])
                        print("I| Telefone: ",cadastro_tripulacao[num_registro][4])
                        print("-"*35)

                except ValueError:
                    print("-"*33)
                    print("I| Registro Não Encontrado\n\"Tente Denovo\"")
                    print("-"*33)
                    os.system("pause")
                    os.system("cls")
        
        os.system("pause")
        print("I| Programa Encerrado.")
        print("I| Obrigado Por Utilizalo.")
        print("-"*26)
        break