texto = ('alice foi atras do coelho, alice mas nao o encontrou alice')
texto = texto.lower() # deixa texto minusculo 
texto = texto.replace(',', ' ') # tira as virgula
texto = texto.split() # 'a', 'b'....

dic = {}
for x in texto:
	if x not in dic:
		dic[x] = 1
	else:
		dic[x] += 1
texto.sort()
print(dic['alice'])