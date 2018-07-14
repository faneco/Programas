lista = []
x = 1
while x <= 5:
	n = int(input('Digite %d inteiro: ' %x))
	lista.append(n)
	x += 1
	n += 1
print (lista)

x = 4
while x >= 0:
	print (lista[x])
	x -= 1
