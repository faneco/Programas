lista = [5.6, 6.8, 4.3, 3.4, 5.7]



menor = lista[0]
maior = lista[0]

for i in lista:
	lista.sort()
	if i < menor:
		menor = i
	if i > maior:
		maior = i

print ('Menor peso %.2f' %(menor))
print ('Maior peso %.2f' %(maior))