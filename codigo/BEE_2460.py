n = int(input())
fila = list(map(int, input().split()))
m = int(input())
saida = list(map(int, input().split()))
##resultado = []
##for i in fila: #50000
##    for j in saida: #50000
##        saiu = False
##        if i == j:
##            saiu = True
##            break
##    if not saiu:
##        resultado.append(i)
##print(*resultado)

##Segunda solução com remove
##for i in saida:
##    fila.remove(i)
##print(*fila)

##Terceira solução
for i in saida:
    fila.pop(fila.index(i))

print(*fila)











