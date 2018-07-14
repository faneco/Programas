total = f = m = 0

while True:
	print ('=' *10)
	print ('CADASTRE UMA PESSOA')
	print ('=' *10)
	sexo = ' '
	idade = int(input('Idade: '))
	while sexo not in 'MF':
		sexo = input('Sexo [M/F]: ').strip().upper()[0]

	if idade > 18:
		total += 1
	if sexo == 'F' and idade <= 20:
		f += 1
	if sexo == 'M':
		m += 1

	c = ' '
	while c not in 'SN':
		c = input('Deseja continua: [S/N]: ').strip().upper()[0]
	if c == 'N':
		print ('Acabou \n')
		break

print ('Total de pessoas com mais de 18 anos: %d' %(total))
print ('Ao todo temos %d homens cadatrados' %(m))
print ('E temos %d mulheres com menos de 20 anos' %(f))