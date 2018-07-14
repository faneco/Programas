notas = []
x = 0
soma = 0

for i in range(1, 5+1):
	num = int(input('Digite %d valor de 5: ' %(i)))
	notas.append(num)
	soma += notas[x]
	x += 1

while True:
	opcao = int(input('Digite posição que deseja ou (0) Sair: '))
	if opcao == 0:
		break
	print ('voce escolheu posição: %d' %(notas[opcao-1]))


