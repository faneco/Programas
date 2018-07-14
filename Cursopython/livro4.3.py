lista = []

for i in range(1, 3+1):
	num = int(input('Digite %d numero: ' %(i)))
	lista.append(num)

maior = lista[0]
menor = lista[0]

for j in lista:
	if j > maior:
		maior = j
	if j < menor:
		menor = j
print ('Maior numero: ', maior)
print ('Menor numero: ', menor)