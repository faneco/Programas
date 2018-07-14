while True:
	num = int(input('Digite um numero (menor que 1000): '))

	if num > 1000:
		print ('numero tem que ser menor que 1000')
	else:
		print (' ')

	nc = num // 100
	nd = (num-(nc*100)) // 10
	nu = (num-(nc*100) - (nd * 10))
	print ('centena: %d dezena: %d unidade: %d' %(nc, nd, nu))
	break