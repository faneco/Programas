ultimo = 10
fila = list(range(1, ultimo+1))
while True:
	print ('\nExitem %d clientes na fila ' %(len(fila)))
	print ('Fila atual: ', fila)
	print ('Digite F para adicionar um cliente ao fim da fila, ')
	print ('ou A para realizar o atendimento. S para Sair.')
	operacao = input('Operação (F, A ou S: ')

	for op in operacao:
	
		if op == 'A':
			if (len(fila)) > 0:
				atendido = fila.pop(-1)
				print ('Cliente %d atendido ' %(atendido))
			else:
				print ('Fila vazia! ninguem para enteder.')
		elif op == 'F':
			ultimo +=1
			fila.append(ultimo)
		elif op == 'S':
			break
		else:
			print ('Operação invalida! Digite apenas F, A ou S!')
