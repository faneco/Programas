x = 1
fat = 1
n = int(input('Digite um numero inteiro: '))
while x <= n:
	fat = fat * x
	x += 1 
print ('fatorial de %d e %d ' %(n, fat))