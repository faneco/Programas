listaProduto = []
listaPreço = []
total = 0
maior = 0

while True:
	print ('-' *20)
	print ('LOJA SUPER BARATÃO')
	print ('-' *20)

	produto = input('Nome do produto: ')
	listaProduto.append(produto)
	preço = int(input('Preco: R$ '))
	listaPreço.append(preço)
	
	c = ' '
	while c not in 'SN': 
		c = input('Deseja continuar [S/N]: ').strip().upper()[0]
	if c == 'N':
		print ('Acabou')
		break

	total += preço
	if preço > 1000:
		maior += 1

produtoMenor = listaProduto[0]
menor = listaPreço[0]
for i, y in enumerate(listaPreço):
	if y < menor:
		menor = y
		produtoMenor = listaProduto[i]


print ('O total da compra foi %.2f' %(total))
print ('Temos %d produto custado mais e R$ 1000.00' %(maior))
print ('O produto mais barato foi %s que custa %d' %(produtoMenor, menor))

'''
total = cont = menor = 0
barato = ' '

while True: 
	produto = input('Nome do poduto: ')
	preço = float(input('preço: R$ '))
	total += preço  

	if preço >= 1000:
		cont += 1

	if cont == 1 or preço < menor:
		menor = preço
		barato = produto


	c = ' '
	while c not in 'NS':
		c = input('Deseja continua [S/N]: ').strip().upper()[0]
	if c == 'N':
		print ('acabou')
		break


print ('O total da compra foi %.2f' %(total))
print ('Temos %d produto custado mais e R$ 1000.00' %(cont))
print ('O produto mais barato foi %s que custa %d' %(barato, menor))
'''