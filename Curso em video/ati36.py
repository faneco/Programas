
contas = []
depositos = []
saldo = 0


def main():

	opcao = bool(int(input('Deseja cria conta 1 ou fechar o programa 0: ')))
	while opcao:
		criaConta()
		VerSaldo()
		opcao = bool(int(input('Deseja criar conta (1) ou fechar o programa (0)')))

def criaConta():
	global contas, depositos, saldo
	num_conta = int(input('Digite um numero de conta: '))

	while num_conta in contas:
		print ('Conta ja existente. Digite novamente: ')
		num_conta = int(input('Digite um numero de conta: '))

	contas.append(num_conta)

	deposito = float(input('Digite o valor do seu primeiro deposito: '))
	while deposito <= 0:
		print ('Valor de deposito invalido')
		deposito = int(input('Digite o valor do deposito: '))

	depositos.append(deposito)
	saldo += deposito

def VerSaldo():
	global saldo 
	opcao = bool(int(input('Deseja ver o saldo do banco (1 - Sim / 2 - nao): ')))
	if opcao:
		print ('O saldo do banco é R$', saldo)



main()