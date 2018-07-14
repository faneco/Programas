from random import randint

secreta = randint(0, 10)

while True:
	num = int(input('Digite o numero: '))
	if num == secreta:
		print ('Parabéns voce acertou %d' %secreta)
		break
	else:
		print ('Alto' if num > secreta else 'baixo')