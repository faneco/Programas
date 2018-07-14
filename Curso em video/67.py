while True:
	x = 0
	num = int(input('Quer ver a tabuada de qual valor?: '))
	if num < 0:
		break
	for c in range(1, 11):
		print ('%d x %d = %d' %(num, c, num*c))
print ('Tabuada encerrada')

		
