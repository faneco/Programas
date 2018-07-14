primeiro = input('Digite primeira letra: ')
segundo = input('Digite segunda letra: ')
terceiro = input('Digite terceira letra: ')

resultado = ''

for letra in primeiro:
	posicao = segundo.find(letra)
	if posicao != -1:
		resultado += terceiro[posicao]
	else:
		resultado += letra

print (resultado)