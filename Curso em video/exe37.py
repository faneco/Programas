matriz = []

m = int(input('Digite o numero de linha da matriz: '))
n = int(input('Digite o numero de coluna: '))

def constroiMatriz(m, n, matriz):
	for i in range(1, m+1):
		linha = []
		for j in range (1, n+1):
			x = int(input('Digite os numero da %d%d da matriz: ' %(i, j)))
			linha.append(x)
		matriz.append(linha)




def trocaElemento(pos1, pos2, matriz):
	elemento1 = matriz[pos1//10-1][pos1%10-1]
	elemento2 = matriz[pos2//10-1][pos2%10-1]
	matriz[pos1//10-1][pos1%10-1] = elemento2
	matriz[pos2//10-1][pos1%10-1] = elemento1

constroiMatriz(m, n, matriz)
print (matriz)

pos1 = int(input('Digite a posicao do elemento 1: '))
pos2 = int(input('Digite a posicao do elemento 2: '))
trocaElemento(pos1, pos2, matriz)
print (matriz)
