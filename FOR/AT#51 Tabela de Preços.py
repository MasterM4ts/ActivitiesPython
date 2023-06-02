#Programa que Monta uma Tabela de Preços de 1 até 50 Produtos.

valor = 0
for preco in range(1,51):
        valor = preco * 1.99
        print("%d - %.2f"%(preco,valor))    