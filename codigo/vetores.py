#Criação de Vetores
vetor = []
lista = list()
selecoes = ['Brasil', 'França', 'Argentina']
notas = [8.5, 9.7, 10]
heterogenea = ['Flamengo', True, 10, 5.5]
print(selecoes[2])
print(notas[2])
print(heterogenea[0])
print(len(heterogenea)) #Tamanho do vetor
#Adicionando elementos na lista
selecoes.append('Marrocos')
print(selecoes)
selecoes.insert(1, 'Paraguai')
print(selecoes)
selecoes.insert(6, 'Teste')
print(selecoes)
#Removendo elementos da lista
#selecoes.pop(3)
del selecoes[3] #Argentina
print(selecoes.pop(3)) #Marrocos
selecoes.pop() #Teste
print(selecoes)
#Percorrer a lista de seleções com indices
for indice in range(len(selecoes)):
    print(selecoes[indice])
#Percorrer a lista de seleções com conteúdo
print('------------------')
for conteudo in selecoes:
    print(conteudo)
#Ordenando a lista de seleções
selecoes.sort()
print(selecoes)
    











