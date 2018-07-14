n = int(input('Digite numero inteiro: '))

while n <= 2:
	print ('Valor muito baixo')
	n = int(input('Digite numero novamente: '))
else:
	for k in range(2, n):
		n % k == 0
		print (k) 
	n = n / k