#Variáveis
nome_pessoa = 'Limeira'
idade_pessoa = '21'
altura_pessoa = '1.76'
status = True
nova_idade = input() #Sempre amazena uma string
#Conversão de Tipos e Operações
idade_int = int(idade_pessoa) + 1 #Soma de inteiros
#altura_int = int(altura_pessoa)
idade_saida = idade_pessoa + str(idade_int) #Concatenação de strings
status = bool(0)
altura_float = float(altura_pessoa) + 0.1
#Saídas
print('Nome:\t',nome_pessoa)
print('Idade:\t',idade_saida)
print('Altura:\t',altura_float)
print('Status:\t',nova_idade)
#Faltou float e saida formatada


