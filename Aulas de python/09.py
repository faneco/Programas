litro = 0
latas = 0
area = int(input('Informe area em metro quadrados: '))
litro = area // 3

if area % 3 > 0:
	litro += 1

print ('numero de litro %d' %(litro))

latas = litro // 18
if litro % 18 > 0:
	latas += 1

print ('Preço apagar R$: ', latas*80)

