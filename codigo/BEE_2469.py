#Entrada de dados
n = int(input())
notas = list(map(int, input().split()))
frequencia = [0] * (max(notas)+1)
#print(frequencia)

for i in notas: #i representa o conteúdo das notas
    frequencia[i] += 1
maior = 0
indice = 0
for i in range(len(frequencia)): #i reprensenta o índice
    if frequencia[i] >= maior:
        maior = frequencia[i]
        indice = i
        
print(indice)

