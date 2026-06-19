n = int(input())
cont = 1
atual = int(input())
status = False
while cont < n:
    proximo = int(input())
    if proximo < atual:
        status = True
    cont += 1
    atual = proximo

if status == True:
    print('A sequência não é crescente')
else:
    print('Crescente')
    
