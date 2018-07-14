string1 = input('Digite primeira palavra: ')
string2 = input('Digite segunda palavra: ')

posicao = string1.find(string2)

if posicao == -1:
	print ('não está contido')
else:
	print ('%s está contido na pisição %d na %s' %(string2, posicao, string1))
