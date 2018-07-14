velociade = 0
multa = 0
velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
	multa = velocidade - 80
	multa *= 5
	print ('A velocidade %d multa do veiculo R$: %.2f' %(velocidade, multa))
else:
	print ('A velocidade %d Sem multa' %(velocidade))