'''Rebebendo entradas inteiras dos usuario que so devem ser
 interropidas com a entrada do numero -1, e recebendo um 
 elemento qualquer, calcular o numero de vezes que esse 
 elemento aparece na sequencia digitada pelo usuario'''

lista = []
num = int(input('Digite numero da sequencia (0 Sair): '))

while num != 0:
	lista.append(num)
	num = int(input('Digite numero da sequencia (0 Sair): '))
	

elemento = int(input('Qual numero procurar repetição: '))

'''cont = 0
for i in range (len(lista)):
	if lista[i] == elemento:
		cont += 1'''

print ('o elemento %d repete %d' %(elemento, lista.count(elemento)))