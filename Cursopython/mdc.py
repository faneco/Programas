def mdc(num1, num2):
	resto = None 
	while resto is not 0:
		resto = num1 % num2
		num1 = num2
		num2 = resto
	return num1

print (mdc(24, 9))
print (mdc(30, 20))

'''Dois números naturais sempre têm divisores comuns. 
Por exemplo: os divisores comuns de 12 e 18 são 1,2,3 e 6. 
Dentre eles, 6 é o maior. Então chamamos o 6 de máximo divisor 
comum de 12 e 18 e indicamos m.d.c.(12,18) = 6.'''