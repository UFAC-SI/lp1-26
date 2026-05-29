#BEE_2987
entrada = input()
#tabela = ['A',....,'Z']
#print(tabela.index(entrada)+1)
valor = ord(entrada) # Função que converte um caracter para decimal
if valor > 64 and valor < 91: 
    print(valor-64)
elif 96 < valor < 123:
    print(valor-96)

#Operador Ternário
resultado = valor-64 if valor > 64 and valor < 91 else valor-96
print(resultado)
