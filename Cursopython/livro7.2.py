primeiro = input('Digite primeira palavra: ')
segundo = input('Digite segunda palavra: ')

terceiro = ''

for letra in primeiro:
	if letra in segundo and letra not in terceiro:
		terceiro += letra


if terceiro == '':
	print ('Não teve letra iguais')
else:
	print ('teve %s de letras iguais' %(terceiro))