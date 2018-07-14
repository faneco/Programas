import random

matriz = []
def geraMatriz(matriz):
	x = 0
	lista = list(range(16))
	for j in range(4):
		lista = []
		for i in range(4):
			x = random.choice(lista)
			lista.append(x)
			lista.remove(x)
		matriz.append(lista)


for i in range(3):
	matriz = []
	geraMatriz(matriz)
	print (matriz)

'''
lista = []
l = list(range(10))
lista.append(l)
print (lista)
'''