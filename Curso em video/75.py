
	
num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print (num)



print ('O numero 9 apareceu ', num.count(9))
print ('O numero 3 apareceu na ', num.index(3)+1)
print ('Os numero pares foi ', end='')
for x in num:
	if x % 2 == 0:
		print (x, end=' ')