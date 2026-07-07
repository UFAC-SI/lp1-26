fila = ['Alemanha', 'Bélgica', 'Croácia', 'Noruega']
print(fila)
pilha = fila[:]  # Criando uma cópia da fila para tratar como pilha
while len(fila) > 0:
    fila.pop(0)  # Retira da primeira posição
    print(fila)

print(pilha)
while len(pilha) > 0:
    pilha.pop()  # Retira da última posição
    print(pilha)
