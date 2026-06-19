contador = 1
soma = 0
while contador < 11:
    soma = soma + contador
    if contador == 10:
        print(contador)
    else:
        print(contador, end=' ')
    contador += 1
print(f'Média: {soma/(contador-1):.2f}')
