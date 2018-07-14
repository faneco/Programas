soma = 0
num = int(input('Digite um numero: '))
for i in range(1, num+1):
	if num % i == 0:
		soma +=1
print ('numero %d foi divisivel %d' %(num, soma))
if soma == 2:
	print ('numero e primo')
else:
	print ('numero nao e primo')