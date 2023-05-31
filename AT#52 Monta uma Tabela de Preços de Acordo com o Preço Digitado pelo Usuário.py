#Programa que Monta uma Tabela de Preços de 1 até 50 Produtos de Acordo com o Preço Digitado pelo Usuário.

preco_pao = float(input("I| Digite o Preço do Pão:\n>> "))
for cont in range(1,51):
        total = cont * preco_pao
        print("%d - %.2f"%(cont,total)) 