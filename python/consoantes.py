lista = []
x = 1
n = 0
while x <= 5:
	n = raw_input('Digite %d letra: ' %x)
	lista.append(n)
	x += 1
x = 0
cont = 0
while x <= 4:
	if lista[x] not in 'aeiou':
		cont += 1
	x += 1
print (cont)