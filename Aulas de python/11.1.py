lista = []
for i in range(1, 4):
	num = int(input('Digite %d numero: ' %i))
	lista.append(num)

lista.sort()
print (lista[::-1])