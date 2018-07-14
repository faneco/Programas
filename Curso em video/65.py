lista = []
resp = 'S'
cont = 0
total = 0
while resp in 'S':
	num = int(input('Digite um numero: '))
	lista.append(num)
	total += num 	
	cont += 1
	resp = input('Deseja continua [S/N]: ').upper().strip()[0]
print ('acabou')


maior = lista[0]
menor = lista[0]

for i in lista:
	if i > maior:
		maior = i
	if i < menor:
		menor = i
print ('Voce digito %d numero e media %.2f' %(cont, total / cont))
print ('O maior %d numero o menor %d' %(maior, menor))