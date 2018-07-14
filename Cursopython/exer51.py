
termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = termo + (10-1) * razao
for i in range(termo, decimo+1, razao):
	print (i)