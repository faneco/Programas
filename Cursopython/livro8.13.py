import random

n = random.randint(1, 10)
i = 0
while i < 3:
	x = int(input('Digite um numero entre 1 e 10: '))
	if x == n:
		print ('voce acertou!')
		break
	else:
		print ('voce errou.')
		print (n)
		i += 1	
