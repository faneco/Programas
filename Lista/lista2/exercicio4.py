lista = []
x = 1
while x <= 3:
	n = input("Digite %d numero: " %x)
	lista.append(n)
	x +=1
print min(lista)
print max(lista)