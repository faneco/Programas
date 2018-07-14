cont = total = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
	total += n
	cont += 1
	n = int(input('Digite um numero [999 para parar]: '))
print ('acabou')
print ('voce digito %d numero e soma dele %d' %(cont, total))