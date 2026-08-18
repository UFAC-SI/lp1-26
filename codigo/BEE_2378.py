n, c = map(int, input().split())
resposta = False
peso_atual = 0
for i in range(n):
    s, e = map(int, input().split())
    peso_atual += e - s
    if peso_atual > c:
        resposta = True
if resposta == True:
    print('S')
else:
    print('N')
    
