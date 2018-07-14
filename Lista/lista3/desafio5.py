lista = []

while True:
	num = int(input('Digite: '))
	if num != 0:
		lista.append(num)
	else:
		break

print (lista[::-1])