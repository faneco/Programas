lista = [1, 2, 3, 4]
print (lista)
indice = int(input('Digite o indice a ser removido: '))
'''
print ('Elemento: ', lista[indice])

b = []

for i in range (len(lista)):
	if i != indice:
		b.append(lista[i])
print (b)
'''
print ('O elemento: ', lista.pop(indice))
print (lista)