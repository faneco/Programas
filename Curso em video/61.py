print ('Gerador de PA')
print ('-=' *10)
num1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

total = 0
termo = 0
c = 0
mais = 10
while mais != 0:
	total += mais
	while c < total:
		print ('%d' %(termo), end=' -> ')
		termo += razão
		c += 1
	print ('Pausa')
	mais = int(input('Quantos termos voce quer a mais?: '))
print ('progressão finalizada com %d termos mostradas.' %(total))
print ('Fim')

'''
num1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
decimo = num1 + (10 - 1) * razão
x = 0
resultado = 0
for i in range(num1, decimo + razão, razão):
	print ('%d' %(i), end=' -> ')
print ('acabou \n', end='')
'''