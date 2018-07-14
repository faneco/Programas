verifica = False

while True:
	print ('1 - segunda')
	print ('2 terça')
	print ('3 - quarta')
	print ('4 - quinta')
	print ('5 - sexta')
	print ('0 - Sair')

	dia = int(input('Digite o dia da semana: '))

	if dia == 1:
		print ('segunda')
		input()
		
	elif dia == 2:
		print ('terça')
		input()

	elif dia == 4:
		print ('quarta')
		input()
	elif dia == 5:
		print ('quinta')
		input()
	elif dia == 6:
		print ('sexta')
		input()
	elif dia == 0:
		print ('Fim')
		break
	else:
		print ('numero invalido')
		input()