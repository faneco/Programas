lista = []

for i in range(1, 5+1):
	num = input('Digite %d valor: ' %(i))
	lista.append(num)	

maior = lista[0]
menor = lista[0]

for j in lista:
    if j > maior:
        maior = j
    elif j < menor:
        menor = j
print(maior)
print(menor)