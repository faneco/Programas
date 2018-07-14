
l = ['super']
s = ['123']
supe = ['123456']
limite = 200
precoTotal = 0

banana = int(125)
bananapreco = float(3.50)
desbanana = int(18)

pera = int(119)
peraPreco = float(7.00)
peraDesconto = int(16)

def man():
	opcao = bool(int(input('entrar com a conta (1) ou Sair (0): ')))
	if opcao:
		criaConta()
		produto()
		bananaProduto()

def criaConta():
	login = input('Digite o login: ')
	for i in l:
		while i != login:
			print ('Login invalido. Digite novamente')
			login = input('Digite o login: ')
		senha = input('Digite a senha: ')
		for j in s:
			while j != senha:
				print ('Senha invalida. Digite novamente')
				senha = input('Digite a senha: ')
			else:
				print ('Bem vindo!')

def produto():
	while True:
		global banana, bananapreco, desbanana, precoTotal
		print ('Codigo |   Descrição do produto |  preco Unit | % Max.Desconto | Estoque')
		print ('3500   |    Banana Prata        |     3,50    |      18%       |', banana)
		print ('4501   |    Pera Argentina      |     7,00    |      16%       |', pera)
		
		print ('\n')
		listaProduto = ['3500', '4501']
		opcao = input('Informe codigo para compra: ')
		for i in listaProduto:
			if i == opcao:
				print ('\n')
				if i == '3500':
					bananaProduto()
				elif i == '4501':
					peraProduto()


				

def bananaProduto():
	global banana, bananapreco, desbanana, precoTotal
	compra = int(input('Informe quantidade de compra: '))
	if compra >= 20:
		if compra > banana:
			print('Essa quantia nao tem no estoque')
			input('Pressione ENTER para continua')
		else:
			print ('compra alta ')
			superVisor = input('Digite a senha do SuperVisor: ')
			for x in supe:
				while x != superVisor:
					superVisor = input('Digite a senha do SuperVisor: ')
				else:
					print ('Compra aprovada')
					input("Pressione ENTER para continuar")

					banana -= compra
					preco = bananapreco * compra
					a = preco
					print ('preco sem desconto: ', preco)
					des = (a / 100) * desbanana
					preco -= des
					precoTotal += preco
					print ('Preco com desconto', preco)
					print ('total: R$', precoTotal)
	else:
		print ('Compra aprovada')
		input("Pressione ENTER para continuar")
		banana -= compra
		preco = bananapreco * compra
		a = preco
		print ('preco sem desconto: ', preco)
		des = (a / 100) * desbanana
		preco -= des
		precoTotal += preco
		print ('Preco com desconto', preco)
		print ('total: R$', precoTotal)


def peraProduto():
	global pera, peraPreco, peraDesconto, precoTotal
	compra = int(input('Informe quantidade de compra: '))
	if compra >= 20:
		if compra > pera:
			print('Essa quantia nao tem no estoque')
			input('Pressione ENTER para continua')
		else:
			print ('compra alta ')
			superVisor = input('Digite a senha do SuperVisor: ')
			for x in supe:
				while x != superVisor:
					superVisor = input('Digite a senha do SuperVisor: ')
				else:
					print ('Compra aprovada')
					input("Pressione ENTER para continuar")

					pera -= compra
					preco = peraPreco * compra
					a = preco
					print ('preco sem desconto: ', preco)
					des = (a / 100) * peraDesconto
					preco -= des
					precoTotal += preco
					print ('Preco com desconto', preco)
					print ('total: R$', precoTotal)
	else:
		print ('Compra aprovada')
		input("Pressione ENTER para continuar")
		pera -= compra
		preco = peraPreco * compra
		a = preco
		print ('preco sem desconto: ', preco)
		des = (a / 100) * peraDesconto
		preco -= des
		precoTotal += preco
		print ('Preco com desconto', preco)
		print ('total: R$', precoTotal)


man()





	
	



