conta = int(input('Conta: '))
pgto = int(input('Pagamento: '))

troco = pgto - conta
notas = [50, 20, 10, 5, 2, 1]
nota = 0
for nota in notas:
	while troco >= nota:
		print ('o troco %d reais' %nota)
		troco -= nota

