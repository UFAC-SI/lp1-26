valor = float(input())
nota = valor // 100
##Várias formas de emitir a saída no print
print('NOTAS:')
print(f'{int(nota)} nota(s) de R$ 100.00') #convertendo para int
resto = valor % 100
nota = resto // 50
print('%d nota(s) de R$ 50.00' % nota) #com o operador %
resto = resto % 50
nota = resto // 20
print('{:.0f} nota(s) de R$ 20.00'.format(nota)) # com o operador .format
resto = resto % 20
nota = resto // 10
print(f'{nota:.0f} nota(s) de R$ 10.00') # com f-string
resto = resto % 10
nota = int(resto) // 5
print(f'{nota} nota(s) de R$ 5.00') # convertendo antes da divisão
resto = resto % 5
nota = int(resto) // 2
print(f'{nota} nota(s) de R$ 2.00')
resto = resto % 2
moeda = int(resto) / 1
print('MOEDAS:')
print(f'{int(moeda)} moeda(s) de R$ 1.00')
resto = resto % 1
resto = int(resto*100)
moeda = resto // 50
print(f'{moeda} moeda(s) de R$ 0.50')
resto = resto % 50
moeda = resto // 25
print(f'{moeda} moeda(s) de R$ 0.25')
resto = resto % 25
moeda = resto // 10
print(f'{moeda} moeda(s) de R$ 0.10')
resto = resto % 10
moeda = resto // 5
print(f'{moeda} moeda(s) de R$ 0.05')
resto = resto % 5 #Durante a aula estava faltando essa linha
moeda = resto
print(f'{int(moeda)} moeda(s) de R$ 0.01')











