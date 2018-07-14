num = int(input('Digite numero inteiro: '))

divisores = 0
n = 1
while n <= num:
	if num % n == 0:
		divisores += 1
	n += 1

print (divisores == 2)

