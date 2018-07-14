m = input('Informe quantidade em (M2): ')
if m % 54 != 0:
	latas = (m / 54) + 1
else:
	latas = m / 54

preco = latas * 80
print ('lata(s) %d | preco R$ %.2f' %(latas, preco))