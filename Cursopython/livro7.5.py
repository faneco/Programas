primeiro = input('Digite a primeiro palavra: ')
segunda = input('Digite a segunda palavra: ')

terceiro = ''

for letra in primeiro:
	if letra not in segunda:
		terceiro += letra


print (terceiro)