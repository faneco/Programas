while True:
	idade = int(input('Digite sua idade: '))

	if idade >= 18:
		print (True)
	else:
		print (False)
	c = ' '
	while c not in 'SN':
		c = input('Deseja continua [S/N]: ').strip().upper()[0]
	if c == 'N':
		break		