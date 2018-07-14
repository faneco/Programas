tabela = {'Alface': 0.45,
		  'Batata': 1.45,
		  'Tomate': 2.30,
		  'Feijão': 1.50}

while True:
	produto = input('Digite o nome do produto (Fim: para terminar): ')
	if produto == 'fim':
		print ('Fim da execução do programa')
		break
	if produto in tabela:
		print ('Preco: %.2f' %(tabela[produto]))
	else:
		print ('Produto nao encontrado')