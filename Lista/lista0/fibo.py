a, b = 0, 1
x = 1
c = 1

num = input('Informe numero: ')
print (c) 
while x <= num:
	a, b = b, a + b
	num -= 1
	print (b)