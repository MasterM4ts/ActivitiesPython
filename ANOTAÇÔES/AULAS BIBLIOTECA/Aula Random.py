import random

print(random.random())

print(random.uniform(4,10)) 

print(random.randint(11,55))

cores = ['verde','vermelho','azul']
print(random.choice(cores))

cartas_Baralho = ['Zap','Sete Copas','Espadilha','Pica Fumo']
random.shuffle(cartas_Baralho)
print(cartas_Baralho)