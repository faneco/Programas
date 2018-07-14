lista = []
num = 0
n = 1
while n <= 3:
	num = int(input('Digite %d numero: ' %n))
	lista.append(num)
	n += 1
print (max(lista))