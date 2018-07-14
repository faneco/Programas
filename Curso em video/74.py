from random import randint

maior = 0
menor = 0
cont = 0
for i in range(5):
	cont += 1
	valor = randint(0, 20)
	print (valor, end=', ')
	if valor > maior:
		maior = valor
	if cont == 1 or valor < menor:
		menor = valor
print ('\nFim')





print ('O maior valor %d' %(maior))
print ('O menor valor %d' %(menor))

'''
from random import randint

maior = 0
menor = 0
cont = 0

valor = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in valor:
	print (n, end=', ')



print ('\n')
print ('O maior valor: ', max(valor))
print ('O menor valor ', min(valor))
'''