palavra = input('Digite um palavra: ')
d = {}

for letra in palavra:
	if letra in d:
		d[letra] += 1
	else:
		d[letra] = 1

print (d)