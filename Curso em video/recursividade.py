
def recursividade(y):
	x = 1
	if x >= y:
		return x

	return recursividade(x + 1) 

print (recursividade(4))