
escolha = int(input('1 - Criar conta | 2 - Sair: ' ))

if escolha == 2:
	print ('ate proxima')
	exit()
else:
	senha = input('Digite a senha de 6 digitos: ')
	while len(senha) < 6:
		senha = input('Digite a senha de 6 digitos: ')
	else:
		print ('senha aceita')

saldo = float(0.0)
while True:
	print ('1 - deposito')
	print ('2 - saldo')
	print ('3 - saque')
	print ('4 - Sair')

	print ('\n')
	opcao = int(input('Digite opcao desejada: '))

	if opcao == 1:
		saldo += float(input('valor: '))
	elif opcao == 2:
		print('Saldo atual: %.2f'%(saldo))
	elif opcao == 3:
		saldo -= float(input('valor: '))
	elif opcao == 4:
		print ('Ate proxima')
		exit ()

