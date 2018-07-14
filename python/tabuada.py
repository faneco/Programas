tam = 1
soma = 0
while tam <= 10:
	print ('Tabuada %d' %tam)
	n = 1
	while n <= 10:
		soma = tam * n
		print ('%d x %d = %d' %(tam, n, soma))
		n += 1
	tam += 1