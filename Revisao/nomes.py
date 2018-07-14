from random import choice
nomes = '''julia ana katarina amanda fernanda hinata'''.split()
print (' '.join(nomes))

chute = ''
sorteado = choice(nomes)

while chute != sorteado:
	chute = input('Digite o nome: ')
	if chute == sorteado:
		print ('Parabens')
	elif chute > sorteado:
		print ('Alto')
	else:
		print ('Baixo')

print ('Fim do jogo')