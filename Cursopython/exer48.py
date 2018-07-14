soma = 0
num = int(input('Digite um numero: '))
for i in range(1, num, 2):
	if i % 3 == 0:
		soma += i
print (soma)