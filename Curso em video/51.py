num1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
decimo = num1 + (10 - 1) * razão
x = 0
resultado = 0
for i in range(num1, decimo + razão, razão):
	print ('%d' %(i), end=' -> ')
print ('acabou \n', end='')