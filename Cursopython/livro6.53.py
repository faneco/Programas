estoque = {'tomate': [1000, 2.30],
		   'alface': [500, 0.45],
		   'batata': [2001, 1.20],
		   'feijão': [100, 1.50]}

venda = [['tomate', 5], ['batata', 10], ['alface', 5]]

total = 0

print ('Vendas: \n')
for operacao in venda:
	produto, quantidade = operacao
	preco = estoque[produto][1]
	custo = preco * quantidade

	print ('%s: %d x %.2f = %.2f' %(produto, quantidade, preco, custo))
	estoque[produto][0] -= quantidade
	total += custo

print ('Custo total %.2f \n' %(total))
print ('Estoque: \n')

for chave, dados in estoque.items():
	print ('Descrição: ', chave)
	print ('Quantidade: ', dados[0])
	print ('Preço: ', dados[1])