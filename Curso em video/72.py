cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
	'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
	num = int(input('Digite um numero entre 0 e 20: '))
	if 0 <= num <= 20:
		print ('Voce digitou o numero: %s' %(cont[num]))
		verifica = ' '
		while verifica not in 'SN':
			verifica = input('Deseja continua [S/N]: ').strip().upper()[0]
		if verifica == 'N':
			break


