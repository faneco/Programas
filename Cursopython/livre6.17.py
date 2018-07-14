estoque = {'tomate': [1000, 2.30],
		   'alface': [500, 0.45],
		   'batata': [2001, 1.20],
		   'feijão': [100, 1.50]}

total = 0

while True:
	produto = input('Digite nome do produto ou (fim) para Sair: ')
	if produto == 'fim':
		print ('Fim do programa')
		break
	else:
		if produto in estoque:
			quantidade = int(input('Digite quantidade: '))
			if quantidade < estoque[produto][0]:
				preco = estoque[produto][1]
				custo = preco * quantidade
				total += custo
				estoque[produto][0] -= quantidade

				print ('Descrição: %s - Quantidade: %d - Preço total: %.2f' %(produto, quantidade, total))
				print ('\n')

				for chave, dados in estoque.items():
					print ('Descrição: ', chave)
					print ('Quantidade: ', dados[0])
					print ('Preço: %.2f' %(dados[1]))

		else:
			print ('Produto não cadastrado')



N