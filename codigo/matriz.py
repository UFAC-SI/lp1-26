#Entrar com uma matriz quadrada de ordem 3 e imprimir
matriz = []
for i in range(3): #linhas
    linha = []
    for j in range(3): #colunas
        linha.append(i+j+10)
    matriz.append(linha)
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriz[i][j])
        else:
            print(matriz[i][j], end=',')
    
