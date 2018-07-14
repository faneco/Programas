num1 = int(input('Digite 1 valor: '))
num2 = int(input('Digite 2 valor: '))

while num1 % num2 != 0:
	num1, num2 = num2, num1 % num2
print (num2)

