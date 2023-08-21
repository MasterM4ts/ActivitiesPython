def soma(n):
    if n == 1:
        return 1
    else:
        return n * soma(n - 1)
numero = 5
result = soma(numero)
print(f"O Fatorial de {numero} é {result}.")