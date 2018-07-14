print ('Sequencia de Fibonacci')
print ('-=' *10)
n = int(input('Quantos termo voce quer mostrar?: '))

t1, t2 = 0, 1

print (t1,'->', t2, end=' -> ')
cont = 3
t3 = 0
while cont <= n:
	t3 = t1 + t2
	print (t3, end=' -> ')
	cont += 1
	t1 = t2
	t2 = t3
print ('Fim')