n = input("Digite o numero: ")
a, b = 0, 1
x = 1
while x <= n:
	a, b = b, a + b
	x += 1
	print (b)
