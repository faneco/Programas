valor = int(input('Digite o valo do saque: '))

total = valor
celulas = 50
cont = 0

while True:
	if celulas <= total:
		total -= celulas
		cont += 1
	else:
		if cont > 0:
			print ('total de celulas %d no valor de %d' %(cont, celulas))
		if total < 50:
			celulas = 20
		if total < 20:
			celulas = 10
		if total < 10:
			celulas = 5
		if total < 5:
			celulas = 1
		cont = 0
		if total == 0:
			break



