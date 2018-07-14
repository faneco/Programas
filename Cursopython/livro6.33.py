lista = [-10, -8, 0, 1, 5, 2, -2, -4]

maior = lista[0]
menor = lista[0]

for l in lista:
	if l > maior:
		maior = l
	elif l < menor:
		menor = l

print ('Maior temperatura %d' %(maior))
print ('Menor temperatuda %d' %(menor))