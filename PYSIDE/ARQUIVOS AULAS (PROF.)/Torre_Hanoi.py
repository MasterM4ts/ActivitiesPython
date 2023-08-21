def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o Disco 1 de {origem} para {destino}.")
        return 1
    mov = 0
    mov += torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o Disco {n} de {origem} para {destino}.")
    mov += 1
    mov += torre_hanoi(n - 1, auxiliar, destino, origem)
    return mov

n = 3
total_mov = torre_hanoi(n, "A", "C", "B")
print(f"Total de Movimentos Necessários: {total_mov}")