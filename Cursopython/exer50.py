soma = 0
for i in range(1, 6+1):
	num = int(input('Digite %d numero: ' %i))
	if num % 2 == 0:
		soma += num

print ('A soma do valores pares: ',soma)