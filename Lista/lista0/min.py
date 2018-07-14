lista = []
x = 1

while x <= 3:
	num = input('Digite %d numero: ' %x)
	lista.append(num)
	x += 1
print min(lista)