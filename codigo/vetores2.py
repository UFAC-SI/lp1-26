lista1 = ['Alemanha', 'Bélgica', 'Croácia', 'Noruega']
lista2 = lista1
print(id(lista1))
print(id(lista2))
#lista1.append('Espanha')
lista2.insert(4, 'Espanha') ##Altera o conteúdo da lista1
print(lista2)
print(lista1)
# Criando uma cópia da lista1
lista3 = lista2[:] # lista3 está armazenada em outro local de memória
print(id(lista1))
print(id(lista3))
lista3.append('Argentina')
print(lista1)
print(lista3)
inicio = 2014
const = 0
for indice, conteudo in enumerate(lista3):
    print(f'Ano {inicio+const}: Eliminação: {conteudo}')
    const += 4













