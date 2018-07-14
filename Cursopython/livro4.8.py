
def man():
	while True:
		lista = []
		esco = 0
		soma = 0

		continua = bool(int(input('Deseja fazer operações (1) ou  Sair (0): ')))
		if continua == 0:
			print ('Saiu do programa')
			exit()
			
		for i in range(1, 2+1):
			num = float(input('Digite %.0f valor: ' %(i)))
			lista.append(num)
		
		print ('1 - Soma')
		print ('2 - Subtração')
		print ('3 - Multiplicação')
		print ('4 - Divisão')

		esco = int(input('Digite qual operação deseja: '))
		
		if  esco == 1:
			soma = lista[0] + lista[1]
			print (soma)
		elif esco == 2:
			soma = lista[0] - lista[1]
			print (soma)
		elif esco == 3:
			soma = lista[0] * lista[1]
			print (soma)
		elif esco == 4:
			soma = lista[0] / lista[1]
			print (soma)
	

man()