print ('=' *10)
print ('BANCO CEV')
print ('=' *10)



valor = int(input('Que valor voce quer sacar?: '))
total = valor
celulas = 50
cont = 0
while True:
	if celulas <= total:
		total -= celulas
		cont += 1
	else:
		if cont > 0:
			print ('total de  %d celulas de R$ %d' %(cont, celulas))
		if total == 50:
			celulas = 20
		elif total == 20:
			celulas = 10
		elif total == 10:
			celulas = 1
		cont = 0
		if total == 0:
			break

print ('Fim')
