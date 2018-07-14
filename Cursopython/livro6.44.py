l = [5, 4, 3, 2, 1]


def dubblesort(l):
	opcao = True
	passnum = len(l)-1
	while passnum > 0 and opcao:
		opcao = False
		for x in range(passnum):
			if l[x] > l[x+1]:
				opcao = True
				aux = l[x]
				l[x] = l[x+1]
				l[x+1] = aux
	return passnum-1

dubblesort(l)
print (l)

