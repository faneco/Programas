import random

inimigos = []
vida = 10

print ('vida: ', vida)
n = int(input('numero inimigos: '))
print ('--------------')

for i in range(n):
	inimigos.append([i, vida])
	print ('inimigo: %d vida: %d' %(i, vida))

jogador = True
while jogador:	

	atk = int(input('Deseja ataca (1) ou cura (2)'))
	if atk == 1:	
		escolher = random.choice(inimigos)
		dano = random.randint(5, 10)
		print (dano, escolher[0])
		escolher[1] -= dano
		print ('inimigo: %d | vida: %d' %(escolher[0], escolher[1]))

		if escolher[1] <= 0:
			print ('O inimigo morreu: %d' %(escolher[0]))
			inimigos.remove(escolher)
		

		if vida <= 0:
			print ('perdeu o jogo')
			jogador = False
		if len(inimigos) == 0:
			print ('Parabens voce ganhou')
			jogador = False
