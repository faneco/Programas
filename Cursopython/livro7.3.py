primeiro = input('Digite primeira palavra: ')
segunda = input('Digite segunda palavra: ')

terceira = ''

for letra in primeiro:
	if letra in segunda and letra not in terceira:
		terceira += letra

if terceira == '':
	print ('não tem palavra iguais')
else:
	print ('%s -  de palavras' %(terceira))
