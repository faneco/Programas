lista = []
x = 1
while x <= 4:
	n = int(input('Digite %d nota: ' %x))
	lista.append(n)
	x += 1
print (lista)

x = 3
soma = 0
while x >= 0:
	soma += lista[x]
	x -= 1
print ('nota: ', soma)
print ('media: %4.2f' %(soma / 4))