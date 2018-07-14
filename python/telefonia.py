min = input('Informe minutos usando: ')
if min < 200:
	preco = 0.20
else:
	if min <= 400:
		preco = 0.18
	else:
		if min <= 800:
			preco = 0.15
		else:
			preco = 0.08

print ('O preco dos minutos usando: R$ %.2f' %(min * preco))