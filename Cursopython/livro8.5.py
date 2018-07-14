def pesquisa(lista, valor):
	if valor in lista:
		return lista.index(valor)
	return None

l = [1, 7, 2, 9, 15]

print (pesquisa(l, 7))