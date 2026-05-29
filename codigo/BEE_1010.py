#Transformando a entrada em um vetor de strings
entrada1 = input().split(' ') 
#print(entrada)
p1 = float(entrada1[1])*float(entrada1[2])
#print(p1)
entrada2 = input().split()
p2 = float(entrada2[1])*float(entrada2[2])
#print("VALOR A PAGAR: R$ %.2f"%(p1+p2))
resultado = p1+p2
print(f"VALOR A PAGAR: R$ {resultado:.2f}")
