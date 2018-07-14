while True:
	num1 = int(input('Primeiro valor: '))
	num2 = int(input('Segundo valor: '))

	print ('[ 1 ] somar')
	print ('[ 2 ] multiplicar')
	print ('[ 3 ] maior')
	print ('[ 4 ] novos numeros')
	print ('[ 5 ] sair do programa')

	opção = int(input('Qaul é a sua opção? '))
	if opção == 1:
		resutaldo = num1 + num2
		print (resutaldo)
	elif opção == 2:
		resutaldo = num1 * num2
		print (resutaldo)
	elif opção == 3:
		if num1 > num2:
			print (num1)
		else:
			print (num2)
	elif opção == 4:
		print ('Informe os valores novamente!')
	elif opção == 5:
		print ('Finalizando...!')
		break
	else:
		print ('Opção inválida. Tente novamente!')
		print ('=-=' *10)
print ('FIm do programa! Volte sempre!')