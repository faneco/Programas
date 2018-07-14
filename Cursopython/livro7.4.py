string = input('Digite a palavra: ')

dic = {}

for letra in string:
	if letra in dic:
		dic[letra] += 1
	else:
		dic[letra] = 1
		
print (dic)

for chave in dic:
	print ('%s: %d ' %(chave, dic[chave]))
