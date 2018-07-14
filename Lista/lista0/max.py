lista = []
x= 1
num = 0
while x <= 3:
	num =  input('Informe %d numero: ' %x)
	lista.append(num)
	x += 1
print max(lista)