num = 1
soma = 0
while True:
	num = int(input('Digite um numero (zero sair): '))
	if num == 0:
		break
	soma += num
print (soma)