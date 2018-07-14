from random import randint

cont = 0
while True:
	num = int(input('Digite um valor: '))
	opção = ' '
	maquina = randint(0, 10)
	total = num + maquina
	while opção not in 'PI':
		opção = input('Par ou Impar? [P/I]: ').strip().upper()[0]
	print (opção)
	if opção == 'P':
		if total % 2 == 0:
			print ('voce jogou %d e o computador %d. Total de %d deu PAR' %(num, maquina, total))
			print ('voce ganhou')
			cont += 1
		else:
			print ('voce jogou %d e o computador %d. Total de %d deu IMPAR' %(num, maquina, total))
			print ('voce perdeu')
			break
	elif opção == 'I':
		if total % 2 == 0:
			print ('voce jogou %d e o computador %d. Total de %d deu PAR' %(num, maquina, total))
			print ('voce perdeu')
			break
		else:
			print ('voce jogou %d e o computador %d. Total de %d deu IMPAR' %(num, maquina, total))
			print ('voce ganhou')
			cont += 1
	print ('Vamos jogar novamente...')
		
print ('Game Over voce vence %d vezes' %(cont))