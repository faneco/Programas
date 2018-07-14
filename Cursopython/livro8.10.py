def fibo(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
		print (a)
	return a

print (fibo(7))