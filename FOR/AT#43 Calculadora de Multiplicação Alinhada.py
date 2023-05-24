#Programa Calculadora de Multiplicação Alinhada.

for x in range(1,11):
    print("="*12) 
    for y in range(1,11):
        result = x * y
        print("%d X %d = %d"%(x,y,result))