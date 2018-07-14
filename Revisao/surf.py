f = open('surf1.txt')
notas = {}
for linha in f:
	nome, pontos = linha.split()
	notas[float(pontos)] = nome

f.close()
for nota in sorted(notas, reverse = True):
	print ('Nome: %s | notas: %4.2f' %(notas[nota], nota))
