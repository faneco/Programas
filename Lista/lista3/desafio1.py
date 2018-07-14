n = int(input('Digite o valor: '))
i = 1
t = 0

while t < n:
	t = i*(i + 1)*(i + 2)
	i += 1

if t == n:
	print ('%d e triangular' %n)
else:
	print ('%d nao e triangular' %n)