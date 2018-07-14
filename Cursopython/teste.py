linha = 30

listagem = ('Lapis', 1.75,
			'Borracha', 2,
			'Caderno', 15.90,
			'Estojo', 25,
			'Transferidor', 4.20,
			'Campasso', 9.99,
			'Mochila', 120.32,
			'Canetas', 22.30,
			'Livro', 34.90)



print ('Listagem de preços')
print ('-' * 30)
for pos in range(0, len(listagem)):
	if pos % 2 == 0:
		total = (linha - len(listagem[pos]))
		l = '.' * total
		print ('%s %s' %(listagem[pos], l), end='')
		print ('\n')




